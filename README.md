# Stickman Velocity Tutorial

This project demonstrates the concept of velocity using a simple stickman animation created with Manim.

## Prerequisites

- Python 3.7 or higher
- Manim library

## Installation

1. Install Manim:

```bash
pip install manim
```

2. For high-quality video rendering, you'll need:
   - FFmpeg
   - LaTeX distribution (MiKTeX for Windows, MacTeX for Mac)

## Running the Animation

To render the animation:

```bash
manim -pql velocity_tutorial.py StickmanVelocityScene
```

Options:

- `-p`: Preview the animation after rendering
- `-q`: Render in medium quality
- `-l`: Use a lower resolution
- `-qh`: Render in high quality (slower)

## Understanding the Animation

The animation shows:

1. A stickman moving with constant velocity
2. A yellow velocity vector above the stickman
3. The velocity magnitude labeled in mathematical notation
