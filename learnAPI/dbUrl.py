from flask import Flask , request, jsonify
import mysql.connector as conn

app = Flask(__name__)
mydb = conn.connect(host = "localhost", user = "root", passwd = "password@123")
cursor = mydb.cursor()

@app.route("/dbaccess")
def test1():
    try:
        db_name = request.args.get("db_name")
        tb_name = request.args.get("tb_name")
        cursor.execute("select * from student.info")
        data = cursor.fetchall()
        mydb.commit()
        mydb.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)

if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/dbaccess?db_name=student &tbname=info