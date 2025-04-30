# Perceptron

Este proyecto universitario implementa un perceptrón en Python con una interfaz gráfica sencilla basada en CustomTkinter.

## Instrucciones

1. Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd perceptron
    ```

2. Instalación de dependencias:
    ```bash
    pip install .
    ```

    O, usando `uv`:
    ```bash
    uv sync
    ```

## Uso

Para ejecutar la aplicación, abre una terminal y ejecuta:
```bash
python main.py
```

O, usando `uv`:
```bash
uv run main.py
```

Esto abrirá la ventana principal de la interfaz del perceptrón, donde podrás interactuar con el modelo.

## Características

- Interfaz de usuario basada en CustomTkinter para una interacción intuitiva.
- Implementación del algoritmo del perceptrón para clasificación binaria.
- Widgets personalizados para entrada de datos y visualización de resultados.

## Pruebas

Las pruebas unitarias de la implementación del perceptrón se encuentran en el directorio `tests`. Para ejecutarlas, usa:
```bash
pytest tests/test_perceptron.py
```

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.