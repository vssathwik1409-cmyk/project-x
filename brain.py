from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

def generate_verdict(user_query, results):
    try:
        context = "\n".join(
            [f"{r['title']} - {r['price']}" for r in results]
        )

        prompt = f"""
You are a smart Indian shopping assistant.

User: {user_query}

Data:
{context}

Give:
- best option
- short comparison
- final verdict (Buy / Wait / Avoid)

Talk like a helpful human.
"""

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception:
        return "Could not generate AI advice. Showing best available options."
