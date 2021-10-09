import os
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def get_info():
    """ Returns 'Running' string. Used to test if api is running """
    return "Running"


@app.route('/count', methods=['GET'])
def getCountReq():
    """ Returns count of requsets """
    global counts
    counts = counter(counts)
    return f"Number of Req: {counts}"

def counter(num):
    return num + 1

if __name__ == '__main__':
    counts = 0
    app.run(debug=True, host='0.0.0.0')
