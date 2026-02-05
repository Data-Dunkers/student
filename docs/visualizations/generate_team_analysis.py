import pandas as pd
import plotly.express as px
import os

# Team URLs
pacers_url = 'https://raw.githubusercontent.com/Data-Dunkers/data/main/NBA/team/2025-2026/IND_2025-2026_players.csv'
raptors_url = 'https://raw.githubusercontent.com/Data-Dunkers/data/main/NBA/team/2025-2026/TOR_2025-2026_players.csv'
celtics_url = 'https://raw.githubusercontent.com/Data-Dunkers/data/main/NBA/team/2025-2026/BOS_2025-2026_players.csv'
knicks_url = 'https://raw.githubusercontent.com/Data-Dunkers/data/main/NBA/team/2025-2026/NY_2025-2026_players.csv'

# Load data
df_pacers = pd.read_csv(pacers_url)
df_raptors = pd.read_csv(raptors_url)
df_celtics = pd.read_csv(celtics_url)
df_knicks = pd.read_csv(knicks_url)

# Extract totals
pacers_total = df_pacers[df_pacers['Name'] == 'Total'].copy()
raptors_total = df_raptors[df_raptors['Name'] == 'Total'].copy()
celtics_total = df_celtics[df_celtics['Name'] == 'Total'].copy()
knicks_total = df_knicks[df_knicks['Name'] == 'Total'].copy()

pacers_total['Team'] = 'Pacers'
raptors_total['Team'] = 'Raptors'
celtics_total['Team'] = 'Celtics'
knicks_total['Team'] = 'Knicks'

df_teams = pd.concat([pacers_total, raptors_total, celtics_total, knicks_total])
df_comparison = df_teams[['Team', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TO']]

# Melt for grouping
df_melted = df_comparison.melt(id_vars='Team', var_name='Metric', value_name='Value')

# Create plot
fig = px.bar(df_melted, 
             x='Metric', 
             y='Value', 
             color='Team', 
             barmode='group', 
             title='Team Performance Comparison: Pacers vs. Raptors',
             labels={'Value': 'Season Average', 'Metric': 'Statistical Category'})

# Export to HTML
output_path = os.path.join(os.path.dirname(__file__), 'team_analysis.html')
fig.write_html(output_path, include_plotlyjs='cdn')
print(f'Visualization saved to {output_path}')
