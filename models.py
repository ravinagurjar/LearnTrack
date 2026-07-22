from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy object
db = SQLAlchemy()


class Skill(db.Model):
    __tablename__ = "skills"

    id = db.Column(db.Integer, primary_key=True)

    skill = db.Column(db.String(100), nullable=False)

    category = db.Column(db.String(50), nullable=False)

    level = db.Column(db.String(20), nullable=False)

    progress = db.Column(db.Integer, nullable=False)

    study_time = db.Column(db.Integer, nullable=False)

    learning = db.Column(db.Text, nullable=False)

    confusion = db.Column(db.Text)

    def __repr__(self):
        return f"<Skill {self.skill}>"