import plotly.figure_factory as ff
  
df = [dict(Task="A", Start='2020-01-01', Finish='2009-02-02'),
      dict(Task="Job B", Start='2020-03-01', Finish='2020-11-11'),
      dict(Task="Job C", Start='2020-08-06', Finish='2020-09-21')]
  
fig = ff.create_gantt(df)
fig.show()
