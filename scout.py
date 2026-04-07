from duckduckgo_search import DDGS
import time
import random
from utils import extract_price

def search_product(query):
    results = []

    try:
        with DDGS() as ddgs:
            search_results = ddgs.text(query, max_results=10)

            for r in search_results:
                title = r.get("title", "")
                link = r.get("href", "")
                snippet = r.get("body", "")

                price = extract_price(title + " " + snippet)

                results.append({
                    "title": title,
                    "price": price,
                    "link": link
                })

                time.sleep(random.uniform(1, 2))

        return results[:5]

    except Exception:
        return []
