import streamlit as st
import awesome_streamlit as ast

def write():
    with st.spinner("Loading About ..."):
        st.markdown(
            """

The Ageless Platform is a biohacking tool to empower individuals. It includes:

* Compounds database - check the change in life expectancy for given compound based on studying other species.
* Liver Disease Prediction - check if you may have liver disease.
* Hearth Disease Prediction - check if you may have heart disease.

---

  **Ageless Platform Core Contributors**
  * [Jason C. Mercurio, MFE](https://www.linkedin.com/in/jasonmercurio/)
  * [Daniel Popoola](https://www.linkedin.com/in/daniel-popoola-984233140/)

""",
        unsafe_allow_html=True)