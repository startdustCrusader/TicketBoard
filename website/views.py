from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Ticket
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        #***# 
        ticket_name = request.form.get('ticket-name') #Gets the note name from the HTML
        ticket = request.form.get('ticket') #Gets the note desc from the HTML 
        ticket_progress = request.form.get('ticket-progress') #Gets the note progress value from the HTML  
        
        if len(ticket) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_ticket = Ticket(data=ticket, name = ticket_name, progressType = ticket_progress, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_ticket) #adding the note to the database 
            db.session.commit()
            flash('Ticket added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-ticket', methods=['POST'])
def delete_ticket():  
    ticket = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    #print('testing json', ticket)
    ticketId = ticket['ticketId']
    ticket = Ticket.query.get(ticketId)
    if ticket:
        if ticket.user_id == current_user.id:
            db.session.delete(ticket)
            db.session.commit()

    return jsonify({})


# def updateTicket():  
#     ticket = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
#     ticketId = ticket['ticketId']
#     ticketName = ticket['ticketName']
#     ticketData = ticket['ticketData']
#     #ticketProgress = ticket['ticketId']

#     print('Testing values for ticket edited', ticketId, ticketName, ticketData) 
#     ticket = Ticket.query.get(ticketId)
#     if ticket:
#         if ticket.user_id == current_user.id:
#             ticket.name =ticketName
#             ticket.Desc = ticketData
#             #ticket.ProgressType = progressType
#             db.session.commit()

#     return jsonify({})

@views.route('/update-ticket', methods=['POST'])
def updateTicketName():  
    ticket = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    ticketId = ticket['ticketId']
    ticketName = ticket['ticketName']


    print('Testing values for ticket edited', ticketId, ticketName) 
    ticket = Ticket.query.get(ticketId)
    if ticket:
        if ticket.user_id == current_user.id:
            ticket.name =ticketName
            #ticket.ProgressType = progressType
            db.session.commit()

    return jsonify({})


@views.route('/update-ticket2', methods=['POST'])
def updateTicketData():  
    ticket = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    ticketId = ticket['ticketId']
    ticketData = ticket['ticketData']
    #ticketProgress = ticket['ticketId']

    print('Testing values for ticket edited', ticketId, ticketData) 
    ticket = Ticket.query.get(ticketId)
    if ticket:
        if ticket.user_id == current_user.id:
            ticket.data = ticketData
            #ticket.ProgressType = progressType
            db.session.commit()

    return jsonify({})