import groq
import streamlit as st
class Groq: 
    def __init__(self):
        # init Client 
        # GROQ_API_KEY = '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'
        self.client = groq.Client(
        api_key= st.secrets["GROQ_API_KEY"]
        )     
        # getting Prompt
        with open('./prompt2.txt', 'r') as myFile: 
            prompt = myFile.read()
        self.sys_msg = {
                    "role": "system", 
                    "content": str(prompt)
                }

    def get_res(self, code: str): 
        chat = self.client.chat.completions.create(
            messages=[
                self.sys_msg,
                {
                    "role": "user", 
                    "content": str(code)
                }
            ],
            model='llama-3.3-70b-versatile'
        )
        content = chat.choices[0].message.content
        comp = content[content.find('O(')-1: content.find(')')+1]

        return comp, content

