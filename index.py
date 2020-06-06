import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import json
import flask

from app import Game, centralCallback 
from finish import Finish
from homepage import Home
from walkthrough import Walkthrough
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
app.config.suppress_callback_exceptions = True

server = app.server

layout = html.Div([
    dcc.Location(id = 'url', refresh = True),
    html.Div(id='page-content')
])

#router
def serve_layout():
    if flask.has_request_context():
        return layout
    return html.Div([
        layout,
        Home(),
        Game()
    ])

app.layout = serve_layout

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])

def display_page(pathname):
    if pathname=='/app.py':
        return Game()
    elif pathname=='/finish.py':
        return Finish()
    elif pathname=='/walkthrough.py':
        return Walkthrough()
    else:
        return Home()

@app.callback(
           [
            Output('memory', 'data'),
            Output('bonus', 'children'),
            Output('algorithm_opinion', 'children'),
            Output('user_answer', 'children'),
            Output('Invite-button-state', 'disabled'), 
            Output('Decline-button-state', 'disabled'),
            Output('dispute-button-state', 'disabled'),
            Output('modal', 'is_open'),
            Output('modal__answer', 'is_open'),
            Output('modal__message', 'children'),
            Output('modal__header', 'children'),
            Output('resume-name', 'children'),
            Output('resume-skills', 'children'),
            Output('resume-experience', 'children'),
            Output('resume-education', 'children'),
            Output('resume-qualities', 'children'),
            Output('resume-money', 'children'),
            Output('modal__finish', 'is_open'),
            Output('finish__header', 'children'),
            Output('finish__message', 'children'),
            Output('money__change', 'children'),
            Output('correctFalse', 'children'),
            Output('resume_count', 'children'),],
            [
            Input('next-button-state', 'n_clicks'),
            Input('Invite-button-state', 'n_clicks'), 
            Input('Decline-button-state', 'n_clicks'),
            Input('dispute-button-state', 'n_clicks'),
            Input('close', 'n_clicks')],
            [State("modal", "is_open"),
            State('memory', 'data')])

def generalCallback(next_n, invite_click, decline_click, dispute_click,close_click,modal_open,memory):
    click = centralCallback(next_n, invite_click, decline_click, dispute_click, close_click,modal_open,memory)
    return click


if __name__ == '__main__':
    app.run_server(debug=True)