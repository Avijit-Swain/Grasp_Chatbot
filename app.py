import streamlit as st
# from langchain.docstore.document import Document
# from io import StringIO
# from langchain.text_splitter import CharacterTextSplitter

# import openai
# from langchain.llms import OpenAI
# import os

# from langchain.chains.summarize import load_summarize_chain
# from langchain.prompts import PromptTemplate
# import textwrap
# import time

# os.environ["OPENAI_API_KEY"] = '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'

# llm = OpenAI(temperature=0)

st.title('Welcome to Grasp')
surgery_type = st.selectbox('Select your surgery type',
            ['Knee Replacement','Hip Replacement','Joint Replacement'])
day = st.selectbox('Select your day of recovery',
            range(1,11))
q1 = st.select_slider('Q1) How would you rate your current level of pain? Express it in percentages between 0-100.',
                      range(0,101))
q2 = st.select_slider('Q2) What percentage of your regular diet did you have?? Express it in percentages between 0-100.',
                      range(0,101))
q3 = st.selectbox('Q3) How was your sleep? Select an option:', ['Very well','Not very well'])
q4 = st.select_slider('Q4) How much of your regular activity were you able to accomplish? Express it in percentages between 0-100.',
                      range(0,101))
q5 = st.select_slider('Q5) What percentage of the pain medication were you able to intake? Express it in percentages between 0-100.',
                      range(0,101))






# label = 'Upload your file here'
# uploaded_file = st.file_uploader(label=label)
# text_splitter = CharacterTextSplitter('')

# if uploaded_file:

#     st.header('Please find the conversation below.')
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     string_data = stringio.read()
#     st.write(string_data)

#     texts = text_splitter.split_text(string_data)
#     docs = [Document(page_content=t) for t in texts[:]]

#     prompt_template = """Given the conversation between a patient and doctor, write a concise summary
#                      of the following: {text} such that when another doctor gets to read the summary, they can
#                     easily understand the patient's past and current condition without going through the entire
#                     conversation."""

#     PROMPT = PromptTemplate(template=prompt_template, 
#                         input_variables=["text"])

#     chain = load_summarize_chain(llm, chain_type="stuff", prompt = PROMPT)
#     output_summary = chain.run(docs)

#     st.header('Please find the summary below.')
#     st.write(output_summary)
