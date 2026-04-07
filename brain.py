from groq import Groq
import streamlit as st

# Load API key safely from Streamlit secrets
if "GROQ_API_KEY" not in st.secrets:
    raise ValueError("GROQ_API_KEY not found in Streamlit secrets")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def generate_verdict(user_query, results):
    try:
        if not results:
            return "I couldn't find enough data to give a solid recommendation."

        context = "\n".join(
            [f"{r['title']} - {r['price']}" for r in results]
        )

        prompt = f"""
You are a smart and friendly Indian shopping assistant.

User said: "{user_query}"

Here are some market options:
{context}

Your job:
- Talk like a human (not robotic)
- Compare options briefly
- Highlight the best deal
- Give a clear final verdict: Buy / Wait / Avoid

Keep it short, practical, and confident.
"""

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ AI couldn't analyze properly. Showing raw results instead.\nError: {str(e)}"
