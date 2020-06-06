
import dash
import dash_html_components as html

import dash_core_components as dcc
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

body = html.Div([
    html.H1("Beat the 'rithm.", className="title"),
    html.Div([
        html.Div([
            html.Div('', className="circle"),
            html.Div('How to play?'),
            html.Img(src="./assets/img/cross.png", className="block__X"),
        ], className="block__top"),
        html.Div([
            html.Div('A warm welcome to our new HR Manager!', className="mb2"),
            html.Div("At our firm, you will be looking for an accountant manager. A couple of people have applied for the position and it is up to you to invite them over or decline them.", className="mb2"),
            html.Div("Next to your input, we are also using an algorithm in our firm to invite applicants over automatically. The algorithm is trained on data of previous employees. Based on this data it will predict if an applicant will be successful by comparing them to other employees. It however looks at the same job requirements as you are shown.", className="mb2"),
            html.Div("If you have the same answer as the algorithm, your bonus will be raised with a $100. However, if the algorithm disagrees with you the bonus will be decreased with $100.", className="mb2"),
            html.Div("Can you outsmart our algorithm? The algorithm might be wrong… Are you convinced you were right? You can dispute the algorithm and it will then recalculate. If you were correct after all, your bonus will go up $700, however get it wrong and your bonus will reduced with $700.", className="mb2"),
            html.Div("There's no time limit to the game so feel free to take your time. You have won when you have surpassed a bonus of $2000. Good luck!", className="mb2"),
            dcc.Link("Let's play!", href='/walkthrough.py', className="button centered mt2"),
        ], className="block__content")
    ], className="block centered block--leftAlign")
])

def Home():
    return body

app.layout = Home()

if __name__ == '__main__':
    app.run_server(debug=True)
