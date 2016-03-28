from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationships, relationship, query, joinedload
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):

    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    user_id = Column(String(20), ForeignKey('user.id'))

class User(Base):

    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    books = relationship('Book', lazy='joined')



engine = create_engine('mysql+mysqlconnector://root:@ian:3306/test')

DBSession = sessionmaker(bind=engine)

session = DBSession()

values = session.query(User).options(joinedload('books')).all()


for item in values:
    print(item.id, item.name, [n.name for n in item.books])

session.close()


#
# new_user = User(id='4', name='Mark')
#
# session.add(new_user)
# session.commit()
# session.close()

