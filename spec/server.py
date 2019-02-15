"""
Main module of the server file
"""

from flask import jsonify
import connexion

# http://127.0.0.1:8080/ui
# http://127.0.0.1:8080/swagger.json

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

spec = "."


def load_api(*args):
    for api in args:
        app.add_api("{api}.yaml".format(api=api, spec=spec))


load_api("timestamp")


# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
