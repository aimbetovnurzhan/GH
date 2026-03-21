import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department_map = department.set_index("id")["name"]
#    employee = employee.sort_values(by=['departmentId', 'salary'], ascending=[True, False]).drop(columns = ['id', 'departmentId'])
    employee['rank'] = employee.groupby('departmentId')['salary'].rank(method = 'dense', ascending = False)
    employee = employee[employee['rank'] < 4]#.drop(columns = ['id', 'departmentId','rank'])
    employee["Department"] = employee["departmentId"].map(department_map)
    employee = employee[['Department', 'name', 'salary']].rename(columns = {'name': 'Employee', 'salary': 'Salary'})
    return employee