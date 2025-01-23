from manim import *

class MaxwellEquations(Scene):
    def construct(self):
        # Create Maxwell's equations in LaTeX
        maxwell1 = MathTex(r"\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}")
        maxwell2 = MathTex(r"\nabla \cdot \mathbf{B} = 0")
        maxwell3 = MathTex(r"\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}")
        maxwell4 = MathTex(r"\nabla \times \mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial \mathbf{E}}{\partial t}")

        # Arrange equations vertically
        equations = VGroup(maxwell1, maxwell2, maxwell3, maxwell4).arrange(DOWN, buff=0.7)
        
        # Title
        title = Text("Maxwell's Equations", font_size=40)
        title.to_edge(UP)

        # Animate each equation
        self.play(Write(title))
        self.wait(0.5)
        
        for eq in equations:
            self.play(Write(eq))
            self.wait(1)
        
        # Final pause
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(equations))
