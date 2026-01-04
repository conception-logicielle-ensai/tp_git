from fastapi import FastAPI

from app.controller.book_controllers import book_router
from app.db.init_db import init_db

app = FastAPI(title="Library API")

init_db()

app.include_router(book_router)

if __name__ == "__main__":
    import uvicorn

    # Run server
    uvicorn.run(app, host="0.0.0.0", port=8000)
