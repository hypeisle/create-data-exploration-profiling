import pandas as pd
from ydata_profiling import ProfileReport

#load a sample dataset
df = pd.read_csv('covid_worldwide.csv')

#generate a profile report
profile = ProfileReport(df, title="Pandas Profiling Report")

#Display it directly in notebook
#profile.to_notebook_iframe()

#Export the report to an html file
profile.to_file("profiling_report.html")