import streamlit as st
import awesome_streamlit as ast

def write():
    with st.spinner("Loading About ..."):
        st.markdown(
            """

[<img src="https://i1.wp.com/agelesspartners.com/wp-content/uploads/2020/11/age-logo.jpg" style="max-width: 190px">](https://agelesspartners.com/)
            ## Information


This platform was developed by **Ageless Partners**.

Ageless Partners brings together aging researchers, developers, and entrepreneurs to build new tools, 
raise awareness, and attract talent to the field.

Learn more about Ageless Partners at [www.agelesspartners.com](https://agelesspartners.com/).

---

  **Ageless Partners Team**
  * [Jason C. Mercurio, MFE](https://www.linkedin.com/in/jasonmercurio/)
  * [Daniel Popoola](https://www.linkedin.com/in/daniel-popoola-984233140/)
  * [Diogo Pinto Flórido](https://www.linkedin.com/in/diogopintof/)
  * [Snega R](https://www.linkedin.com/in/snega-r-2809a11a9/)

""",
        unsafe_allow_html=True)