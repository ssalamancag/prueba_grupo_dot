from flask import Flask, jsonify, request
from flask_migrate import Migrate
from database import db
from models import Quotation

app = Flask(__name__)

USER_DB = 'testuser'
PASS_DB = 'testpass'
URL_DB = 'localhost'
NAME_DB = 'development_database'
CONECTION_URL = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = CONECTION_URL
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db.init_app(app)


migrate = Migrate()
migrate.init_app(app, db)

# Endpoint to get the quote of the given amount
@app.route('/quotation')
def calculate_quotation():
    print(request.args.get('amount'))
    try:
        amount = int(request.args.get('amount'))
        if amount <= 0:
            return jsonify({'Error': 'Valor no valido no valido'})

        option = Quotation.query.filter(Quotation.max_amount >= amount).order_by(Quotation.rate).first()
        print(option)

        if option is None:
            return jsonify({'Error': 'No hay socio disponible'}), 404
        else:
            print(option)
            print(option.id)
            total_value = amount * (1 + 36 * (option.rate / 100))
            monthly_fee = round(total_value / 36, 2)
            response = {
                'partner': option.name,
                'monthly_fee': f'${monthly_fee}',
                'total_pay': f'${total_value}',
                'rate': f'{option.rate}%'
            }
            return jsonify(response), 200
    except:
        return jsonify({'Erorr': 'Error en la solicitud'}), 400


# Endpoint to create a new value in the db
@app.route('/quotation', methods=['POST'])
def func_name():
    data = request.get_json()
    me = Quotation(data['name'], data['rate'], data['max_amount'])
    db.session.add(me)
    db.session.commit()
    return '', 201




