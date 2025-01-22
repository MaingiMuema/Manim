from manim import *
import numpy as np

class LorenzAttractor(ThreeDScene):
    def construct(self):
        # Set up the scene
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.camera.set_zoom(1.5)  # Adjust the camera zoom to fit the attractor
        
        # Lorenz system parameters
        sigma, rho, beta = 10, 28, 8/3
        dt = 0.01
        num_points = 5000  # Increased number of points for smoother curve
        
        # Initial conditions
        pos = np.array([0.1, 0.1, 0.1])
        points = [pos.copy()]
        
        # Generate points using Lorenz equations
        for _ in range(num_points):
            dx = sigma * (pos[1] - pos[0])
            dy = pos[0] * (rho - pos[2]) - pos[1]
            dz = pos[0] * pos[1] - beta * pos[2]
            
            pos += np.array([dx, dy, dz]) * dt
            points.append(pos.copy())
        
        # Convert points to 3D coordinates and scale them down
        points = np.array(points)
        scale_factor = 0.1  # Scale down the points to fit within the screen
        points *= scale_factor
        
        # Center the points by subtracting the centroid
        centroid = np.mean(points, axis=0)
        points -= centroid
        
        # Create the curve
        curve = VMobject()
        curve.set_points_smoothly([
            np.array([p[0], p[1], p[2]]) for p in points
        ])
        
        # Style the curve with a gradient color
        curve.set_color_by_gradient(BLUE, RED)
        curve.set_stroke(width=2)
        
        # Add 3D axes for reference
        axes = ThreeDAxes()
        
        # Animation
        self.add(axes)  # Add axes to the scene
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(Create(curve), run_time=10)  # Increased run time for smoother animation
        self.wait(10)
        self.stop_ambient_camera_rotation()

if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = LorenzAttractor()
        scene.render()