from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    # if file to be rendered is in a subdirectory, must reference entire path
    return render_template("Dan.html")


if __name__ == "__main__":
    app.run(debug=True)
