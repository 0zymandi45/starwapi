from app import create_app
from routes.planet_routes import planet_blueprint
from routes.films_routes import film_blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv
import os

load_dotenv()
app = create_app()

# Register routes
app.register_blueprint(planet_blueprint, url_prefix="/planets")
app.register_blueprint(film_blueprint, url_prefix="/films")

# Swagger
swagger_url = os.getenv("SWAGGER_URL")
api_url = os.getenv("API_URL")
swaggerui_blueprint = get_swaggerui_blueprint(swagger_url, api_url)
app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)

if __name__ == "__main__":
    app.run(debug=True)
