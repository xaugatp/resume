from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


    

@app.route('/')
def hello_world():
    return render_template('index.html')
    #return 'This is Saugat website'

@app.route('/products')
#anything inside static can be seen using the file name 
def products():
    return 'This is site for products'

if __name__ == "__main__":
    app.run(debug=True)