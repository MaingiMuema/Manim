from manim import *

class GlowingFlowers(Scene):
    def construct(self):
        # Create a glowing flower
        flower = self.create_glowing_flower(num_petals=6, petal_color=YELLOW, center_color=ORANGE)
        flower.move_to(ORIGIN)  # Position the flower at the center

        # Animate the flower growing and glowing
        self.play(DrawBorderThenFill(flower))
        self.wait(2)

        # Create multiple glowing flowers
        flowers = VGroup(*[
            self.create_glowing_flower(num_petals=6, petal_color=color, center_color=ORANGE).move_to(pos)
            for color, pos in zip([PINK, BLUE, GREEN], [LEFT * 3, RIGHT * 3, UP * 2])
        ])

        # Animate multiple flowers
        self.play(LaggedStart(*[DrawBorderThenFill(flower) for flower in flowers], lag_ratio=0.5))
        self.wait(2)

    def create_glowing_flower(self, num_petals=6, petal_color=YELLOW, center_color=ORANGE):
        """Create a glowing flower with a given number of petals."""
        # Create petals
        petals = VGroup(*[
            Circle(radius=0.5, color=petal_color, fill_opacity=0.8)
            for _ in range(num_petals)
        ])

        # Arrange petals in a circular pattern
        angle_step = 360 / num_petals
        for i, petal in enumerate(petals):
            petal.rotate(i * angle_step * DEGREES)
            petal.move_to(1.5 * np.array([np.cos(i * angle_step * DEGREES), np.sin(i * angle_step * DEGREES), 0]))

        # Add glowing effect to petals
        for petal in petals:
            glow = SurroundingRectangle(petal, color=petal_color, buff=0.2, fill_opacity=0.2, stroke_width=0)
            petal.add(glow)

        # Create flower center
        center = Dot(radius=0.3, color=center_color, fill_opacity=1)
        center_glow = SurroundingRectangle(center, color=center_color, buff=0.2, fill_opacity=0.2, stroke_width=0)

        # Combine petals and center into a single flower
        flower = VGroup(petals, center, center_glow)
        return flower