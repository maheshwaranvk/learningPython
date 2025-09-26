from week4.assignment.DataTransformer import DataTransformer
import pandas as pd

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
if __name__=="__main__":
    obj1 = CoronaCaseAnalyzer()
    obj1.summarizeCaseCountsByRegion()
    obj1.filterLowCaseRecords()
    obj1.regionWithHighestConfirmedCases()
    obj1.sortingDataByConfirmedCases()
    obj1.gettingTopCountriesByCaseCount(5)
    obj1.regionWithLowestDeathCount()
    obj1.countriesCaseSummary('India')
    obj1.caculateMortalityRatesByRegion()
    obj1.compareRecoveryRatesAcrossRegion()
    obj1.detectOutlinersInCaseCounts('Active')
    obj1.groupDataByCountryAndRegion()
    obj1.regionsWithZeroRecoveredCases()