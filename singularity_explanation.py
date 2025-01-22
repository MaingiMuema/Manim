from manim import *

class SingularityExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Understanding Singularities", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Gravitational Singularity
        self.gravitational_singularity()
        self.wait(2)

        # Transition
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

        # Technological Singularity
        self.technological_singularity()
        self.wait(2)

    def gravitational_singularity(self):
        # Title
        title = Text("Gravitational Singularity", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Black hole and spacetime curvature
        black_hole = Dot(radius=0.5, color=BLACK).set_fill(BLACK, opacity=1)
        event_horizon = Circle(radius=1.5, color=WHITE)
        singularity = Dot(radius=0.1, color=RED).move_to(black_hole.get_center())

        self.play(Create(black_hole), Create(event_horizon))
        self.wait(1)

        # Spacetime grid
        grid = NumberPlane()
        self.play(Create(grid))
        self.wait(1)

        # Warp spacetime
        warped_grid = grid.copy().apply_function(
            lambda p: np.array([
                p[0] + 0.5 * np.exp(-p[0]**2 - p[1]**2),
                p[1] + 0.5 * np.exp(-p[0]**2 - p[1]**2),
                0
            ])
        )
        self.play(Transform(grid, warped_grid))
        self.wait(1)

        # Add singularity
        self.play(Create(singularity))
        singularity_label = Text("Singularity", font_size=24).next_to(singularity, DOWN)
        self.play(Write(singularity_label))
        self.wait(2)

        # Explanation
        explanation = Text(
            "A gravitational singularity is a point\n"
            "where gravity becomes infinite,\n"
            "and spacetime curvature is undefined.",
            font_size=24
        ).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(3)

    def technological_singularity(self):
        # Title
        title = Text("Technological Singularity", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Exponential growth curve
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 10],
            axis_config={"color": BLUE},
        )
        labels = axes.get_axis_labels(x_label="Time", y_label="AI Capability")

        self.play(Create(axes), Write(labels))
        self.wait(1)

        # Exponential curve
        curve = axes.plot(lambda x: np.exp(x), color=YELLOW)
        curve_label = Text("Exponential Growth", font_size=24).next_to(curve, UR)
        self.play(Create(curve), Write(curve_label))
        self.wait(1)

        # Singularity point
        singularity_point = Dot(color=RED).move_to(axes.c2p(8, np.exp(8)))
        singularity_label = Text("Singularity", font_size=24).next_to(singularity_point, UR)
        self.play(Create(singularity_point), Write(singularity_label))
        self.wait(1)

        # Explanation
        explanation = Text(
            "The technological singularity is the point\n"
            "where AI surpasses human intelligence,\n"
            "leading to unpredictable changes.",
            font_size=24
        ).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(3)