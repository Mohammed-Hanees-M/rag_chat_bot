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
   Hide Sidebar
--------------------------------*/

section[data-testid="stSidebar"]{
display:none;
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
   Toolbar Columns - Remove Container Styling
--------------------------------*/

[data-testid="column"] {

background: transparent !important;

border: none !important;

box-shadow: none !important;

}


/* Remove gap/margin around toolbar columns */

[data-testid="column"] > [data-testid="stVerticalBlockBorderWrapper"] {

background: transparent !important;

border: none !important;

box-shadow: none !important;

padding: 0 !important;

}


/* Buttons
--------------------------------*/

.stButton>button{

border-radius:10px;

height:40px;

font-weight:600;

font-size:14px;

}


/* Buttons in non-toolbar sections */

button:not(.toolbar-card *) {

border-radius: 8px;

}


/* -------------------------------
   Sidebar (if used)
--------------------------------*/

section[data-testid="stSidebar"]{

background:#111827;

border-right:1px solid #2d3748;

}


/* -------------------------------
   Text Input
--------------------------------*/

.stTextInput input{

border-radius:12px;

padding:12px;

font-size:13px;

}


/* -------------------------------
   Selectbox
--------------------------------*/

[data-testid="stSelectbox"] {

border-radius: 8px;

}


/* -------------------------------
   Success Box
--------------------------------*/

div[data-testid="stAlert"]{

border-radius:12px;

padding: 8px 12px;

font-size: 13px;

margin: 0;

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

margin-top:12px;

margin-bottom:12px;

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