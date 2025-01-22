from manim import *

class ResponsiveDesignIntro(Scene):
    def construct(self):
        # Introduction
        title = Text("How Responsive Web Design Works", font_size=48)
        subtitle = Text("Under the Hood", font_size=36).next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

class MediaQueriesExplanation(Scene):
    def construct(self):
        # Explain media queries
        text = Text("CSS Media Queries", font_size=36).to_edge(UP)
        self.play(Write(text))

        # Create a screen and layout
        screen = Rectangle(width=6, height=4, color=BLUE)
        layout = VGroup(
            Rectangle(width=5, height=1, color=GREEN),
            Rectangle(width=5, height=1, color=YELLOW),
            Rectangle(width=5, height=1, color=RED)
        ).arrange(DOWN, buff=0.2).move_to(screen.get_center())

        self.play(Create(screen), Create(layout))
        self.wait(1)

        # Show screen resizing
        new_screen = screen.copy().scale(0.5).to_edge(LEFT)
        new_layout = VGroup(
            Rectangle(width=2, height=1, color=GREEN),
            Rectangle(width=2, height=1, color=YELLOW),
            Rectangle(width=2, height=1, color=RED)
        ).arrange(DOWN, buff=0.2).move_to(new_screen.get_center())

        self.play(Transform(screen, new_screen), Transform(layout, new_layout))
        self.wait(2)

class FlexboxExplanation(Scene):
    def construct(self):
        # Explain flexbox
        text = Text("Flexbox System", font_size=36).to_edge(UP)
        self.play(Write(text))

        # Create a flexbox row
        boxes = VGroup(
            *[Square(side_length=1, color=BLUE) for _ in range(4)]
        ).arrange(RIGHT, buff=0.5)
        self.play(Create(boxes))
        self.wait(1)

        # Show rearrangement
        new_boxes = boxes.copy().arrange(DOWN, buff=0.5).scale(0.7)
        self.play(Transform(boxes, new_boxes))
        self.wait(2)

class GridExplanation(Scene):
    def construct(self):
        # Explain CSS grid
        text = Text("CSS Grid System", font_size=36).to_edge(UP)
        self.play(Write(text))

        # Create a grid layout
        grid = VGroup(
            *[Rectangle(width=1.5, height=1.5, color=ORANGE) for _ in range(6)]
        ).arrange_in_grid(rows=2, cols=3, buff=0.2)
        self.play(Create(grid))
        self.wait(1)

        # Show grid adjustment
        new_grid = grid.copy().arrange_in_grid(rows=3, cols=2, buff=0.2)
        self.play(Transform(grid, new_grid))
        self.wait(2)

class ResponsiveDesignConclusion(Scene):
    def construct(self):
        # Conclusion
        text = Text("Responsive Design: Adapting to Every Screen", font_size=36)
        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))

# Run the scenes
if __name__ == "__main__":
    from manim import config

    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 30
    config.output_file = "responsive_design_explainer.mp4"

    ResponsiveDesignIntro().render()
    MediaQueriesExplanation().render()
    FlexboxExplanation().render()
    GridExplanation().render()
    ResponsiveDesignConclusion().render()