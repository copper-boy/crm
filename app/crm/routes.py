from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application") -> None:
    from app.crm.views import AddUserView, GetUserView, ListUsersView
    app.router.add_view('/add_user', AddUserView)
    app.router.add_view('/get_user', GetUserView)
    app.router.add_view('/list_users', ListUsersView)

