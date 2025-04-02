import os
from dotenv import load_dotenv
load_dotenv()

MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")
PORT = os.getenv("PORT")
HOST = os.getenv("HOST")
MONGODB_URI =f"mongodb://{HOST}:{PORT}/{MONGODB_DB_NAME}"

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

ALLOWED_URLS = [
    "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets",
    "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops",
    "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
]