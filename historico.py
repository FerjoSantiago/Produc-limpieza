import pandas as pd
import numpy as np

def cargar_historico():
    meses = ["Oct", "Nov", "Dic", "Ene", "Feb", "Mar"]
    data = []

    for mes in meses:
        data.append({
            "Mes": mes,
            "Limpiador Multiusos": np.random.randint(300, 520),
            "Desinfectante": np.random.randint(200, 350),
            "Jabón Líquido": np.random.randint(600, 850)
        })

    return pd.DataFrame(data)
