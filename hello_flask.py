import flask
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

# Define a route for the default URL, which loads the form
@app.route('/hellopage')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
# @app.route('/hello/test', methods=['POST'])
# def hello():
# 	post_body = flask.request.get_data()
#     # name=flask.request.form("yourname")
#     # # name=flask.request.args.get("yourname")
#     # name=flask.request.json("yourname")

#     # email=flask.request.form("youremail")
#     # # email=flask.request.args.get("youremail")
#     # email=flask.request.json("youremail")
#     return "Hello World!"

@app.route('/hello/test', methods=['POST'])
def hello():
	try:
		post_body = flask.request.get_json()
		name = post_body['yourname']
		email = post_body['youremail']
	except:
		return flask.jsonify({
			"error": "Please double check your input"
		}
		)
	return "%s and %s information submitted" %(name, email)

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("80")
  )