import pandas as pd
import plotly.express as px
import os

# Load data
df = pd.read_csv('https://raw.githubusercontent.com/Data-Dunkers/data/refs/heads/main/NBA/player/nba_player_stats_2024-2025.csv')

# Filter for players
player1 = "Pascal Siakam"
player2 = "Stephen Curry"
comparison = df[(df['Name'] == player1) | (df['Name'] == player2)]

# Melt the dataframe for easier plotting if needed, but px.bar can handle multiple y columns
# However, for a grouped bar chart with different scales (PTS vs FG%), it's sometimes tricky.
# In the notebook: px.bar(comparison, x='Name', y=['FG%', '3P%', 'PTS', 'AST', 'REB'], barmode='group', title=f'Comparing {player2} to {player1}')

fig = px.bar(comparison, 
             x='Name', 
             y=['FG%', '3P%', 'PTS', 'AST', 'REB'], 
             barmode='group', 
             title=f'Comparing {player2} to {player1}')

# Save to the visualizations directory
output_path = os.path.join(os.getcwd(), 'docs', 'visualizations', 'interpreting_bar_graphs.html')
fig.write_html(output_path)
print(f"Visualization saved to {output_path}")
