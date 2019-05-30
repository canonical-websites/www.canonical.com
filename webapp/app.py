"""
A Flask application for maas.io
"""

# Packages
import flask
import talisker.flask
from canonicalwebteam.yaml_responses.flask_helpers import (
    prepare_deleted,
    prepare_redirects,
)
from webapp.helpers import (
    versioned_static,
)
from werkzeug.contrib.fixers import ProxyFix
from werkzeug.debug import DebuggedApplication

from webapp.views import TemplateFinder

app = flask.Flask(
    __name__, template_folder="../templates", static_folder="../static"
)

app.url_map.strict_slashes = False

app.wsgi_app = ProxyFix(app.wsgi_app)
if app.debug:
    app.wsgi_app = DebuggedApplication(app.wsgi_app)


talisker.flask.register(app)
talisker.logs.set_global_extra({"service": "canonical.com"})

app.before_request(prepare_redirects())  # Read redirects.yaml
app.before_request(prepare_deleted())  # Read deleted.yaml

app.add_url_rule('/', view_func=TemplateFinder.as_view('home'))
app.add_url_rule('/<path:subpath>', view_func=TemplateFinder.as_view('all_routes'))

@app.errorhandler(404)
def not_found_error(error):
    return flask.render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return flask.render_template("500.html"), 500


@app.context_processor
def context():
    return dict(
        ASSET_SERVER_URL='https://assets.ubuntu.com/v1/',
        YEAR='2019'
    )

@app.template_filter("versioned_static")
def versioned_static_filter(filename):
    return versioned_static(filename)