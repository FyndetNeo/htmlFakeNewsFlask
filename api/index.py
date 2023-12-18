from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from api.db import init_db, query_db

date_format = "%Y-%m-%d %H:%M:%S"


def init_app(app):
    # Configuration for serving the Swagger file
    SWAGGER_URL = '/swagger'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = '/static/swagger.yaml'  # Our Swagger document
    swagger_destination_path = './static/swagger.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Tisch Reservierung"
        }
    )

    # Register blueprint at URL
    # (URL must match the one given to get_swaggerui_blueprint)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    @app.route('/check-it-games')
    def get_check_it_games():
        games = query_db("SELECT * FROM checkItGame")
        return games

    @app.route('/check-it-games', methods=["POST"])
    def add_check_it_games():
        params = request.json
        query_db("INSERT INTO checkItGame (text, isTrue) VALUES (value1, value2)")
        return {'message': 'CheckItGame added successfully'}, 201

    @app.route('/check-it-games/<int:checkItGameId>', methods=["DELETE"])
    def delete_check_it_games(checkItGameId):
        query_db("DELETE FROM Scenes WHERE sceneId = ?", [checkItGameId])
        return {'message': 'CheckItGame deleted successfully'}, 200

    @app.route('/scenes', methods=['GET'])
    def get_scenes():
        scenes = query_db("SELECT * FROM Scenes")
        return jsonify([{'sceneId': scene['sceneId'], 'data': scene['data']} for scene in scenes])

    @app.route('/scenes', methods=['POST'])
    def add_scene():
        scene_data = request.json
        query_db("INSERT INTO Scenes (data) VALUES (?)", [json.dumps(scene_data)])
        return {'message': 'Scene added successfully'}, 201

    @app.route('/scenes/<int:scene_id>', methods=['DELETE'])
    def delete_scene(scene_id):
        query_db("DELETE FROM Scenes WHERE sceneId = ?", [scene_id])
        return {'message': 'Scene deleted successfully'}, 200


def create_app():
    app = Flask(__name__)
    init_app(app)
    init_db(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
