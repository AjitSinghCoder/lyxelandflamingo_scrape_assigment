# Web Scraper API

A FastAPI-based web scraping backend that extracts product names and prices

## Features

- Asynchronous scraping tasks with Celery
- MongoDB storage with MongoEngine ORM
- RESTful API endpoints for scraping and retrieving results

## Setup Instructions

### Prerequisites

- Python : 3.10.12

### Installation and Setup

1. Install MongoDB
2. Create virtual environment:

   ```
    python3 -m venv myenv
   ```
3. Activate environment
   (a) For Linux / macos
   ```
     source myenv/bin/activate
   ```

   (b) For Windows OS

   ```
     myenv\Scripts\activate
   ```
4. Install Python dependencies:

   ```
   pip3 install -r requirements.txt
   ```
5. Set environment variables:

   ```
   Create .env file in root directory (lyxelandflamingo_scrape_assigment/.env) add required  variable
   As per the sample.env file 
   ```
6. Start the FastAPI server:

   ```
   uvicorn app.main:app --reload
   ```
7. In a separate terminal, start the Celery worker:

   ```
   celery -A app.celery_worker worker --loglevel=info
   ```

## API Usage Examples

    Once your project runs successfully, open this URL: "http://127.0.0.1:8000/docs". Here, you will find the API documentation on how to use it.

    Brief:
      First, send a POST request to the "/scrap" API with a URL from the following list:

      "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
      "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
      "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

      In the response, the API will return a unique request_id. Use this request_id to send a GET request to the "/result" API.
        If the scraping is completed, it will return status: "finished" along with the scraped data.
        If the scraping is not yet completed, it will return status: "pending" with an empty data field.

      The "/logs" API returns a log of all requests, showing how many times you have requested scraped data.


## Do you want to check for pending status  you have to add time.sleep() inside scrape_products function
  