import os
from config import app
from turmas.turmas_routes import turmas_blueprint

app.register_blueprint(turmas_blueprint)

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )