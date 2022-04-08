import flask
from absl import app
import routes

def main(unused_argv):
  flask_app = flask.Flask('flask_app', instance_relative_config=True)
  routes.add_routes_to_app(flask_app)    
  flask_app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
  app.run(main)