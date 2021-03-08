from numbers import Real

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Product(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    preco = Column(Integer)

    def __repr__(self):
        return f'Product(nome={self.nome}, preco={self.preco})'

Base.metadata.create_all(engine)

p1 = Product(nome='Computador', preco='2000')
p2 = Product(nome='Smart TV', preco='1500')
p3 = Product(nome='Teclado', preco='200')
p4 = Product(nome='Mouse', preco='150')
p5 = Product(nome='Smartphone', preco='1700')

session.add(p1)
session.add_all([p2, p3, p4])

session.commit()


session.add(p5)

session.flush()
