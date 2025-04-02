import logging
import requests
from parsel import Selector
from app.models import ScrapingRequest

logger = logging.getLogger(__name__)

def scrape_products(request_id: str, url: str):
    """
    Scrape product data from the specified URL
    """
    try:
        print("I am here")
        # Get the scraping request document
        scraping_request = ScrapingRequest.objects(request_id=request_id).first()
        if not scraping_request:
            logger.error(f"Scraping request with ID {request_id} not found")
            return
        
        cookies = {
            'test': 'original_toggled_annually',
            'first_visit_url': f'{url}',
            '_gcl_au': '1.1.29290091.1743613200',
            '_gid': 'GA1.2.743844545.1743613201',
            '_ga': 'GA1.1.141634129.1743613201',
            '_ga_Q9KY1T6XJQ': 'GS1.1.1743613200.1.1.1743613892.55.0.0',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        }

        response = requests.get(
            url,
            cookies=cookies,
            headers=headers,
        )

        selector = Selector(response.text)
        names =selector.xpath('//div[@class="col-md-4 col-xl-4 col-lg-4"]//a/text()').getall()
        prices = selector.xpath('//div[@class="col-md-4 col-xl-4 col-lg-4"]//span[@itemprop="price"]/text()').getall()
        
        products_data = []
        for name,price in zip(names, prices):
            prepare_data = {"product_name" : name.strip(), "price" :price}
            products_data.append(prepare_data)

        # Update the document with the scraped data
        scraping_request.data = products_data
        scraping_request.status = "finished"
        scraping_request.save()

        logger.info(
            f"Successfully scraped {len(products_data)} products from {url}"
        )

    except Exception as e:
        logger.error(f"Error while scraping {url}: {str(e)}")
       