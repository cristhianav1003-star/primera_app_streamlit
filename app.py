# Cotizador de reparaciones - Technicell
import pandas as pd
import streamlit as st

# Configuramos la presentación de la aplicación.
st.set_page_config(page_title="Technicell", page_icon="📱")
st.title("Technicell - Cotizador de reparaciones")
st.caption("Ejemplo de clase con datos hipotéticos.")

# 1. Lo que escribe el usuario.
servicios = {"Cambio de pantalla": (150, 2),
             "Cambio de batería": (80, 1),
             "Cambio de puerto de carga": (60, 2),
             "Reparación de software": (40, 1)}

servicio = st.selectbox("Tipo de reparación", list(servicios))
repuestos = st.number_input("Costo de repuestos (S/)", min_value=0.0, value=50.0)
descuento = st.slider("Descuento (%)", 0, 30, 10)

# 2. Calculamos el precio y el tiempo de reparación.
mano_obra, tiempo = servicios[servicio]
subtotal = mano_obra + repuestos
ahorro = subtotal * descuento / 100
total = subtotal - ahorro

# 3. Mostramos los resultados de la cotización.
col1, col2, col3 = st.columns(3)
col1.metric("Precio final", f"S/ {total:.2f}")
col2.metric("Ahorro", f"S/ {ahorro:.2f}")
col3.metric("Tiempo estimado", f"{tiempo} h")

# 4. Presentamos el detalle de los costos.
tabla = pd.DataFrame({
    "Concepto": ["Mano de obra", "Repuestos", "Descuento", "Total"],
    "Importe (S/)": [mano_obra, repuestos, -ahorro, total]
})
st.dataframe(tabla, hide_index=True)
