import streamlit as st
import re
# Autor de la aplicación
st.markdown("**Autor:** Esta app fue elaborada por Joseph Vargas")
def evaluar_contrasena(contrasena):
    """Evalúa la fortaleza de una contraseña dada.

    Args:
        contrasena (str): La contraseña a evaluar.

    Returns:
        bool: True si la contraseña es segura, False en caso contrario.
    """

    # Expresión regular para validar contraseñas fuertes
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.fullmatch(patron, contrasena) is not None

def main():
    st.title("Evaluador de Contraseñas")
    
    contrasena = st.text_input("Ingrese su contraseña")
    st.text_input("La contraseña debe usar al menos 8 caractares, incluir al menos una letra minúscula, incluir al menos una letra mayúscula, incluir al menos un número y al menos un carácter especial (@, $, !, %, *, ?, &).")

    if contrasena:
        if evaluar_contrasena(contrasena):
            st.success("¡Excelente! Tu contraseña es muy segura.")
        else:
            st.error("Tu contraseña no es lo suficientemente segura. Te recomendamos:")
            if len(contrasena) < 8:
                st.write("- Usar al menos 8 caracteres.")
            if not re.search(r'[a-z]', contrasena):
                st.write("- Incluir al menos una letra minúscula.")
            if not re.search(r'[A-Z]', contrasena):
                st.write("- Incluir al menos una letra mayúscula.")
            if not re.search(r'\d', contrasena):
                st.write("- Incluir al menos un número.")
            if not re.search(r'[@$!%*?&]', contrasena):
                st.write("- Incluir al menos un carácter especial (@, $, !, %, *, ?, &).")

if __name__ == "__main__":
    main()
