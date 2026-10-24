# Hangman 1.0 — Juego del Ahorcado en Consola

Proyecto práctico evaluativo de desarrollo modular en Python para la asignatura **Técnicas de Modelado de Software**.

---

## Información del Estudiante

* **Nombre:** Joseph David Gallego Medina
* **Correo institucional:** j.gallego10@gmail.com
* **Directorio de trabajo:** `hangman_1_0`
* **Lenguaje:** Python 3.x

---

## 📖 Descripción del Proyecto

El programa implementa el tradicional juego del Ahorcado en consola. El sistema selecciona de forma aleatoria una palabra secreta de una lista predefinida en un archivo externo, ocultando sus letras con guiones bajos (`_`). 

El jugador cuenta con **6 vidas** representadas mediante arte ASCII y debe ingresar letras una a una hasta descubrir la palabra o agotar sus intentos.

> 💡 **Nota de diseño:** El proyecto aplica el principio de **modularidad en 3 archivos**, separando estrictamente la lógica principal de los recursos de texto y de los componentes gráficos.

---

## 📁 Estructura Modular del Proyecto

El sistema se distribuye en tres módulos independientes dentro del directorio de trabajo:

1. **`main.py`:** Archivo principal que gestiona el ciclo de vida del juego, la captura y validación de entradas por parte del usuario, el control de turnos y el menú de reinicio.
2. **`words.py`:** Módulo de datos encargado de almacenar el banco de palabras secretas en una lista de Python.
3. **`figures.py`:** Módulo visual que contiene las 7 representaciones en arte ASCII del monigote correspondientes a los estados de las 6 vidas del jugador.

> ⚠️ **Importante:** Los archivos `words.py` y `figures.py` deben residir en la misma carpeta para ser importados directamente por `main.py` sin conflictos de rutas.

---

## 🚀 Instrucciones de Ejecución

### Prerrequisitos
* Tener instalado **Python 3.8 o superior** en el sistema.

### Pasos para ejecutar
1. Abre tu terminal, consola o línea de comandos.
2. Navega hasta el directorio del proyecto:
   ```bash
   cd hangman_1_0
   ```
3. Ejecuta el archivo principal del juego:
   ```bash
   python main.py
   ```
