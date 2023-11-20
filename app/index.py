import math

from flask import render_template, request, redirect
from app import dao, app
from app import login
from flask_login import login_user

@app.route('/')
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    cates = dao.load_categories()
    products = dao.load_products(kw, cate_id, page)

    num = dao.count_product()

    return render_template('index.html', categories = cates, products = products,
                           pages= math.ceil(num/app.config['PAGE_SIZE']) )


@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username= username, password= password)
    if user:
        login_user(user= user)

    return redirect('/admin')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)
if __name__ == '__main__':
    from app import admin
    app.run(debug=True)