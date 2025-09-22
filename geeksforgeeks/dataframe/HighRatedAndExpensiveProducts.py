import pandas as pd

products_data = [
    [101, "iPhone 13", 4.8, 10, 999.99],
    [102, "Samsung Galaxy S21", 4.2, 0, 799.99],
    [103, "MacBook Pro 16", 4.7, 5, 2399.99],
    [104, "AirPods Pro", 4.4, 3, 249.99],
    [105, "Sony WH-1000XM4", 4.9, 2, 349.99],
    [106, "LG OLED TV", 4.6, 15, 1499.99],
    [107, "Samsung QLED TV", 4.7, 12, 1799.99],
    [108, "Dell XPS 13", 4.8, 8, 1499.99],
    [109, "Microsoft Surface", 4.6, 4, 1299.99],
    [110, "Bose QuietComfort", 4.9, 7, 399.99]
]

productsDataDf = pd.DataFrame(products_data, columns=["ID", "Product_Name", "Rating", "Stock", "Price"])

print(productsDataDf)

print(productsDataDf[(productsDataDf['Rating']>=4.5) & (productsDataDf['Stock']>0) & (productsDataDf['Price']>300)])