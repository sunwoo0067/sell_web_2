from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.products import router as products_router

app = FastAPI(title="Sell Web API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(products_router, prefix="/api/v1", tags=["products"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Sell Web API"}
