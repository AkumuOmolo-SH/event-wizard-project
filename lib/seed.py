from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.location import Location, Base

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

loc1 = Location.create(session, name="Alchemist", capacity=500, num_bars=2, num_toilets=3)
loc2 = Location.create(session, name="Muse", capacity=150, num_bars=5, num_toilets=4)
loc3 = Location.create(session, name="Geco", capacity=250, num_bars=2, num_toilets=3)

print("Seeded locations:")
for loc in Location.get_all(session):
    print(loc)

session.close()