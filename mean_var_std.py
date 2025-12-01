import numpy as np

def calculate(list_of_numbers):
    # Paso 1: Validación de longitud
    if len(list_of_numbers) != 9:
        # Aumenta la excepción ValueError con el mensaje exacto requerido
        raise ValueError("List must contain nine numbers.")
    
    # Paso 2: Convertir a array 3x3
    arr = np.array(list_of_numbers).reshape(3, 3)
    
    # Helper para convertir escalares numpy a python (float o int)
    # Esto es crucial para asegurar que el resultado aplanado (flattened)
    # sea un tipo nativo de Python, como exigen las pruebas.
    def scalar_to_native(x):
        return x.item()
    
    # Paso 3 y 4: Calcular y construir el diccionario
    calculations = {
        'mean': [
            np.mean(arr, axis=0).tolist(),    # Media por columnas (axis=0)
            np.mean(arr, axis=1).tolist(),    # Media por filas (axis=1)
            scalar_to_native(np.mean(arr))    # Media del array aplanado
        ],
        'variance': [
            np.var(arr, axis=0).tolist(),     # Varianza por columnas
            np.var(arr, axis=1).tolist(),     # Varianza por filas
            scalar_to_native(np.var(arr))     # Varianza del array aplanado
        ],
        'standard deviation': [
            np.std(arr, axis=0).tolist(),     # Desviación estándar por columnas
            np.std(arr, axis=1).tolist(),     # Desviación estándar por filas
            scalar_to_native(np.std(arr))     # Desviación estándar aplanada
        ],
        'max': [
            np.max(arr, axis=0).tolist(),     # Máximo por columnas
            np.max(arr, axis=1).tolist(),     # Máximo por filas
            scalar_to_native(np.max(arr))     # Máximo aplanado
        ],
        'min': [
            np.min(arr, axis=0).tolist(),     # Mínimo por columnas
            np.min(arr, axis=1).tolist(),     # Mínimo por filas
            scalar_to_native(np.min(arr))     # Mínimo aplanado
        ],
        'sum': [
            np.sum(arr, axis=0).tolist(),     # Suma por columnas
            np.sum(arr, axis=1).tolist(),     # Suma por filas
            scalar_to_native(np.sum(arr))     # Suma aplanada
        ]
    }
    
    return calculations

if __name__ == "__main__":
    # Ejemplo de uso para verificar la salida
    ejemplo = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(calculate(ejemplo))
    try:
        calculate([1, 2, 3])
    except ValueError as e:
        print(f"Error esperado: {e}")
