from models import *
import json

# users


@app.route("/users")
def users_page():
    user_list = User.query.all()

    user_response = []

    for user in user_list:
        user_response.append(
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age,
                "email": user.email,
                "role": user.role,
                "phone": user.phone,
            }
        )

    return json.dumps(user_response)


@app.route("/users/<int:id>")
def users_page_id(id: int):
    user = User.query.get(id)

    if user is None:
        return "Пользователь не найден!"

    return json.dumps(
        {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
            "email": user.email,
            "role": user.role,
            "phone": user.phone,
        }
    )


# offers


@app.route("/offers")
def offers_page():
    offers_list = Offer.query.all()

    offers_response = []

    for offer in offers_list:
        offers_response.append(
            {
                "id": offer.id,
                "order_id": offer.order_id,
                "executor_id": offer.executor_id,
            }
        )
    return json.dumps(offers_response)


@app.route("/offers/<int:id>")
def offers_id_page(id):
    offer = Offer.query.get(id)

    if offer is None:
        return "Предложение не найдено!"

    return json.dumps(
        {
            "id": offer.id,
            "order_id": offer.order_id,
            "executor_id": offer.executor_id,
        }
    )


# orders


@app.route("/orders")
def page_orders():
    orders_list = Order.query.all()

    order_response = []

    for order in orders_list:
        order_response.append(
            {
                "id": order.id,
                "name": order.name,
                "description": order.description,
                "start_date": order.start_date,
                "end_date": order.end_date,
                "adress": order.adress,
                "price": order.price,
                "customer_id": order.customer_id,
                "executor_id": order.customer_id,
            }
        )

    return json.dumps(order_response)


@app.route("/orders/<int:id>")
def order_id_page(id):
    order = Order.query.get(id)

    if order is None:
        return "Заказ не найден!"

    return json.dumps(
        {
            "id": order.id,
            "name": order.name,
            "description": order.description,
            "start_date": order.start_date,
            "end_date": order.end_date,
            "adress": order.adress,
            "price": order.price,
            "customer_id": order.customer_id,
            "executor_id": order.customer_id,
        }
    )
