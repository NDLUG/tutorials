from flask import Flask, render_template, request

# the app is the flask application object that we made
app = Flask(__name__)
nick_names = {
    "noah":  "silver",
    "bui":   "pbui",
    "peter": "pbui",
    "mike":  "android kit kat"
}

# special python syntax essentially we are modifying main to run when
# we sent a request to "/" of the server
@app.route("/")
def main():
    # returns the html file "main.html" inside templates directory
    return render_template("main.html")

# same with this function
@app.route("/myroute")
def myroute():
    # request.json
    # request.values
    # request.args
    # request.form

    # request is a variable we have access to from flask, it gets modified
    # when the server gets a request
    msg = request.args["info"]
    print(msg)
    msg = msg.lower()

    # if the message is in the nick names dictionary
    if msg in nick_names:
        nick_name = nick_names[msg]
        html = "<h3>Hey, this was a nickname!</h3>"
        html = html + "<div style='color: red'>{} = {}</div>".format(msg, nick_name)
        return html

    # what you return gets displayed to the webpage
    # you can either return raw html, or an html template file using render_template()
    return "Handled by first route: lowercase message = <div style='color: blue'>{}</div>".format(msg)


@app.route("/secondroute")
def anotherroute():
    msg = request.args["message"]
    print(msg)
    # uppercase the message
    msg = msg.upper()
    return render_template("info.html", message=msg)

@app.route("/list")
def list_nicks():
    nicks = []
    for key, value in nick_names.items():
        nicks.append((key, value))

    return render_template("nicks.html", nicks=nicks)

@app.route("/info")
def help():
    # list of links
    links = [
        "https://www.w3schools.com/html/",
        "http://flask.palletsprojects.com/en/1.1.x/",
        "https://www.w3schools.com/js/",
        "https://www.w3schools.com/css/"
    ]
    html_list = ""
    # build up the string that we will return as our HTML
    for item in links:
        html_list += "<li><a href='" + item + "'>" + item + "</a></li>"

    return "<ul>" + html_list + "</ul>"

@app.route("/color")
def color():
    color = request.args["color"]
    return "<h1 style='background-color: {}'>Is this the color you put in?</h1>".format(color)

if __name__ == "__main__":
    # the host is 0.0.0.0, or our local host
    # debug=True makes it so the server reloads when we modify files
    app.run(debug=True, host="0.0.0.0")

