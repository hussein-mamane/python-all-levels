from flask import Flask, request
import logging

app = Flask(__name__)

# custom logging
logging.basicConfig(filename='request.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')


@app.route('/', methods=['GET'])
def index():
    # log the incoming request
    log_request(request)
    return 'Hello, World!'


# function to log incoming requests
def log_request(req):
    log_info = {
        'method': req.method,
        'path': req.path,
        'ip': req.remote_addr,
        'user_agent': req.user_agent.string
    }
    logging.info(log_info)


if __name__ == '__main__':
    app.run(debug=True)
