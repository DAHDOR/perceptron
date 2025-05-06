import numpy as np

def read_weights(path: str) -> tuple[float, np.ndarray]:
    with open(path, 'r', encoding='utf-8') as f: content = f.read().strip()

    parts = [p.strip() for p in content.split(',') if p.strip()]
    if len(parts) < 2: raise ValueError("El archivo debe contener al menos el bias y un peso")

    try: values = [float(p) for p in parts]
    except ValueError: raise ValueError("Valores no válidos en el archivo de configuración")

    bias = values[0]
    weights = np.array(values[1:])

    return bias, weights

def read_vectors(path: str) -> np.ndarray:
    try: return np.loadtxt(path, delimiter=',')
    except Exception as e: raise ValueError(f"Error leyendo vectores: {e}")