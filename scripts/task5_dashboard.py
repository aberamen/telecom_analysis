import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load data
engagement_data = pd.read_csv("results/task_2_user_engagement.csv")
experience_data = pd.read_csv("results/task_3_experience.csv")
satisfaction_data = pd.read_csv("results/task_4_satisfaction.csv")

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Telecom Data Insights Dashboard"),
    dcc.Tabs([
        dcc.Tab(label="Engagement Analysis", children=[
            dcc.Graph(figure=px.histogram(engagement_data, x="session_duration", title="Session Duration"))
        ]),
        dcc.Tab(label="Experience Analysis", children=[
            dcc.Graph(figure=px.scatter(experience_data, x="RTT", y="throughput", title="RTT vs Throughput"))
        ]),
        dcc.Tab(label="Satisfaction Analysis", children=[
            dcc.Graph(figure=px.bar(satisfaction_data, x="MSISDN", y="satisfaction_score", title="User Satisfaction Scores"))
        ])
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)
