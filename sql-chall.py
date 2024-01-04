from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///postgres")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Games(base):
    __tablename__ = "Games"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Progammer table
chess = Games(
    name="Chess",
    gender="A",
)

netball = Games(
    name="Netball",
    gender="F",
)

soccer = Games(
    name="Soccer",
    gender="A",
)

hockey = Games(
    name="Hockey",
    gender="A",
)

# add each instance of our programmers to our session
#session.add(chess)
#session.add(netball)
#session.add(soccer)
#session.add(hockey)

#people = session.query(Games)
#for person in people:
#    if person.gender == "F":
#        person.gender = "Female"
#    elif person.gender == "M":
#        person.gender = "Male"
#    elif person.gender == "A":
#        person.gender = "All genders"
#    else:
#        print("Gender not defined")
#    session.commit()

removes = session.query(Games)
for remove in removes:
    if remove.gender == "Female":
        session.delete(remove)
        session.commit()

#session.delete(Games).filter_by(id = 8).first()
#session.commit()

# delete multiple/all records
#removes = session.query(Games)
#for remove in removes:
     #session.delete(remove)
     #session.commit()

# query the database to find all Programmers
games= session.query(Games)
for game in games:
    print(
        game.id,
        game.name,
        game.gender,
        sep=" | "
    )