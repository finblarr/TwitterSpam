import flask
from absl import app
import routes

def main(unused_argv):
  config= {'name': 'VitalikButerin'}
  flask_app = flask.Flask(__name__, 
                          template_folder='templates')
  routes.add_routes_to_app(flask_app, config=config)
  flask_app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
  app.run(main)