from flask import *
from db.scripts.operations_db import register_user

app = Flask(__name__)


print(register_user('lirikffest', 'passwd', 'Dimitrii', 'base'))

if __name__ == '__main__':
    app.run(port=1024, host='127.0.0.1')
