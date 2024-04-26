from db.database import db
from sqlalchemy import func


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
