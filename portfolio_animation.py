from manim import *

class PortfolioAnimation(Scene):
    def construct(self):
        # Custom colors
        self.BACKGROUND_COLOR = "#1e1e2f"  # Dark blue
        self.TITLE_COLOR = "#00ffcc"  # Cyan
        self.TEXT_COLOR = "#ffffff"  # White
        self.HIGHLIGHT_COLOR = "#ff6f61"  # Coral
        self.SKILLS_COLOR = "#00ccff"  # Light blue
        self.INTERESTS_COLOR = "#ff6f61"  # Coral

        # Set background color
        self.camera.background_color = self.BACKGROUND_COLOR

        # Add a gradient background for a more immersive feel
        gradient = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_opacity=1,
        )
        gradient.set_fill(color=[self.BACKGROUND_COLOR, "#2e2e4f"], opacity=1)
        self.add(gradient)

        # Section 1: Greeting
        greeting = Text("Hello there! 👋", font_size=72, color=self.TITLE_COLOR, weight=BOLD)
        greeting.to_edge(UP)
        self.play(Write(greeting, run_time=1.5))
        self.wait(1)

        # Section 2: Introduction
        introduction = Text("I'm Mark Maingi", font_size=48, color=self.HIGHLIGHT_COLOR, weight=BOLD)
        introduction.next_to(greeting, DOWN)
        self.play(FadeIn(introduction, shift=UP, run_time=1))
        self.wait(1)

        # Brief description
        description = Text(
            "A Frontend Developer & UI/UX Engineer\n"
            "with a passion for creating value through design and code.",
            font_size=32,
            color=self.TEXT_COLOR,
            line_spacing=1.5,
        )
        description.next_to(introduction, DOWN * 2)
        self.play(FadeIn(description, shift=UP, run_time=2))
        self.wait(2)

        # Section 3: Skills and Journey
        skills_title = Text("My Skills & Journey", font_size=48, color=self.SKILLS_COLOR, weight=BOLD)
        skills_title.to_edge(UP)

        # Animate transition to skills section
        self.play(
            ReplacementTransform(greeting, skills_title),
            FadeOut(introduction, shift=UP),
            FadeOut(description, shift=UP),
        )
        self.wait(1)

        # Skills list with icons
        skills = VGroup(
            self.create_skill_item("Frontend Development", "HTML5, CSS3, JavaScript, React.js, ReactNative, Next.js"),
            self.create_skill_item("Backend Development", "Node.js, Express.js, PHP, Laravel, Python, C"),
            self.create_skill_item("Databases", "MySQL, PostgreSQL, Supabase"),
            self.create_skill_item("UI/UX Design, SEO, Agile Workflow, RESTful APIs"),
            self.create_skill_item("LLM Integration, Prompt Engineering"),
        )
        skills.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        skills.next_to(skills_title, DOWN)

        # Animate skills list
        self.play(LaggedStart(*[FadeIn(skill, shift=UP) for skill in skills], lag_ratio=0.3))
        self.wait(3)

        # Section 4: Call to Action
        cta_title = Text("Let's Learn Together!", font_size=48, color=self.INTERESTS_COLOR, weight=BOLD)
        cta_title.to_edge(UP)

        # Animate transition to CTA section
        self.play(
            ReplacementTransform(skills_title, cta_title),
            FadeOut(skills, shift=UP),
        )
        self.wait(1)

        # Call to Action text
        cta_text = Text(
            "I’ll be creating explainer videos on concepts I’ve learned\n"
            "during my journey as a developer.\n"
            "If you’d like to stick around, you’ll definitely benefit! 🚀",
            font_size=32,
            color=self.TEXT_COLOR,
            line_spacing=1.5,
        )
        cta_text.next_to(cta_title, DOWN * 2)

        # Animate CTA text
        self.play(FadeIn(cta_text, shift=UP, run_time=2))
        self.wait(2)

        # Final Call to Action
        final_text = Text("Let's connect and build something amazing!", font_size=36, color=self.TITLE_COLOR, weight=BOLD)
        final_text.to_edge(UP)

        # Animate final text
        self.play(
            ReplacementTransform(cta_title, final_text),
            FadeOut(cta_text, shift=UP),
        )
        self.wait(2)

    def create_skill_item(self, title, description=None):
        """Create a skill item with a custom icon."""
        # Custom icon (a square with a gradient fill)
        icon = Square(side_length=0.6, color=self.SKILLS_COLOR, fill_opacity=1)
        icon.set_fill(color=[self.SKILLS_COLOR, self.HIGHLIGHT_COLOR], opacity=1)
        icon.scale(0.5)

        title_text = Text(title, font_size=28, color=self.TEXT_COLOR)
        if description:
            desc_text = Text(description, font_size=24, color=self.TEXT_COLOR)
            desc_text.next_to(title_text, DOWN, aligned_edge=LEFT)
            group = VGroup(icon, title_text, desc_text)
        else:
            group = VGroup(icon, title_text)

        group.arrange(RIGHT, buff=0.5)
        return group