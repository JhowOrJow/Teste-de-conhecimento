from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("inventario_top_20_small.xlsx")
escolha = list(df["Descrição"].unique())
escolha.append("todos os componentes")


fig = px.bar(df, x="Material", y="Saldo", color="Descrição", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Controle de Inventário'),
    
    html.H2(children=' TOP 20 Small'),
    
    html.H2(children='Gráfico dos principais componentes com Déficit da semana!!'),
    
    html.Div(children='''       
        Dashboard feito em python\n
        by: JONATHAN N VELOSO 
    '''),
    dcc.Dropdown (escolha, value='todos os componentes',id='lista_componentes'),
    
    dcc.Graph(
        id='Gráfico_do_Inventário',
        figure=fig
    )
])

@app.callback(
    Output('Gráfico_do_Inventário', 'figure'),
    Input('lista_componentes','value')
)
def  update_output(value):
    if value == "todos os componentes":
        fig = px.bar(df, x="Material", y="Saldo", color="Descrição", barmode="group")
    else:
        tabela_filtrada = df.loc[df['Descrição']==value,:]    
        fig = px.bar(tabela_filtrada, x="Material", y="Saldo", color="Descrição", barmode="group")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)