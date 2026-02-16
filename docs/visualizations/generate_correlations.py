import pandas as pd
import plotly.express as px
import os

# Load data
url = 'https://raw.githubusercontent.com/Data-Dunkers/data/refs/heads/main/NBA/player/nba_player_stats_2024-2025.csv'
df = pd.read_csv(url)

# Create visualization
# Correlation matrix (numeric only)
fig = px.imshow(df.corr(numeric_only=True), 
                title='Correlation Matrix of 2024-2025 NBA Player Stats', 
                height=800, 
                text_auto='.2f')

# Save to the visualizations directory
# We use the absolute path to ensure it lands in the right place regardless of where the script is run from
output_path = r'd:\My Documents\GitHub\student\docs\visualizations\correlation_matrix.html'
fig.write_html(output_path)
print(f"Visualization saved to {output_path}")
