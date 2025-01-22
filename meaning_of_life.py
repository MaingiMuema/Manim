from manim import *

class MeaningOfLife(Scene):
    def construct(self):
        # Introduction
        self.introduction()
        self.wait(2)

        # Connection
        self.connection()
        self.wait(2)

        # Growth
        self.growth()
        self.wait(2)

        # Purpose
        self.purpose()
        self.wait(2)

        # Existence
        self.existence()
        self.wait(2)

        # Conclusion
        self.conclusion()
        self.wait(3)

    def introduction(self):
        # Pose the question
        question = Text("What is the meaning of life?", font_size=48, gradient=(BLUE, TEAL))
        self.play(Write(question, run_time=2))
        self.wait(2)
        self.play(FadeOut(question, shift=UP))

    def connection(self):
        # Show interconnectedness
        title = Text("Connection", font_size=36, gradient=(YELLOW, ORANGE)).to_edge(UP)
        self.play(FadeIn(title, shift=DOWN))

        # Create nodes and links
        nodes = VGroup(*[Dot(radius=0.2, color=BLUE) for _ in range(6)])
        nodes.arrange_in_grid(rows=2, cols=3, buff=2)
        
        # Add a glowing effect to nodes using SurroundingRectangle
        for node in nodes:
            glow = SurroundingRectangle(node, color=BLUE, buff=0.2, fill_opacity=0.2, stroke_width=0)
            self.add(glow, node)

        links = VGroup(
            Line(nodes[0], nodes[1], color=WHITE, stroke_width=2),
            Line(nodes[1], nodes[2], color=WHITE, stroke_width=2),
            Line(nodes[0], nodes[3], color=WHITE, stroke_width=2),
            Line(nodes[3], nodes[4], color=WHITE, stroke_width=2),
            Line(nodes[4], nodes[5], color=WHITE, stroke_width=2),
            Line(nodes[2], nodes[5], color=WHITE, stroke_width=2),
        )

        self.play(LaggedStart(*[GrowFromCenter(node) for node in nodes], lag_ratio=0.2))
        self.play(LaggedStart(*[Create(link) for link in links], lag_ratio=0.2))
        self.wait(1)

        # Highlight connections
        for link in links:
            self.play(link.animate.set_color(BLUE).set_stroke_width(4), run_time=0.5)
        self.wait(1)

        # Explanation
        explanation = Text(
            "Life is about connections:\n"
            "with others, with nature, and with ourselves.",
            font_size=24, gradient=(BLUE, GREEN)
        ).to_edge(DOWN)
        self.play(FadeIn(explanation, shift=UP))
        self.wait(2)
        self.play(FadeOut(VGroup(nodes, links, explanation, title)))

    def growth(self):
        # Show growth
        title = Text("Growth", font_size=36, gradient=(GREEN, YELLOW)).to_edge(UP)
        self.play(FadeIn(title, shift=DOWN))

        # Draw a growing tree
        trunk = Rectangle(height=3, width=0.5, color=rgb_to_color([0.65, 0.16, 0.16])).to_edge(DOWN)
        leaves = VGroup(*[
            Circle(radius=0.5, color=GREEN, fill_opacity=0.8).move_to(trunk.get_top() + UP * i + LEFT * j)
            for i in range(3)
            for j in [-1, 0, 1]
        ])

        # Add a glowing effect to leaves using SurroundingRectangle
        for leaf in leaves:
            glow = SurroundingRectangle(leaf, color=GREEN, buff=0.2, fill_opacity=0.2, stroke_width=0)
            self.add(glow, leaf)

        self.play(GrowFromCenter(trunk))
        self.wait(0.5)
        self.play(LaggedStart(*[GrowFromCenter(leaf) for leaf in leaves], lag_ratio=0.2))
        self.wait(1)

        # Explanation
        explanation = Text(
            "Life is about growth:\n"
            "learning, evolving, and becoming who we are.",
            font_size=24, gradient=(GREEN, BLUE)
        ).to_edge(DOWN)
        self.play(FadeIn(explanation, shift=UP))
        self.wait(2)
        self.play(FadeOut(VGroup(trunk, leaves, explanation, title)))

    def purpose(self):
        # Show purpose
        title = Text("Purpose", font_size=36, gradient=(PURPLE, PINK)).to_edge(UP)
        self.play(FadeIn(title, shift=DOWN))

        # Draw a path leading to a star
        path = Line(LEFT * 4, RIGHT * 4, color=WHITE, stroke_width=2).to_edge(DOWN)
        star = Star(n=5, color=YELLOW, fill_opacity=1).scale(0.5).move_to(path.get_end() + UP * 2)
        dot = Dot(color=BLUE).move_to(path.get_start())

        # Add a glowing effect to the star and dot using SurroundingRectangle
        star_glow = SurroundingRectangle(star, color=YELLOW, buff=0.2, fill_opacity=0.2, stroke_width=0)
        dot_glow = SurroundingRectangle(dot, color=BLUE, buff=0.2, fill_opacity=0.2, stroke_width=0)

        self.play(Create(path), FadeIn(star, shift=DOWN), FadeIn(star_glow))
        self.wait(0.5)
        self.play(FadeIn(dot, shift=UP), FadeIn(dot_glow))
        self.play(dot.animate.move_to(path.get_end()), run_time=3)
        self.wait(1)

        # Explanation
        explanation = Text(
            "Life is about purpose:\n"
            "finding what drives us and pursuing it.",
            font_size=24, gradient=(PURPLE, BLUE)
        ).to_edge(DOWN)
        self.play(FadeIn(explanation, shift=UP))
        self.wait(2)
        self.play(FadeOut(VGroup(path, star, dot, star_glow, dot_glow, explanation, title)))

    def existence(self):
        # Show existence
        title = Text("Existence", font_size=36, gradient=(ORANGE, RED)).to_edge(UP)
        self.play(FadeIn(title, shift=DOWN))

        # Create a galaxy-like spiral
        spiral = VGroup()
        for i in range(100):
            dot = Dot(radius=0.05, color=interpolate_color(BLUE, WHITE, i / 100))
            angle = i * 0.2
            radius = i * 0.05
            dot.move_to(radius * np.array([np.cos(angle), np.sin(angle), 0]))

            # Add a glowing effect to the dot using SurroundingRectangle
            glow = SurroundingRectangle(dot, color=interpolate_color(BLUE, WHITE, i / 100), buff=0.1, fill_opacity=0.2, stroke_width=0)
            spiral.add(glow, dot)

        self.play(Create(spiral, run_time=3))
        self.wait(1)

        # Explanation
        explanation = Text(
            "Life is about existence:\n"
            "embracing the mystery and beauty of being.",
            font_size=24, gradient=(ORANGE, YELLOW)
        ).to_edge(DOWN)
        self.play(FadeIn(explanation, shift=UP))
        self.wait(2)
        self.play(FadeOut(VGroup(spiral, explanation, title)))

    def conclusion(self):
        # Conclusion
        conclusion_text = Text(
            "The meaning of life is not a single answer,\n"
            "but a journey of connection, growth, purpose, and existence.",
            font_size=36, gradient=(TEAL, BLUE), line_spacing=1.5
        )
        self.play(Write(conclusion_text, run_time=3))
        self.wait(3)
        self.play(FadeOut(conclusion_text))