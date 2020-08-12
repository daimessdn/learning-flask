# importing Flask
from flask import Flask, render_template

app = Flask(__name__)

# main route directory: "/"
@app.route("/")
def hello_world():
  return """Hello, world!<br />
    <a href="/about">about</a><br />
    <a href="/html">view HTML</a>"""

# /about directory
@app.route("/about")
def about():
  return """This is a about page<br />
    <a href="/">back to home</a>"""

@app.route("/html")
def home_html():
  return render_template("index.html")

@app.route("/html/about")
def about_html():
  return render_template("about.html")

if __name__ == "__main__":
  app.run(debug= True)