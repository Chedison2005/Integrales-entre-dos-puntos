import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Título
st.title("🧮 Calculadora de Integrales con Gráfica")

# Entrada de la función
funcion_str = st.text_input("Ingresa la función a integrar (usa 'x' como variable):", "sin(x)")
x = sp.Symbol('x')

# Tipo de integral
tipo = st.radio("Selecciona el tipo de integral:", ("Indefinida", "Definida"))

# Intenta calcular la integral y graficar
try:
    # Parsear la función
    funcion = sp.sympify(funcion_str)
    funcion_lambd = sp.lambdify(x, funcion, modules=["numpy"])

    # Valores por defecto para el gráfico
    a, b = -10, 10

    if tipo == "Definida":
        a = st.number_input("Límite inferior (a):", value=0.0)
        b = st.number_input("Límite superior (b):", value=1.0)
        resultado = sp.integrate(funcion, (x, a, b))
        st.latex(r"\int_{" + str(a) + r"}^{" + str(b) + r"} " + sp.latex(funcion) + r"\,dx = " + sp.latex(resultado))
    else:
        resultado = sp.integrate(funcion, x)
        st.latex(r"\int " + sp.latex(funcion) + r"\,dx = " + sp.latex(resultado))

    # Graficar función
    st.subheader("📈 Gráfica de la función")

    x_vals = np.linspace(a, b, 400)
    y_vals = funcion_lambd(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f"f(x) = {funcion_str}")
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

except Exception as e:
    st.error(f"Error al procesar la función: {e}")
