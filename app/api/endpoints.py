from fastapi import APIRouter, HTTPException
from .schema import LogEntry, LogsResponse, ResultResponse, ScrapeRequest, ScrapeResponse
from app.celery_worker import scrape_url
from app.config import ALLOWED_URLS
from app.models import ScrapingRequest

router = APIRouter()

@router.post("/scrape", response_model=ScrapeResponse)
async def create_scrape_task(scrape_request: ScrapeRequest):
    """
    It scrape the given url data using celery to mantain asyc
    """
    url = str(scrape_request.url)

    # Check if URL is in allowed list
    if url not in ALLOWED_URLS:
        raise HTTPException(
            status_code=400,
            detail=f"Please use one of the allowed URLs: {ALLOWED_URLS}",
        )

    # it store the url in database to get the request id for that
    scraping_request = ScrapingRequest(url=url)
    scraping_request.save()

    # start celery taks
    scrape_url.delay(scraping_request.request_id, url)

    return {"request_id": scraping_request.request_id}


@router.get("/result/{request_id}", response_model=ResultResponse)
async def get_scrape_result(request_id: str):
    """
    Get the results of a scraping task for particular request
    """
    scraping_request = ScrapingRequest.objects(request_id=request_id).first()

    if not scraping_request:
        raise HTTPException(
            status_code=404, detail=f"Request ID {request_id} not found"
        )

    # prepare result 
    results = {
        "status": scraping_request.status,
        "data": scraping_request.data if scraping_request.status == "finished" else [],
    }
    return results


@router.get("/logs", response_model=LogsResponse)
async def get_logs():
    """
    Get logs of all scraping requests
    """
    scraping_requests = ScrapingRequest.objects().order_by("-timestamp")
    logs = []
    for req in scraping_requests:
        log = LogEntry(
            request_id=req.request_id,
            timestamp=req.timestamp.isoformat(),
            status=req.status,
        )
        logs.append(log)

    return {"data": logs}
