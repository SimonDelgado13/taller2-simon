import numpy as np
import pandas as pd
import datetime

df = pd.read_csv("BikePrices.csv")

df.isna().sum()
df['Ex_Showroom_Price'] = df['Ex_Showroom_Price'].interpolate()

df.duplicated().sum()
df.drop_duplicates()
