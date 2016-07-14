from flask import Flask
from os import environ
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
@app.route("/hello")
def say_hi():
#    return "Hello World!"
  return render_template('hello_world.html')


@app.route("/jedi/<first_name>/<last_name>")
def hello_jedi(first_name,last_name):
  
  a = first_name[0:2]
  b = last_name[0:3]
  jedi_name = b + a

  return render_template('jedi.html', jedi_name = jedi_name) 


if __name__ == "__main__":
    app.run(host=environ['IP'],
#            port=int(environ['PORT']))
	     port=int('8081'))
