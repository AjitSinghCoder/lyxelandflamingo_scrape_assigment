from celery import Celery
from app.scraper import scrape_products
from app.config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

# Initialize Celery app
celery_app = Celery(
    'scraper_worker',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)
@celery_app.task(name='tasks.scrape_url')
def scrape_url(request_id: str, url: str):
    " It run task async"
    scrape_products(request_id, url)

    return {"status": "finished", "request_id": request_id}