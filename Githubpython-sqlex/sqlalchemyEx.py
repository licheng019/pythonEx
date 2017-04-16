from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,backref

def createBaseAndSession():
    # Create engine
    # foramt mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
    engine = create_engine('mysql+mysqlconnector://root:password@127.0.0.1:3306/test?charset=utf8', echo=True)
    base = declarative_base()
    base.metadata.create_all(engine)
    # Create session
    Session = sessionmaker(engine)
    session = Session()
    return base,session

Base,session = createBaseAndSession()

# define mapping
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    name = Column(String(40))
    orders = relationship('Order')

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    orders = relationship('Order')

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    otime = Column(DateTime)
    uid = Column(Integer,ForeignKey('users.id'))
    pid = Column(Integer, ForeignKey('products.id'))

#Add new record
'''
 chris = User(name='Chris')
 session.add(chris)
 game = Product(name='Game')
 session.add(game)
 session.commit()
'''
chris = session.query(User).filter(User.name=='chris').one()
product1 = session.query(Product).filter(Product.name=='Game').one()
order1 = Order(uid=chris.id,pid=product1.id)
session.add(order1)
session.commit()
#this is because of the relationship setup of User and Product
orders = chris.orders
for order in orders:
    print order.id


