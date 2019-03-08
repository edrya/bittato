from flask import render_template, flash, redirect, url_for, request
from app import app, db
from sqlalchemy import desc
from app.models import Transaction, Potato
from datetime import datetime
import csv


def init_potato():
    import csv

    with open('data/PotatoesInfo.csv', 'r') as f:
        potatos = csv.reader(f, delimiter=',')
        count = 0
        print(next(potatos))
        for row in potatos:
                t = Potato(variety_name=row[1], country=row[2], product_id=row[0])
                db.session.add(t)
                db.session.commit()
                print(row)


@app.route('/', methods=['GET', 'POST'])
def index():
    transactions = Transaction.query.order_by(desc(Transaction.created_date)).all()
    p = Potato.query.all()
    return render_template('index.html', transactions=transactions, potatoes=p)


@app.route('/transaction', methods=['POST'])
def storage():
    if request.method == 'POST':
        fee = request.form['fee']
        variety= request.form['variety']

        market_price = request.form['market_price']
        location = request.form['location']
        tdate = request.form['tdate']
        quantity = request.form['quantity']
        medium = request.form['medium']

        # get Potato object
        p = Potato.query.filter_by(product_id=int(variety)).first()

        if tdate:
            tdate = datetime.strptime(tdate, '%Y-%m-%d')

            t = Transaction(fee=fee, variety=p.variety_name, quantity=quantity,
                            medium=medium, market_price=market_price, transaction_date=tdate, location=location, transaction=p)
        else:
            t = Transaction(fee=fee, variety=p.variety_name, quantity=quantity, medium=medium, market_price=market_price,
                            location=location, transaction=p)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('.index'))
