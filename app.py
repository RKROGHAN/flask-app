from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/transaction')
def transaction():
    return render_template('transaction.html')

@app.route('/account-creation')
def account_creation():
    return render_template('account_creation.html')

@app.route('/check-balance')
def check_balance():
    return render_template('check_balance.html')

@app.route('/deposit')
def deposit():
    return render_template('deposit.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

@app.route('/account-login')
def account_login():
    return render_template('account_login.html')

@app.route('/statement')
def statement():
    return render_template('statement.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
