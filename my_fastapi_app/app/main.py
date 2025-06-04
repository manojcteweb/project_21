from fastapi import FastAPI
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
async def read_root():
    logger.info("Root endpoint called")
    return {"Hello": "World"}

# Additional setup for security and other configurations can be added here
