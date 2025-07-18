import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calcular_pendiente(x1, y1, x2, y2):
    """
    Calcula la pendiente entre dos puntos.
    
    Args:
        x1, y1: Coordenadas del primer punto
        x2, y2: Coordenadas del segundo punto
    
    Returns:
        float: Pendiente de la recta
    """
    if x2 - x1 == 0:
        return float('inf')  # Pendiente infinita (recta vertical)
    return (y2 - y1) / (x2 - x1)

def ecuacion_recta(x1, y1, pendiente):
    """
    Calcula la ecuación de la recta en forma y = mx + b
    
    Args:
        x1, y1: Coordenadas de un punto conocido
        pendiente: Pendiente de la recta
    
    Returns:
        float: Intercepto b
    """
    if pendiente == float('inf'):
        return None  # Recta vertical
    return y1 - pendiente * x1

def main():
    st.title("📐 Calculadora de Pendiente entre Dos Puntos")
    st.markdown("Esta aplicación calcula la pendiente entre dos puntos y muestra el gráfico de la recta.")
    
    # Crear columnas para organizar la interfaz
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Punto 1")
        x1 = st.number_input("Coordenada X₁", value=0.0, step=0.1, format="%.2f")
        y1 = st.number_input("Coordenada Y₁", value=0.0, step=0.1, format="%.2f")
    
    with col2:
        st.subheader("Punto 2")
        x2 = st.number_input("Coordenada X₂", value=1.0, step=0.1, format="%.2f")
        y2 = st.number_input("Coordenada Y₂", value=1.0, step=0.1, format="%.2f")
    
    # Calcular pendiente
    pendiente = calcular_pendiente(x1, y1, x2, y2)
    
    # Mostrar resultados
    st.subheader("📊 Resultados")
    
    if pendiente == float('inf'):
        st.error("⚠️ **Recta vertical**: La pendiente es infinita (los puntos tienen la misma coordenada X)")
        st.write(f"Ecuación de la recta: **x = {x1}**")
    else:
        st.success(f"🎯 **Pendiente (m)**: {pendiente:.4f}")
        
        # Calcular intercepto
        b = ecuacion_recta(x1, y1, pendiente)
        
        if b >= 0:
            st.write(f"📐 **Ecuación de la recta**: y = {pendiente:.4f}x + {b:.4f}")
        else:
            st.write(f"📐 **Ecuación de la recta**: y = {pendiente:.4f}x - {abs(b):.4f}")
        
        # Interpretación de la pendiente
        if pendiente > 0:
            st.info("📈 **Interpretación**: La recta es creciente (pendiente positiva)")
        elif pendiente < 0:
            st.info("📉 **Interpretación**: La recta es decreciente (pendiente negativa)")
        else:
            st.info("➡️ **Interpretación**: La recta es horizontal (pendiente cero)")
    
    # Distancia entre puntos
    distancia = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    st.write(f"📏 **Distancia entre puntos**: {distancia:.4f}")
    
    # Opción para mostrar gráfico
    st.subheader("📈 Visualización")
    mostrar_grafico = st.checkbox("Mostrar gráfico", value=True)
    
    if mostrar_grafico:
        # Crear el gráfico
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Configurar el rango del gráfico
        x_min = min(x1, x2) - 2
        x_max = max(x1, x2) + 2
        y_min = min(y1, y2) - 2
        y_max = max(y1, y2) + 2
        
        if pendiente != float('inf'):
            # Generar puntos para la recta
            x_vals = np.linspace(x_min, x_max, 100)
            b = ecuacion_recta(x1, y1, pendiente)
            y_vals = pendiente * x_vals + b
            
            # Dibujar la recta
            ax.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'y = {pendiente:.2f}x + {b:.2f}')
        else:
            # Recta vertical
            ax.axvline(x=x1, color='blue', linewidth=2, label=f'x = {x1}')
        
        # Dibujar los puntos
        ax.plot(x1, y1, 'ro', markersize=10, label=f'Punto 1 ({x1}, {y1})')
        ax.plot(x2, y2, 'go', markersize=10, label=f'Punto 2 ({x2}, {y2})')
        
        # Línea punteada entre los puntos
        ax.plot([x1, x2], [y1, y2], 'r--', alpha=0.7, linewidth=1)
        
        # Configurar el gráfico
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('X', fontsize=12)
        ax.set_ylabel('Y', fontsize=12)
        ax.set_title('Recta que pasa por los dos puntos', fontsize=14, fontweight='bold')
        ax.legend()
        
        # Establecer límites
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        
        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)
        
        # Información adicional del gráfico
        with st.expander("ℹ️ Información del gráfico"):
            st.write("- **Puntos rojos y verdes**: Los dos puntos dados")
            st.write("- **Línea azul**: La recta que pasa por ambos puntos")
            st.write("- **Línea roja punteada**: Conexión directa entre los puntos")
            st.write("- **Cuadrícula**: Facilita la lectura de coordenadas")

if __name__ == "__main__":
    main()