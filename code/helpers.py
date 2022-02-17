import streamlit as st

import pandas as pd
import numpy as np

def clean_file(input_file):
    # Define parameters
    if input_file.endswith(".xls"):
        output_file = input_file.replace(".xls", "_clean.xlsx")
    elif input_file.endswith(".xlsx"):
        output_file = input_file.replace(".xlsx", "_clean.xlsx")
    else:
        st.error("El archivo debe ser .xls o .xlsx")
        return None

    # Read excel file
    df = pd.read_excel(input_file, skiprows=1)#, dtype=str)

    # Get a mask of rows to keep
    col3 = df.columns[3]
    m_to_keep = np.logical_not(df[col3].isnull())

    # forward fill of data
    df = df.ffill()

    # keep only rows with data from column 3 (fechas)
    df_out = df[m_to_keep]

    # Save file
    df_out.to_excel(output_file, index=False)

    return output_file