from week5.assignment.DataTransformer import DataTransformer
import pandas as pd
import matplotlib.pyplot as plt

class DataVisualizer(DataTransformer):
    def __init__(self):
        super().__init__()

    def visBar(self, x, y, xlabel, ylabel, title, color, width, alpha):
        barChart = plt.bar(x, y, color=color, width=width, alpha=alpha)
        plt.grid()
        plt.title(title)
        plt.bar_label(barChart, fmt='%.1f')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

    def visPie(self, x, startangleValue, autopctValue, legendValue):
        plt.pie(x, startangle=startangleValue, autopct=autopctValue)
        plt.legend(legendValue)
        plt.show()

    def visLine(self, x, y, xlabel, ylabel, title, label, marker, color):
        plt.plot(x, y, label=label, marker=marker, color=color)
        plt.legend()
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
    
    def visScatter(self, x, y, label, color, displayChart):
        plt.scatter(x, y, color=color, label=label)
        plt.legend()
        if displayChart==True : plt.show()

    def visHistogram(self, x, binsValues, xlabel, ylabel, edgeColorValue):
        plt.hist(x, bins=binsValues, edgecolor = edgeColorValue)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.show()

    def visBoxPlot(self, x, color):
        plt.boxplot(x,
            vert=True,
            patch_artist=True,
            notch=True,
            showmeans=True,
            boxprops=dict(facecolor="lightblue"),
            medianprops=dict(color="red", linewidth=2),
            meanprops=dict(marker="o", markerfacecolor="green", markersize=8),
            flierprops=dict(marker="x", color=color))
        plt.show()
    
    def doubleChart(self, x, y1, y2, label1, label2, color1, color2):
        self.visScatter(x, y1, label1, color1, False)
        self.visScatter(x, y2, label2, color2, False)
        plt.legend()
        plt.show()

    def pandaPlotChart(self, df: pd.DataFrame, chart_type: str, x: str = None, y: str = None):
        match chart_type.lower():
            case "scatter":
                if x and y:
                    df.plot.scatter(x=x, y=y)
                else:
                    raise ValueError("Scatter plot requires both x and y.")
            
            case "line":
                df.plot.line(x=x, y=y)
            
            case "bar":
                df.plot.bar()
            
            case "hist":
                df[y].plot.hist(bins=10)
            
            case "box":
                df[y].plot.box()
            
            case "area":
                df.plot.area(x=x, y=y)
            
            case "pie":
                if y:
                    df[y].value_counts().plot.pie(autopct='%1.1f%%')
                else:
                    raise ValueError("Pie chart requires y column.")
            
            case _:
                raise ValueError(f"Chart type '{chart_type}' is not supported.")
        
        plt.title(f"{chart_type.capitalize()} Chart")
        plt.xlabel(x if x else "")
        plt.ylabel(y if y else "")
        plt.show()