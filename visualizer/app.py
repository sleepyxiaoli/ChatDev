import logging
import requests
import os
import threading
import subprocess
import json
from flask import Flask, send_from_directory, request, jsonify
import argparse
import socket
os.environ['OPENAI_API_KEY'] = "sk-UfintTNkIFLGE3vkB6E6346bBfFa45E59f211b22CcB6DdC0"
os.environ['OPENAI_BASE_URL'] = "https://api.laozhang.ai/v1"


app = Flask(__name__, static_folder='static')
app.logger.setLevel(logging.ERROR)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
messages = []
port = [8000]  # Default port

# 新增：任务状态管理
current_task = None
task_thread = None
task_status = {
    'running': False,
    'current_task': None,
    'progress': '待机中'
}

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def send_msg(role, text):
    try:
        data = {"role": role, "text": text}
        response = requests.post(
            f"http://127.0.0.1:{port[-1]}/send_message", json=data)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send message: {e}")
        return False

# 新增：运行ChatDev任务的函数
def run_chatdev_task(task_description, project_name):
    global task_status, messages
    
    try:
        task_status['running'] = True
        task_status['current_task'] = project_name
        task_status['progress'] = '正在初始化...'
        
        # 添加系统消息
        system_message = {
            "role": "System",
            "text": f"开始开发项目：{project_name}\n需求：{task_description}",
            "avatarUrl": "/static/avatars/default.png"
        }
        messages.append(system_message)
        
        # 构建运行命令
        cmd = [
            'python', 'run.py',
            '--task', task_description,
            '--name', project_name,
            '--model', 'GPT_4O_MINI',
            '--org', 'WebDev'
        ]
        
        task_status['progress'] = '正在启动开发流程...'
        
        # 运行ChatDev
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            universal_newlines=True
        )
        
        # 读取输出并更新状态
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                # 解析输出并更新进度
                line = output.strip()
                if "**[" in line and "]**" in line:
                    # 提取阶段信息
                    stage = line.split("**[")[1].split("]**")[0]
                    task_status['progress'] = f'当前阶段：{stage}'
                    
                    # 添加阶段消息
                    stage_message = {
                        "role": "System",
                        "text": f"进入阶段：{stage}",
                        "avatarUrl": "/static/avatars/default.png"
                    }
                    messages.append(stage_message)
                
                # 如果是角色对话，解析并添加消息
                if "**[" in line and "]<->[" in line and "]**" in line:
                    try:
                        # 解析角色对话格式
                        parts = line.split("**[")[1].split("]<->[")
                        if len(parts) == 2:
                            role1 = parts[0]
                            rest = parts[1].split("]**")
                            if len(rest) >= 2:
                                role2 = rest[0]
                                content = rest[1].strip()
                                
                                if content:
                                    role_message = {
                                        "role": f"{role1} -> {role2}",
                                        "text": content,
                                        "avatarUrl": "/static/avatars/default.png"
                                    }
                                    messages.append(role_message)
                    except:
                        pass
        
        # 等待进程完成
        return_code = process.wait()
        
        if return_code == 0:
            task_status['progress'] = '开发完成'
            completion_message = {
                "role": "System",
                "text": f"项目 {project_name} 开发完成！请查看 WareHouse 目录中的生成文件。",
                "avatarUrl": "/static/avatars/default.png"
            }
            messages.append(completion_message)
        else:
            task_status['progress'] = '开发失败'
            error_output = process.stderr.read()
            error_message = {
                "role": "System",
                "text": f"项目开发失败：{error_output}",
                "avatarUrl": "/static/avatars/default.png"
            }
            messages.append(error_message)
            
    except Exception as e:
        task_status['progress'] = f'错误：{str(e)}'
        error_message = {
            "role": "System",
            "text": f"运行错误：{str(e)}",
            "avatarUrl": "/static/avatars/default.png"
        }
        messages.append(error_message)
    finally:
        task_status['running'] = False

@app.route("/")
def index():
    return send_from_directory("static", "chatdev_interface.html")

@app.route("/chain_visualizer")
def chain_visualizer():
    return send_from_directory("static", "chain_visualizer.html")

@app.route("/replay")
def replay():
    return send_from_directory("static", "replay.html")

@app.route("/get_messages")
def get_messages():
    return jsonify(messages)

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    if not data or 'role' not in data or 'text' not in data:
        return jsonify({"error": "Invalid request"}), 400

    role = data.get("role")
    text = data.get("text")
    avatarUrl = find_avatar_url(role)

    message = {"role": role, "text": text, "avatarUrl": avatarUrl}
    messages.append(message)
    return jsonify(message), 200

# 新增：启动任务的接口
@app.route("/start_task", methods=["POST"])
def start_task():
    global task_thread, task_status
    
    if task_status['running']:
        return jsonify({"error": "已有任务正在运行"}), 400
    
    data = request.get_json()
    if not data or 'task' not in data or 'name' not in data:
        return jsonify({"error": "缺少必要参数"}), 400
    
    task_description = data.get("task")
    project_name = data.get("name")
    
    if not task_description.strip() or not project_name.strip():
        return jsonify({"error": "任务描述和项目名称不能为空"}), 400
    
    # 在新线程中运行任务
    task_thread = threading.Thread(
        target=run_chatdev_task,
        args=(task_description, project_name)
    )
    task_thread.daemon = True
    task_thread.start()
    
    return jsonify({"message": "任务已启动"}), 200

# 新增：获取任务状态的接口
@app.route("/task_status")
def get_task_status():
    return jsonify(task_status)

# 新增：清空消息的接口
@app.route("/clear_messages", methods=["POST"])
def clear_messages():
    global messages
    messages = []
    return jsonify({"message": "消息已清空"}), 200

def find_avatar_url(role):
    role = role.replace(" ", "%20")
    avatar_filename = f"avatars/{role}.png"
    static_path = os.path.join(app.static_folder, avatar_filename)

    # Check if avatar actually exists
    if not os.path.exists(static_path):
        return "/static/avatars/default.png"  # Fallback to default avatar

    return f"/static/{avatar_filename}"

if __name__ == "__main__":
    print(f"正在启动服务器，端口：{port[-1]}...")
    try:
        app.run(host='0.0.0.0', port=port[-1], debug=False)  # 关闭debug避免重载问题
    except Exception as e:
        print(f"启动服务器失败：{e}")