
from flask import Flask

app = Flask(__name__)  # Create a Flask application instance

@app.route("/")
def hello_world():
    return "Hello World!"  # Define a route that returns "Hello World!"


if __name__=="__main__":
    app.run(debug=True)
# When no port is specified, starts at default port 5000