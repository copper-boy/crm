from typing import TYPE_CHECKING, Optional
from uuid import UUID

from app.crm.models import User

if TYPE_CHECKING:
    from app.web.app import Application


class CrmAccessor:
    def __init__(self) -> None:
        self.app: Optional['Application'] = None

    async def connect(self, app: 'Application') -> None:
        self.app = app

        try:
            self.app.database['users']
        except KeyError:
            self.app.database['users'] = []

    async def disconnect(self) -> None:
        self.app = None

    async def add_user(self, user: User) -> None:
        self.app.database['users'].append(user)

    async def get_user(self, id: UUID) -> Optional[User]:
        for user in self.app.database['users']:
            if user.id == id:
                return user

    async def list_users(self) -> list[User]:
        return self.app.database['users']

