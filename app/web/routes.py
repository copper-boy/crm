from aiohttp.web_app import Application

from app.crm.routes import setup_routes as crm_setup_routes


def setup_routes(app: Application) -> None:
    crm_setup_routes(app)

