from models import Dog

def create_table(base, engine):
    """Create the dogs table using the SQLAlchemy Base"""
    base.metadata.create_all(engine)

def save(session, dog):
    """Save a dog instance to the database"""
    session.add(dog)
    session.commit()

def get_all(session):
    """Return all dog records"""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Find a dog by name"""
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    """Find a dog by id"""
    return session.query(Dog).get(id)

def find_by_name_and_breed(session, name, breed):
    """Find a dog by name and breed"""
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    """Update a dog's breed and commit"""
    dog.breed = breed
    session.commit()
