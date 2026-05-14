from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola FastAPI 🐀"


@app.get("/github")
async def url():
    return {"url_profile":"https://github.com/dgroes"}


