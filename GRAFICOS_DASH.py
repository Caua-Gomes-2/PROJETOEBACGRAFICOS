import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv('ecommerce_estatistica.csv')

# Visualizando as primeiras linhas do DataFrame
print(df.head())

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Inicializando a aplicação Dash
app = dash.Dash(__name__)

# Criando um layout básico
app.layout = html.Div([
    html.H1("Visualização de Estatísticas de Ecommerce"),

    dcc.Dropdown(
        id='grafico-dropdown',
        options=[
            {'label': 'Gráfico de Vendas', 'value': 'vendas'},
            {'label': 'Gráfico de Clientes', 'value': 'clientes'},
            # Adicione mais opções conforme necessário
        ],
        value='vendas'  # Valor padrão
    ),

    dcc.Graph(id='grafico')
])


# Callback para atualizar o gráfico com base na seleção do dropdown
@app.callback(
    Output('grafico', 'figure'),
    Input('grafico-dropdown', 'value')
)
def update_graph(selected_graph):
    if selected_graph == 'vendas':
        fig = px.bar(df, x='data', y='vendas', title='Vendas ao Longo do Tempo')
    elif selected_graph == 'clientes':
        fig = px.line(df, x='data', y='clientes', title='Número de Clientes ao Longo do Tempo')
    # Adicione mais condições para outros gráficos
    else:
        fig = px.bar(df, x='data', y='vendas', title='Vendas ao Longo do Tempo')  # Gráfico padrão

    return fig


# Executando a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)