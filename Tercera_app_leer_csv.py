import streamlit as st
import pandas as pd
import re
import xlsxwriter

def extraer_info(row):
    nombre = re.search(r'^[A-Z][a-zA-Z]*', row['cliente']).group()
    email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-zA-Z]{2,4}\b', row['cliente']).group()
    telefono = re.search(r'\d{3}-\d{3}-\d{4}', row['cliente']).group()
    return nombre, email, telefono

def procesar_csv(file):
    df = pd.read_csv(file)
    df[['nombre', 'email', 'telefono']] = df.apply(extraer_info, axis=1, result_type='expand')
    return df

def crear_excel(df):
    with pd.ExcelWriter('output.xlsx') as writer:
        df.to_excel(writer, index=False)

def main():
    st.title("Procesador de CSV a Excel")

    uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

    if uploaded_file is not None:
        df = procesar_csv(uploaded_file)
        crear_excel(df)
        st.success("¡Archivo Excel generado exitosamente!")

if __name__ == "__main__":
    main()
