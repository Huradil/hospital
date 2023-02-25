from . import db


class Client(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fio=db.Column(db.String)
    birth_date=db.Column(db.DateTime)
    inn=db.Column(db.String)
    gender=db.Column(db.String)
    phone_num=db.Column(db.String)
    address=db.Column(db.String)
    date_app=db.Column(db.DateTime)

    def __str__(self):
        return self.fio


class Doctor(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fio=db.Column(db.String)
    birth_date=db.Column(db.DateTime)
    position=db.Column(db.String)
    experience=db.Column(db.Integer)

    def __str__(self):
        return self.fio

class MedicalHistory(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    client_id=db.Column(db.Integer,db.ForeignKey('client.id'))
    client=db.relationship('Client',backref=db.backref('medical_histories',lazy='dynamic'))
    doctor_id=db.Column(db.Integer,db.ForeignKey('doctor.id'))
    doctor=db.relationship('Doctor',backref=db.backref('medical_histories',lazy='dynamic'))
    diagnosis=db.Column(db.String)



