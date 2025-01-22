from manim import *

class BubbleUniverses(Scene):
    def construct(self):
        # Title
        title = Text("Bubble Universes (Level II Multiverse)").scale(0.8)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Create a higher-dimensional space
        space = NumberPlane()
        self.play(Create(space))
        self.wait(1)

        # Create bubbles representing different universes
        bubble1 = Circle(radius=1, color=BLUE).shift(LEFT * 3)
        bubble2 = Circle(radius=1.5, color=RED).shift(RIGHT * 3)
        bubble3 = Circle(radius=0.8, color=GREEN).shift(UP * 2 + LEFT * 1)
        bubble4 = Circle(radius=1.2, color=YELLOW).shift(DOWN * 2 + RIGHT * 1)

        self.play(
            GrowFromCenter(bubble1),
            GrowFromCenter(bubble2),
            GrowFromCenter(bubble3),
            GrowFromCenter(bubble4)
        )
        self.wait(2)

        # Animate collisions between bubbles
        self.play(
            bubble1.animate.shift(RIGHT * 2),
            bubble2.animate.shift(LEFT * 2)
        )
        self.wait(1)

        collision_text = Text("Collision Creates New Universes").scale(0.6)
        self.play(Write(collision_text))
        self.wait(2)
        self.play(FadeOut(collision_text))

        # Show new bubbles forming from collisions
        new_bubble = Circle(radius=0.5, color=PURPLE).shift(UP * 1)
        self.play(GrowFromCenter(new_bubble))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(bubble1),
            FadeOut(bubble2),
            FadeOut(bubble3),
            FadeOut(bubble4),
            FadeOut(new_bubble),
            FadeOut(space)
        )

if __name__ == "__main__":
    scene = BubbleUniverses()
    scene.render()