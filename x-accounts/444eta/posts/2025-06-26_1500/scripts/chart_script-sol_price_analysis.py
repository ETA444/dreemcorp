import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Load the data
sol_data = pd.read_csv("sol_analysis_data.csv")
price_targets = pd.read_csv("sol_price_targets.csv")

# Convert date column to datetime
sol_data['date'] = pd.to_datetime(sol_data['date'])

# Create the main figure
fig = go.Figure()

# Add candlestick chart
fig.add_trace(go.Candlestick(
    x=sol_data['date'],
    open=sol_data['open'],
    high=sol_data['high'],
    low=sol_data['low'],
    close=sol_data['close'],
    name='SOL Price',
    increasing_line_color='#1FB8CD',
    decreasing_line_color='#B4413C',
    increasing_fillcolor='#1FB8CD',
    decreasing_fillcolor='#B4413C'
))

# Define probability-based colors
def get_color_by_probability(prob):
    if prob >= 70:
        return '#1FB8CD'  # High probability - cyan
    elif prob >= 60:
        return '#D2BA4C'  # Medium probability - yellow
    else:
        return '#B4413C'  # Low probability - red

# Get current price (latest close price)
current_price = sol_data['close'].iloc[-1]

# Add horizontal price target lines
for _, target in price_targets.iterrows():
    if target['Source'] != 'Current Price':  # Skip current price
        color = get_color_by_probability(target['Probability'])
        prob_text = f"{target['Probability']:.0f}%"
        
        fig.add_hline(
            y=target['Price_Target'],
            line=dict(color=color, width=2, dash='dash'),
            annotation_text=f"${target['Price_Target']:.0f} ({prob_text})",
            annotation_position="right",
            annotation=dict(font=dict(size=12))
        )

# Add current price line
fig.add_hline(
    y=current_price,
    line=dict(color='#FFC185', width=3),
    annotation_text=f"Current ${current_price:.0f}",
    annotation_position="right",
    annotation=dict(font=dict(size=12, color='#FFC185'))
)

# Update layout
fig.update_layout(
    title="SOL Price Analysis",
    xaxis_title="Date",
    yaxis_title="Price ($)",
    xaxis_rangeslider_visible=False,
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

# Format y-axis to show prices in a clean format
fig.update_yaxes(tickformat="$,.0f")

# Save the chart
fig.write_image("sol_price_analysis.png")
print("Chart saved successfully!")