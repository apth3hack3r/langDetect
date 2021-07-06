import streamlit as st

st.markdown(r'<div style="text-align: center"> <h1><ins>Quiz App</ins></h1> </div>', unsafe_allow_html=True)
st.write("")


descs=["Apan","Idiot!!","Pattren","Bacche","Arey main so gaya tha","Tune order kiya hai to tu hi khaega","Arey mereko batati na tera birthday hai, main cdc se cake bhijwa deta tere gharpe","Ruko pehle main tera github set karwata hu: peter hai mori maiya","Pitne ke kaam kar raha hai tu ab"]

img_urls=["https://i.imgflip.com/amucx.jpg",
"https://i.redd.it/w3kr4m2fi3111.png",
"https://i.imgflip.com/amucx.jpg",
"https://i.redd.it/w3kr4m2fi3111.png",
"https://i.redd.it/w3kr4m2fi3111.png",
"https://i.redd.it/w3kr4m2fi3111.png",
"https://i.redd.it/w3kr4m2fi3111.png",
"https://i.redd.it/w3kr4m2fi3111.png",
"https://i.redd.it/w3kr4m2fi3111.png",
"https://i.redd.it/w3kr4m2fi3111.png"]

values=["Peter","Jayati","Sonia Khetrapaul","Parul Singh","Peter","Jayati","Rohit Bhaiya","Peter","Maddy","Jayati"]

# Initializing state variables

if 'key' not in st.session_state:
	st.session_state.key = 0

if 'desc' not in st.session_state:
	st.session_state.desc = descs[0]

if 'img_url' not in st.session_state:
	st.session_state.img_url = img_urls[0]

if 'value' not in st.session_state:
	st.session_state.value = values[0]


if 'score_bar' not in st.session_state:
	st.session_state.score_bar = st.progress(0)


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
	if(text_input.lower()==values[st.session_state.key].lower()):
		st.session_state.key=st.session_state.key+1
		st.session_state.desc=descs[st.session_state.key]
		st.session_state.img_url=img_urls[st.session_state.key]
		st.session_state.value=values[st.session_state.key]
		score = st.session_state.key
		st.session_state.score_bar.progress(score) 
		st.success("WELL DONE!!!")
	else:
		st.error("Error!!! Wrong answer!")
	

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
		st.form_submit_button(label='Check answer',on_click=form_callback)

