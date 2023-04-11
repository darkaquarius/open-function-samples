import functions_framework
from flask import Flask

app = Flask(__name__)

# localhost:8080/testGet?name=zhangsan&age=20
@functions_framework.http
@app.route("/testGet", method=["GET"])
def hello_get(request):
    name = request.args.get("name")
    age = request.args.get("age")
    return name + " : " + age

#
'''
localhost:8080/testPost
    {
        "name": "zhangsan"
        "age" : "30"
    }
'''
@functions_framework.http
@app.route("/testPost", methods=["POST"])
def hello_post(request):
    data = request.json
    name = data["name"]
    age = data["age"]
    return name + " : " + age

def hello_world(request):
    return "hello, world1"
