import redis

######################
# 변수선언
######################
HOST_NAME = "localhost"
USERNAME = "fastapi_user"
PASSWORD = "fastapi_user"

r = redis.Redis(host='localhost', port=6379, db=0)

