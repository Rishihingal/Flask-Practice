from datetime import datetime
from email import message
from flask import Flask,render_template
import logging as log 
log.basicConfig(level="DEBUG")

FlaskInstance = Flask(__name__)

if __name__ == '__main__':
    log.debug("Starting the Application")
    from Api import *
    FlaskInstance.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
     