import streamlit as st
from main import run_agent

# Streamlit page setup
st.set_page_config(page_title="Web Research Agent", page_icon="🔍")
st.title("Web Research Agent")

# Input field for user query
st.write("Enter a topic or question, and I'll search the web and summarize the information for you.")
query = st.text_input("Enter your topic or question:")

# Trigger the agent when the button is clicked
if st.button("Get Summary"):
    if not query:
        st.warning("Please enter a search query.")
    else:
        st.info("Searching and summarizing... please wait.")
        result = run_agent(query)
        st.success("Summary:")
        st.write(result)