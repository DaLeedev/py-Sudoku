# py-Sudoku

Proyecto en Python para resolver Sudokus utilizando dos enfoques diferentes: reconocimiento de imágenes mediante visión por computadora y redes neuronales, y resolución algorítmica mediante backtracking con satisfacción de restricciones (CSP).

## Estructura del proyecto

```
py-Sudoku/
├── Sudoku/
│   ├── final.ipynb      # Notebook con el pipeline de visión por computadora
│   ├── modelo.h5        # Modelo de red neuronal entrenado para reconocer dígitos
│   └── sudo.png         # Imagen de ejemplo de un Sudoku
├── Backtracking/
│   └── bt-Sudoku.py     # Resolución de Sudoku mediante backtracking (CSP)
└── README.md
```

## Requisitos y dependencias

### Enfoque de visión por computadora (Sudoku/)

- Python 3.x
- TensorFlow / Keras
- OpenCV (cv2)
- NumPy
- Matplotlib

### Enfoque de backtracking (Backtracking/)

- Python 3.x
- simpleai

## Enfoque de visión por computadora

El notebook `Sudoku/final.ipynb` implementa un pipeline completo para reconocer un Sudoku a partir de una imagen y extraer los dígitos. El proceso consta de las siguientes etapas:

1. **Carga y preparación de datos**: Se cargan los datos del dataset MNIST para entrenar un modelo de reconocimiento de dígitos.

2. **Detección y recorte del tablero**: Se lee la imagen del Sudoku (`sudo.png`), se convierte a escala de grises, se aplica un umbral binario y se detectan los contornos exteriores para recortar únicamente el tablero.

3. **Procesamiento de la imagen**: Se aplica un filtro gaussiano para reducir el ruido, se binariza la imagen y se eliminan los bordes exteriores del tablero.

4. **Segmentación de celdas**: Se divide la imagen procesada del tablero en 81 celdas individuales (9x9), cada una guardada como imagen independiente.

5. **Entrenamiento del modelo**: Se entrena una red neuronal convolucional (CNN) con el dataset MNIST, utilizando aumentación de datos para mejorar la generalización. La arquitectura incluye capas convolucionales, max pooling, dropout y capas densas.

6. **Reconocimiento de dígitos**: Se utiliza el modelo entrenado para predecir el dígito de cada celda. Las celdas vacías (con valor de píxel promedio bajo) se asignan como 0.

## Enfoque de backtracking

El archivo `Backtracking/bt-Sudoku.py` resuelve un Sudoku modelado como un problema de satisfacción de restricciones (CSP) utilizando la biblioteca `simpleai`.

### Funcionamiento

- **Variables**: Cada celda del tablero 9x9 se representa como una tupla `(fila, columna)`.
- **Dominios**: Las celdas vacías (valor 0) pueden tomar valores del 1 al 9. Las celdas con valores predefinidos tienen un dominio fijo con ese único valor.
- **Restricciones**: Se definen tres tipos de restricciones para garantizar que no haya números repetidos:
  - En cada fila.
  - En cada columna.
  - En cada subcuadro de 3x3.
- **Resolución**: Se utiliza el algoritmo de backtracking proporcionado por `simpleai` para encontrar una asignación válida que satisfaga todas las restricciones.

## Cómo ejecutar

### Backtracking

```bash
pip install simpleai
python Backtracking/bt-Sudoku.py
```

El script imprimirá la solución del Sudoku definido en el código, o un mensaje indicando que no se encontró solución.

### Visión por computadora

1. Instalar las dependencias:

```bash
pip install tensorflow opencv-python numpy matplotlib
```

2. Abrir y ejecutar el notebook `Sudoku/final.ipynb` celda por celda en Jupyter Notebook o JupyterLab.

3. Asegurarse de que la imagen `sudo.png` se encuentre en el directorio `Sudoku/`.
