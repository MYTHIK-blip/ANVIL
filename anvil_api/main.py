from fastapi import FastAPI
from .routers import crucible_router, forge_router

app = FastAPI(title="Anvil Agentic Framework API")

app.include_router(crucible_router.router, prefix="/crucible", tags=["Crucible"])
app.include_router(forge_router.router, prefix="/forge", tags=["Forge"])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Anvil Framework API"}
