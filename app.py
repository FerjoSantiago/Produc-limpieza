import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from articulos import cargar_articulos
from inventarios import cargar_inventario
from historico import cargar_historico
from calculos import (
    calcular_consumo_total,
    calcular_importes,
    calcular_proyeccion,
    detectar_alertas
)

st.set_page_config(page_title="Control Productos de Limpieza", layout="wide")

st.title("📦 Control de Inventarios y Consumo – Productos de Limpieza")

menu = st.sidebar.selectbox(
    "Módulos",
    [
        "Dashboard",
        "Catálogo de Artículos",
        "Inventario y Costos",
        "Alertas y Desviaciones",
        "Histórico y Tendencias"
    ]
)

articulos_df = cargar_articulos()
inventario_df = cargar_inventario()
historico_df = cargar_historico()

if menu == "Dashboard":
    st.header("📊 Indicadores Generales")

    consumo_total = calcular_consumo_total(inventario_df)
    proyeccion = calcular_proyeccion(consumo_total)
    importes = calcular_importes(consumo_total, articulos_df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Consumo Total (piezas)", int(consumo_total.sum()))
    col2.metric("Proyección Mes", int(sum(proyeccion)))
    col3.metric("Gasto Total ($)", f"${sum(importes.values()):,.2f}")

    st.subheader("Proyección por artículo")
    fig, ax = plt.subplots()
    ax.bar(proyeccion.index, proyeccion.values)
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif menu == "Catálogo de Artículos":
    st.header("📋 Catálogo y Límites")
    st.dataframe(articulos_df)

elif menu == "Inventario y Costos":
    st.header("💰 Inventario por Sucursal")
    st.dataframe(inventario_df)

    consumo_total = calcular_consumo_total(inventario_df)
    importes = calcular_importes(consumo_total, articulos_df)

    st.subheader("Costo total por artículo")
    costo_df = pd.DataFrame.from_dict(
        importes, orient="index", columns=["Importe"]
    )
    st.dataframe(costo_df)

elif menu == "Alertas y Desviaciones":
    st.header("🚨 Alertas de Consumo")

    consumo_total = calcular_consumo_total(inventario_df)
    proyeccion = calcular_proyeccion(consumo_total)

    alertas = detectar_alertas(proyeccion, articulos_df)

    if alertas:
        for a in alertas:
            st.error(
                f"⚠️ {a[0]} proyecta {int(a[1])} piezas (máximo permitido {a[2]})"
            )
    else:
        st.success("✅ No se detectan alertas críticas")

elif menu == "Histórico y Tendencias":
    st.header("📈 Históricos 6 Meses")

    st.dataframe(historico_df)

    articulo = st.selectbox(
        "Seleccione artículo",
        historico_df.columns[1:]
    )

    fig, ax = plt.subplots()
    ax.plot(historico_df["Mes"], historico_df[articulo], marker="o")
    ax.set_title(f"Tendencia histórica - {articulo}")
    st.pyplot(fig)
