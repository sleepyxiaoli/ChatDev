# chatdev_runner.py
import os
import sys
import argparse
from datetime import datetime

# 添加项目根目录到路径
root = os.path.dirname(__file__)
sys.path.append(root)

from chatdev.chat_chain import ChatChain
from camel.typing import ModelType
import logging

try:
    from openai.types.chat.chat_completion_message_tool_call import ChatCompletionMessageToolCall
    from openai.types.chat.chat_completion_message import FunctionCall
    openai_new_api = True
except ImportError:
    openai_new_api = False

def get_config(company):
    """获取配置文件路径"""
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

def run_chatdev(task, name, config="Default", org="DefaultOrganization", model="GPT_4O_MINI", callback=None):
    """
    运行ChatDev开发流程
    callback: 用于发送进度更新的回调函数
    """
    try:
        if callback:
            callback("System", "🔧 正在初始化ChatDev...")
        
        # 配置文件路径
        config_path, config_phase_path, config_role_path = get_config(config)
        
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

        if callback:
            callback("System", "📋 正在创建ChatChain...")

        # 初始化ChatChain
        chat_chain = ChatChain(
            config_path=config_path,
            config_phase_path=config_phase_path,
            config_role_path=config_role_path,
            task_prompt=task,
            project_name=name,
            org_name=org,
            model_type=args2type[model],
            code_path=""
        )

        if callback:
            callback("System", f"📁 项目将保存到: WareHouse/{name}_{org}_<timestamp>")

        # 设置日志
        logging.basicConfig(
            filename=chat_chain.log_filepath, 
            level=logging.INFO,
            format='[%(asctime)s %(levelname)s] %(message)s',
            datefmt='%Y-%d-%m %H:%M:%S', 
            encoding="utf-8"
        )

        if callback:
            callback("System", "⚙️ 正在进行预处理...")
        chat_chain.pre_processing()

        if callback:
            callback("System", "👥 正在招募开发团队...")
        chat_chain.make_recruitment()

        if callback:
            callback("System", "🚀 开发团队已组建，开始协作开发...")
        chat_chain.execute_chain()

        if callback:
            callback("System", "🔄 正在进行后处理...")
        chat_chain.post_processing()

        if callback:
            callback("System", "✅ 项目开发完成！")
            callback("System", f"📂 请查看 WareHouse 目录中的项目文件")

        return True, f"WareHouse/{name}_{org}"

    except Exception as e:
        if callback:
            callback("System", f"❌ 开发过程中出错: {str(e)}")
        return False, str(e)

if __name__ == "__main__":
    # 如果直接运行这个文件，提示用户使用web界面
    print("=" * 60)
    print("🚀 ChatDev Web Interface")
    print("=" * 60)
    print("请使用以下命令启动web界面:")
    print("python3 app.py")
    print("")
    print("然后访问: http://127.0.0.1:8000/chatdev")
    print("=" * 60)