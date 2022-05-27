from flask_restful import Resource
import logging as log
class Task(Resource):
    def get(Self):
        log.debug("Inside GET Method")
        return {"Message":"You are inside the GET method"},200  # 200 is a success call
    def post(Self):
        log.debug("Inside POST Method")
        return {"Message":"You are inside the POST method"},200 
    def put(Self):
        log.debug("Inside PUT Method")
        return {"Message":"You are inside the PUT method"},200 
    def delete(Self):
        log.debug("Inside DELETE Method")
        return {"Message":"You are inside the DELETE method"},200  