from manim import *

class MultiverseTheory(Scene):
    def construct(self):
        # Title
        title = Text("The Multiverse Theory", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Define objects
        universes = VGroup()
        for i in range(5):
            universe = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).shift(UP * (i - 2) * 1.5)
            universe_label = Text(f"Universe {i+1}", font_size=24, color=WHITE).next_to(universe, DOWN)
            universes.add(universe, universe_label)
        self.play(Create(universes))
        self.wait(2)

        # Animate the universes expanding
        self.play(universes.animate.scale(1.5))
        self.wait(2)

        # Animate the universes moving apart
        self.play(universes.animate.arrange(RIGHT, buff=2))
        self.wait(2)

        # Animate the universes merging
        self.play(universes.animate.arrange(LEFT, buff=0))
        self.wait(2)

        # Animate the universes separating
        self.play(universes.animate.arrange(RIGHT, buff=2))
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
        scene = MultiverseTheory()
        scene.render()