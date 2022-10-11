# flask is a library or framework which is going to help you to exposr your function to the outer world
from flask import Flask , request, jsonify
# pip install flask
app = Flask(__name__) # object of class Flask
# we can send the data using different http methods get, post, put, delete etc.
#  API is set of protocol through which you will be able to reach to the particular system and able to execute th efunction
# when we try to form communication b/w two heterogenous system then we use some protocol i.e called HTTP or HTTPs protocol
# Difference between GET and POST? :-> meaning of both is same i.e sending a data via url and body.
# send the data via url is called GET eg:- google search, send the data via body i.e login gmail is calld POST method. In case of maintaining the data security we use post method.
#This is called decorator. It is tryint to decorate test1() function. route is the function inside the flask. where '/abc' is the route of function test1(). @ means just after this line call the function written i.e test1 here.
@app.route('/abc', methods = ['GET' , 'POST'])
def test1():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify((str(result)))

@app.route('/abc1/madhu', methods = ['GET','POST'])
def test2():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify(str(result))


@app.route('/abc1/madhu/test3', methods = ['GET','POST'])
def test3():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a - b
        return jsonify(str(result))

@app.route('/abc1/madhu/test4', methods = ['GET','POST'])
def test4():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a ** b
        return jsonify(str(result))

@app.route('/abc1/madhu/test5', methods = ['GET','POST'])
def test5():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a / b
        return jsonify(str(result))



if __name__ == '__main__' :
    app.run()
# 200:- success
# 400:- check the request(the server cannot or will not process the request due to something that is perceived to be a client error (for example, malformed request syntax, invalid request message framing, or deceptive request routing).)
# 404:- page not found (server was unable to find what was requested)
# 500:- server error(server encountered an unexpected condition that prevented it from fulfilling the request.)

# def test(a,b) :
#     return a+b

# print(test(4,5))

# i want to call this function from somewhere else may be from postman or browser
