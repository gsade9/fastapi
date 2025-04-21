from sqlalchemy.dialects.postgresql import insert
from fastapi import FastAPI
from . import models
from .database import engine
from . import models
from .routers import post, users, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


from .database import engine
from .routers import post, users, auth, vote
from .config import settings

# Create tables
models.Base.metadata.create_all(bind=engine)


print(settings.database_username)


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def read_root():
    return {"message": "Hello World uccessfully deployed from CI/CD pipeline"}
