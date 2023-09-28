import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import YoutubeLoader
from langchain.chains.summarize import load_summarize_chain

# Sidebar for taking user API key
st.sidebar.header("API Key")
api_key = st.sidebar.text_input("Enter your API key", type="password")

# Streamlit app
if api_key:
    
    # Load the summarization chain
    llm = ChatOpenAI(openai_api_key=api_key, temperature=0)
    chain = load_summarize_chain(llm, chain_type="refine")
    
    st.title("YouTube Video Summarizer")

    # Input form for YouTube URL
    url = st.text_input("Enter YouTube URL")

    if st.button("Generate Summary"):
        if url:
            # Load YouTube video and generate summary
            loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
            docs = loader.load()
            response = chain.run(docs)

            # Display the summary
            st.subheader("Summary")
            st.write(response)
        else:
            st.warning("Please enter a valid YouTube URL.")

else:
    st.warning("Please enter your API Key")