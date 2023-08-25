import streamlit as st
# from langchain.docstore.document import Document
# from io import StringIO
# from langchain.text_splitter import CharacterTextSplitter

import openai
from langchain.llms import OpenAI
import os
from langchain import PromptTemplate, LLMChain

os.environ['OPENAI_API_KEY'] = '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'

# from langchain.chains.summarize import load_summarize_chain
# from langchain.prompts import PromptTemplate
# import textwrap
# import time

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


llm = OpenAI(temperature=0)

st.header('AI Conversation')
# question = st.text_input('Please put your question here:')

# if question:
#     output = 'Ans: ' + llm(question)
#     st.write(output)

prompt = PromptTemplate(
    input_variables = ['surgery_type','day','q1','q2','q3','q4','q5'],
    template = '''You are a knee replacement surgeon with 30 years of experience, who performed a knee replacement surgery 
    on me yesterday. Today is day 1 of the post operation recovery process. Here are the questions to which I have 
    already provided my responses. They are as follows in between double quotes:

    """
    Q1) Select your surgery type.
    Response: {surgery_type} 
    Q2) Select your day of recovery.
    Response: {day}
    Q3) How would you rate your current level of pain? Express it in percentages between 0-100.
    Response: {q1} 
    Q4) What percentage of your regular diet did you have?? Express it in percentages between 0-100.
    Response: {q2}
    Q5) How was your sleep? Select an option:
    Response: {q3}
    Q6) How much of your regular activity were you able to accomplish? Express it in percentages between 0-100.
    Response: {q4}
    Q7) What percentage of the pain medication were you able to intake? Express it in percentages between 0-100.
    Response: {q5} 
   
    Now, you need to ask me 5 open ended questions to investigate further about my condition based on the above responses. 

    The questions that you ask me should be as if a real surgeon is asking in real life to understand the patient's condition 
    in depth. Remember you are a real surgeon who knows what question to ask after another and in which order.

    Tone: conversational, spartan, use less corporate jargon'''
)
# st.write(prompt.format(surgery_type = surgery_type, day = day, q1 = q1,
#                         q2 = q2, q3 = q3, q4 = q4, q5 = q5))

button = st.button('Generate Dynamic Questions')

if button:
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(surgery_type = surgery_type, day = day, q1 = q1,
                      q2 = q2, q3 = q3, q4 = q4, q5 = q5)
    st.write(response)
    













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
