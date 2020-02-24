from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    columns = ['Code','Name','Email']
    return render_template('index.html',columns= columns)

if __name__ == '__main__':
    app.debug = True
    app.run()