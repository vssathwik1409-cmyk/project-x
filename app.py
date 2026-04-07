import streamlit as st
from scout import search_product
from brain import generate_verdict
from utils import interpret_query

st.set_page_config(page_title="Project X", layout="wide")

st.title("🚀 Project X — Smart Buying Assistant")

user_input = st.text_input("What are you looking for?")

if st.button("Search"):
    if not user_input:
        st.warning("Enter something first")
    else:
        query = interpret_query(user_input)

        with st.spinner("Scanning market..."):
            results = search_product(query)

            if not results:
                st.error("No results found")
            else:
                verdict = generate_verdict(user_input, results)

                for r in results:
                    st.write(f"**{r['title']}**")
                    st.write(f"💰 {r['price']}")
                    st.write(f"[View]({r['link']})")
                    st.write("---")

                st.success(verdict)               
