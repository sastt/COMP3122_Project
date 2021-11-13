#! /usr/bin/python

import sys
import redis
from flask import Flask

#port = int(sys.argv[1])
port = 6379
app = Flask(__name__)
db = redis.Redis(host='db', port=port)

# TEST: try to insert some data to db
db.set('foo', 'bar2')
msg = db.get('foo')
print(msg)

# API Gateway
@app.route('/')
def main():
    return 'hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
