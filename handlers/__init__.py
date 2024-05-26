from aiogram import Router


def setup_routers() -> Router:
    from . import (
        start,
        menu,
        about_us,
        review,
        send_review,
        scrap
    )
    router = Router()
    router.include_router(start.router)
    router.include_router(about_us.router)
    router.include_router(review.router)
    router.include_router(send_review.router)
    router.include_router(scrap.router)
    router.include_router(menu.router)
    return router