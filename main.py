from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
@app.route("/list", methods=['POST', 'GET'])
def list_story():
    result = request.form
    print(result)
    return render_template("list.html", result=result)


@app.route("/story")
def story():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000, debug=True)
