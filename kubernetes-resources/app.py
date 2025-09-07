import logging
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Get version from environment variable or default
APP_VERSION = os.getenv("APP_VERSION", "v1")

app = FastAPI(
    title="FastAPI ML GitOps App", 
    version=APP_VERSION,
    description="A FastAPI application with ML prediction capabilities for GitOps demonstration"
)

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": f"Hello from FastAPI GitOps {APP_VERSION}!", "status": "running"}

@app.get("/version")
async def version():
    logger.info("Version endpoint accessed")
    return {"version": APP_VERSION, "app": "FastAPI ML GitOps"}

@app.get("/health")
async def health():
    logger.info("Health check endpoint accessed")
    return {"status": "healthy", "version": APP_VERSION}

@app.get("/predict")
async def predict():
    logger.info("Prediction endpoint accessed")
    # Mock ML prediction - in real scenario, this would call your ML model
    import random
    predictions = ["positive", "negative", "neutral"]
    prediction = random.choice(predictions)
    confidence = round(random.uniform(0.7, 0.99), 2)
    
    result = {
        "prediction": prediction,
        "confidence": confidence,
        "model_version": "1.0.0",
        "timestamp": "2025-01-27T12:00:00Z"
    }
    logger.info(f"Prediction made: {result}")
    return result

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting FastAPI application version {APP_VERSION}")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)