from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/testfun")
def test():
    # pass multiple data
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get("mail_id")
    return "This is my first function for get {} {} {}".format(get_name, mobile_number, mail_id )


if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/testfun?get_name=Madhu Priya &mobile=324234234&mail_id=madhu.priya@klh.edu.in