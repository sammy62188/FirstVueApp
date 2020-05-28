from flask import Flask, jsonify,request
from flask_cors import CORS
from flask_mysqldb import MySQL

app=Flask(__name__)

CORS(app, resourses=r'/api/*')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sammy'
app.config['MYSQL_DB'] = 'labsan'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/api/regis", methods=['GET','POST'])
def regis():
    response_object= {'success': 'Book added'}
    if request.method == 'POST':
        post_data = request.get_json()
        name = post_data['name']
        email = post_data['email']
        message = post_data['message']
        phone = post_data['tel']
        information = post_data['Information']
        cur = mysql.connection.cursor()
        cur.execute("Insert into Profile(name,email_address,information,message,phone) VALUES(%s,%s,%s,%s,%s)",(name,email,information,message,phone))
        mysql.connection.commit()
        cur.close()
        return 'success'
    else:
        return 'Not succesful'

if __name__ == '__main__':
    app.run()