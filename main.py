from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from libs.orm import db

app = Flask(__name__)
app.secret_key = r'nfjkewjiokjw@#fgg&d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://clay:lry1998@119.45.200.179:3306/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

manager = Manager(app)

db.init_app(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.route('/')
def home():
    '''首页'''
    return 'hello world'


if __name__ == "__main__":
    manager.run()
