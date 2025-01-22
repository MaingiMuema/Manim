from manim import *

class WaterCycle(Scene):
    def construct(self):
        # Title
        title = Text("The Water Cycle", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Define objects
        ocean = Rectangle(height=2, width=6, color=BLUE, fill_opacity=0.5).shift(DOWN * 3)
        sun = Circle(radius=0.5, color=YELLOW, fill_opacity=0.5).shift(UP * 3 + LEFT * 4)
        cloud = Circle(radius=0.5, color=WHITE, fill_opacity=0.5).shift(UP * 3 + RIGHT * 4)
        cloud.add(Circle(radius=0.4, color=WHITE, fill_opacity=0.5).shift(RIGHT * 0.5 + UP * 0.2))
        cloud.add(Circle(radius=0.3, color=WHITE, fill_opacity=0.5).shift(LEFT * 0.5 + UP * 0.2))
        rain = VGroup(*[Line(start=cloud.get_bottom(), end=cloud.get_bottom() + DOWN * 0.5, color=BLUE) for _ in range(10)])

        # Draw the ocean
        self.play(Create(ocean))
        self.wait(1)

        # Draw the sun
        self.play(Create(sun))
        self.wait(1)

        # Animate evaporation
        evaporation = Arrow(start=ocean.get_top(), end=sun.get_bottom(), color=WHITE)
        evaporation_label = Text("Evaporation", font_size=24, color=WHITE).next_to(evaporation, LEFT)
        self.play(GrowArrow(evaporation), Write(evaporation_label))
        self.wait(2)

        # Draw the cloud
        self.play(Create(cloud))
        self.wait(1)

        # Animate condensation
        condensation = Arrow(start=sun.get_bottom(), end=cloud.get_left(), color=WHITE)
        condensation_label = Text("Condensation", font_size=24, color=WHITE).next_to(condensation, UP)
        self.play(GrowArrow(condensation), Write(condensation_label))
        self.wait(2)

        # Animate precipitation
        precipitation = Arrow(start=cloud.get_bottom(), end=ocean.get_top(), color=BLUE)
        precipitation_label = Text("Precipitation", font_size=24, color=BLUE).next_to(precipitation, RIGHT)
        self.play(GrowArrow(precipitation), Write(precipitation_label))
        self.wait(2)

        # Animate rain
        self.play(Create(rain))
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
        scene = WaterCycle()
        scene.render()