from flask import Flask, render_template, request
from model import UserStory

app = Flask(__name__)


@app.route("/")
@app.route("/story")
def story():
    return render_template("form.html")


@app.route("/list", methods=['POST', 'GET'])
def list_story():
    # Import the add_story method from db, what save the data to the database.
    # In the method argument: Get the request, then convert a cool form to my peewee class (dict in list)
    UserStory.add_story([dict(request.form.items())])
    # Give all data to the list.html
    return render_template("list.html", data=UserStory.select())


if __name__ == "__main__":
    # just for fun
    app.run(host='0.0.0.0', port=10000, debug=True)
