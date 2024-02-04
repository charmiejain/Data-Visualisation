# 1
# Generate a histogram using any library to visualize the distribution of salaries among employees in the dataset.

import matplotlib as mpl
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 

employee=pd.read_csv(r'C:/Users/charm/OneDrive/Desktop/Datasets/Employee data.csv')
print(employee.head())
employee.plot(kind = 'hist')
plt.title('Distribution of salaries')
plt.xlabel('Salary')
plt.ylabel('Gender of employee')
plt.show()

# for only 2 columns
df_employee = employee.drop(employee.columns[[0,2,3,4,6,7,8,9]], axis=1)
print(df_employee.head())
df_employee.plot(kind="hist")
plt.title("Distribution of Salaries based on GENDER")
plt.show()


# 2
# Generate a bar plot to compare the average salary of male and female employees using any library.
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

employee=pd.read_csv(r'C:/Users/charm/OneDrive/Desktop/Datasets/Employee data.csv')

average=employee.groupby('gender')['salary'].mean()
average.plot(kind='bar',color=['brown','red'])
plt.title('Average salary of male and female')
plt.xlabel('Gender')
plt.ylabel('Salary')
plt.show()

# 3
# Create a scatter plot using any library to illustrate the relationship between previous work experience (prevexp) and the current salary of employees.
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

employee=pd.read_csv(r'C:/Users/charm/OneDrive/Desktop/Datasets/Employee data.csv')
employee.plot(kind='scatter',
              x='prevexp',
              y='salary')
plt.title('Relationship between prevexp and salary')
plt.xlabel('prevexp')
plt.ylabel('current salary')
plt.show()

# 4
# Generate a pie chart to visualize the distribution of educational backgrounds among employees.
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

employee=pd.read_csv(r'C:/Users/charm/OneDrive/Desktop/Datasets/Employee data.csv')

df_employee = employee.groupby('educ', axis=0).sum()
df_employee['salary'].plot(kind='pie')

plt.title('Distribution of Educational Backgrounds Among Employees')
plt.show()



# 5
# Use any AI library such as sweetviz or dtale to generate the summary of the data. 
import pandas as pd
import sweetviz as sv
employee=pd.read_csv(r'C:/Users/charm/OneDrive/Desktop/Datasets/Employee data.csv')
employee_report=sv.analyze(employee)
employee_report.show_html('employee.html')

