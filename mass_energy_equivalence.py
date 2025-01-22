from manim import *

class MassEnergyEquivalence(Scene):
    def construct(self):
        # Title
        title = Text("Einstein's Mass-Energy Equivalence", font_size=48, color=BLUE)
        equation = MathTex("E = mc^2", font_size=64, color=YELLOW).next_to(title, DOWN)
        self.play(Write(title), Write(equation))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(equation))

        # Define objects
        mass = 1  # Mass in kg
        speed_of_light = 3e8  # Speed of light in m/s
        energy = mass * speed_of_light**2  # Energy in Joules

        # Create a block to represent mass
        mass_block = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        mass_label = MathTex(f"m = {mass}\,kg", color=WHITE).next_to(mass_block, UP)
        self.play(Create(mass_block), Write(mass_label))
        self.wait(1)

        # Show the speed of light
        speed_of_light_label = MathTex(f"c = {speed_of_light}\,m/s", color=GREEN).next_to(mass_block, DOWN)
        self.play(Write(speed_of_light_label))
        self.wait(2)

        # Animate the transformation of mass into energy
        energy_label = MathTex(f"E = {energy:.2e}\,J", color=RED).next_to(mass_block, RIGHT * 2)
        self.play(
            mass_block.animate.scale(0.5).shift(LEFT * 2),
            FadeOut(mass_label),
            FadeOut(speed_of_light_label),
            Write(energy_label)
        )
        self.wait(2)

        # Highlight the equation E = mc²
        equation = MathTex("E = mc^2", font_size=64, color=YELLOW).to_edge(UP)
        self.play(Write(equation))
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
        scene = MassEnergyEquivalence()
        scene.render()