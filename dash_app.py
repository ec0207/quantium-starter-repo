# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc,  Input, Output
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('./output_sales_data.csv')

colors = {
    'background': "#4745D9",
    'text': '#45D7D9'
}

fig = px.line(df, x="date", y="sales", line_group='region')
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    title_x=0.5
)

app.layout = html.Div(
    children=[
    html.H1(children='Pink Morsel Sales', 
            style={'textAlign': "center", 
                    "color": "#D9458D",
                    "background": colors["background"]}),
    html.H2(children="Select Sales in region:", 
           style={"color": colors["text"]}),
    dcc.RadioItems(
        id="region-radio",
        options=[
            {"label": r, "value": r} for r in df["region"].unique() 
        ] + [{"label": "All Regions", "value": "ALL"}],
        value=df["region"].unique()[0],
        inline=True   # display buttons horizontally
    ),
    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-radio", "value")
)
def update_graph(selected_region):
    
    if selected_region == "ALL":
        filtered = df
        title = "Sales in All Regions"
        fig = px.line(
        filtered,
        x="date",
        y="sales",
        title=title,
        color="region")
    else: 
        filtered = df[df["region"] == selected_region]
        title =  f"Sales in {selected_region}" 
        fig = px.line(
        filtered,
        x="date",
        y="sales",
        title=title)

    

    return fig


if __name__ == '__main__':
    app.run(debug=True)
