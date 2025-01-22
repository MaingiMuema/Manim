from manim import *

class QuantumManyWorlds(Scene):
    def construct(self):
        # Title
        title = Text("Quantum Many-Worlds Interpretation (Level III Multiverse)").scale(0.7)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Create a particle (electron)
        particle = Dot(color=BLUE).shift(LEFT * 4)
        self.play(GrowFromCenter(particle))
        self.wait(1)

        # Animate the particle moving to the right
        self.play(particle.animate.shift(RIGHT * 2))
        self.wait(1)

        # Decision point: particle splits into two paths
        decision_point = Dot(color=WHITE).shift(RIGHT * 2)
        self.play(GrowFromCenter(decision_point))
        self.wait(1)

        # Create two new particles representing different outcomes
        particle1 = Dot(color=GREEN).move_to(decision_point.get_center())
        particle2 = Dot(color=RED).move_to(decision_point.get_center())
        self.play(
            particle1.animate.shift(UP * 1.5 + RIGHT * 2),
            particle2.animate.shift(DOWN * 1.5 + RIGHT * 2),
            FadeOut(particle)
        )
        self.wait(2)

        # Label the paths as "Universe A" and "Universe B"
        label_a = Text("Universe A", color=GREEN).scale(0.5).next_to(particle1, UP)
        label_b = Text("Universe B", color=RED).scale(0.5).next_to(particle2, DOWN)
        self.play(Write(label_a), Write(label_b))
        self.wait(2)

        # Show more branching paths
        particle1a = Dot(color=YELLOW).move_to(particle1.get_center())
        particle1b = Dot(color=ORANGE).move_to(particle1.get_center())
        self.play(
            particle1a.animate.shift(UP * 1 + RIGHT * 2),
            particle1b.animate.shift(DOWN * 1 + RIGHT * 2),
            FadeOut(particle1)
        )
        self.wait(1)

        # Label the new branches
        label_a1 = Text("Universe A1", color=YELLOW).scale(0.5).next_to(particle1a, UP)
        label_a2 = Text("Universe A2", color=ORANGE).scale(0.5).next_to(particle1b, DOWN)
        self.play(Write(label_a1), Write(label_a2))
        self.wait(2)

        # Conclusion: Show a tree diagram of all branches
        tree = VGroup(
            Line(decision_point.get_center(), particle1.get_center(), color=GREEN),
            Line(decision_point.get_center(), particle2.get_center(), color=RED),
            Line(particle1.get_center(), particle1a.get_center(), color=YELLOW),
            Line(particle1.get_center(), particle1b.get_center(), color=ORANGE)
        )
        self.play(Create(tree))
        self.wait(2)

        # Final text
        final_text = Text("Every quantum decision creates a new universe.").scale(0.7)
        self.play(Write(final_text))
        self.wait(3)
        self.play(FadeOut(final_text), FadeOut(tree), FadeOut(particle1a), FadeOut(particle1b), FadeOut(particle2))

if __name__ == "__main__":
    scene = QuantumManyWorlds()
    scene.render()