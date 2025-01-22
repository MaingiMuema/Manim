from manim import *

class JavaScriptEventLoop(Scene):
    def construct(self):
        # Create sections for Call Stack, Web APIs, Callback Queue, and Event Loop
        call_stack = Rectangle(width=2, height=4, fill_opacity=0.5, fill_color=BLUE)
        web_apis = Rectangle(width=3, height=2, fill_opacity=0.5, fill_color=YELLOW)
        callback_queue = Rectangle(width=3, height=1, fill_opacity=0.5, fill_color=GREEN)
        event_loop = Circle(radius=0.5, fill_opacity=0.5, fill_color=RED)

        # Position the sections
        call_stack.to_edge(LEFT)
        web_apis.to_edge(UP).shift(RIGHT * 3)
        callback_queue.next_to(web_apis, DOWN, buff=1)
        event_loop.move_to(DOWN * 2 + RIGHT * 3)

        # Add labels
        call_stack_label = Text("Call Stack").next_to(call_stack, UP)
        web_apis_label = Text("Web APIs").next_to(web_apis, UP)
        callback_queue_label = Text("Callback Queue").next_to(callback_queue, UP)
        event_loop_label = Text("Event Loop").next_to(event_loop, DOWN)

        # Draw all sections and labels
        self.play(
            Create(call_stack),
            Create(web_apis),
            Create(callback_queue),
            Create(event_loop),
            Write(call_stack_label),
            Write(web_apis_label),
            Write(callback_queue_label),
            Write(event_loop_label),
        )
        self.wait(1)

        # Add code blocks to the call stack
        code_block_1 = Text("console.log('Start')", font_size=24).move_to(call_stack.get_top() + DOWN * 0.5)
        code_block_2 = Text("setTimeout(cb, 1000)", font_size=24).move_to(call_stack.get_top() + DOWN * 1.5)
        code_block_3 = Text("console.log('End')", font_size=24).move_to(call_stack.get_top() + DOWN * 2.5)

        self.play(Write(code_block_1))
        self.wait(1)
        self.play(Write(code_block_2))
        self.wait(1)
        self.play(Write(code_block_3))
        self.wait(1)

        # Move setTimeout to Web APIs
        setTimeout_block = code_block_2.copy()
        self.play(setTimeout_block.animate.move_to(web_apis.get_center()))
        self.wait(1)

        # Simulate Web API processing
        processing_text = Text("Processing...", font_size=20).move_to(web_apis.get_center())
        self.play(Transform(setTimeout_block, processing_text))
        self.wait(2)

        # Move callback to the Callback Queue
        callback_block = Text("cb", font_size=24).move_to(callback_queue.get_left())
        self.play(Transform(processing_text, callback_block))
        self.wait(1)

        # Show Event Loop checking the Call Stack and Callback Queue
        event_loop_arrow = Arrow(event_loop.get_top(), callback_queue.get_bottom(), buff=0.1, color=RED)
        self.play(Create(event_loop_arrow))
        self.wait(1)

        # Move callback to the Call Stack
        callback_in_stack = callback_block.copy().move_to(call_stack.get_top() + DOWN * 0.5)
        self.play(Transform(callback_block, callback_in_stack))
        self.wait(1)

        # Execute the callback
        executed_text = Text("Executed!", font_size=24).move_to(call_stack.get_center())
        self.play(Transform(callback_in_stack, executed_text))
        self.wait(2)

        # Clear the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)
