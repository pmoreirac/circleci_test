# This is a sample Python script.
import pandas
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def pandas_to_list(df):
    return df.to_list()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lst = pandas_to_list(pd.Series([1,2,3,4,5]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
