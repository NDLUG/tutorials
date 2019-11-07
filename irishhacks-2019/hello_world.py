from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def func():
    return render_template("new_main.html")

@app.route("/help")
def help():
    return

if __name__ == "__main__":
    # int main() {}
    app.run()