import streamlit as st
from Plot import Plot
from Groq import Groq
from io import StringIO
from detect_lang import extension_language_map

st.set_page_config(layout="wide")


# init session states
if 'client' not in st.session_state:
    st.session_state.client = Groq()
    st.session_state.res = ''
    st.session_state.comp = 'NA'
    st.session_state.lang = None
    st.session_state.code_as_text = ''

with st.sidebar: 
    code_as_file = st.file_uploader('Upload the code file')
    if code_as_file: 
        stringio = StringIO(code_as_file.getvalue().decode("utf-8"))
        language = extension_language_map[str(code_as_file.name).split('.')[1]]
        code_as_text = stringio.read()
        st.code(code_as_text,language=language, height=400)
        
    else: 
        code_as_text = st.text_area(label=" ", placeholder="Insert your code", label_visibility='collapsed')
        language = st.selectbox("Select Language:", options=extension_language_map.keys())
    if language and code_as_text:
        clicked = st.button("Analyse My Code",use_container_width= True)
        if clicked:
            st.session_state.code_as_text = code_as_text
            st.session_state.lang = language
            st.session_state.comp , st.session_state.res = st.session_state.client.get_res(st.session_state['code_as_text'])


if st.session_state.lang != None :
    st.title(''':violet-background[*Analyzed Code*:]''')
else: 
    st.title(''':violet-background[*You Need To Insert Your Code*:]''', help="You can insert your code using the side bar!")

col1, col2 = st.columns([0.5, 0.5], vertical_alignment='top', border=True, gap="large")
with col1:
    st.subheader("*Your Code:*",divider = "violet")
    st.code(st.session_state.res, language=st.session_state.lang, wrap_lines=True,height= 550)


with col2: 
    st.subheader("*Time Complexity:*",divider = "violet")
    p = Plot()
    p.draw(st.session_state.comp.strip())
    fig = p.get_fig()
    st.pyplot(fig, use_container_width=True)