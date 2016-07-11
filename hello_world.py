from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name)

@app.route("/jedi/<first_name>/<last_name>")
def hello_jedi(first_name,last_name):
  
  a = first_name[0:2]
  b = last_name[0:3]
  jedi_name = b + a
  html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
  return html.format(jedi_name)


#def hi_person(name):
#  return "hello {}!" .format(name.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
