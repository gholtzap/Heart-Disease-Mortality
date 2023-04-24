import numpy as np
from scipy.stats import ttest_ind_from_stats

male_data = np.array([386.7, 535.9, 447, 609, 332.1, 370.3, 525.7, 416.6, 481.5, 435, 587.1, 449.1, 328.5, 503.1, 387.2, 481.2, 317, 416.9, 343.6, 500.6, 463.4, 385.5, 384, 546.3, 436.7, 594.3, 458.4, 424.9, 565.7, 434.7])
female_data = np.array([224.7, 245.3, 324.3, 241.9, 202.7, 136.8, 136.7, 222.2, 90.7, 97.7, 315.1, 105.9, 256, 143.9, 114, 93.6, 260, 203.3, 389.4, 186.1, 185.6, 115.1, 144.8, 160.8, 110.1, 92.7, 254.4, 150, 164.4, 208.6])

mean1 = np.mean(male_data)
mean2 = np.mean(female_data)
var1 = np.var(male_data, ddof=1)
var2 = np.var(female_data, ddof=1)
n1 = len(male_data)
n2 = len(female_data)

pooled_variance = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)

t_statistic, p_value = ttest_ind_from_stats(mean1, np.sqrt(var1), n1, mean2, np.sqrt(var2), n2, equal_var=True)

print("t-statistic:", t_statistic)
print("p-value:", p_value)
