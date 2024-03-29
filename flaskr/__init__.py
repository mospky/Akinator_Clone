import os

from flask import Flask, jsonify

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'game.db'),
    )

     # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    #  DATABASE=os.path.join(app.instance_path, 'game.db'),

    #DEBUG
    str = "DEBUG : " + "__name__ = " + __name__
    print(str)
    str = "DEBUG : " + "app.instance_path = " + app.instance_path
    print(str)
    bool = test_config
    print(bool)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('development.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # DB 初期化
    from .controllers import db
    db.init_app(app)

    # 
    from .controllers import auth
    app.register_blueprint(auth.bp)

    # 
    from .controllers import recommend
    app.register_blueprint(recommend.bp)
    app.add_url_rule('/', endpoint='recommend')

    # 
    from .controllers import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/blog', endpoint='blog')

    return app