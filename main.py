from fastapi import FastAPI

app = FastAPI()

@app.get("/health_check")
def health_check():
    return "healthy"


@app.on_event("startup")
async def startup():
    print("APPLICATION STARTED")
