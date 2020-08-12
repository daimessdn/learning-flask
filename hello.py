# importing Flask
from flask import Flask

app = Flask(__name__)

# main route directory: "/"
@app.route("/")
def hello_world():
  return """Hello, world!<br />
    <a href="/about">about</a>"""

# /about directory
@app.route("/about")
def about():
  return """This is a about page<br />
    <a href="/">back to home</a>"""

@app.route("/html")
def home_html():
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug= True)