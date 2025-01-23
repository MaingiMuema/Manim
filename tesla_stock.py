from manim import *
import yfinance as yf

# Fetch Tesla stock data for the last 10 years
tesla = yf.Ticker("TSLA")
hist = tesla.history(period="10y")
hist = hist.reset_index()  # Reset index to use Date as a column

# Extract the year and the closing price
hist['Year'] = hist['Date'].dt.year
yearly_data = hist.groupby('Year')['Close'].mean().reset_index()

class TeslaStockBarChart(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[min(yearly_data['Year']), max(yearly_data['Year']), 1],
            y_range=[0, max(yearly_data['Close']) + 100, 100],
            axis_config={"color": BLUE},
        )
        axes_labels = axes.get_axis_labels(x_label="Year", y_label="Close Price (\\$)")  # Escape the $ symbol

        # Create bars
        bars = VGroup()
        for index, row in yearly_data.iterrows():
            bar = Rectangle(
                height=row['Close'] / 10,  # Scale down the height for better visualization
                width=0.5,
                fill_color=BLUE,
                fill_opacity=0.7,
                stroke_color=WHITE,
            )
            bar.move_to(axes.c2p(row['Year'], row['Close'] / 20, 0))  # Position the bar
            bars.add(bar)

        # Animate the bars
        self.play(Create(axes), Write(axes_labels))
        self.play(LaggedStart(*[Create(bar) for bar in bars], lag_ratio=0.1))
        self.wait(2)