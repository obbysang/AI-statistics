import pandas as pd
import plotly.express as px

# Your code here
data = {
    'AI Model': ['GPT-4', 'BERT', 'T5', 'ResNet', 'YOLOv4'],
    'Release Year': [2023, 2018, 2019, 2015, 2020],
    'Parameters (Billions)': [175, 0.34, 11, 60, 0.06],
    'Accuracy (%)': [95, 92, 94, 96, 91],
    'Training Time (Days)': [30, 4, 10, 14, 7]
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file (optional)
df.to_csv('ai_statistics.csv', index=False)
