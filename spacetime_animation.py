from manim import *

class IntroScene(Scene):
    def construct(self):
        title = Text("Time and Space", font_size=72)
        subtitle = Text("A Journey Through Physics", font_size=48)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.wait()
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.wait(1)
        
        # Add explanation text
        explanation = Text(
            "Understanding the fabric of our universe",
            font_size=36
        ).next_to(subtitle, DOWN * 2)
        
        self.play(Write(explanation))
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in [title, subtitle, explanation]]
        )

class SpaceTimeGrid(Scene):
    def construct(self):
        # Create a 3D coordinate system
        axes = ThreeDAxes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[-3, 3],
        )
        
        # Labels for axes
        x_label = Text("Space (x)", font_size=24).next_to(axes.x_axis, RIGHT)
        y_label = Text("Space (y)", font_size=24).next_to(axes.y_axis, UP)
        t_label = Text("Time (t)", font_size=24).next_to(axes.z_axis, UP)
        
        # Create and animate grid
        self.play(Create(axes))
        self.play(Write(x_label), Write(y_label), Write(t_label))
        self.wait()
        
        # Add moving particle
        dot = Dot(color=YELLOW)
        path = VMobject()
        path.set_points_smoothly([
            axes.coords_to_point(-2, -2, -2),
            axes.coords_to_point(0, 0, 0),
            axes.coords_to_point(2, 2, 2),
        ])
        
        self.play(
            MoveAlongPath(dot, path),
            Create(path),
            run_time=3
        )
        
        # Add explanation
        explanation = Text(
            "A particle moving through spacetime",
            font_size=32
        ).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(VGroup(axes, x_label, y_label, t_label, dot, path, explanation)))

class TimeDilation(Scene):
    def construct(self):
        # Time dilation explanation
        title = Text("Time Dilation", font_size=48)
        formula = MathTex(
            "t' = \\frac{t}{\\sqrt{1-\\frac{v^2}{c^2}}}"
        )
        explanation = Text(
            "Time slows down as velocity increases",
            font_size=32
        )
        
        formula.next_to(title, DOWN * 2)
        explanation.next_to(formula, DOWN * 2)
        
        self.play(Write(title))
        self.wait()
        self.play(Write(formula))
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(VGroup(title, formula, explanation)))

class RelativityConcepts(Scene):
    def construct(self):
        # Einstein's equation
        equation = MathTex("E = mc^2")
        
        # Light cone visualization
        cone = Surface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                u
            ]),
            u_range=[-2, 2],
            v_range=[0, TAU],
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        
        self.play(Write(equation))
        self.wait()
        
        # Add explanation for E=mc²
        explanation = Text(
            "Mass and energy are equivalent",
            font_size=32
        ).next_to(equation, DOWN)
        
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(VGroup(equation, explanation)))
        
        # Light cone with better explanation
        cone_label = Text(
            "Light Cone: Past and Future",
            font_size=32
        ).to_edge(UP)
        self.play(Write(cone_label))
        self.play(Create(cone))
        self.wait(2)
        self.play(FadeOut(VGroup(cone, cone_label)))

class Conclusion(Scene):
    def construct(self):
        text = Text("Thank you for watching!", font_size=48)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))

def main():
    # This is a test scene
    with tempconfig({"preview": True}):
        scene = SpaceTimeGrid()
        scene.render()

if __name__ == "__main__":
    main()
