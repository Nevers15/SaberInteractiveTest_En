# Test Task for Saber Interactive (Data Analyst Position)



***STATUS:*** **Completed**


## Project Goals:

The task involves completing a test assignment, which includes composing two SQL queries based on the provided data and creating an interactive application using one of the web frameworks (streamlit/dash/panel) according to the layout.

## Tasks:

### SQL 1:

Write a query that will output the average time tasks of each group spend in the "Open" status.
Conditions:
By group, we mean the first character in the task key. For example, for the key "C-40460," the group will be "C."
A task can transition to the same status multiple times.
Convert the time to hours rounded to two decimal places.

#### SQL 1 Task Execution Result:

<img src="https://i.imgur.com/VDryupk.png" alt="SQL1"/>

### SQL 2:

Write a query that will output the task key, the last status, and its creation time for tasks that are currently open.
Conditions:
Tasks are considered open if their last status at the moment is not "Closed" or "Resolved."
A task can transition to the same status multiple times.
Format the query so that, by changing the date, it can be used to search for open tasks at any point in the past.
Convert the time to textual representation.

#### 
Execution Result of SQL 2 Task:

<img src="https://i.imgur.com/A1Oj2vi.png" alt="SQL2"/>

There are 40 open tasks.

### Python Task:

Create an interactive application using one of the web frameworks (streamlit/dash/panel), based on the following layout.
Historical data and the list of assets should be obtained using the API:   https://docs.coincap.io/

Layout:

<img src="https://i.imgur.com/1xdHWwq.png" alt="Python_ex"/>

#### Python Task Execution Result:

In my solution, I used the Dash framework.

<img src="https://i.imgur.com/kylSVMg.png" alt="Python_Mine"/>

My version of the chart shows the points of maximum and minimum for the selected date range and allows switching between dates and currencies. The model has an additional interactive feature for zooming in and out of the chart.

The code for all tasks is available in this repository.

## Project Tools

- Python
- Pandas
- Sklearn
- Matplotlib.pyplot
- Dash
- SQLite3
