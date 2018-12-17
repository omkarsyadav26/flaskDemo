from flask import Flask, render_template, request
app = Flask(__name__)

posts = [
    {
        'title':'Title no 1',
        'author':'Omkar yadav',
        'posted_date':'Dec 2018',
        'content':'My first content'
    },
    {
        'title':'Title no 2',
        'author':'Saurabh yadav',
        'posted_date':'Nov 2018',
        'content':' Second posted content'
    }
]

@app.route("/")
def index():
    return render_template("index.html", title="index")
@app.route("/home", methods=["GET","POST"])
def home():
    if request.method == "GET":
        return "Please submit your name first"
    else:
        name = request.form.get("name")
        return render_template("home.html", posts=posts, title="home", name=name)
@app.route("/about")
def about():
    return render_template('about.html', title="about")

if __name__ == '__main__':
    app.run(debug = True)
