import flask

def add_routes_to_app(app: flask.Flask):
  @app.route('/')
  def hello_world():
    return flask.render_template('templates/index.html')