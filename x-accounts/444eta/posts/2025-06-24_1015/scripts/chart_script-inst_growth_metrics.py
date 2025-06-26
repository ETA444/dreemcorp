import pandas as pd
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('institutional_growth_metrics.csv')

# Abbreviate metric names to 15 characters max
metrics_abbreviated = [
    "ETHA ETF AUM",
    "ETH ETF Inflows", 
    "DeFi TVL",
    "Staked ETH"
]

# Extract the data for each time period
q1_values = df['Q1_2025'].tolist()
q2_values = df['Q2_2025'].tolist()
current_values = df['Current_June'].tolist()

# Create the grouped bar chart
fig = go.Figure()

# Add bars for each time period using brand colors with cliponaxis=False
fig.add_trace(go.Bar(
    name='Q1 2025',
    x=metrics_abbreviated,
    y=q1_values,
    marker_color='#1FB8CD',
    text=[f'{val}' for val in q1_values],
    textposition='outside',
    cliponaxis=False
))

fig.add_trace(go.Bar(
    name='Q2 2025',
    x=metrics_abbreviated,
    y=q2_values,
    marker_color='#FFC185',
    text=[f'{val}' for val in q2_values],
    textposition='outside',
    cliponaxis=False
))

fig.add_trace(go.Bar(
    name='Current June',
    x=metrics_abbreviated,
    y=current_values,
    marker_color='#ECEBD5',
    text=[f'{val}' for val in current_values],
    textposition='outside',
    cliponaxis=False
))

# Update layout
fig.update_layout(
    title='Institutional Ethereum Adoption Surge',
    xaxis_title='Metrics',
    yaxis_title='Values',
    barmode='group',
    yaxis=dict(range=[0, 75]),
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Save the chart
fig.write_image('institutional_adoption_chart.png')
print("Chart saved successfully!")