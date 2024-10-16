import pytest
from run import app

parameters = {
    1: {
        "poster_name": "leo",
        "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
        "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
        "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
        "views_count": 376,
        "likes_count": 154,
        "pk": 1,
    },
    2: {
        "poster_name": "johnny",
        "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
        "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
        "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
        "views_count": 233,
        "likes_count": 101,
        "pk": 2,
    },
    3: {
        "poster_name": "hank",
        "poster_avatar": "https://randus.org/avatars/m/383c7e7e3c3c1818.png",
        "pic": "https://images.unsplash.com/photo-1612450632008-22c2a5437dc1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
        "content": "Смотрите-ка – ржавые елки! Раньше на этом месте была свалка старых машин, а потом все засыпали песком. Теперь тут ничего не растет – только ржавые елки , кусты и грязь. Да и не может тут ничего расти: слишком много пыли и песка. Зато теперь стало очень красиво – все-таки это не свалка.",
        "views_count": 187,
        "likes_count": 67,
        "pk": 3,
    },
}


class TestAPI:
    #  Тест всех постов
    def test_app_all_posts_status_code(self):
        """Тест списка"""
        response = app.test_client().get("/api/posts", follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "aplication/json", "Получен не JSON"

    def test_app_all_posts_type_count_content(self):
        """Тест правильности получения данных"""
        response = app.test_client().get("/api/posts", follow_redirects=True)
        assert type(response.json) is list, "Получен не список"
        assert (
            len(response.json) == 8
        ), "Получено не верное колличество элементов в списке"

    def test_api_single_post_check_keys(self):
        """Тест правильности полученных ключей"""

        keys = {
            "poster_name",
            "poster_avatar",
            "pic",
            "content",
            "views_count",
            "likes_count",
            "pk",
        }

        response = app.test_client().get("/api/posts/1", follow_redirects=True)
        first_keys = set(response.json.keys())
        assert keys == first_keys, "Полученные ключи не совпадают"

    @pytest.mark.parametrize(
        "pk, data", [(1, parameters[1]), (2, parameters[2]), (3, parameters[3])]
    )
    def test_api_single_post_check_values(self, pk, data):
        """Тест правильности значения ключей"""

        response = app.test_client().get("/api/posts/{pk}", follow_redirects=True)
        response_data = response.json

        assert response_data["poster_name"] == data["poster_name"]
        assert response_data["poster_avatar"] == data["poster_avatar"]
        assert response_data["pic"] == data["pic"]
        assert response_data["content"] == data["content"]
        assert response_data["views_count"] == data["views_count"]
        assert response_data["likes_count"] == data["likes_count"]
        assert response_data["pk"] == data["pk"]

        print("parametrized correct")
