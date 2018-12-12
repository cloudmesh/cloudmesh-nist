import connexion
from flask import render_template, send_from_directory
from flask_cors import CORS
from pathlib import Path
from os import path
from specsynthase.specbuilder import SpecBuilder
from swagger_ui_bundle import swagger_ui_3_path
from connexion.resolver import Resolver
from connexion.utils import get_function_from_name
from db.mongo import MongoDb

spec_dir = "./specs"
current_dir = path.dirname(__file__)
spec_path = Path(f"{current_dir}/{spec_dir}").resolve()

spec = SpecBuilder()\
    .add_spec(spec_path.joinpath("cm4.yaml")) \
    .add_spec(spec_path.joinpath("vm.yaml")) \
    .add_spec(spec_path.joinpath("flavor.yaml"))\
    .add_spec(spec_path.joinpath("image.yaml"))

options = {'swagger_path': swagger_ui_3_path}

app = connexion.FlaskApp(__name__, specification_dir=spec_dir, options=options)

# Inject the `controllers` namespace into `operationId`s specified in the spec
# files. This allows for the (potentially many) controllers to be organized
# into thier own folder and to potentially have multiple versions of the
# controller classes in different folders.
custom_resolver = Resolver(
    function_resolver=lambda fname:
        get_function_from_name(f"controllers.{fname}")
)
app.add_api(spec, resolver=custom_resolver)
CORS(app.app)


@app.route("/")
def home():
    return render_template("index.html")

# Expose js, css, img static folders as if they were
# root folders, not under `static/` because it's easier
# than getting the JS app to rewrite all of the URLs to
# include `static/`.


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)


if __name__ == "__main__":
    # Sets default db connection and build
    # if it is not already generated.
    MongoDb().check_db()
    app.run(port=8080, debug=True)
