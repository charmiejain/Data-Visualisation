import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
# from __future__ import print_function
 #adds compatibilty to python2


#install xlrd
# pip install xlrd
# print("xlrd installed!")

df_canada=pd.read_excel(r'C:/Users/charm/OneDrive/Desktop/Datasets/Canada.xlsx',
   #link of df,
    sheet_name="Canada by Citizenship",
    skiprows=range(20),
    skipfooter=2,
    index_col="OdName")

#print(df_canada.head())
df_canada = df_canada.rename_axis('Country')
df_canada = df_canada.rename(columns = {'AreaName' : 'Continent', 'RegName' : 'Region'}) 
df_canada = df_canada.drop(df_canada.columns[[0,1,2,4,6]],axis = 1)
df_canada['Total'] = df_canada.loc[:,1980:2013].sum(axis=1)
df_canada.loc['Haiti',range(1980,2014)].plot(kind = 'line')
plt.title('Imigration from Haiti')
plt.xlabel('Years')
plt.ylabel('Number of imigrants')
plt.show()




