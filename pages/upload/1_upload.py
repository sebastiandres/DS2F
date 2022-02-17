import streamlit as st

from code import helpers

st.title("Datos")

st.markdown("""
* Subir el archivo excel a analizar (indicar el formato a utilizar)
* Validar que archivo esté correcto
""")

# Upload button
upload_text = "Cargar un excel de producción Fishtalk"
uploaded_file = st.file_uploader(upload_text)

# Work and use a progress bar
if uploaded_file:
    # Save the file
    input_excel_filepath = "xlsx_data/" + uploaded_file.name
    with open(input_excel_filepath, "wb") as f:
        f.write(uploaded_file.read())

    # Download the processed file
    st.markdown("Descargar versión procesada")
    output_excel_filepath = helpers.clean_file(input_excel_filepath)
    filename = output_excel_filepath.split("/")[-1]
    with open(output_excel_filepath, "rb") as fh:
        btn = st.download_button(
                label="Download",
                data=fh,
                file_name=filename,
            )