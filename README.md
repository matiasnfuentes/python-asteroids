# 🎮 Python Asteroids

A modern take on the classic **Asteroids** arcade game, built with **Python** and **Pygame**. Pilot your triangular spaceship, dodge and blow up lumpy asteroids, collect power-ups, and rack up the high score.

---

## 🧭 What is this project?

This is a Python-based remake and extension of the arcade classic **Asteroids**, featuring:

- 🎮 **Gameplay**: Fly a rotating triangular ship, shoot incoming asteroids that split on impact, dodge fragments, use shields and power-ups, and manage lives to aim for a high score.
- 🧱 **Graphics & Physics**: Procedurally generated lumpy asteroid shapes, friction-based motion, screen wrapping, and smooth ship rotation.
- 🎯 **Collision Detection**: Uses `pygame.mask` for accurate shape collisions—circles, triangles, and irregular polygons.
- 🔌 **Extensible Structure**: Modular architecture to plug in new shooting strategies, shapes, power-ups, and behaviors.

> ✍️ **Note**: This project is an **extension** of the **Asteroids game project** taught in the [Boot.dev Python course](https://boot.dev).  
> Special thanks to the Boot.dev team for their great learning content and inspiration!

---

## 💾 Installation & Running the Game

### Prerequisites

- Python 3.8+
- [`uv`](https://github.com/astral-sh/uv) installed globally

You can install `uv` using:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Steps

```bash
# 1. Clone this repository
git clone https://github.com/matiasnfuentes/python-asteroids.git
cd python-asteroids

# 2. Create a virtual environment using uv
uv venv
source .venv/bin/activate

# 3. Install dependencies
uv pip install pygame

# 4. Run the game
python main.py
```

Use **A/D** to rotate, **W/S** for thrust/brake, and **Space** to shoot.

---

## ⚙️ Game Features

| Feature                 | Description                                                                   |
| ----------------------- | ----------------------------------------------------------------------------- |
| **Ship**                | Rotates and accelerates with momentum and friction; wraps around screen edges |
| **Asteroids**           | Lumpy, procedurally drawn shapes; split into smaller pieces when hit          |
| **Power-Ups & Shields** | Collectable items that protect and assist your ship                           |
| **Scoring & Lives**     | Track score; lose a life on collision; game ends when lives run out           |
| **Collision System**    | Mask-based collision for precise detection of irregular shapes                |

---

## 🗂️ Project Structure

```
.
├── main.py                 # Entry point, game loop setup
├── circleshape.py          # Base class for all shapes
├── asteroid.py             # Asteroid class with splitting logic
├── player.py               # Player ship class with movement and shooting
├── collision_detector.py   # Centralized collision handling
├── explosion.py            # Explosion visual effects
├── shooting_strategies/    # Modular shooting behaviors
├── constants.py            # Settings (screen size, speeds, radii, etc.)
└── assets/                 # Optional assets (fonts, images, sounds)
```

---

## 👋 Thanks for checking it out! Happy asteroid blasting! 🚀
