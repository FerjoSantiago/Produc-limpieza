import pandas as pd
import numpy as np

def cargar_inventario():
    data = {
        "Sucursal": ["0002", "0003", "0004"],
        "Limpiador Multiusos": [180, 260, 340],
        "Desinfectante": [120, 200, 350],
        "Jabón Líquido": [400, 500, 800]
    }
    return pd.DataFrame(data)
