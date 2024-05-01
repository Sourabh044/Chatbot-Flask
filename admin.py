from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from db import database
from db.models import *
from flask_admin.base import AdminIndexView, expose
from flask_login import login_required, current_user


class RelatedQuestionAdminView(ModelView):
    column_display_pk = True  # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    column_list = ('id', 'question_id', 'related_question_id')
    edit_modal = True


class CustomAdminHomeView(AdminIndexView):

    @expose('/')
    @login_required
    def index(self):
        return self.render('admin/index.html')


admin = Admin(name="ChatBot", template_mode="bootstrap3")


admin.add_view(ModelView(User, database.session))
admin.add_view(ModelView(ChatRecords, database.session))
admin.add_view(ModelView(Question, database.session))
admin.add_view(ModelView(Answer, database.session))
admin.add_view(RelatedQuestionAdminView(RelatedQuestion, database.session))
