from typing import TYPE_CHECKING

from app.store.crm.accessor import CrmAccessor

if TYPE_CHECKING:
    from app.web.app import Application


def setup_accessors(app: "Application") -> None:
    app.crm_accessor = CrmAccessor()
    app.on_startup.append(app.crm_accessor.connect)
    app.on_cleanup.append(app.crm_accessor.disconnect)

