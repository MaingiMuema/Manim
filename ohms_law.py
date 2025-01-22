from manim import *

class OhmsLaw(Scene):
    def construct(self):
        # Title
        title = Text("Ohm's Law", font_size=48, color=BLUE)
        equation = MathTex("V = IR", font_size=64, color=YELLOW).next_to(title, DOWN)
        self.play(Write(title), Write(equation))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(equation))

        # Define objects
        voltage = 12  # Voltage in volts
        current = 2  # Current in amperes
        resistance = voltage / current  # Resistance in ohms

        # Create a circuit diagram
        battery = Rectangle(height=1, width=0.5, color=RED, fill_opacity=0.5).shift(LEFT * 3)
        resistor = Rectangle(height=1, width=0.5, color=BLUE, fill_opacity=0.5).shift(RIGHT * 3)
        wire1 = Line(battery.get_right(), resistor.get_left(), color=WHITE)
        wire2 = Line(resistor.get_right(), battery.get_left(), color=WHITE)
        circuit = VGroup(battery, resistor, wire1, wire2)
        self.play(Create(circuit))
        self.wait(1)

        # Label the components
        voltage_label = MathTex(f"V = {voltage}\,V", color=RED).next_to(battery, UP)
        current_label = MathTex(f"I = {current}\,A", color=GREEN).next_to(wire1, UP)
        resistance_label = MathTex(f"R = {resistance}\,\Omega", color=BLUE).next_to(resistor, UP)
        self.play(Write(voltage_label), Write(current_label), Write(resistance_label))
        self.wait(2)

        # Highlight the equation V = IR
        equation = MathTex("V = IR", font_size=64, color=YELLOW).to_edge(UP)
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
        scene = OhmsLaw()
        scene.render()