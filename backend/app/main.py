from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import simulacao

app = FastAPI(title="Amora Imovel", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(simulacao.router,prefix='/api/v1')

app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True, log_level="info")