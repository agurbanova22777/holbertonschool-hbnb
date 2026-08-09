from part3.app import db
from part3.app.models.base import BaseModel

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False)

    # Many-to-Many relationship back to Place
    # We use back_populates to keep both sides of the relationship in sync
    places = db.relationship('Place', secondary='place_amenity', back_populates='amenities')

    def __init__(self, name=None):
        super().__init__()
        if name:
            self.name = name