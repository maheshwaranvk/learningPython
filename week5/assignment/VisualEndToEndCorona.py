import pandas as pd
import matplotlib.pyplot as plt

rawCSVData = pd.read_csv("country_wise_latest.csv")

# 1. Bar Chart of Top 10 Countries by Confirmed Cases 

top10Countries = rawCSVData.sort_values('Confirmed', ascending=False, ignore_index=True).head(10)
print(top10Countries[['country/Region','Confirmed']])
print(top10Countries['country/Region'])
barChart = plt.bar(top10Countries['country/Region'], top10Countries['Confirmed'], color='r', width=0.5, alpha=0.5)
plt.grid()
plt.title("Top 10 Countries by Confirmed Cases")
plt.bar_label(barChart, fmt='%.1f')
plt.xlabel('Countries')
plt.ylabel('Confirmed Cases in Millions')
plt.show()

#2. Pie Chart of Global Death Distribution by Region
deathDistribution = rawCSVData.groupby('WHO Region')['Deaths'].sum()
plt.pie(deathDistribution.values, startangle=90, autopct="%1.0f%%")
plt.legend(deathDistribution.index)
plt.show()

#3. Line Chart comparing Confirmed and Deaths for Top 5 Countries 
top5Countries = rawCSVData.sort_values('Confirmed', ascending=False, ignore_index=True).head(5)
confirmedTop5Countries = top5Countries[['country/Region','Confirmed']]
top5Country = rawCSVData.sort_values('Deaths', ascending=False, ignore_index=True).head(5)
deathTop5Countries = top5Country[['country/Region','Deaths']]
print(confirmedTop5Countries)
print(deathTop5Countries)
fig, subPlotLine = plt.subplots(1,2, figsize=(12,6))
subPlotLine[0].plot(confirmedTop5Countries['country/Region'],confirmedTop5Countries['Confirmed'], label='Top 5 Countries with Confirmed Cases', marker='o', color='b')
subPlotLine[0].set_xlabel('Countries')
subPlotLine[0].set_ylabel('Confirmed in Million')
subPlotLine[1].plot(deathTop5Countries['country/Region'],deathTop5Countries['Deaths'],  label='Top 5 Countries with Death Cases', marker='o', color='g')
subPlotLine[1].set_xlabel('Countries')
subPlotLine[1].set_ylabel('Death Count')
subPlotLine[0].legend()
subPlotLine[1].legend()
plt.show()

#4. Scatter Plot of Confirmed Cases vs Recovered Cases
confirmedAndRecovered = rawCSVData.groupby('WHO Region')[['Confirmed','Recovered']].sum()
print(confirmedAndRecovered)
plt.scatter(confirmedAndRecovered.index,confirmedAndRecovered['Confirmed'],color='r', label='Confirmed Cases')
plt.scatter(confirmedAndRecovered.index,confirmedAndRecovered['Recovered'], color = 'g', label='Recovered Cases')
plt.xticks(confirmedAndRecovered.index, rotation=90)
plt.legend()
plt.show()

#5. Histogram of Death Counts across all Regions
deathRegion = rawCSVData.groupby('WHO Region')['Deaths'].sum()
plt.hist(deathRegion.values, bins=4,edgecolor='black')
plt.xlabel("Death Count")
plt.ylabel("Number of Countries")
plt.show()

#6. Stacked Bar Chart of Confirmed, Deaths, and Recovered for 5 Selected Countries
countries = ['India','US','Chile','France','Russia']
cdrCountry = rawCSVData[rawCSVData['country/Region'].isin(countries)]
print(cdrCountry)
confirmedBar = plt.bar(cdrCountry['country/Region'],cdrCountry['Confirmed'],label='Confirmed', width=0.5, color='red',alpha=0.5)
plt.bar_label(confirmedBar)
deathBar = plt.bar(cdrCountry['country/Region'],cdrCountry['Deaths'],label='Deaths', width=0.5, color='black', bottom=cdrCountry['Confirmed'],alpha=0.5)
plt.bar_label(deathBar)
recoveredBar = plt.bar(cdrCountry['country/Region'],cdrCountry['Recovered'],label='Recovered', width=0.5, color='green', bottom=cdrCountry['Confirmed'],alpha=0.5)
plt.bar_label(recoveredBar)
plt.legend()
plt.show()

#7. Box Plot of Confirmed Cases across Regions
confirmedRegion = rawCSVData.groupby('WHO Region')['Confirmed'].sum()
plt.boxplot(confirmedRegion,
            vert=True,
            patch_artist=True,
            notch=True,
            showmeans=True,
            boxprops=dict(facecolor="lightblue"),
            medianprops=dict(color="red", linewidth=2),
            meanprops=dict(marker="o", markerfacecolor="green", markersize=8),
            flierprops=dict(marker="x", color="orange"))
plt.show()

# 8. Trend Line: Plot Confirmed cases for India vs another chosen country (side by side comparison).
countries = ['India','US']
confirmedCountry = rawCSVData[rawCSVData['country/Region'].isin(countries)]
df = pd.DataFrame(confirmedCountry[['country/Region','Confirmed']].groupby('country/Region').sum())
print(df)
df.plot(kind='bar', color=['blue','green'])
plt.show()