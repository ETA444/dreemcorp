import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the whale accumulation data
df = pd.read_csv('whale_accumulation_june2025.csv')

# Convert date column to datetime if needed
df['Date'] = pd.to_datetime(df['Date'])

# Create the bar chart
fig = go.Figure()

# Define neon colors - use neon blue/green for bars, highlight June 15th with bright cyan
colors = ['#5D878F' if date != pd.to_datetime('2025-06-15') else '#1FB8CD' for date in df['Date']]

# Add bars with data labels
fig.add_trace(go.Bar(
    x=df['Date'],
    y=df['Daily_Accumulation_ETH'] / 1000,  # Convert to thousands
    marker_color=colors,
    text=[f"{val/1000:.0f}k" for val in df['Daily_Accumulation_ETH']],
    textposition='outside',
    cliponaxis=False,
    showlegend=False
))

# Update layout with dark theme and shortened text
fig.update_layout(
    title="ETH Whale Acc: $2.5B Single-Day Record",
    xaxis_title="Date",
    yaxis_title="Daily Acc (k ETH)",
    # Dark background theme
    plot_bgcolor='#1a1a1a',
    paper_bgcolor='#1a1a1a',
    font_color='white'
)

# Update axes with better styling for dark theme
fig.update_xaxes(
    tickformat='%b %d',
    tickangle=45,
    gridcolor='#404040',
    linecolor='white'
)
fig.update_yaxes(
    ticksuffix='k',
    gridcolor='#404040',
    linecolor='white'
)

# Save the chart
fig.write_image('whale_accumulation_chart.png')