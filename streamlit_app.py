import streamlit as st
import streamlit_book as stb

import streamlit as st
import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(layout="wide", page_title="DS4F", page_icon=":fish:",)

# Streamit book properties
stb.set_library_config(menu_title="",
                       options=["Introducción", 
                                "Carga de datos", 
                                "Visualización", 
                                "Predicciones", 
                                ], 
                       paths=["pages/intro", 
                              "pages/upload", 
                              "pages/viz", 
                              "pages/predictions",
                              ],
                       icons=["code", 
                              "robot", 
                              "moon", 
                              "alarm", 
                              ],
                       )