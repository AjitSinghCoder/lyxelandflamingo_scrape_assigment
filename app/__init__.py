
import logging
from app.config import MONGODB_URI
from mongoengine import connect
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

try:
    logger.info(f"Connecting to MongoDB: {MONGODB_URI}")
    connect(host=MONGODB_URI)  # Attempt to connect
    logger.info("Connection established successfully")
except Exception as e:
    logger.error(f"MongoDB connection error: {e}")
    sys.exit(1)  # Exit with error

