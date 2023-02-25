from . import app
from .views import doctor_create,client_create,index,history,doctor_list,client_list,history_list

app.add_url_rule('/',view_func=index)
app.add_url_rule('/client',view_func=client_list)
app.add_url_rule('/doctor',view_func=doctor_list)
app.add_url_rule('/history',view_func=history_list)
app.add_url_rule('/doctor/create',view_func=doctor_create,methods=['GET','POST'])
app.add_url_rule('/client/create',view_func=client_create,methods=['GET','POST'])
app.add_url_rule('/history/create',view_func=history,methods=['GET','POST'])