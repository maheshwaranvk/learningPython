from week5.assignment.DataTransformer import DataTransformer
from week5.assignment.DataVisualizer import DataVisualizer
import pandas as pd
import matplotlib.pyplot as plt

class CoronaCaseAnalyzer(DataTransformer):
    def __init__(self):
        super().__init__()
        self.updateColumnHeaderFormat()
        self.removeDuplicateRows()
        self.createCleanDataSet(self.readPropertyFile()['cleanedDataSet'])

    #Req1
    def summarizeCaseCountsByRegion(self):
        self.writeCSVFile(
        pd.DataFrame([self.groupByFiltersAndColumn('Who region', 'Confirmed', 'sum') ,
                      self.groupByFiltersAndColumn('Who region', 'Deaths', 'sum'),
                      self.groupByFiltersAndColumn('Who region', 'Recovered', 'sum')]).transpose(),
                      "./generatedReports/1_ConfirmedDeathRecoveredCases.csv",True)
        
    #Req2
    def filterLowCaseRecords(self):
        confirmedCases = pd.DataFrame(self.groupByFiltersAndColumn('Country/region', 'Confirmed', 'sum'))
        self.writeCSVFile((confirmedCases[confirmedCases['Confirmed']>10]), "./generatedReports/2_LowCaseRecords.csv",True)

    #Req3
    def regionWithHighestConfirmedCases(self):
        highestConfirmedCases = pd.DataFrame(self.groupByFiltersAndColumn('Who region', 'Confirmed', 'max'))
        print("3. Region with Highest Confirmed Cases")
        print(highestConfirmedCases['Confirmed'].idxmax(), ":", highestConfirmedCases['Confirmed'].max())

    #Req4
    def sortingDataByConfirmedCases(self):
        confirmedCases = pd.DataFrame(self.groupByFilters('Confirmed','sum')).sort_values('Confirmed')
        self.writeCSVFile(confirmedCases, "./generatedReports/4_SortedCoronaCases.csv",True)
        
    #Req5
    def gettingTopCountriesByCaseCount(self, totalTopCountriesRequired):
        topCountries = pd.DataFrame(self.groupByFilters('New cases','sum')).sort_values('New cases', ascending=False).head(totalTopCountriesRequired)
        self.writeCSVFile(topCountries, "./generatedReports/5_TopCountriesByCaseCount.csv",True)
    
    #Req6
    def regionWithLowestDeathCount(self):
        lowestDeathRate = pd.DataFrame(self.groupByFiltersAndColumn('Who region', 'Deaths', 'sum'))
        print("6. Region with Lowest Death Rate")
        print(lowestDeathRate['Deaths'].idxmin(), ":", lowestDeathRate['Deaths'].min())
    
    #Req7
    def countriesCaseSummary(self, countryName):
        rawCSVData = self.getRawData()
        self.writeCSVFile(pd.DataFrame(rawCSVData[rawCSVData['Country/region']==countryName]), "./generatedReports/7_CountrySummary.csv",False)

    #Req8
    def caculateMortalityRatesByRegion(self):
        ConfirmedCasesDF = pd.DataFrame(self.groupByFiltersAndColumn('Who region','Confirmed','sum'))
        DeathCasesDF = pd.DataFrame(self.groupByFiltersAndColumn('Who region','Deaths','sum'))
        CFR = pd.DataFrame((DeathCasesDF['Deaths']/ConfirmedCasesDF['Confirmed'])*100)
        CFR = CFR.rename(columns={0:"CFR"})
        self.writeCSVFile(CFR,"./generatedReports/8_MortalityRatesByRegion.csv", True)

    #Req9
    def compareRecoveryRatesAcrossRegion(self):
        self.writeCSVFile(pd.DataFrame(self.groupByFiltersAndColumn('Who region','Recovered','sum')),
                          "./generatedReports/9_RecoveredRatesAcrossRegion.csv",True)
        
    #Req10
    def detectOutlinersInCaseCounts(self, dataPoint):
        startingOutliner = self.getRawData()[dataPoint].mean()
        endingOutliner = 2*self.getRawData()[dataPoint].std()
        lowerBound = startingOutliner - endingOutliner
        upperBound = startingOutliner + endingOutliner
        self.writeCSVFile(pd.DataFrame(self.getRawData()[(self.getRawData()[dataPoint]>lowerBound) & (self.getRawData()[dataPoint]<upperBound)]),
                          "./generatedReports/10_OutlinerDetection.csv",False)
        
    #Req11
    def groupDataByCountryAndRegion(self):
        self.writeCSVFile(self.groupByFilters(['Who region','Country/region'],'sum'),
                          "./generatedReports/11_CountryRegionGroupData.csv",True)
        
    #Req12
    def regionsWithZeroRecoveredCases(self):
        self.writeCSVFile(pd.DataFrame(self.getRawData()[self.getRawData()['Recovered']==0].reset_index(drop=True)),
                          "./generatedReports/12_RegionWithZeroRecoveryCases.csv",False)

# Week 5 Assignment
class CoronaCaseVisualizer(DataVisualizer):
    def __init__(self):
        super().__init__()
        self.updateColumnHeaderFormat()
        self.removeDuplicateRows()
        self.createCleanDataSet(self.readPropertyFile()['cleanedDataSet'])

    # 1. Bar Chart of Top 10 Countries by Confirmed Cases 
    def barChartForTop10CountriesConfirmedCases(self):
        top10Countries = self.getRawData().sort_values('Confirmed', ascending=False, ignore_index=True).head(10)
        self.visBar(top10Countries['Country/region'], top10Countries['Confirmed'], "Countries", "Confirmed Cases in Millions", "Top 10 Countries  by Confirmed Cases", 'b', 0.5, 0.5)

    #2. Pie Chart of Global Death Distribution by Region
    def pieChartForGlobalDeathDisRegion(self):
        globalDeath = self.groupByFiltersAndColumn('Who region',"Deaths", 'sum')
        self.visPie(globalDeath.values, 90, "%1.0f%%", globalDeath.index)

    #3. Line Chart comparing Confirmed and Deaths for Top 5 Countries
    def lineChartComparingConfirmedAndDeathTop5Countries(self):
        top5Countries = self.getRawData().sort_values('Confirmed', ascending=False, ignore_index=True).head(5)
        confirmedTop5Countries = top5Countries[['Country/region','Confirmed']]
        top5Country = self.getRawData().sort_values('Deaths', ascending=False, ignore_index=True).head(5)
        deathTop5Countries = top5Country[['Country/region','Deaths']]
        fig, subPlotLine = plt.subplots(1,2, figsize=(12,6))
        subPlotLine[0].plot(confirmedTop5Countries['Country/region'],confirmedTop5Countries['Confirmed'], label='Top 5 Countries with Confirmed Cases', marker='o', color='b')
        subPlotLine[0].set_xlabel('Countries')
        subPlotLine[0].set_ylabel('Confirmed in Million')
        subPlotLine[1].plot(deathTop5Countries['Country/region'],deathTop5Countries['Deaths'],  label='Top 5 Countries with Death Cases', marker='o', color='g')
        subPlotLine[1].set_xlabel('Countries')
        subPlotLine[1].set_ylabel('Death Count')
        subPlotLine[0].legend()
        subPlotLine[1].legend()
        plt.show()

    #4. Scatter Plot of Confirmed Cases vs Recovered Cases
    def scatterPlotOfConfirmedRecovered(self):
        confirmedRecovered = self.groupByFiltersAndColumn('Who region',['Confirmed','Recovered'], 'sum')
        self.doubleChart(confirmedRecovered.index, confirmedRecovered['Confirmed'], confirmedRecovered['Recovered'], "Confirmed Cases", "Recovered Cases",
                         'r', 'g')
        
    #5. Histogram of Death Counts across all Regions
    def histogramDeathCounts(self):
        globalDeath = self.groupByFiltersAndColumn('Who region',"Deaths", 'sum')
        self.visHistogram(globalDeath.values, 4, "Death Count", "Number of Countries", 'b')

    #6. Stacked Bar Chart of Confirmed, Deaths, and Recovered for 5 Selected Countries
    def stackedBarConfirmedDeathsRecoveredCases(self):
        countries = ['India','US','Chile','France','Russia']
        cdrCountry = self.getRawData()[self.getRawData()['Country/region'].isin(countries)]
        confirmedBar = plt.bar(cdrCountry['Country/region'],cdrCountry['Confirmed'],label='Confirmed', width=0.5, color='red',alpha=0.5)
        plt.bar_label(confirmedBar)
        deathBar = plt.bar(cdrCountry['Country/region'],cdrCountry['Deaths'],label='Deaths', width=0.5, color='black', bottom=cdrCountry['Confirmed'],alpha=0.5)
        plt.bar_label(deathBar)
        recoveredBar = plt.bar(cdrCountry['Country/region'],cdrCountry['Recovered'],label='Recovered', width=0.5, color='green', bottom=cdrCountry['Confirmed'],alpha=0.5)
        plt.bar_label(recoveredBar)
        plt.legend()
        plt.show()
        
    #7. Box Plot of Confirmed Cases across Regions
    def boxPlotConfirmedCases(self):
        globalConfirmed = self.groupByFiltersAndColumn('Who region',"Confirmed", 'sum')
        self.visBoxPlot(globalConfirmed, "orange")

    # 8. Trend Line: Plot Confirmed cases for India vs another chosen country (side by side comparison).
    def pandaPlotConfirmedCases(self):
        countries = ['India','US']
        confirmedCountry = self.getRawData()[self.getRawData()['Country/region'].isin(countries)]
        df = pd.DataFrame(confirmedCountry[['Country/region','Confirmed']].groupby('Country/region').sum())
        self.pandaPlotChart(df, "bar")
        print(df)
if __name__=="__main__":
#     obj1 = CoronaCaseAnalyzer()
#     obj1.summarizeCaseCountsByRegion()
#     obj1.filterLowCaseRecords()
#     obj1.regionWithHighestConfirmedCases()
#     obj1.sortingDataByConfirmedCases()
#     obj1.gettingTopCountriesByCaseCount(5)
#     obj1.regionWithLowestDeathCount()
#     obj1.countriesCaseSummary('India')
#     obj1.caculateMortalityRatesByRegion()
#     obj1.compareRecoveryRatesAcrossRegion()
#     obj1.detectOutlinersInCaseCounts('Active')
#     obj1.groupDataByCountryAndRegion()
#     obj1.regionsWithZeroRecoveredCases()

    obj2 = CoronaCaseVisualizer()
    obj2.stackedBarConfirmedDeathsRecoveredCases()