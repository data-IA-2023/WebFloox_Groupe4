from flask import Flask, request, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get("name", "Rebi")
    return f'Hello, {escape(name)}!'

@app.route('/page')
def page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
