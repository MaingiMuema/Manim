#!/usr/bin/env python3
from manim import *

class StickmanVelocityScene(Scene):
    def construct(self):
        # Create a grid background for context
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )
        self.add(grid)

        # Create stickman
        head = Circle(radius=0.3, color=WHITE, fill_opacity=1, fill_color=BLACK)
        body = Line(ORIGIN, DOWN * 1.5, color=WHITE)
        arms = Line(LEFT * 0.5, RIGHT * 0.5, color=WHITE).move_to(body.get_top() + DOWN * 0.5)
        legs = VGroup(
            Line(body.get_end(), body.get_end() + DL * 0.5, color=WHITE),
            Line(body.get_end(), body.get_end() + DR * 0.5, color=WHITE)
        )
        stickman = VGroup(head, body, arms, legs)

        # Add facial expression
        eye_left = Dot(point=head.get_center() + LEFT * 0.1 + UP * 0.1, color=WHITE)
        eye_right = Dot(point=head.get_center() + RIGHT * 0.1 + UP * 0.1, color=WHITE)
        mouth = Arc(radius=0.1, start_angle=-PI / 2, angle=PI, color=WHITE).move_to(head.get_center() + DOWN * 0.1)
        stickman.add(eye_left, eye_right, mouth)

        # Initial position
        stickman.move_to(LEFT * 4 + DOWN * 1)

        # Create velocity vector
        vector = Arrow(LEFT, RIGHT, buff=0, color=YELLOW)
        vector.next_to(stickman, UP)

        # Labels
        velocity_label = Text("v = 2 m/s", color=YELLOW, font_size=24)
        velocity_label.next_to(vector, UP)

        # Title
        title = Text("Understanding Velocity", font_size=40, color=BLUE)
        title.to_edge(UP)

        # Animations
        self.play(Write(title))
        self.play(FadeIn(stickman, shift=UP))
        self.play(
            GrowArrow(vector),
            Write(velocity_label)
        )

        # Animate stickman walking
        def walk_animation(mob, dt):
            # Move arms and legs to simulate walking
            mob[2].rotate(0.2 * np.sin(4 * self.renderer.time))  # Arms
            mob[3][0].rotate(0.2 * np.sin(4 * self.renderer.time))  # Left leg
            mob[3][1].rotate(-0.2 * np.sin(4 * self.renderer.time))  # Right leg

        stickman.add_updater(walk_animation)

        # Move stickman with constant velocity
        self.play(
            stickman.animate.shift(RIGHT * 8),
            vector.animate.shift(RIGHT * 8),
            velocity_label.animate.shift(RIGHT * 8),
            run_time=4,
            rate_func=linear
        )

        # Stop updating the stickman's walking animation
        stickman.remove_updater(walk_animation)

        # Final wait
        self.wait(2)