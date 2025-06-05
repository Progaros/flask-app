from flask import Flask, render_template, request
from nice_module import nice_function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mvg_form():
    if request.method == 'POST':
        from_station = request.form.get('from_station')
        to_station = request.form.get('to_station')
        return f"<h2>MVG Graph</h2><p>From: {from_station}<br>To: {to_station}</p>"
    return render_template('mvg_form.html')

@app.route('/time')
def time():
    return nice_function()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
