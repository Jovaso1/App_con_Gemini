import streamlit as st
import re

def validar_nombre(nombre):
    """Valida si un nombre solo contiene caracteres alfabéticos e inicia con mayúscula."""
    patron = r"^[A-Z][a-zA-Z]*$"
    return re.fullmatch(patron, nombre)

def validar_email(email):
    """Valida una dirección de correo electrónico básica."""
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.fullmatch(patron, email)

def validar_telefono(telefono):
    """Valida un número de teléfono en formato XXX-XXX-XXXX."""
    patron = r"^\d{3}-\d{3}-\d{4}$"
    return re.fullmatch(patron, telefono)

def validar_fecha(fecha):
    """Valida una fecha en formato AA-MM-DD."""
    patron = r"^\d{2}-\d{2}-\d{4}$"
    return re.fullmatch(patron, fecha)

def main():
    st.title("Validador de Formularios")

    nombre = st.text_input("Ingrese su nombre:")
    email = st.text_input("Ingrese su correo electrónico (correo@dominio.com):")
    telefono = st.text_input("Ingrese su número de teléfono (XXX-XXX-XXXX):")
    fecha = st.text_input("Ingrese una fecha (AA-MM-DD):")

    if st.button("Validar"):
        if validar_nombre(nombre):
            st.success("Nombre válido.")
        else:
            st.error("Nombre inválido. Solo se permiten letras y debe iniciar con mayúscula.")

        if validar_email(email):
            st.success("Correo electrónico válido.")
        else:
            st.error("Correo electrónico inválido.")

        if validar_telefono(telefono):
            st.success("Número de teléfono válido.")
        else:
            st.error("Número de teléfono inválido. Use el formato XXX-XXX-XXXX.")

        if validar_fecha(fecha):
            st.success("Fecha válida.")
        else:
            st.error("Fecha inválida. Use el formato AA-MM-DD.")

if __name__ == "__main__":
    main()
