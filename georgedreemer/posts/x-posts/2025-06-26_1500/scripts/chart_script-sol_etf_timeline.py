import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Load the data
df = pd.read_csv('sol_etf_timeline.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Create color mapping for status types
status_colors = {
    'Filed': '#1FB8CD',      # Strong cyan
    'Launched': '#FFC185',   # Light orange
    'Completed': '#ECEBD5',  # Light green
    'Expected': '#5D878F',   # Cyan
    'Extended': '#D2BA4C',   # Moderate yellow
    'Final Deadline': '#B4413C'  # Moderate red
}

# Create figure with secondary y-axis
fig = go.Figure()

# Add approval odds line
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Approval_Odds'],
    mode='lines+markers',
    name='Approval %',
    line=dict(color='#1FB8CD', width=3),
    marker=dict(size=8, color='#1FB8CD'),
    yaxis='y2',
    hovertemplate='<b>%{text}</b><br>Date: %{x}<br>Approval: %{y}%<extra></extra>',
    text=df['Event'].str[:15],
    cliponaxis=False
))

# Add timeline events as scatter points
for status in df['Status'].unique():
    status_df = df[df['Status'] == status]
    fig.add_trace(go.Scatter(
        x=status_df['Date'],
        y=[1] * len(status_df),  # All events at y=1 for timeline
        mode='markers',
        name=status[:12],  # Limit to 12 chars for legend
        marker=dict(
            size=15,
            color=status_colors.get(status, '#1FB8CD'),
            symbol='circle',
            line=dict(width=2, color='white')
        ),
        hovertemplate='<b>%{text}</b><br>Date: %{x}<br>Status: ' + status + '<br>Approval: %{customdata}%<extra></extra>',
        text=status_df['Event'].str[:15],
        customdata=status_df['Approval_Odds'],
        cliponaxis=False
    ))

# Update layout
fig.update_layout(
    title='SOL ETF Timeline & Approval Odds',
    xaxis=dict(
        title='Date',
        showgrid=True,
        gridcolor='rgba(128,128,128,0.3)'
    ),
    yaxis=dict(
        title='Timeline',
        showticklabels=False,
        showgrid=False,
        range=[0.5, 1.5]
    ),
    yaxis2=dict(
        title='Approval %',
        overlaying='y',
        side='right',
        range=[0, 100],
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)'
    ),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.05,
        xanchor='center',
        x=0.5
    ),
    showlegend=True,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

# Add watermark annotation
fig.add_annotation(
    text="Created by @444eta / George Dreemer",
    xref="paper", yref="paper",
    x=0.99, y=0.01,
    xanchor='right', yanchor='bottom',
    showarrow=False,
    font=dict(size=10, color='gray'),
    opacity=0.7
)

# Save the chart
fig.write_image('sol_etf_timeline.png')
print("Chart saved successfully!")