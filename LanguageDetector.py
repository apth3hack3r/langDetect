import streamlit as st
from pycountry import languages
st.title("Language Detector")
import fasttext
model = fasttext.load_model('model_q.bin')
st.write("Enter text to Detect language.")
text = st.text_input("")
if st.button('Detect'):
	out=model.predict(text,k=2)
	lang_name_tup=out[0]
	lang_per_arr=out[1]
	for i in range(2):

		lang_name = languages.get(alpha_3=(lang_name_tup[i])[9:]).name
		st.write(lang_name +"\t",end="")
		st.write(lang_per_arr[i]*100)
