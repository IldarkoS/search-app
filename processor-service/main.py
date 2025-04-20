from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Processor service is running"}
