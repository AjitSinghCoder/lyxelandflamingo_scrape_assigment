import logging
from fastapi import FastAPI
from app.api.endpoints import router
from app.config import MONGODB_URI
from mongoengine import connect
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Create FastAPI app
app = FastAPI(
    title="Web Scraper API",
    description="An API for scraping product information from e-commerce websites",
)



# Include API endpoints
app.include_router(router)

