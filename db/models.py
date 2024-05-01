from db.database import db
from sqlalchemy import func
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"
    # __bind_key__ = 'zerodha'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False, unique=True)
    isAdmin = db.Column(db.Boolean(), default=False)

    # Timestamps
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    last_login = db.Column(db.DateTime(timezone=True),
                           default=None, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    related_questions = relationship(
        "RelatedQuestion", back_populates="question", foreign_keys="[RelatedQuestion.question_id]")
    answers = relationship("Answer", back_populates="question")

    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f"{self.text}"

class RelatedQuestion(db.Model):
    __tablename__ = 'related_questions'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    related_question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    question = relationship(
        "Question", back_populates="related_questions", foreign_keys=[question_id])
    related_question = relationship(
        "Question", foreign_keys=[related_question_id])

    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    is_deleted = db.Column(db.Boolean, default=False)
class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    question = relationship("Question", back_populates="answers")

    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f"{self.text}"
class ChatRecords(db.Model):
    __tablename__ = 'chat_records'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    question = db.Column(db.String(300), nullable=False)
    answer = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    extra_data = db.Column(db.JSON, nullable=True)
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return f"{self.user_id} , {self.question}, {self.answer}"
