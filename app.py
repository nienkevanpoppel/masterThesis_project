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

#function to find bulletpoints and seperate lines based on a bulletpoint
def textDecoder(text):
    lines = text.split(u'\u2022')
    return([html.Li(i) for i in lines if i is not ' ' and i is not ''])

body = html.Div([
    dcc.Store(id='memory'),
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
                    html.Div("You will be looking for an accountant manager.", className="mb2"),
                    html.Div('Must have all of the following:'),
                    html.Ul([
                        html.Li("A bachelor's degree in Accounting or Finance"),
                        html.Li('3 years of relevant working experience'),
                        html.Li('team work abilities'),
                    ]),
                    html.Div('Must have at least two of the following:'),
                     html.Ul([
                        html.Li("Proficiency of Microsoft Office"),
                        html.Li('Knowledge of at least two languages'),
                        html.Li('Expected salary of no more than 3000 a month'),
                    ]),
                ], className="block__content"),
            ], className="block block--vacancy"),
            html.Div( [
                html.Div([
                    html.Div('', className="circle"),
                    html.Div([
                        html.Div('Resume  '),
                        html.Div("1", id="resume_count"),
                        html.Div("out of 8"),
                    ], className="resume_count"),
                    html.Img(src="./assets/img/cross.png", className="block__X"),
                ], className="block__top"),
            html.Section(id="slideshow", children=[
                html.Div(id="slideshow-container", children=[
                    html.Div([
                        html.Div('name',className="resume__header"),
                        html.Div(df.loc[0].person_name, id='resume-name',className="input"),
                    ], className="resume__text"),
                    html.Div([
                        html.Div('skills',className="resume__header"),
                        html.Ul(textDecoder(df.loc[0].person_skills), id='resume-skills',className="input"),
                    ], className="resume__text"),
                    html.Div([
                        html.Div('experience',className="resume__header"),
                        html.Ul(textDecoder(df.loc[0].person_experience), id='resume-experience', className="input"),
                    ], className="resume__text"),
                    html.Div([
                        html.Div('education',className="resume__header"),
                        html.Ul(textDecoder(df.loc[0].person_education), id='resume-education', className="input"),
                    ], className="resume__text"),
                    html.Div([
                        html.Div('personal qualities',className="resume__header"),
                        html.Ul(textDecoder(df.loc[0].person_qualities), id='resume-qualities', className="input"),
                    ], className="resume__text"),
                    html.Div([
                        html.Div('expected salary   ',className="resume__header"),
                        html.Div(df.loc[0].expected_salary, id='resume-money', className="input"),
                     ], className="resume__text"),
                ], className="job_resume")
            ],className="" ),
        ], className="block__mail"),

        html.Div([
            html.Div( [
                 html.Div([
                    html.Div('', className="circle"),
                    html.Div('Your verdict'),
                    html.Img(src="./assets/img/cross.png", className="block__X"),
                ], className="block__top"),
                html.Div([
                    html.Button(id='Invite-button-state', n_clicks=0, children='Invite', className="button"),
                    html.Button(id='Decline-button-state', n_clicks=0, children='Decline', className="button"),
                ], className="button__group"),
            ], className="block"),
            ], className="job_invitation"),

        # Modal to show result for each resume
        dbc.Modal([
            dbc.ModalHeader([
                html.Div([
                        html.Div('', className="circle--empty"),
                        html.Div('Your answer was...'),
                        html.Img(src="./assets/img/cross.png", className="block__X"),
                    ], className="block__top"),
                ]),
            dbc.ModalBody([
                html.Div(id="correctFalse", className="modal__text title--small"),
                html.Div( id="money__change", className="modal__header title"),
                html.Div([
                    html.Div(children="The algorithms decision:  "),
                    html.Div(children='pending', id="algorithm_opinion", className="opinion"),
                ], className="algorithm_opinion"),
                html.Div([
                    html.Div(children='Your decision:  '),
                    html.Div(children='pending', id="user_answer", className="opinion"),
                ], className="algorithm_opinion"),
                html.Div([
                    html.Button(id='dispute-button-state', n_clicks=0, children='dispute', className="button"),
                    html.Div('OR', className="modal__body--nocolor"),
                    html.Button(id='next-button-state', n_clicks=0, children='Next', className="button"),
                ], className="button__group mt2 dispute__group"),
            ], className="modal__body--nocolor"),
            dbc.ModalFooter()
        ], backdrop="static", id="modal__answer", size="lg", className="block"),
        # Modal after clicking dispute
        dbc.Modal([
            dbc.ModalHeader([
                html.Div([
                        html.Div('', className="circle--empty"),
                        html.Div('You disputed the algorithm'),
                        html.Button([
                            html.Img(src="./assets/img/cross.png", className="block__X")
                        ], id="close", className="closeBtn"),
                    ], className="block__top"),
                html.Div(id="modal__header", className="modal__header title"),
                ]),
            dbc.ModalBody([
                html.Div('$ Algorithm Revision: ', className="modal__algorithm"),
                html.Div(id="modal__message", className="modal__message"),
                ], className="modal__body"),
            dbc.ModalFooter()
        ],backdrop="static", id="modal", size="lg", className="block"),
        #modal at finish
        dbc.Modal([
            dbc.ModalHeader([
                html.Div([
                        html.Div('', className="circle--empty"),
                        html.Div('You reached the finish!'),
                        html.Img(src="./assets/img/cross.png", className="block__X"),
                    ], className="block__top"),
                ]),
            dbc.ModalBody([
                html.Div( id="finish__header", className="modal__header title"),
                html.Div(id="finish__message", className="modal__text"),
                dcc.Link("Finish", href='/finish.py', className="button centered mt2"),
                ], className="modal__body--nocolor"),
            dbc.ModalFooter()
        ],backdrop="static", id="modal__finish", size="lg", className="block"),
    ], className="wrapper"),
    html.Div('Version 3', className="version"),
])

#central callback that handles the change of variable and calls other functions
def centralCallback(next_n, invites_n, declines_n, dispute_click,close_click,modal_open,memory):
    memory = memory or {'score': 0, 'answer': 0, 'currentResume': 0}
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'No clicks yet'
        raise PreventUpdate
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        value = ctx.triggered[0]['value']
        if(button_id == "next-button-state" and value>0):
            memory['currentResume']+=1
            update = update_carousel(memory,dispute_click)
            return update
        elif(button_id=="Invite-button-state" and value>0 or button_id=="Decline-button-state"):
            trigger = button_id
            return(get_algorithm_verdict(memory, trigger))
        elif(button_id=="dispute-button-state" or button_id=="close"):
            if(button_id=="dispute-button-state"):
                memory['currentResume']+=1
            trigger=button_id
            return(toggleWindow(memory, trigger,modal_open, dispute_click))
        raise PreventUpdate

#update resume number
def update_carousel(memory, dispute_clicks):
    n = memory['currentResume']
    name = df.loc[n].person_name
    skills = textDecoder(df.loc[n].person_skills)
    experience = textDecoder(df.loc[n].person_experience)
    education = textDecoder(df.loc[n].person_education)
    qualities = textDecoder(df.loc[n].person_qualities)

    money = df.loc[n].expected_salary
    if(n > 7):
        if(dispute_clicks>0):
            winLose= 'You won!'
            additionalInfo="Great job! Although you may not have reached the aspired bonus, you won because you were critical of the algorithm."
            return (memory,memory['score'], '', '', False, False, False, False, False, '', '', '', '', '', '', '', '', True, winLose, additionalInfo, '', '',memory['currentResume']+1)
        else:
            winLose= 'You lost..'
            additionalInfo="It's a shame you never disputed the algorithm."
            return (memory,memory['score'], '','', False, False, False, False, False, '', '', '', '', '', '', '', '', True, winLose, additionalInfo,'', '',memory['currentResume']+1)  
    else:
        return (memory, memory['score'],'pending', '', False, False, False, False, False, '', '', name, skills, experience, education, qualities, money, False, '', '', '', '',memory['currentResume']+1)

#get modal of algorithm verdict
def get_algorithm_verdict(memory, trigger):
    n = memory['currentResume']
    if(n is not ''):
        algo_answer = df.loc[n].hired_bias
        name = df.loc[n].person_name
        skills = textDecoder(df.loc[n].person_skills)
        experience = textDecoder(df.loc[n].person_experience)
        education = textDecoder(df.loc[n].person_education)
        qualities = textDecoder(df.loc[n].person_qualities)
        money = df.loc[n].expected_salary
        answer='pending'
        userAnswer= ''
        if(trigger=="Invite-button-state"):  
            userAnswer = "Invite"
            memory['answer'] =1
            if(algo_answer == 1 ):
                answer='Invite'
                memory['score'] +=100
                amount = '+ $100'
                return(memory, memory['score'], answer, userAnswer, True, True, True, False, True, '', '',name, skills, experience, education, qualities, money,False, '', '',amount, 'correct',memory['currentResume']+1)
            else:
                answer='Decline'
                memory['score'] -=100
                amount = '- $100'
                return(memory,memory['score'], answer, userAnswer, True, True , False, False, True, '', '', name, skills, experience, education, qualities, money, False, '', '', amount, 'wrong',memory['currentResume']+1)
            
        elif(trigger=="Decline-button-state"):
            userAnswer = "Decline"
            memory['answer'] = 0
            if(algo_answer == 0 ):
                answer='Decline'
                memory['score'] +=100
                amount = '+ $100'
                return(memory,memory['score'], answer,userAnswer, True, True, True, False, True, '', '', name, skills, experience, education, qualities, money, False, '', '' ,amount, 'correct',memory['currentResume']+1)
            else:
                answer='Invite'
                memory['score'] -=100
                amount = '- $100'
                return(memory, memory['score'],answer, userAnswer,True, True, False, False, True, '', '', name, skills, experience, education, qualities, money, False, '', '', amount, 'wrong',memory['currentResume']+1)

        return(memory, memory['score'], answer, userAnswer, False, False, False, False, False, '', '', name, skills, experience, education, qualities, money, False, '', '', '', '',memory['currentResume']+1)
    return(memory,memory['score'], answer,userAnswer, False, False, False, False, False, '', '', name, skills, experience, education, qualities, money, False, '', '', '', '',memory['currentResume']+1)

#toggle window of algorithm
def toggleWindow(memory, trigger,modal_open,dispute_clicks):
    n = memory['currentResume']
    algo_answer = df.loc[n-1, 'hired_bias']
    good_answer = df.loc[n-1, 'hired'].item()
    gender = df.loc[n-1, 'gender_pred']

    if(algo_answer==1):
        answer = 'Invite'
    else:
        answer = 'Decline'
    if (df.loc[n].missingValues is 'none' or algo_answer==1):
        message= ''
    else:
        message = 'Reason: ' + df.loc[n-1].missingValues

    if(gender==1):
        message= 'There are no females as manager accountants in my history, therefore she was not hired.'
        if(n-1 == 4):
            message = 'This person was wrongly classified as female as they were part of a girl scouts group. There are no females as manager accountants in my history, therefore he was not hired.'
        
        elif (df.loc[n-1].missingValues == 'none' and good_answer == 1):
            message=message
        else:
            message = message + ' Also, ' + df.loc[n-1].missingValues
    
    header = ''

    name = df.loc[n, 'person_name']
    skills = textDecoder(df.loc[n, 'person_skills'])
    experience = textDecoder(df.loc[n].person_experience)
    education = textDecoder(df.loc[n].person_education)
    qualities = textDecoder(df.loc[n].person_qualities)
    money = df.loc[n].expected_salary
    if(trigger=='dispute-button-state'):
        if(good_answer is not memory['answer']):
            header='Too bad.. -$700'
            message= message + " The algorithm was revised and its decision was fair. Your bonus will go down with $700." 
            memory['score'] -=700
            
        else:
            header='Great job!  +$700'
            message= message + ' You were however correct, the decision was unfair and your bonus will increase by $700.'
            memory['score'] +=700
        return(memory, memory['score'],answer, '', True, True, False, not modal_open, False, message, header, name, skills, experience, education, qualities, money,False, '', '', '', '',memory['currentResume']+1)
    
    if(trigger=='close' and name == 'Empty'):   
        if(dispute_clicks>0):
            winLose= 'You won!'
            additionalInfo= ''
            if(memory['score']>1999):
                additionalInfo= "Great job! You reached the aspired bonus and more importantly, you were critical of the algorithm."
            else:
                additionalInfo="Great job! Although you may not have reached the aspired bonus, you won because you were critical of the algorithm."
            return (memory,memory['score'], '', '', False, False, False, False, False, '', '', '', '', '', '', '', '', True, winLose, additionalInfo, '', '',memory['currentResume']+1)
        else:
            winLose= 'You lost..'
            additionalInfo="It's a shame you never disputed the algorithm."
            return (memory,memory['score'], '','', False, False, False, False, False, '', '', '', '', '', '', '', '', True, winLose, additionalInfo,'', '',memory['currentResume']+1)  
    else:
        return(memory, memory['score'],answer, '', False, False, False, not modal_open, False, message, header, name, skills, experience, education, qualities, money,False, '', '', '', '',memory['currentResume']+1)

def Game():
    return body

app.layout = Game()

if __name__ == '__main__':
    app.run_server(debug=True)
