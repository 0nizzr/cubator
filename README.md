# Cubator

Cubator is a simple Python program that uses Pygame and OpenGL to create a 3D rotating cube animation with customizable colors and perspective. The cube is created using vertices, edges, and surfaces, and is rendered using OpenGL commands.

## Installation

To run Cubator, you'll need to have Python 3 installed, as well as the Pygame and PyOpenGL packages. You can install these dependencies using pip:

```
pip install pygame PyOpenGL
```

Alternatively, you can install the dependencies listed in the `requirements.txt` file by running:

```
pip install -r requirements.txt
```

## Usage

To run Cubator, simply run the `cubator.py` file using Python:

```
python3 cubator.py
```

The program will open a window displaying the rotating cube animation. You can adjust the perspective of the animation by modifying the `gluPerspective` function in the `main` function of the `cubator.py` file.

## Credits

cubator was created by [0nizzr](https://twitter.com/0nizzr).
