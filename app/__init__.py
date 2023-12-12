from flask import Flask
from werkzeug.utils import import_string
import glob

from app.models.db import db

app = Flask(__name__)
app.config.from_object('config')  # 导入配置文件
db.init_app(app)

# 动态注册路由，api文件命名规范
apis = glob.glob('app/HTTPapis/*Api.py')

for api in apis:
    module_name = api.replace('/', '.').rstrip('.py')
    api_module = import_string(module_name)
    app.register_blueprint(api_module.api)

