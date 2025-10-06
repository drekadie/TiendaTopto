from typing import List, Dict


def get_all_products() -> List[Dict]:
    """
    Return a list of products scraped from various Chilean stores.
    Currently this function returns example data. Replace this with
    real scraping logic for each store (Falabella, Paris, Ripley, etc.).
    Each product dictionary should include at least:
      - name: str
      - store: str
      - price: float
      - original_price: float (or None if unknown)
    """
    products: List[Dict] = [
        {
            "name": "Audífonos Inalámbricos XYZ",
            "store": "Falabella",
            "price": 49990,
            "original_price": 129990,
        },
        {
            "name": "Notebook Gamer ABC",
            "store": "Paris",
            "price": 549990,
            "original_price": 899990,
        },
        {
            "name": "Televisor 55\" 4K",
            "store": "Ripley",
            "price": 279990,
            "original_price": 699990,
        },
        # Puedes añadir más productos de ejemplo aquí
    ]

    return products
