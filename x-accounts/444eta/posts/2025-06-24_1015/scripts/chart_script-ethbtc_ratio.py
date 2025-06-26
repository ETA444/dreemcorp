import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Load the data
df = pd.read_csv('ethbtc_ratio_analysis.csv')

# Convert date column to datetime if needed
df['Date'] = pd.to_datetime(df['Date'])

# Create the line chart with smooth line
fig = go.Figure()

# Add the line trace with smoothing
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['ETH_BTC_Ratio'],
    mode='lines',
    name='ETH/BTC',
    line=dict(color='#1FB8CD', width=3, shape='spline', smoothing=1.3),
    cliponaxis=False,
    hovertemplate='<b>%{x}</b><br>Ratio: %{y:.4f}<extra></extra>'
))

# Update layout with title under 40 characters
fig.update_layout(
    title='ETH/BTC: Generational Opportunity',
    xaxis_title='Date',
    yaxis_title='ETH/BTC Ratio',
    yaxis=dict(range=[0, 0.09])
)

# Save the chart
fig.write_image('ethbtc_ratio_chart.png', width=800, height=600)