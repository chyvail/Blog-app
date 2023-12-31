# importing the flask class here
from flask import Flask,render_template,url_for

# create variable app and settting it to an instance of the Flask class. Variable passed is needed so py can know 
# where to look for resources
app = Flask(__name__)

posts = [
    {
        "author": "John Chivile",
        "title": "Having a coversation with God",
        "content": "Its important to have faith...",
        "date_posted": "December 25, 2023"
    },
    {
        "author": "Jill Chivile",
        "title": "Self Confidence",
        "content": "If i can make it, so can you...",
        "date_posted": "December 20, 2023"
    }
]

# export FLASK_APP=blog.py then run flask run
# export FLASK_DEBUG=1 --> for debuging purposes

# this decorator tells flask what url should trigger this function : go to / or home
# it binds a function to a url

@app.route("/")
@app.route("/home")
def index():
    # to render templates create template folder with the files
    return render_template("home.html", posts=posts, title="Home Page") # an easy way to pass the posts to our templates

@app.route("/about")
def about():
    return render_template("about.html", title="About-title")

# another option for the env variables to enable debugging

if "__name__" == "__main__":
    app.run(debug=True)