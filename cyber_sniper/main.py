from fastapi import FastAPI
from typing import List, Dict

# Import local modules
from analyzer import detect_anomalies
from scraper.scraper import get_all_products

app = FastAPI()

@app.get("/products")
def list_products() -> List[Dict]:
    """
    Returns all scraped products.
    """
    return get_all_products()

@app.get("/anomalies")
def list_anomalies() -> List[Dict]:
    """
    Returns products with anomalous discounts.
    """
    products = get_all_products()
    anomalies = detect_anomalies(products)
    return anomalies
