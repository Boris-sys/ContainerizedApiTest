import os
from dotenv import load_dotenv
import MySQLdb
from flask import Flask

load_dotenv()
def connection():
    try:
        print(os.getenv("DATABASE2"))
        connection = MySQLdb.connect(
        host= os.getenv("HOST2"),
        user=os.getenv("USERNAME2"),
        passwd= os.getenv("PASSWORD2"),
        db= os.getenv("DATABASE2"),
        autocommit = True,
        ssl={}
        )


        # Making Cursor Object For Query Execution
        cursor=connection.cursor()
        # Executing Query
        cursor.execute("SELECT * FROM Persons;")

        # Above Query Gives Us The Current Date
        # Fetching Data
        m = cursor.fetchone()
        # Closing Database Connection
        connection.close()
        return m
    except Exception as e:
        print("error: {}".format(e))

 
# Printing Result Of Above
#print("data: ",m)




 
app = Flask(__name__)
 
@app.route('/')
def home():
    m = connection()
    out = (
        f'Example container application.<br>'
        "data: {}".format(m)
    )
    return out
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')