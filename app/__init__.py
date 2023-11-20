from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = 'jifysgfuqwyigbri2b484398y1iybfd897y23401`3yuhb'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('triduyPH819?')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 2
# so luong san pham tren moi trang

db = SQLAlchemy(app=app)
login = LoginManager(app=app)