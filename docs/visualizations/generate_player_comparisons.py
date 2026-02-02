import pandas as pd
import plotly.express as px
import plotly.io as pio

# Load data
url = "https://raw.githubusercontent.com/Data-Dunkers/data/refs/heads/main/NBA/player/nba_player_stats_2024-2025.csv"
df = pd.read_csv(url)

# Reduce to essential columns for the plot
df['HoverInfo'] = df.apply(lambda x: f"{x['Name']}<br>POS: {x['POS']}<br>PTS: {x['PTS']}<br>FG%: {x['FG%']}<br>MIN: {x['MIN']}", axis=1)

# Filter for noise (players with very few minutes or games might clutter the chart)
df_filtered = df[(df['GP'] > 10) & (df['MIN'] > 10)]

# Create Scatter Plot
fig = px.scatter(
    df_filtered,
    x="PTS",
    y="FG%",
    color="POS",
    size="MIN",
    hover_name="Name",
    hover_data={"PTS": True, "FG%": True, "POS": False, "MIN": False, "Name": False}, 
    title="NBA Player Comparison: Scoring Volume vs. Efficiency (2024-2025)",
    labels={"PTS": "Points Per Game (PTS)", "FG%": "Field Goal Percentage (FG%)", "POS": "Position", "MIN": "Minutes Per Game"},
    height=700
)

# Customize layout for better embedding
fig.update_layout(
    margin=dict(l=20, r=20, t=60, b=20),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

# Save to HTML
output_file = "d:/My Documents/GitHub/student/docs/visualizations/player_comparisons.html"
pio.write_html(fig, file=output_file, include_plotlyjs='cdn', full_html=True)
print(f"Visualization saved to {output_file}")
