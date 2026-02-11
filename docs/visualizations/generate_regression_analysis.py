import pandas as pd
import plotly.express as px
import os

# Load data
url = "https://raw.githubusercontent.com/Data-Dunkers/data/main/WNBA/player/wnba_player_stats_all.csv"
df = pd.read_csv(url)

# Create visualization
fig = px.scatter(df, 
                 x='MIN', 
                 y='PTS', 
                 trendline='ols', 
                 title='Points versus Minutes Played Per Game')

# Save to the visualizations directory
output_path = os.path.join(os.getcwd(), 'docs', 'visualizations', 'regression_analysis.html')
fig.write_html(output_path)
print(f"Visualization saved to {output_path}")
