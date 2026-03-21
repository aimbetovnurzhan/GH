import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    try:
        sal2 = employee['salary'].drop_duplicates().sort_values(ascending = False).iloc[1]
    except IndexError:
        sal2 = None
    # employee['rank'] = employee['salary'].rank(method = 'dense', ascending = False)
    # res = employee[employee['rank'] == 2][['salary']].rename(columns = {'salary':'SecondHighestSalary'})
    return pd.DataFrame({'SecondHighestSalary': [sal2]})