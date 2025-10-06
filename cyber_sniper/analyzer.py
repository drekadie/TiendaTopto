from typing import List, Dict


def detect_anomalies(products: List[Dict]) -> List[Dict]:
    """
    Given a list of product dictionaries, return only those products that
    have an unusually high discount (e.g., >= 80%).

    Each product is expected to have keys: 'price' and 'original_price'.
    """
    anomalies: List[Dict] = []
    for product in products:
        price = product.get("price")
        original_price = product.get("original_price")
        # Ensure both price and original_price are valid numbers
        if price is not None and original_price:
            try:
                discount_fraction = 1 - (float(price) / float(original_price))
                if discount_fraction >= 0.80:
                    anomalies.append(product)
            except (ValueError, ZeroDivisionError):
                # Skip products with invalid numerical values
                continue
    return anomalies
