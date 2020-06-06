import dash
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True

server = app.server

body = html.Div([
    html.Div([
        html.Div([
            html.Div('', className="circle"),
            html.Div('Finish'),
            html.Img(src="./assets/img/cross.png", className="block__X"),
        ], className="block__top"),
        html.Div([
            html.Div('Thank you for playing!', className="mb2"),
            html.Div("Algorithms like these are used all the time in real life, this specific algorithm was inspired by Amazon’s hiring algorithm. Amazon’s algorithm was supposed to rank candidates from one to five stars and then calculate a top 5 out of a range of resumes. This algorithm was soon criticized as it apparently had taught itself that male candidates were more successful than female applicants and started penalizing resumes that included words such as ‘girl scouts’ or ‘women’s chess club’."),
            html.Div("We increasingly rely on algorithms without knowing how they were trained. While the algorithm in the game explained why certain decisions were made, in reality they often do not. Most algorithms are black boxes in which decisions are made based on historic data and factual numbers and offer no insights to humans.", className="mb2"),
            html.Div([
                html.Div("To contribute to my research, please fill in the following questionnaire:"),
                html.A("Click here", href='https://forms.gle/WXu7PetFs9fjfbvh8', target="_blank", className="external__link")
            ], className="mb2"),
            
            html.Div("Thanks in advance, Nienke.", className="mb2"),
        ], className="block__content")
    ], className="block centered block--leftAlign ")
], className="finish__page")

def Finish():
    return body

app.layout = Finish()

if __name__ == '__main__':
    app.run_server(debug=True)
