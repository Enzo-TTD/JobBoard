from App.database import db


class JobListing(db.model):
    __tablename__ = 'job_listings'
    id= db.Column(db.Interger, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.text, nullable=False)
    employerId = db.column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    employer = db.relationship('Employer', backref='job_listings')

    def __init__(self, title, description, employerId):
        self.title = title
        self.description = description
        self.employerId = employerId

    def to_json(self):
        return{
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'employer_id' : self.employerId
        }