from fastapi import FastAPI

app = FastAPI(title="Payments API")

@app.get("/")
def root():
    return {"message": "Payments API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
