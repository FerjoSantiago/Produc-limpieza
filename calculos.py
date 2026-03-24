import pandas as pd

def calcular_consumo_total(inventario_df):
    return inventario_df.drop("Sucursal", axis=1).sum()

def calcular_importes(consumos, articulos_df):
    resultado = {}
    for articulo, piezas in consumos.items():
        costo = articulos_df.loc[
            articulos_df["Articulo"] == articulo, "Costo_Unitario"
        ].values[0]
        resultado[articulo] = piezas * costo
    return resultado

def calcular_proyeccion(consumo_actual, dias_transcurridos=10, dias_mes=30):
    return consumo_actual * (dias_mes / dias_transcurridos)

def detectar_alertas(proyeccion, articulos_df):
    alertas = []
    for articulo, valor in proyeccion.items():
        maximo = articulos_df.loc[
            articulos_df["Articulo"] == articulo, "Max_Mensual"
        ].values[0]
        if valor > maximo:
            alertas.append((articulo, valor, maximo))
    return alertas
