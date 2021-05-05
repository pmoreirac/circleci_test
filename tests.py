import pandas as pd

from main import pandas_to_list


def test_same_shape():
	series = pd.Series([1,2,3,4,5])
	lst = pandas_to_list(series)
	assert series.size == len(lst)

def test_df_sum():
	df = pd.DataFrame([1,2,3,4,5])
	assert df.sum() == 15