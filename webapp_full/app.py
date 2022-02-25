import streamlit as st
import awesome_streamlit as ast
import pages.info
import pages.liver
import pages.heart
import pages.drugs

PAGES = {
    "Information": pages.info,
    "Compounds Database": pages.drugs,
    "Liver Disease Prediction": pages.liver,
    "Heart Disease Prediction": pages.heart,
}

def main():
    
    st.set_page_config(page_title = "Ageless Partners | Disease prediction")

    st.sidebar.markdown(
        """
        [<img src="https://i2.wp.com/agelesspartners.com/wp-content/uploads/2021/10/age-software-logo.jpg" style="max-width: 302px" >](https://agelesspartners.com/ageless-software/)
        """,
        unsafe_allow_html=True)
    #st.sidebar.title("Navigation")
    selection = st.sidebar.selectbox("", list(PAGES.keys()))

    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

    st.sidebar.title("")
    st.sidebar.info(
        """
        This app is built by **Ageless Partners** for **biohackers**.
        """
    )

if __name__ == "__main__":
    main()