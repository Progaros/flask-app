from flask import Flask
from nice_module import nice_function

app = Flask(__name__)

@app.route('/')
def home():
    return nice_function()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
