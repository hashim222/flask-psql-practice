from practice_database import db


class EnterdData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_data = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return self.input_data
