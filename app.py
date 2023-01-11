import streamlit as st


st.title("FD App")
st.subheader("Papa")

st.header("Papa")


st.text('''People love to hate on pigeons for the way they foul up parked cars or flock 
to food scraps on the sidewalk. But with more than 300 species of wild pigeon 
found on Earth—many of them stunning—it’s past time the lowly pigeon gets its coo.''')


#https://www.markdownguide.org/cheat-sheet/
st.markdown(">Papa")

st.caption("Hello")
#https://katex.org/docs/supported.html
st.latex(r"\begin{pmatrix}   a & b \\   c & d\end{pmatrix}")

a={"name":"Manoj" , "age":34}
st.json(a)


code='''

print('Hello World!!')
'''

st.code(code)



st.code(code,language='python')
