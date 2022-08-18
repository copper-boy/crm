from typing import TYPE_CHECKING

from aiohttp.web_exceptions import HTTPForbidden, HTTPUnauthorized

from app.web.utils import check_basic_auth

if TYPE_CHECKING:
    from app.web.app import Request


class AuthMixin:
    def try_auth(self, request: 'Request') -> None:
        if not request.headers.get('Authorization'):
            raise HTTPUnauthorized
        if not check_basic_auth(request.headers.get('Authorization'), username=request.app.config.username,
                                password=request.app.config.password):
            raise HTTPForbidden

