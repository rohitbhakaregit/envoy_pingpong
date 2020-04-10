from flask import Flask

app = Flask(__name__)

@app.route('/ding')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'dong'

@app.route('/ready')
def healthcheck():
    """Print 'Hello, world!' as the response body."""
    return 'yes'


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0", port= 8090)