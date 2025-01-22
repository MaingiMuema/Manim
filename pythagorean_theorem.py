from manim import *

class PythagoreanTheoremExplainer(Scene):
    def construct(self):
        # Title
        title = Text("The Pythagorean Theorem", font_size=48, color=BLUE)
        subtitle = Text("a² + b² = c²", font_size=36, color=YELLOW)
        subtitle.next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Draw a right-angled triangle
        triangle = Polygon([-2, -1, 0], [2, -1, 0], [2, 2, 0], color=WHITE)
        right_angle = RightAngle(Line([2, -1, 0], [2, 2, 0]), Line([2, -1, 0], [-2, -1, 0]), length=0.3)
        self.play(Create(triangle), Create(right_angle))
        self.wait(1)

        # Label the sides
        a_label = MathTex("a", color=RED).next_to(triangle, DOWN).shift(LEFT * 1.5)
        b_label = MathTex("b", color=GREEN).next_to(triangle, RIGHT).shift(DOWN * 0.5)
        c_label = MathTex("c", color=BLUE).next_to(triangle, UP).shift(RIGHT * 1.5)
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(2)

        # Animate squares on each side
        # Square on side 'a'
        a_square = Square(side_length=3, color=RED).move_to([-3.5, -2.5, 0])
        a_square_label = MathTex("a^2", color=RED).next_to(a_square, DOWN)
        self.play(Create(a_square), Write(a_square_label))
        self.wait(1)

        # Square on side 'b'
        b_square = Square(side_length=4, color=GREEN).move_to([4, -2.5, 0])
        b_square_label = MathTex("b^2", color=GREEN).next_to(b_square, DOWN)
        self.play(Create(b_square), Write(b_square_label))
        self.wait(1)

        # Square on side 'c'
        c_square = Square(side_length=5, color=BLUE).move_to([0, 3.5, 0])
        c_square_label = MathTex("c^2", color=BLUE).next_to(c_square, UP)
        self.play(Create(c_square), Write(c_square_label))
        self.wait(2)

        # Highlight the theorem
        theorem = MathTex("a^2 + b^2 = c^2", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(theorem))
        self.wait(2)

        # Visual proof: Move squares to show a² + b² = c²
        self.play(
            a_square.animate.move_to([-2, 1, 0]),
            b_square.animate.move_to([2, 1, 0]),
            c_square.animate.move_to([0, -2, 0])
        )
        self.wait(2)

        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

        # Final message
        final_message = Text("Thanks for watching!", font_size=48, color=BLUE)
        self.play(Write(final_message))
        self.wait(2)
        self.play(FadeOut(final_message))

if __name__ == "__main__":
    with tempconfig({"quality": "high_quality", "preview": True}):
        scene = PythagoreanTheoremExplainer()
        scene.render()