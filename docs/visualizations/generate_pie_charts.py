import pandas as pd
import plotly.express as px
import os

# Load data
df = pd.read_csv("https://raw.githubusercontent.com/Data-Dunkers/data/refs/heads/main/NBA/team/2024-2025/IND_2024-2025_players.csv")

# Visualization 1: Points Per Game Distribution
df_pacers = df[df['Name'] != 'Total']
df_pacers = df_pacers.sort_values(by="PTS", ascending=False)
fig1 = px.pie(df_pacers, values='PTS', names='Name', title='Points Per Game: Pacers 2024-2025')

# Save Visualization 1
output_path1 = os.path.join(os.getcwd(), 'docs', 'visualizations', 'interpreting_pie_charts_pts.html')
fig1.write_html(output_path1)
print(f"Visualization 1 saved to {output_path1}")

# Visualization 2: Pascal Siakam Scoring Breakdown
siakam_stats = df_pacers[df_pacers['Name'].str.contains('Siakam')].iloc[0]
two_pointers = siakam_stats['2PM'] * 2
three_pointers = siakam_stats['3PM'] * 3
free_throws = siakam_stats['FTM']

fig2 = px.pie(values=[two_pointers, three_pointers, free_throws], 
             names=['2-Pointers', '3-Pointers', 'Free Throws'], 
             title="Pascal Siakam's Scoring")

# Save Visualization 2
output_path2 = os.path.join(os.getcwd(), 'docs', 'visualizations', 'interpreting_pie_charts_siakam.html')
fig2.write_html(output_path2)
print(f"Visualization 2 saved to {output_path2}")
