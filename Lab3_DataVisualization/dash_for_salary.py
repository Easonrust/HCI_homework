import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

s_b_r = pd.read_csv('salaries-by-region.csv')
s_b_c_t=pd.read_csv('salaries-by-college-type.csv')
d_t_p_b=pd.read_csv('degrees-that-pay-back.csv')

app.layout = html.Div([
    dcc.Tabs(id='dataset', value='Salaries by Region', children=[
        dcc.Tab(label='Salaries by Region', value='Salaries by Region'),
        dcc.Tab(label='Salaries by College Type', value='Salaries by College Type'),
    ],style={'height': '2%'}),
    html.Div([
            dcc.Dropdown(
                id='x',
                options=[{'label': 'Starting Median Salary', 'value': 'Starting Median Salary'},
                {'label': 'Mid-Career Median Salary', 'value': 'Mid-Career Median Salary'},
                {'label': 'Mid-Career 10th Percentile Salary', 'value': 'Mid-Career 10th Percentile Salary'},
                {'label': 'Mid-Career 25th Percentile Salary', 'value': 'Mid-Career 25th Percentile Salary'},
                {'label': 'Mid-Career 75th Percentile Salary', 'value': 'Mid-Career 75th Percentile Salary'},
                {'label': 'Mid-Career 90th Percentile Salary', 'value': 'Mid-Career 90th Percentile Salary'}],
                value='Starting Median Salary'
            )
        ],
        style={'width': '50%', 'display': 'inline-block'}),

    html.Div([
            dcc.Dropdown(
                id='y',
             options=[{'label': 'Starting Median Salary', 'value': 'Starting Median Salary'},
                {'label': 'Mid-Career Median Salary', 'value': 'Mid-Career Median Salary'},
                {'label': 'Mid-Career 10th Percentile Salary', 'value': 'Mid-Career 10th Percentile Salary'},
                {'label': 'Mid-Career 25th Percentile Salary', 'value': 'Mid-Career 25th Percentile Salary'},
                {'label': 'Mid-Career 75th Percentile Salary', 'value': 'Mid-Career 75th Percentile Salary'},
                {'label': 'Mid-Career 90th Percentile Salary', 'value': 'Mid-Career 90th Percentile Salary'}],
                value='Mid-Career Median Salary'
            )
        ],
        style={'width': '49%', 'display': 'inline-block'}),

    ##scatter graph
    html.Div([dcc.Graph(id='scatter')],style={'width': '50%','display': 'inline-block'}),
    html.Div([
        dcc.Graph(id='column'),dcc.Graph(id='pie')],
        style={'width': '49%','display': 'inline-block'}),
])
@app.callback(
    dash.dependencies.Output('scatter', 'figure'),
    [dash.dependencies.Input('dataset', 'value'),
    dash.dependencies.Input('x', 'value'),
    dash.dependencies.Input('y', 'value')])

def choose_dataset(dateset,xtype,ytype):
    df=s_b_r
    Class=''
    if dateset=='Salaries by Region':
        df=s_b_r
        Class='Region'
    elif dateset=='Salaries by College Type':
        df=s_b_c_t
        Class='School Type'
    return {
        'data': [go.Scatter(
            x=df[df[Class] == i][xtype],
            y=df[df[Class] == i][ytype],
            text=df[df[Class] == i]['School Name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        )for i in df[Class].unique()],
        'layout': go.Layout(
            xaxis={
                'title': xtype
            },
            yaxis={
                'title': ytype
            },
            height=600,
            title=dateset,
            hovermode='closest'
        )
        }


@app.callback(
    dash.dependencies.Output('column', 'figure'),
    [dash.dependencies.Input('x', 'value'),
    dash.dependencies.Input('y', 'value')])
def choose_column(col_type_1,col_type_2):
    df=d_t_p_b
    return {
        'data': [go.Bar(
            x=df['Undergraduate Major'],
            y=df[col_type_1],
            #marker=go.bar.Marker(
                   # color='rgb(55, 83, 109)'
                #),
            name=col_type_1),
            go.Bar(
            x=df['Undergraduate Major'],
            y=df[col_type_2],
            #marker=go.bar.Marker(
                   # color='rgb(55, 83, 109)'
                #),
            name=col_type_2)
            ],
        'layout': go.Layout(
            title='Salaries by Major Type',
            barmode='group',
            height=300
        )
        }

@app.callback(
    dash.dependencies.Output('pie', 'figure'),
    [dash.dependencies.Input('dataset', 'value')])

def choose_pie(dateset):
    df=s_b_r
    Class=''
    if dateset=='Salaries by Region':
        df=s_b_r
        Class='Region'
        return {
        'data': [go.Pie(
            labels=df[Class].unique(),
            values=[len(df[df[Class] == 'California']),len(df[df[Class] == 'Western']),len(df[df[Class] == 'Midwestern']),len(df[df[Class] == 'Southern']),len(df[df[Class] == 'Northeastern'])],
            hoverinfo='label+percent', textinfo='value',
            marker=dict(colors=['rgb(33, 75, 99)',
                                  'rgb(79, 129, 102)',
                                  'rgb(151, 179, 100)',
                                  'rgb(175, 49, 35)',
                                  'rgb(36, 73, 147)'])
        )],
        'layout': go.Layout(
            height=300,
            title=dateset,
        )
        }
    elif dateset=='Salaries by College Type':
        df=s_b_c_t
        Class='School Type'
        return {
        'data': [go.Pie(
            labels=df[Class].unique(),
            values=[len(df[df[Class] == 'Engineering']),len(df[df[Class] == 'Party']),len(df[df[Class] == 'Liberal Arts']),len(df[df[Class] == 'Ivy League']),len(df[df[Class] == 'State'])],
            hoverinfo='label+percent', textinfo='value',
            marker=dict(colors=['rgb(146, 123, 21)',
                                  'rgb(177, 180, 34)',
                                  'rgb(206, 206, 40)',
                                  'rgb(175, 51, 21)',
                                  'rgb(35, 36, 21)'])
        )],
        'layout': go.Layout(
            height=300,
            title=dateset,
        )
        }
  



if __name__ == '__main__':
    app.run_server()