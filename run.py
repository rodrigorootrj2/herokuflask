from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if 'run' == "__main__":
    app.run(debug=True, host='0.0.0.0', port=443)