from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/main')
def main():
    return 'main'


if __name__ == '__main__':
    app.run()
