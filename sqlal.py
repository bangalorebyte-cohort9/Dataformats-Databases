import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
	__tablename__ = 'person'
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable=False)

class Address(Base):
	__tablename__ = 'Address'
	id = Column(Integer, primary_key = True)
	street_name = Column(String(250))
	street_number = Column(String(250))
	post_code = Column(String(250), nullable=False)
	person_id = Column(Integer, ForeignKey('person.id'))
	person = relationship(Person)

engine = create_engine('sqlite:///sqlalchemy.db')
Base.metadata.create_all(engine)


Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_person1 = Person(name='Byte')
new_person2 = Person(name='Academy')
session.add(new_person1)
session.add(new_person2)
session.commit()

new_address1 = Address(post_code='560022',person=new_person1)
new_address2 = Address(post_code='560021',person=new_person2)

session.add(new_address1)
session.add(new_address2)

session.commit()

#print(session.query(Person).all())
p = session.query(Person).first()
print(p.name)

print(session.query(Address).filter(Address.person == new_person1).all())
add = session.query(Address).filter(Address.person == new_person2).one()
print(add.post_code)

