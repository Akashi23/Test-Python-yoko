from api.endpoints import login, users, items, stores, orders, visits
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core.config import settings

api_router = FastAPI()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    api_router.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(stores.router, prefix="/stores", tags=["stores"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(visits.router, prefix="/visits", tags=["visits"])
api_router.include_router(items.router, prefix="/items", tags=["items"])