from models import *
import json

# users


@app.route("/users", methods=["GET", "POST"])
def users_all_page():
    if request.method == "GET":
        user_list = User.query.all()

        user_response = []

        for user in user_list:
            user_response.append(user_list.create_dict())

        return json.dumps(user_response)

    if request.method == "POST":
        user_data = json.loads(request.data)
        new_user = User(
            id=user_data.get("id"),
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            age=user_data.get("age"),
            email=user_data.get("email"),
            role=user_data.get("role"),
            phone=user_data.get("phone"),
        )
        db.session.add(new_user)
        db.session.commit()
        return "User added"


@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def users_page_id(id: int):
    if request.method == "GET":
        return json.dumps(User.query.get(id).create_dict())

    if User.query.get(id) is None:
        return "Пользователь не найден!"

    if request.method == "PUT":
        user_data = json.loads(request.data)
        update_user = (User.query.get(id),)
        update_user.first_name = user_data.get("first_name")
        update_user.last_name = user_data.get("last_name")
        update_user.age = user_data.get("age")
        update_user.email = user_data.get("email")
        update_user.role = user_data.get("role")
        update_user.phone = user_data.get("phone")

        db.session.add(update_user)
        db.session.commit()

        return "Data user update"

    if request.method == 'DELETE':
        user = User.


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
