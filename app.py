import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# ------------------ DATA LOADING ------------------ #
def load_data():
    try:
        df = pd.read_csv('formatted_sales_data.csv')
        df['date'] = pd.to_datetime(df['date'])

        price_increase_date = pd.Timestamp('2021-01-15')
        df['price_period'] = df['date'].apply(
            lambda x: 'After Price Increase' if x >= price_increase_date else 'Before Price Increase'
        )
        return df
    except FileNotFoundError:
        print("Error: formatted_sales_data.csv not found.")
        return None


# ------------------ LOAD DATA ------------------ #
df = load_data()

if df is not None:
    total_sales = df['sales'].sum()
    avg_daily_sales = df.groupby('date')['sales'].sum().mean()
    date_range = f"{df['date'].min().strftime('%b %d, %Y')} to {df['date'].max().strftime('%b %d, %Y')}"

    before = df[df['date'] < pd.Timestamp('2021-01-15')]
    after = df[df['date'] >= pd.Timestamp('2021-01-15')]

    before_avg = before.groupby('date')['sales'].sum().mean() if not before.empty else 0
    after_avg = after.groupby('date')['sales'].sum().mean() if not after.empty else 0
    percent_change = ((after_avg - before_avg) / before_avg * 100) if before_avg > 0 else 0
else:
    total_sales = avg_daily_sales = before_avg = after_avg = percent_change = 0
    date_range = "No data"

# ------------------ STYLES ------------------ #
card_style = {
    'flex': '1',
    'padding': '25px',
    'borderRadius': '16px',
    'background': 'rgba(255,255,255,0.05)',
    'color': 'white',
    'boxShadow': '0 8px 25px rgba(0,0,0,0.5)'
}

glass_card = {
    'marginTop': '30px',
    'padding': '25px',
    'borderRadius': '16px',
    'background': 'rgba(255,255,255,0.04)'
}

impact_style = {
    'background': 'linear-gradient(135deg, #1a1a2e, #2b0a2e)',
    'padding': '35px',
    'borderRadius': '18px',
    'marginTop': '30px'
}

filter_style = {
    'marginTop': '30px',
    'padding': '20px',
    'background': '#000',
    'borderRadius': '12px'
}

# ------------------ APP INIT ------------------ #
app = dash.Dash(__name__)
app.title = "Soul Foods - Sales Dashboard"

# ------------------ HELPER ------------------ #
def stat_box(title, value, color):
    return html.Div([
        html.P(title, style={'color': '#bbb'}),
        html.H3(f"${value:,.2f}", style={'color': color})
    ], style={
        'flex': '1',
        'background': '#111',
        'padding': '20px',
        'borderRadius': '12px',
        'textAlign': 'center'
    })

# ------------------ LAYOUT ------------------ #
app.layout = html.Div([

    # HEADER
    html.Div([
        html.H1("🍬 Soul Foods Sales Dashboard", style={'color': 'white', 'textAlign': 'center'}),
        html.P("Performance before & after Jan 15, 2021 price increase",
               style={'color': '#bbbbbb', 'textAlign': 'center'})
    ], style={
        'background': 'linear-gradient(135deg, #1f0036, #3b0a57)',
        'padding': '35px',
        'borderRadius': '18px',
        'marginBottom': '30px',
        'boxShadow': '0px 10px 35px rgba(0,0,0,0.6)'
    }),
    
    # STATS TILES
    html.Div([
        html.Div([html.H4("📅 Date Range", style={'color': '#EF61FF'}),
                  html.P(date_range, style={'fontSize': '22px', 'fontWeight': 'bold'})], style=card_style),

        html.Div([html.H4("💰 Total Sales", style={'color': '#EF61FF'}),
                  html.P(f"${total_sales:,.2f}", style={'fontSize': '22px', 'fontWeight': 'bold'})], style=card_style),

        html.Div([html.H4("📊 Avg Daily Sales", style={'color': '#EF61FF'}),
                  html.P(f"${avg_daily_sales:,.2f}", style={'fontSize': '22px', 'fontWeight': 'bold'})], style=card_style),
    ], style={'display': 'flex', 'gap': '15px'}),

    # Price Increase Impact
    html.Div([
        html.H2("📈 Price Increase Impact", style={'color': 'white', 'textAlign': 'center'}),
        html.Div([
            stat_box("Before Jan 15, 2021", before_avg, "#4CAF50"),
            html.Div([
                html.H1("➜", style={'color': 'white'}),
                html.H3(f"{percent_change:+.1f}%",
                        style={'color': '#00E676' if percent_change > 0 else '#FF5252'})
            ], style={'textAlign': 'center', 'flex': '0.6'}),
            stat_box("After Jan 15, 2021", after_avg, "#FF5722"),
        ], style={'display': 'flex', 'alignItems': 'center'})
    ], style=impact_style),

    # LINE GRAPH
    html.Div([
        html.H3("📊 Sales Trend Over Time", style={'color': '#EF61FF'}),
        dcc.Graph(id='main-chart')
    ], style=glass_card),

    # REGIONS OPTIONS
    html.Div([
        html.Label("Filter by Region:", style={'color': 'white', 'fontWeight': 'bold'}),
        dcc.RadioItems(
            id='region-filter',
            options=[{'label': f" {r}", 'value': r.lower()} for r in ['All', 'North', 'South', 'East', 'West']],
            value='all',
            inline=True,
            labelStyle={'color': '#EF61FF', 'marginRight': '25px'}
        )
    ], style=filter_style),

    # RESULT
    html.Div([
        html.H3("🧠 Business Insight", style={'color': '#EF61FF'}),
        html.Div([
            html.P(f"Daily sales changed by {percent_change:+.1f}% after the price increase.",
                   style={'color': 'white'})
        ], style={'background': 'rgba(0,255,150,0.06)', 'padding': '20px',
                  'borderRadius': '12px', 'borderLeft': '5px solid #00E676'})
    ], style={'marginTop': '30px'}),

], style={'backgroundColor': '#0f0f1a', 'padding': '30px', 'fontFamily': 'Segoe UI'})

# ------------------ CALLBACK ------------------ #
@app.callback(Output('main-chart', 'figure'), [Input('region-filter', 'value')])
def update_chart(region):
    if df is None:
        return {}

    filtered = df if region == 'all' else df[df['region'] == region]
    daily = filtered.groupby('date')['sales'].sum().reset_index()

    fig = px.line(daily, x='date', y='sales', template='plotly_dark')
    fig.add_vline(x='2021-01-15', line_dash="dash", line_color="red")
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    return fig

# ------------------ MAIN ------------------ #
if __name__ == '__main__':
    app.run(debug=True)
