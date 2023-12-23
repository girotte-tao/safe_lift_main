import os

# 日志文件的路径
log_dir = 'log'
access_log_file = os.path.join(log_dir, 'access.log')
error_log_file = os.path.join(log_dir, 'error.log')

# 检查日志目录是否存在，如果不存在，则创建它
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Gunicorn 配置
loglevel = 'debug'
accesslog = access_log_file
errorlog = error_log_file
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
