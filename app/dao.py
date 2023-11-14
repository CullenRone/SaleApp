def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    },{
        'id': 2,
        'name': 'Tablet'
    }]
def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'Iphone13',
        'price': 20000000,
        'image': 'https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg'
    }, {
        'id': 2,
        'name': 'Iphone14',
        'price': 25000000,
        'image': 'https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg'
    }, {
        'id': 3,
        'name': 'Iphone15',
        'price': 30000000,
        'image': 'https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg'
    }, {
        'id': 4,
        'name': 'Galaxy S23',
        'price': 27000000,
        'image': 'https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg'
    }, {
        'id': 5,
        'name': 'Galaxy Note 22Ultra',
        'price': 40000000,
        'image': 'https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg'
    }, {
        'id': 6,
        'name': 'Galaxy S22',
        'price': 35000000,
        'image': 'https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg'
    }, {
        'id': 7,
        'name': 'Ipad',
        'price': 39000000,
        'image': 'https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg'
    },{
        'id': 8,
        'name': 'Honor',
        'price': 15000000,
        'image': 'https://i.pinimg.com/originals/0d/39/f8/0d39f85da06513d277f3b0a7912d51bf.jpg'
    }]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products