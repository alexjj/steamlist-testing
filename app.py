import streamlit as st
text = st.text_area('Type or paste some  text')
if text:
  words = text.split()
  st.write(f'Number of words in your text:\n\n{len(words)}')