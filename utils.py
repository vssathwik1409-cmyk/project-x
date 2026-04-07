import re

def extract_price(text):
    match = re.search(r'₹\s?[\d,]+', text)
    return match.group() if match else "N/A"


def interpret_query(user_input):
    user_input = user_input.lower()

    if "phone" in user_input:
        category = "smartphone"
    elif "tv" in user_input:
        category = "television"
    elif "laptop" in user_input:
        category = "laptop"
    else:
        category = user_input

    return f"{category} price India"
