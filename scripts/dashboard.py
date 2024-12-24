import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

def create_dashboard(data_path):
    data = pd.read_csv(data_path)
    app = dash.Dash(__name__)

    # Layout
    app.layout = html.Div([
        html.H1("Telecom Data Dashboard"),
        dcc
