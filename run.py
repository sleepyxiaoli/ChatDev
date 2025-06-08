from chatdev.chat_chain import ChatChain
import logging
import os
import sys
import json
from flask import Flask, request, jsonify
from camel.typing import ModelType

# 创建 Flask 应用
app = Flask(__name__)

# 基础路径设置
root = os.path.dirname(__file__)
sys.path.append(root)

try:
    from openai.types.chat.chat_completion_message_tool_call import ChatCompletionMessageToolCall
    from openai.types.chat.chat_completion_message import FunctionCall
    openai_new_api = True
except ImportError:
    openai_new_api = False
    print(
        "Warning: Your OpenAI version is outdated. \n "
        "Please update as specified in requirement.txt. \n "
        "The old API interface is deprecated and will no longer be supported.")


def get_config(company):
    config_dir = os.path.join(root, "CompanyConfig", company)
    default_config_dir = os.path.join(root, "CompanyConfig", "Default")
    config_files = [
        "ChatChainConfig.json",
        "PhaseConfig.json",
        "RoleConfig.json"
    ]
    config_paths = []
    for config_file in config_files:
        company_config_path = os.path.join(config_dir, config_file)
        default_config_path = os.path.join(default_config_dir, config_file)
        if os.path.exists(company_config_path):
            config_paths.append(company_config_path)
        else:
            config_paths.append(default_config_path)
    return tuple(config_paths)

@app.route('/run_chatdev', methods=['POST'])
def run_chatdev():
    """运行ChatDev工作流的后端接口
    
    前端需要以JSON格式提供参数：
    {
        "task": "开发任务描述",
        "name": "项目名称",
        "config": "Default",  # 可选
        "org": "DefaultOrganization",  # 可选
        "model": "GPT_4O_MINI",  # 可选
        "path": ""  # 可选
    }
    """
    try:
        # 从请求中获取JSON数据
        data = request.get_json()
        
        # 验证必要参数
        if not data or 'task' not in data or 'name' not in data:
            return jsonify({
                "status": "error",
                "message": "必须提供 task 和 name 参数"
            }), 400
        
        # 提取参数
        task = data['task']
        name = data['name']
        config = data.get('config', "Default")
        org = data.get('org', "DefaultOrganization")
        model = data.get('model', "GPT_4O_MINI")
        path = data.get('path', "")
        
        # 模型类型映射
        args2type = {
            'GPT_3_5_TURBO': ModelType.GPT_3_5_TURBO,
            'GPT_4': ModelType.GPT_4,
            'GPT_4_TURBO': ModelType.GPT_4_TURBO,
            'GPT_4O': ModelType.GPT_4O,
            'GPT_4O_MINI': ModelType.GPT_4O_MINI,
        }
        
        if openai_new_api:
            args2type['GPT_3_5_TURBO'] = ModelType.GPT_3_5_TURBO_NEW

        # 初始化ChatChain
        config_path, config_phase_path, config_role_path = get_config(config)
        chat_chain = ChatChain(
            config_path=config_path,
            config_phase_path=config_phase_path,
            config_role_path=config_role_path,
            task_prompt=task,
            project_name=name,
            org_name=org,
            model_type=args2type[model],
            code_path=path
        )

        # 配置日志
        logging.basicConfig(
            filename=chat_chain.log_filepath,
            level=logging.INFO,
            format='[%(asctime)s %(levelname)s] %(message)s',
            datefmt='%Y-%d-%m %H:%M:%S',
            encoding="utf-8"
        )

        # 执行工作流
        chat_chain.pre_processing()
        chat_chain.make_recruitment()
        chat_chain.execute_chain()
        chat_chain.post_processing()

        # 返回成功响应
        return jsonify({
            "status": "success",
            "message": f"项目 {name} 生成完成！",
            "output_path": chat_chain.warehouse_path
        })
    
    except Exception as e:
        # 捕获并返回异常信息
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    # 启动Flask服务
    app.run(host='0.0.0.0', port=5000, debug=True)