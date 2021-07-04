import streamlit as st

st.markdown(r'<div style="text-align: center"> <h1><ins>Quiz App</ins></h1> </div>', unsafe_allow_html=True)
st.write("")

values=["tabar1",
"tabar2",
"tabar3",
"tabar4"]

img_urls=["https://i.imgflip.com/amucx.jpg",
"https://i.redd.it/w3kr4m2fi3111.png",
"https://i.imgflip.com/amucx.jpg",
"https://i.redd.it/w3kr4m2fi3111.png"]

descs=[" One of the QR code has link to meet, Find it and join the meet. We will give you the key for this level",
"2nd Description",
"3rd Description",
"4th Description"]

# Initializing state variables

if 'key' not in st.session_state:
	st.session_state.key = 0

if 'desc' not in st.session_state:
	st.session_state.desc = descs[0]

if 'img_url' not in st.session_state:
	st.session_state.img_url = img_urls[0]

if 'value' not in st.session_state:
	st.session_state.value = values[0]





# Aligning Image to Center (jugaadu way).

col1, col2, col3 = st.beta_columns([1,5,1])

with col1:
	st.write("")

with col2:
	st.image(st.session_state.img_url)

with col3:
	st.write("")

# Description using markdown so that it is center aligned.

st.markdown(r' <div style="text-align: center"> '+ st.session_state.desc + '</div>', unsafe_allow_html=True)


def form_callback():
	if(text_input==values[st.session_state.key]):
		st.session_state.key=st.session_state.key+1
		st.session_state.desc=descs[st.session_state.key]
		st.session_state.img_url=img_urls[st.session_state.key]
		st.session_state.value=values[st.session_state.key]
		st.write("WELL DONE!!!")





with st.form(key='my_form'):
	text_input = st.text_input("")
	col1, col2, col3 , col4, col5, col6, col7 = st.beta_columns(7)
	with col1:
		pass
	with col2:
		pass
	with col3:
		pass
	with col5:
		pass
	with col6:
		pass
	with col7:
		pass
	with col4 :
		submit_button = st.form_submit_button(label='Check',on_click=form_callback)

