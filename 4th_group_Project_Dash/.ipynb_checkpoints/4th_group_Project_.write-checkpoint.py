
import dash
from dash.dependencies import Input, Output
from dash import html
import dash_pivottable
from data import data

def Header(name, app):
    img_style = {"float": "right", "height": 40, "margin-right": 10}
    kma_logo = html.Img(src=app.get_asset_url("sig2.png"), style=img_style)
    sisul_logo = html.Img(src=app.get_asset_url("logo.gif"), style=img_style)
    fcseoul_logo = html.Img(src=app.get_asset_url("img_logo_gold.png"), style=img_style)
    

    return html.Div(
        [
            html.H1(name, style={"margin": 10, "display": "inline"}),
            html.A(fcseoul_logo, href="https://m.fcseoul.com/", target="_blank"),
            html.A(sisul_logo, href="https://www.sisul.or.kr/open_content/main/", target="_blank"),
            html.A(kma_logo, href="https://www.weather.go.kr/w/index.do", target="_blank"),
            
            html.A(
                html.Button(
                    "서울월드컵경기장",
                    style={
                        "float": "right",
                        "margin-right": "10px",
                        "margin-top": "5px",
                        "padding": "5px 10px",
                        "font-size": "15px",
                    },
                ),
                href="https://www.sisul.or.kr/open_content/worldcup/", target="_blank",
            ),
            html.Hr(),
        ]
    )


app = dash.Dash(__name__)
app.title = "Dash Pivottable"
server = app.server

app.layout = html.Div(
    [
        Header("월드컵 경기장 기상별 그래프", app),
        dash_pivottable.PivotTable(
            id="table",
            data=data,
            cols=["할인여부"],
            colOrder="key_a_to_z",
            rows=["휴일 여부"],
            rowOrder="key_a_to_z",
            rendererName="Grouped Column Chart",
            aggregatorName="Average",
            vals=["수입금(원)"],
            
        ),
        html.Div(id="output"),
    ]
)


@app.callback(
    Output("output", "children"),
    [
        Input("table", "cols"),
        Input("table", "rows"),
        Input("table", "rowOrder"),
        Input("table", "colOrder"),
        Input("table", "aggregatorName"),
        Input("table", "rendererName"),
    ],
)
def display_props(cols, rows, row_order, col_order, aggregator, renderer):
    return [
        html.P(str(cols), id="columns"),
        html.P(str(rows), id="rows"),
        html.P(str(row_order), id="row_order"),
        html.P(str(col_order), id="col_order"),
        html.P(str(aggregator), id="aggregator"),
        html.P(str(renderer), id="renderer"),
    ]


if __name__ == "__main__":
    app.run_server(debug=False)
