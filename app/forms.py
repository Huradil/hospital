from flask_wtf import FlaskForm
import wtforms as wf
import datetime

class ClientForm(FlaskForm):
    fio=wf.StringField(label='фио клиента')
    birth_date=wf.DateField(label='дата рождения')
    inn=wf.StringField(label='ИНН',validators=[
        wf.validators.Length(min=16,max=16)
    ])
    gender=wf.SelectField(label='пол',choices=['male','female'])
    phone_num=wf.StringField(label='номер телефона',validators=[
        wf.validators.data_required(),
        wf.validators.Length(min=13,max=13)
    ])
    address=wf.StringField(label='адрес')
    date_app=wf.DateField(label='дата обращения')

    def validate_fio(self,field):
        if not field.data.isalpha() or field.data.isascii():
            raise wf.validators.ValidationError('введите символы на кириллице и без спецсимволов')

    def validate_birth_date(self,field):
        current_year=datetime.datetime.now().year
        age=int(current_year)-int(field.data.year)
        if age<18:
            raise wf.validators.ValidationError('age error')

    def validate_inn(self,field):
        if not field.data.isdigit():
            raise wf.validators.ValidationError('строка должна состоять только из цифр')

    def validate(self, extra_validators=None):
        if not super().validate():
            return False
        year=int(self.inn.data[5:9])
        if year != int(self.birth_date.data.year):
            self.inn.errors.append("год рождения и инн должны совпадать")
            return False
        return True

    def validate_phone_num(self,field):
        if not field.data.startswith("+"):
            raise wf.validators.ValidationError('номер должен начинаться  с +')

    def validate_address(self,field):
        if field.data.isdigit() or field.data.isalpha():
            raise wf.validators.ValidationError('адрес должен состоять из цифр и букв')

    def validate_date_app(self,field):
        date=datetime.date.today()
        if not field.data==date:
            raise wf.validators.ValidationError('введите текущую дату')


class DoctorForm(FlaskForm):
    fio=wf.StringField(label="фио")
    position=wf.StringField(label='специализация')
    birth_date=wf.DateField(label='дата роождения')
    experience=wf.IntegerField(label='стаж')

    def validate_fio(self,field):
        if not field.data.isalpha() or field.data.isascii():
            raise wf.validators.ValidationError('введите символы на кириллице и без спецсимволов')

    def validate_birth_date(self,field):
        current_year=datetime.datetime.now().year
        age=int(current_year)-int(field.data.year)
        if age<25:
            raise wf.validators.ValidationError('age error')

    def validate(self, extra_validators=None):
        year=datetime.datetime.now().year
        age=int(year)-int(self.birth_date.data.year)
        if not super().validate():
            return False
        if age<self.experience.data:
            self.experience.errors.append("стаж не может быть болбьше чем возраст")
            return False
        return True

    def validate_position(self,field):
        if not '-' in field.data and not any(ch.isalpha() for ch in field.data ):
            raise wf.validators.ValidationError('строка должна состоять из букв и -')

class MedicalHistoryForm(FlaskForm):
    client_id=wf.SelectField(label='клиент',coerce=int)
    doctor_id=wf.SelectField(label='доктор',coerce=int)
    diagnosis=wf.StringField(label='диагноз')







