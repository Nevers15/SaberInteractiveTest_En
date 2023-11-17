import dash
from dash import html, dcc
import requests
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from dash.dependencies import Input, Output



def get_data(symbol):
    url = f"https://api.coincap.io/v2/assets/{symbol}/history?interval=d1"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Ошибка при получении данных с API")
    
    data = response.json()
    
    if "data" not in data:
        raise Exception("Нет данных для выбранной криптовалюты")
    
    df = pd.DataFrame(data["data"])
    df["date"] = pd.to_datetime(df["date"])
    return df


app = dash.Dash(__name__)

symbols = ["bitcoin", "ethereum", "litecoin", "xrp"]

app.layout = html.Div([
    html.H1("Price History"),
    dcc.Dropdown(
        id="symbol",
        options=[{"label": s.capitalize(), "value": s} for s in symbols],
        value="bitcoin"
    ),
    dcc.DatePickerRange(
        id="date_range",
        min_date_allowed=pd.to_datetime("2013-04-28").date(),
        max_date_allowed=pd.Timestamp.today().date(),
        start_date=pd.Timestamp.today().date() - pd.Timedelta(days=30),
        end_date=pd.Timestamp.today().date()
    ),
    dcc.Graph(id="graph")
])

@app.callback(
    Output("graph", "figure"),
    Input("symbol", "value"),
    Input("date_range", "start_date"),
    Input("date_range", "end_date")
)
def update_figure(symbol, start_date, end_date):
    df = get_data(symbol)
    df = df[df["date"].between(start_date, end_date)]
    
    df = df.set_index("date").resample("D").mean().reset_index()
    
    fig = go.Figure(data=[go.Candlestick(x=df["date"],
                                         open=df["priceUsd"],
                                         high=df["priceUsd"],
                                         low=df["priceUsd"],
                                         close=df["priceUsd"])])

    max_price = df['priceUsd'].max()
    min_price = df['priceUsd'].min()
    annotations = [
        go.layout.Annotation(
            x=df.loc[df['priceUsd']==max_price,
            "date"].iloc[0],
            y=max_price,
            text=f"Max price: {max_price:.2f}",
            showarrow=True,
            arrowhead=1,
            ax=-40,
            ay=-40
        ),
        go.layout.Annotation(
            x=df.loc[df['priceUsd']==min_price, "date"].iloc[0],
            y=min_price,
            text=f"Min price: {min_price:.2f}",
            showarrow=True,
            arrowhead=1,
            ax=40,
            ay=40
        )
    ]
    layout = go.Layout(
        title=f"Price history for {symbol.capitalize()}",
        xaxis=dict(title="Date"),
        yaxis=dict(title="Price (USD)"),
        annotations=annotations
    )

    fig.update_layout(layout)

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)