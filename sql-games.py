from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

class Games(base):
    __tablename__ = "Games"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    play_from = Column(Integer)


Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)

chess = Games(
    name = "Chess",
    play_from = 1973
)

session.add(chess)

session.commit()

games = session.query(Games)
for game in games:
    print(
        game.id,
        game.name,
        game.play_from,
        sep = " | "
    )
