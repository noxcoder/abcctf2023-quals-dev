from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return 'Welcome developers to the ABCCTF 2023 competition for developers!'

if __name__ == '__main__':
    app.run()