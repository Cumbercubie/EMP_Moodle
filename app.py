from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route("/")
def index():
    if request.method == "POST":
        result = request.form
        username = result.get("username") 
        pw = result.get("password")
        if pw=="123":
             return redirect('index.html')
    columns = ['Code','Name','Email']
    return render_template('login.html')

@app.route("/index.html",methods=["POST","GET"])
def default():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()