import streamlit as st
import sympy as sp

# Título de la aplicación
st.title("🧮 Calculadora de Integrales con SymPy")

# Entrada del usuario
funcion_str = st.text_input("Ingresa la función a integrar (usa 'x' como variable):", "sin(x)")
x = sp.Symbol('x')

# Mostrar opciones
tipo = st.radio("Selecciona el tipo de integral:", ("Indefinida", "Definida"))

# Cálculo de la integral
try:
    funcion = sp.sympify(funcion_str)

    if tipo == "Indefinida":
        resultado = sp.integrate(funcion, x)
        st.latex(r"\int " + sp.latex(funcion) + r"\,dx = " + sp.latex(resultado))

    elif tipo == "Definida":
        a = st.number_input("Límite inferior (a):", value=0.0)
        b = st.number_input("Límite superior (b):", value=1.0)
        resultado = sp.integrate(funcion, (x, a, b))
        st.latex(r"\int_{" + str(a) + r"}^{" + str(b) + r"} " + sp.latex(funcion) + r"\,dx = " + sp.latex(resultado))

except Exception as e:
    st.error(f"Error al interpretar la función: {e}")
