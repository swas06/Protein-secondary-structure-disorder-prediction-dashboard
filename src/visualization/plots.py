import plotly.express as px

def create_disorder_plot(df):
    return px.line(df, x="Position", y="Disorder Score")