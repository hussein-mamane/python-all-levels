from flask import Flask, request
import logging

app = Flask(__name__)

# Configure custom logging
logging.basicConfig(filename='request.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# Endpoint for handling GET requests
@app.route('/', methods=['GET'])
def index():
    # Log the incoming request
    log_request(request)
    # Your endpoint logic goes here
    return 'Hello, World!'

# Function to log incoming requests
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

