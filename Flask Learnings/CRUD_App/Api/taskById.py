from flask_restful import Resource
import logging as log
class taskById(Resource):
    def get(self,TaskId):
        log.debug("Inside GET Method")
        return {"Message":"You are inside the GET By TaskId method {}".format(TaskId)},200  # 200 is a success call
    def post(self,TaskId):
        log.debug("Inside POST Method")
        return {"Message":"You are inside the POST By TaskId method {}".format(TaskId)},200 
    def put(self,TaskId):
        log.debug("Inside PUT Method")
        return {"Message":"You are inside the PUT By TaskId method {}".format(TaskId)},200 
    def delete(self,TaskId):
        log.debug("Inside DELETE Method")
        return {"Message":"You are inside the DELETE By TaskId method {}".format(TaskId)},200 