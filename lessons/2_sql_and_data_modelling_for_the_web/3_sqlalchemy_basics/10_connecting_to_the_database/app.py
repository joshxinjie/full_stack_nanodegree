from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://student@localhost:5432/example'
db = SQLAlchemy(app)

# listen to homepage route
@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)