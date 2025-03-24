import logging

def init_logging():
    """初始化结构化日志系统"""
    logging.basicConfig(
        format='%(asctime)s | %(levelname)s | %(module)s | %(message)s',
        level=logging.INFO,
        handlers=[
            logging.FileHandler('d:/Agent/AgentProject/Logs/execution.log'),
            logging.StreamHandler()
        ]
    )