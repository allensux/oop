
import logging

LOG_FORMAT = "%(asctime)s=======%(levelname)s+++++++%(message)s"

logging.basicConfig(filename="tulignxueyuan.log", level=logging.DEBUG, format=LOG_FORMAT)

# # 默认输出到控制台
# logging.basicConfig(level=logging.DEBUG)
# # 修改日志文件输出位置，创建文件
# logging.basicConfig(filename="tulignxueyuan.log", level=logging.DEBUG)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")


logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")