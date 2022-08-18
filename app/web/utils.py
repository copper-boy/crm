import base64
from base64 import b64decode
from typing import Any, Optional

from aiohttp.web import json_response as aiohttp_json_response
from aiohttp.web_response import Response


def json_response(data: Optional[Any] = None, status: str = 'ok') -> Response:
    if data is None:
        data = {}
    return aiohttp_json_response(data={'status': status, 'data': data})


def error_json_response(http_status: int, status: Optional[str] = None, message: Optional[str] = None,
                        data: Optional[dict] = None) -> Response:
    if data is None:
        data = {}
    return aiohttp_json_response(status=http_status,
                                 data={
                                     'status': status,
                                     'message': message,
                                     'data': data})


def check_basic_auth(raw_credentials: str, username: str, password: str) -> bool:
    credentials = b64decode(raw_credentials).decode('utf-8')
    try:
        __username, __password = credentials.split(':')
    except ValueError:
        return False

    return __username == username and __password == password


