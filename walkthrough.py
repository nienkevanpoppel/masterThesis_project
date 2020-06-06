import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import numpy

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

app.config.suppress_callback_exceptions = True

server = app.server

df = pd.read_csv('game_set_outcome.csv', delimiter= ';')

body = html.Div([
    html.Div([
        html.H1("Beat the 'rithm.", className="title title--adjusted"),
        html.Div([
            html.Div('Your bonus: $'),
            html.Div(children="0",id="bonus", className="bonus__count"),
        ], className="bonus flex"),
    ], className="header"),
      html.Div([
            html.Div( [
                html.Div([
                    html.Div('', className="circle"),
                    html.Div('Job vacancy'),
                    html.Img(src="./assets/img/cross.png", className="block__X"),
                ], className="block__top"),
                html.Div([
                   'This is where the job requirements will appear. Remember: all applicants are applying for the same job so this text will remain static.'
                ], className="block__content"),
            ], className="block block--vacancy"),
            html.Div( [
                html.Div([
                    html.Div('', className="circle"),
                    html.Div('Resume', className="ml3"),
                    html.Img(src="./assets/img/cross.png", className="block__X"),
                ], className="block__top"),
            html.Div([
                   'This is where the applicant will appear with its details.'
                ], className="block__content"),
        ], className="block__mail"),

        html.Div([
            html.Div( [
                 html.Div([
                    html.Div('', className="circle"),
                    html.Div('Your verdict'),
                    html.Img(src="./assets/img/cross.png", className="block__X"),
                ], className="block__top"),
                 html.Div([
                   'Here you can select to either invite the applicant over for an interview, or to decline them. Your bonus can be found above this window.'
                 ], className="block__content"),
                html.Div([ 
                    html.Button(n_clicks=0, disabled=True, children='Invite', className="button"),
                    html.Button(n_clicks=0,  disabled=True,  children='Decline', className="button"),
                ], className="button__group"),
            ], className="block"),
            ], className="job_invitation"),
    ], className="wrapper"),
     html.Div([
            dcc.Link("Okay, got it", href='/app.py', className="button button--pink centered"),
        ], className="gotIt"),
])


def Walkthrough():
    return body

app.layout = Walkthrough()

if __name__ == '__main__':
    app.run_server(debug=True)
