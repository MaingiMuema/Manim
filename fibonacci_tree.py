from manim import *

class FibonacciTree(Scene):
    def construct(self):
        # Define the recursive function to draw the Fibonacci tree
        def draw_tree(node, depth, angle, length_scale):
            if depth == 0:
                return
            # Draw the current branch
            branch = Line(node, node + length_scale * UP, color=GREEN)
            self.play(Create(branch), run_time=0.5)
            
            # Calculate the end point of the current branch
            end_point = branch.get_end()
            
            # Draw left and right subtrees
            if depth > 1:
                # Left branch (Fibonacci recursion)
                left_branch = Line(
                    end_point,
                    end_point + length_scale * np.array([-np.cos(angle), np.sin(angle), 0]),
                    color=GREEN
                )
                self.play(Create(left_branch), run_time=0.5)
                draw_tree(left_branch.get_end(), depth - 1, angle, length_scale * 0.6)
                
                # Right branch (Fibonacci recursion)
                right_branch = Line(
                    end_point,
                    end_point + length_scale * np.array([np.cos(angle), np.sin(angle), 0]),
                    color=GREEN
                )
                self.play(Create(right_branch), run_time=0.5)
                draw_tree(right_branch.get_end(), depth - 2, angle, length_scale * 0.6)
        
        # Set initial parameters
        start_point = ORIGIN + 3 * DOWN
        depth = 6  # Depth of the tree (adjust for more or fewer levels)
        angle = 45 * DEGREES  # Angle between branches
        length_scale = 1.5  # Length of the initial branch
        
        # Draw the Fibonacci tree
        draw_tree(start_point, depth, angle, length_scale)
        
        # Display the Fibonacci sequence
        fib_sequence = [0, 1]
        for _ in range(depth):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        fib_text = Text(f"Fibonacci Sequence: {', '.join(map(str, fib_sequence))}", font_size=24)
        fib_text.to_edge(DOWN)
        self.play(Write(fib_text))
        
        self.wait(2)

# Run the scene
if __name__ == "__main__":
    scene = FibonacciTree()
    scene.render()