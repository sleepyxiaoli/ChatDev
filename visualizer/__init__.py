# visualizer/__init__.py
from .app import app  # 导出 app 对象
# 从 database_mine 导入所需函数
from .database_mine import init_db, register_user, validate_login

__all__ = ["app", "init_db", "register_user", "validate_login"]  # 定义可公开访问的接口
