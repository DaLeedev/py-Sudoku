# py-Sudoku

Proyecto en Python para resolver Sudokus utilizando dos enfoques diferentes: reconocimiento de imagenes mediante vision por computadora y redes neuronales, y resolucion algorítmica mediante backtracking con satisfaccion de restricciones (CSP).

## Estructura del proyecto

```
py-Sudoku/
├── Sudoku/
│   ├── final.ipynb      # Notebook con el pipeline de vision por computadora
│   ├── modelo.h5        # Modelo de red neuronal entrenado para reconocer digitos
│   └── sudo.png         # Imagen de ejemplo de un Sudoku
├── Backtracking/
│   └── bt-Sudoku.py     # Resolucion de Sudoku mediante backtracking (CSP)
└── README.md
```

## Requisitos y dependencias

### Enfoque de vision por computadora (Sudoku/)

- Python 3.x
- TensorFlow / Keras
- OpenCV (cv2)
- NumPy
- Matplotlib

### Enfoque de backtracking (Backtracking/)

- Python 3.x
- simpleai

## Enfoque de vision por computadora

El notebook `Sudoku/final.ipynb` implementa un pipeline completo para reconocer un Sudoku a partir de una imagen y extraer los digitos. El proceso consta de las siguientes etapas:

1. **Carga y preparacion de datos**: Se cargan los datos del dataset MNIST para entrenar un modelo de reconocimiento de digitos.

2. **Deteccion y recorte del tablero**: Se lee la imagen del Sudoku (`sudo.png`), se convierte a escala de grises, se aplica un umbral binario y se detectan los contornos exteriores para recortar unicamente el tablero.

3. **Procesamiento de la imagen**: Se aplica un filtro gaussiano para reducir el ruido, se binariza la imagen y se eliminan los bordes exteriores del tablero.

4. **Segmentacion de celdas**: Se divide la imagen procesada del tablero en 81 celdas individuales (9x9), cada una guardada como imagen independiente.

5. **Entrenamiento del modelo**: Se entrena una red neuronal convolucional (CNN) con el dataset MNIST, utilizando aumentacion de datos para mejorar la generalizacion. La arquitectura incluye capas convolucionales, max pooling, dropout y capas densas.

6. **Reconocimiento de digitos**: Se utiliza el modelo entrenado para predecir el digito de cada celda. Las celdas vacias (con valor de pixel promedio bajo) se asignan como 0.
