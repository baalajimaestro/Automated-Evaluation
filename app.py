# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
from flask import Flask, abort, request,jsonify
from selenium_app import selenium_runner
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def respond():
    creds = json.loads(request.json)
    print(creds)
    uname=creds["uname"]
    passwd=creds["passwd"]
    print("Starting selenium")
    x=selenium_runner(uname, passwd)
    return str(x)
app.run(host='localhost', port=1313, debug=True)
