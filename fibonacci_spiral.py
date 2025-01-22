from manim import *

class FibonacciSpiral(Scene):
    def construct(self):
        # Initialize the first two Fibonacci numbers
        a, b = 0, 1
        fib_numbers = [a, b]
        
        # Create the first square
        square = Square(side_length=1, color=BLUE)
        square.move_to(ORIGIN)
        self.play(Create(square))
        
        # Label the first square with the Fibonacci number
        label = Text("1", font_size=24).next_to(square, DOWN)
        self.play(Write(label))
        
        # Initialize the position for the next square
        position = square.get_corner(UR)
        
        # Initialize a list to store the arcs for the spiral
        arcs = []
        
        # Generate and display the next Fibonacci numbers
        for i in range(7):  # Adjust the range for more or fewer Fibonacci numbers
            # Calculate the next Fibonacci number
            a, b = b, a + b
            fib_numbers.append(b)
            
            # Create a new square with side length equal to the previous Fibonacci number
            new_square = Square(side_length=fib_numbers[-2], color=BLUE)
            new_square.move_to(position)
            
            # Position the new square correctly
            if i % 4 == 0:
                position = new_square.get_corner(UR)
            elif i % 4 == 1:
                position = new_square.get_corner(DR)
            elif i % 4 == 2:
                position = new_square.get_corner(DL)
            elif i % 4 == 3:
                position = new_square.get_corner(UL)
            
            # Animate the creation of the new square
            self.play(Create(new_square))
            
            # Label the new square with the Fibonacci number
            new_label = Text(str(b), font_size=24).next_to(new_square, DOWN)
            self.play(Write(new_label))
            
            # Add a quarter-circle arc for the spiral
            if i % 4 == 0:
                arc = Arc(radius=fib_numbers[-2], start_angle=0, angle=PI/2, color=YELLOW)
                arc.move_to(new_square.get_corner(DL))
            elif i % 4 == 1:
                arc = Arc(radius=fib_numbers[-2], start_angle=PI/2, angle=PI/2, color=YELLOW)
                arc.move_to(new_square.get_corner(UL))
            elif i % 4 == 2:
                arc = Arc(radius=fib_numbers[-2], start_angle=PI, angle=PI/2, color=YELLOW)
                arc.move_to(new_square.get_corner(UR))
            elif i % 4 == 3:
                arc = Arc(radius=fib_numbers[-2], start_angle=3*PI/2, angle=PI/2, color=YELLOW)
                arc.move_to(new_square.get_corner(DR))
            
            arcs.append(arc)
            self.play(Create(arc))
        
        # Combine all arcs into a single spiral
        spiral = VGroup(*arcs)
        
        # Animate the spiral growing
        self.play(spiral.animate.set_color(RED), run_time=2)
        
        # Display the final Fibonacci sequence
        fib_text = Text("Fibonacci Sequence: " + ", ".join(map(str, fib_numbers)), font_size=24)
        fib_text.to_edge(DOWN)
        self.play(Write(fib_text))
        
        self.wait(2)

# Run the scene
if __name__ == "__main__":
    scene = FibonacciSpiral()
    scene.render()