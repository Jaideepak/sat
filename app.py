from flask import Flask, render_template, request, redirect, url_for, flash
import logging

app = Flask(__name__)
app.secret_key = 'any_secret_key_here'

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Hardcoded credentials (Register No. and DOB)
VALID_REG = '41110531'
VALID_DOB = '09/04/2004'  # Format must match exactly

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        regno = request.form.get('regno', '').strip()
        dob = request.form.get('dob', '').strip()

        logging.debug(f"User submitted: regno={regno}, dob={dob}")

        if regno == VALID_REG and dob == VALID_DOB:
            logging.debug("✅ Login successful")
            return redirect(url_for('result'))
        else:
            logging.debug("❌ Login failed: Invalid credentials")
            flash("Invalid Register Number or Date of Birth", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/result')
def result():
    logging.debug("📄 Reached /result page")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
