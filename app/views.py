from flask import render_template,url_for,redirect,request,flash
from . import db,app
from .forms import ClientForm,DoctorForm,MedicalHistoryForm
from .models import Client,Doctor,MedicalHistory


def index():
    return 'arl kot'

def client_create():
    form=ClientForm()
    if request.method=='POST':
        if form.validate_on_submit():
            client=Client()
            form.populate_obj(client)
            db.session.add(client)
            db.session.commit()
            flash("успешно",'succes')
            return redirect(url_for('client_list'))
        else:
            print(form.errors)
    return render_template('standart_form.html',form=form)


def doctor_create():
    form=DoctorForm()
    if request.method=='POST':
        if form.validate_on_submit():
            doctor=Doctor()
            form.populate_obj(doctor)
            db.session.add(doctor)
            db.session.commit()
            flash("успешно",'succes')
            return redirect(url_for('doctor_list'))
        else:
            flash('ошибка', 'danger')
    return render_template('standart_form.html',form=form)

def history():
    form=MedicalHistoryForm()
    form.doctor_id.choices=[(g.id, g.fio) for g in Doctor.query.order_by('fio')]
    form.client_id.choices=[(g.id, g.fio) for g in Client.query.order_by('fio')]
    if request.method=="POST":
        if form.validate_on_submit():
            history=MedicalHistory()
            form.populate_obj(history)
            db.session.add(history)
            db.session.commit()
            flash("история успешно создана","succes")
            return redirect(url_for('history_list'))
        else:
            flash('ошибка','danger')
    return render_template('standart_form.html',form=form)


def doctor_list():
    doctors=Doctor.query.all()
    return render_template('doctor_list.html',doctors=doctors)

def client_list():
    clients=Client.query.all()
    return render_template('client_list.html',clients=clients)

def history_list():
    histories=MedicalHistory.query.all()
    return render_template('history_list.html',histories=histories)

