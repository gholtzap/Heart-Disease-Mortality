from scipy.stats import f

F_statistic,df1,df2 = 2.62314347555,29,29

# Calculate the p-value using the survival function (1 - CDF)
print("p-value:", f.sf(F_statistic, df1, df2))
