import streamlit as st
import re

def evaluar_contrasena(contrasena):
    # Expresión regular para validar la contraseña
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    
    if re.match(patron, contrasena):
        return "La contraseña es segura."
    else:
        sugerencias = []
        if len(contrasena) < 8:
            sugerencias.append("La contraseña debe tener al menos 8 caracteres.")
        if not re.search('[a-z]', contrasena):
            sugerencias.append("La contraseña debe incluir al menos una letra minúscula.")
        if not re.search('[A-Z]', contrasena):
            sugerencias.append("La contraseña debe incluir al menos una letra mayúscula.")
        if not re.search('\d', contrasena):
            sugerencias.append("La contraseña debe incluir al menos un número.")
        if not re.search('[@$!%*?&]', contrasena):
            sugerencias.append("La contraseña debe incluir al menos un caracter especial.")
        return "La contraseña no es segura. Sugerencias: " + ", ".join(sugerencias)

def main():
    st.title("Evaluador de Contraseñas")
    
    contrasena = st.text_input("Ingrese su contraseña")
    
    if st.button("Evaluar"):
        resultado = evaluar_contrasena(contrasena)
        st.write(resultado)

if __name__ == "__main__":
    main()
