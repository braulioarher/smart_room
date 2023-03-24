from db import db

class Temperature(db.Model):
    __tablebame__ = "Temperatures"

    Date = db.Column(db.Date, primary_key=True)
    DeviceID = db.Column(db.Integer)
    Temperature = db.Column(db.Float(10,2))
