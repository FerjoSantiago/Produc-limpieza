import pandas as pd

def cargar_articulos():
    data = {
        "Articulo": ["Limpiador Multiusos", "Desinfectante", "Jabón Líquido"],
        "Max_Mensual": [500, 300, 700],
        "Min_Mensual": [200, 120, 300],
        "Costo_Unitario": [45.0, 60.0, 25.0]
    }
    return pd.DataFrame(data)
