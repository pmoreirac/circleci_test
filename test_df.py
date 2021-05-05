import pandas as pd

from main import pandas_to_list, sum_df

series = pd.Series([1,2,3,4,5])
lst = pandas_to_list(series)
assert series.size == len(lst)

df = pd.Series([1,2,3,4,5])
assert sum_df(df) == 17