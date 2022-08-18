from json import loads
from typing import TYPE_CHECKING, Any

from aiohttp.typedefs import Handler
from aiohttp.web_exceptions import HTTPException, HTTPUnprocessableEntity
from aiohttp.web_middlewares import middleware
from aiohttp.web_request import Request
from aiohttp_apispec.middlewares import validation_middleware

from app.web.utils import error_json_response

if TYPE_CHECKING:
    from app.web.app import Application


@middleware
async def error_handling_middleware(request: Request, handler: Handler) -> Any:
    try:
        response = await handler(request)
        return response
    except HTTPUnprocessableEntity as exception:
        return error_json_response(http_status=400, status='bad request', message=exception.reason,
                                   data=loads(exception.text))
    except HTTPException as exception:
        return error_json_response(http_status=exception.status, status='error', message=str(exception))
    except Exception as exception:
        return error_json_response(http_status=500, status='internal server error', message=str(exception))


def setup_middlewares(app: 'Application') -> None:
    app.middlewares.append(error_handling_middleware)
    app.middlewares.append(validation_middleware)

