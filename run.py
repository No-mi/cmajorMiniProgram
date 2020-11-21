from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/monitor_system'
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
