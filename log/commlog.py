import logging
from logging.config import fileConfig


# 读取日志配置文件内容
fileConfig('log/logger.conf')

# 创建一个日志器logger
logger = logging.getLogger('simpleExample')