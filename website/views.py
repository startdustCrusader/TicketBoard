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
        ticket = request.form.get('ticket') #Gets the note from the HTML 

        if len(ticket) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_ticket = Ticket(data=ticket, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_ticket) #adding the note to the database 
            db.session.commit()
            flash('Ticket added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-ticket', methods=['POST'])
def delete_ticket():  
    ticket = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    ticketId = ticket['ticketId']
    ticket = Ticket.query.get(ticketId)
    if ticket:
        if ticket.user_id == current_user.id:
            db.session.delete(ticket)
            db.session.commit()

    return jsonify({})