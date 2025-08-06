from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Vulnerable Demo!'

@app.route('/cmd')
def cmd():
    cmd = request.args.get('cmd', 'echo no-cmd')
    return os.popen(cmd).read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
