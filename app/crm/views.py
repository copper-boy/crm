from typing import Optional
from uuid import uuid4, UUID

from aiohttp.web_exceptions import HTTPBadRequest
from aiohttp.web_response import Response
from aiohttp_apispec import docs, request_schema, response_schema, querystring_schema

from app.crm.mixins import AuthMixin
from app.crm.models import User
from app.crm.schemas import UserAddSchema, ListUsersResponseSchema, UserGetRequestSchema, UserGetResponseSchema, \
    UserSchema
from app.web.app import View
from app.web.schemas import OkResponseSchema
from app.web.utils import json_response


class AddUserView(View, AuthMixin):
    @docs(tags=['crm'], summary='Add new user', description='Add new user to database')
    @request_schema(UserAddSchema)
    @response_schema(OkResponseSchema, 200)
    async def post(self) -> Response:
        self.try_auth(self.request)

        data = self.request['data']
        user = User(email=data['email'], id=uuid4())
        await self.request.app.crm_accessor.add_user(user)
        return json_response()


class ListUsersView(View, AuthMixin):
    @docs(tags=['crm'], summary='List users', description='List users from database')
    @response_schema(ListUsersResponseSchema, 200)
    async def get(self) -> Response:
        self.try_auth(self.request)

        users = await self.request.app.crm_accessor.list_users()
        raw_users = [UserSchema().dump(user) for user in users]
        return json_response(data={'users': raw_users})


class GetUserView(View, AuthMixin):
    @docs(tags=['crm'], summary='Get user', description='Get user by id from database')
    @querystring_schema(UserGetRequestSchema)
    @response_schema(UserGetResponseSchema, 200)
    async def get(self) -> Optional[Response]:
        self.try_auth(self.request)

        user_id = self.request.query.get('id')
        user = await self.request.app.crm_accessor.get_user(UUID(user_id))
        try:
            return json_response(data={'user': UserSchema().dump(user)})
        except AttributeError:
            raise HTTPBadRequest

