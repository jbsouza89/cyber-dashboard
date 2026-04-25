from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Cybersecurity Learning API")

# CORS: deixa qualquer origem acessar (bom pra teste).
# Depois, você pode trocar "*" pelo domínio do seu frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/hello")
def hello():
    return {"message": "Olá, Render! Seu backend FastAPI está no ar."}
