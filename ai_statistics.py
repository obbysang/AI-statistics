# Install required libraries
!pip install plotly pandas

# Import libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create dataset
data = {
    'AI Model': ['GPT-4', 'BERT', 'T5', 'ResNet', 'YOLOv4'],
    'Release Year': [2023, 2018, 2019, 2015, 2020],
    'Parameters (Billions)': [175, 0.34, 11, 60, 0.06],
    'Accuracy (%)': [95, 92, 94, 96, 91],
    'Training Time (Days)': [30, 4, 10, 14, 7]
}

df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv('ai_statistics.csv', index=False)

# Create interactive plots
# Bar Plot for Parameters
fig1 = px.bar(df, x='AI Model', y='Parameters (Billions)', title='Parameters of Leading AI Models')
fig1.show()

# Scatter Plot for Accuracy vs Training Time
fig2 = px.scatter(df, x='Training Time (Days)', y='Accuracy (%)', color='AI Model', 
                  title='Accuracy vs Training Time')
fig2.show()

# Line Plot for Release Year
fig3 = px.line(df, x='AI Model', y='Release Year', title='Release Year of AI Models')
fig3.show()

# Combine plots into a dashboard
fig = make_subplots(rows=2, cols=2, subplot_titles=("Parameters", "Accuracy vs Training Time", "Release Year"))

fig.add_trace(go.Bar(x=df['AI Model'], y=df['Parameters (Billions)']), row=1, col=1)
fig.add_trace(go.Scatter(x=df['Training Time (Days)'], y=df['Accuracy (%)'], mode='markers'), row=1, col=2)
fig.add_trace(go.Scatter(x=df['AI Model'], y=df['Release Year'], mode='lines'), row=2, col=1)

fig.update_layout(height=600, width=800, title_text="AI Models Statistics Dashboard")
fig.show()

# Push to GitHub
import os

# Navigate to the repository directory
os.chdir('/content/AI-statistics')

# Add the new file to Git
!git add ai_statistics.py

# Commit the changes
!git commit -m "Added AI statistics Python script with interactive plots"

# Push the changes to GitHub
!git push origin main
