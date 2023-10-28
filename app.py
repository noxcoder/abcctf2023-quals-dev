from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return 'Welcome to ABCCTF 2023'

app.secret_key = 'abcctf{all_devs_use_git_right?}'

if __name__ == '__main__':
    app.run()