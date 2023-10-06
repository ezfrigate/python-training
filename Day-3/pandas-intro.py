#pandas for data analytics
#series : 1D data strcut dataframes : 2D data strct
import pandas
d = {'name': ['sb', 'bs'], 'age':['2', '5']}
df = pandas.DataFrame(d)
df.describe()
#check in nbook

df = pandas.read_csv(r'C:/Users/SESA509164/Desktop/data.csv')