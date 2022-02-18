import streamlit as st

from code import helpers
import pandas as pd

st.title("Datos")

st.markdown("Cargue un archivo de datos en formato Fishtalk para su procesamiento.")

c1, c2, c3 = st.columns([3,1,3])

# Upload button
upload_text = "Cargar archivo"
uploaded_file = c1.file_uploader(upload_text)

# Work and use a progress bar
if uploaded_file:
    # Save the file
    input_excel_filepath = "xlsx_data/" + uploaded_file.name
    with open(input_excel_filepath, "wb") as f:
        f.write(uploaded_file.read())

    # Download the processed file
    info_box = st.empty()
    with st.spinner():
        info_box.info("Procesando archivo...")
        output_excel_filepath = helpers.clean_file(input_excel_filepath)
    info_box.empty()
    c3.markdown("\n")
    c3.markdown("Descargar versión procesada")
    filename = output_excel_filepath.split("/")[-1]
    with open(output_excel_filepath, "rb") as fh:
        btn = c3.download_button(
                label="Download file",
                data=fh,
                file_name=filename,
            )
    
    # Load the data into a dataframe
    st.session_state.df = pd.read_excel(output_excel_filepath)
    st.info("Archivo cargado y listo para visualizar.")