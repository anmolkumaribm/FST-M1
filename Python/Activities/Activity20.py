import pandas

dataframe = pandas.read_excel('sample.xlsx')
print("Number of rows and columns:", dataframe.shape)

print("Email:")
print(dataframe['Email'])
print("Sorted data")
print(dataframe.sort_values('FirstName'))