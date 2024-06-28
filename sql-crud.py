from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

#create a class-based model for the "Progremmer" table
class Programmer(base):
    __tablename__= "Programmer"
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

#instead of cinnecting to tha database directly, we will ask for a session
#create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
#opens an acrual session by calling the Session() subclass defined above
session = Session()

#creating the database using declarative_base subclass
base.metadata.create_all(db)

#creating records on our table

ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL language"
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American",
    famous_for = "Apolo 11"
)


desislava_naydenova = Programmer(
    first_name = "Desislava",
    last_name = "Naydenova",
    gender = "F",
    nationality = "Bulgarian",
    famous_for = "Best person ever"
)
#add each instance of our programmers to our session
# session.add(ada_lovelace)
session.add(alan_turing)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(desislava_naydenova)

#commit our session to tha database
session.commit()

#query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name+" "+programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep = "  |  "
    )
