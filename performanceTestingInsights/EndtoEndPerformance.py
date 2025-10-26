import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rawData = pd.read_csv("api_performance_dataset.csv")

#selecting only needed data
performanceDF = rawData.groupby(["endpoint","concurrent_users"])["response_time_ms"].sum().reset_index().rename(columns={"response_time_ms":"total_response_time"})

fig, axes = plt.subplots(5, 2, figsize=(6, 10))
axes = axes.flatten()
endpoints = performanceDF['endpoint'].unique()

for idx, endpoint in enumerate(endpoints[:10]):
    endpoint_data = performanceDF[performanceDF['endpoint'] == endpoint]
    axes[idx].plot(performanceDF['concurrent_users'],performanceDF['total_response_time'],alpha=0.5)
    axes[idx].set_title(f'Endpoint: {endpoint}')
    axes[idx].set_xlabel('Concurrent Users')
    axes[idx].set_ylabel('Response Time (ms)')
    axes[idx].grid(True)
    
plt.tight_layout()
plt.show()


#2
perfDataDF = rawData.groupby(["timestamp","endpoint"])["response_time_ms"].sum().reset_index().rename(columns={"response_time_ms":"total_response_time"})

perfDataDF['timestamp'] = pd.to_datetime(perfDataDF['timestamp'], errors='coerce')

fig, axes = plt.subplots(5, 2, figsize=(6, 10))
axes = axes.flatten()
endpoints = perfDataDF['endpoint'].unique()

for idx, endpoint in enumerate(endpoints[:10]):
    endpoint_data = perfDataDF[perfDataDF['endpoint'] == endpoint].dropna(subset=['timestamp']).sort_values('timestamp')
    axes[idx].plot(endpoint_data['timestamp'], endpoint_data['total_response_time'], alpha=0.6, marker='o')
    
    axes[idx].set_title(f'Endpoint: {endpoint}')
    axes[idx].set_xlabel('Date')
    axes[idx].set_ylabel('Total Response Time (ms)')
    axes[idx].grid(True)

for ax in axes[len(endpoints[:10]):]:
    ax.set_visible(False)

plt.tight_layout()
plt.show()

#3
errorDf = rawData[rawData['status_code']==500].groupby('endpoint')['status_code'].count().reset_index().rename(columns={'status_code':'500ErrorsCount'})
print(errorDf)
plt.plot(errorDf['endpoint'],errorDf['500ErrorsCount'],marker='o', label='500 Errors for every End Point')
plt.legend()
plt.show()

#4
correlation_with_closure = rawData.corr(numeric_only=True)[['response_time_ms']].drop(index='response_time_ms')
sns.heatmap(correlation_with_closure, annot=True, fmt=".0f", cmap='viridis', cbar=True)
plt.title('Correlation Heatmap')
plt.show()
