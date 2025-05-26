from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.simulacao import router

app = FastAPI(title="Amora Imovel", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}, 200


def soma(a:float,b:float):
    return a+b

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True, log_level="info")
