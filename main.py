from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)

#Home

@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    data = dbHandler.listListing()
    return render_template('/index.html', content=data)

#Log_In
@app.route('/log_in.html', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # NOT DONE
        return "Login attempt received"
    return render_template('log_in.html')

#Sydney, Australia
@app.route('/sydney.html', methods=['GET', 'POST'])
def sydney():
    data = dbHandler.listListing()
    return render_template('/sydney.html', content=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)