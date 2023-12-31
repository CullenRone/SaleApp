import math

from flask import render_template, request, redirect, session, jsonify
from app import dao, app
import utils
from app import login
from flask_login import login_user


@app.route('/')
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    products = dao.load_products(kw, cate_id, page)

    num = dao.count_product()

    return render_template('index.html', products=products,
                           pages=math.ceil(num / app.config['PAGE_SIZE']))


@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')


@app.route('/api/cart', methods=['post'])
def add_to_cart():
    """  # khi nhấn vào đặt hàng sản phẩm 1 thì sẽ tạo ra món hàng đó, mặc định số lượng là 1
    {
        "cart" : {
            "1": {
                "id": "1",
                "name": "abc",
                "price": 12,
                "quantity": 2
            }, "2": {
                "id": "2",
                "name": "abc",
                "price": 12,
                "quantity": 1
            }
        }
    }
    :return:
    """
    data = request.json

    cart = session.get('cart')
    if cart is None:
        cart = {}

    id = str(data.get("id"))
    if id in cart:  # sản phẩm đã có trong giỏ
        cart[id]['quantity'] += 1

    else:  # sản phẩm chưa có trong giỏ
        cart[id] = {
            "id": id,
            "name": data.get('name'),
            "price": data.get('price'),
            "quantity": 1
        }

    session['cart'] = cart  # lưu tạm trong biến session

    return jsonify(utils.count_cart(cart))


@app.route('/cart')
def cart():
    return render_template('cart.html')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


@app.context_processor # trang nào cũng sẽ có mobile, tablet,..
def common_response():
    return {
        'categories': dao.load_categories(),
        'cart': utils.count_cart(session.get('cart'))
    }


if __name__ == '__main__':
    from app import admin

    app.run(debug=True)
