#절대 경로를 위한 import다.
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#절대경로로 현재 파일 위치를 알려준다.
#C:\User\kanghyun\git_local\flask_database_CRUD
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# 일반 URI는 다음과 같은 형태를 나타낸다.
# scheme:[//[user[:password]@]host[:port]][/path][?query][#fragment]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class AOA(db.Model):
    
    __table__name = "AOA"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    birth = db.Column(db.Integer)

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

    def __repr__(self):
        return f"AOA의 멤버 {self.name}의 출생년도는 {self.birth}년 입니다."
    