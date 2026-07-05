"""
=========================================
UI Styles
=========================================

Contains all custom CSS used throughout
the Streamlit application.
"""

import streamlit as st


def load_css():
    """
    Apply custom styling to Streamlit.
    """

    st.markdown(
        """
<style>

/* -------------------------------
   Hide Streamlit Branding
--------------------------------*/

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}


/* -------------------------------
   Main Page
--------------------------------*/

.block-container{

padding-top:2rem;
padding-bottom:2rem;
padding-left:2rem;
padding-right:2rem;

}


/* -------------------------------
   Sidebar
--------------------------------*/

section[data-testid="stSidebar"]{

background:#111827;

border-right:1px solid #2d3748;

}


/* -------------------------------
   Buttons
--------------------------------*/

.stButton>button{

width:100%;

border-radius:10px;

height:46px;

font-weight:600;

font-size:15px;

}


/* -------------------------------
   Text Input
--------------------------------*/

.stTextInput input{

border-radius:12px;

padding:14px;

}


/* -------------------------------
   File Uploader
--------------------------------*/

[data-testid="stFileUploader"]{

border-radius:12px;

}


/* -------------------------------
   Success Box
--------------------------------*/

div[data-testid="stAlert"]{

border-radius:12px;

}


/* -------------------------------
   Chat Message
--------------------------------*/

[data-testid="stChatMessage"]{

border-radius:12px;

padding:12px;

margin-bottom:15px;

}


/* -------------------------------
   Horizontal Divider
--------------------------------*/

hr{

margin-top:25px;

margin-bottom:25px;

}


/* -------------------------------
   Scroll Bar
--------------------------------*/

::-webkit-scrollbar{

width:8px;

}

::-webkit-scrollbar-thumb{

background:#555;

border-radius:20px;

}

::-webkit-scrollbar-track{

background:transparent;

}

</style>
""",
        unsafe_allow_html=True,
    )