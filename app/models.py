from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key= True, autoincrement = True)
    name = Column(String(50), nullable= False, unique= True)
    product = relationship('Product', backref= 'category', lazy= True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default= 0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable= False)


if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name = 'Mobile')
        # c2 = Category(name='Tablet')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        p1 = Product(name= 'Iphone13', price= 20000000, category_id =1,
                     image= 'https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg')
        p2 = Product(name='Iphone14', price=30000000, category_id=1,
                     image='https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg')
        p3 = Product(name='Iphone15', price=35000000, category_id=1,
                     image='https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg')
        p4 = Product(name='Ipad', price=45000000, category_id=2,
                     image='https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg')
        p5 = Product(name='Tab S9', price=34000000, category_id=2,
                     image='https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg')
        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()

        # db.create_all()