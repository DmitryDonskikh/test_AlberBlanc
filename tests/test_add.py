import pytest
import constant_functions as f


# ADD TESTS: тесты проверяют работу метода add
# Кейс проверяет корректность полей ответа при успешном добавлении юзера в базу
@pytest.mark.parametrize("response_field, value, error_message", [('id', f.data_1_id, 'Wrong id value in response'),
                                                                  ('method', 'add', 'Wrong method value in response'),
                                                                  ('status', 'success', 'Wrong status value in response')])
def test_add_positive(cleaner, response_field, value, error_message):
        result = f.add(f.data_1_id, f.data_1_phone, f.data_1_name, f.data_1_surname, f.data_1_age)
        assert result[response_field] == value, error_message


# Кейс проверяет наличие пользователя в базе при успешном добавлении
def test_add_positive_users(cleaner):
        f.add(f.data_1_id, f.data_1_phone, f.data_1_name, f.data_1_surname, f.data_1_age)
        select_result = f.select_by_phone(f.data_1_id, f.data_1_phone)
        assert len(select_result['users']) == 1, 'There is not note in data base'


# Кейс проверяет корректность данных пользователя, который был добавлен в базу
@pytest.mark.parametrize("response_user_field, value, error_message",
                         [('phone', f.data_1_phone, 'Wrong phone value in data base'),
                          ('name', f.data_1_name, 'Wrong name value in data base'),
                          ('surname', f.data_1_surname, 'Wrong surname value in data base'),
                          ('age', f.data_1_age, 'Wrong age value in data base')])
def test_add_positive_users_fields(cleaner, response_user_field, value, error_message):
        f.add(f.data_1_id, f.data_1_phone, f.data_1_name, f.data_1_surname, f.data_1_age)
        select_result = f.select_by_phone(f.data_1_id, f.data_1_phone)
        assert select_result['users'][0][response_user_field] == value, error_message


# Кейс проверяет добавление пользователя без поля "phone"
@pytest.mark.parametrize("field, value, message", [('id', f.data_1_id, 'Wrong id value in response'),
                                                   ('method', 'add', 'Wrong method value in response'),
                                                   ('status', 'failure', 'Wrong status value in response')])
def test_add_negative_without_phone_field(cleaner, field, value, message):
        result = f.add_kwargs(id=f.data_1_id, name=f.data_1_name, surname=f.data_1_surname, age=f.data_1_age)
        #print(result)
        assert result[field] == value, message


# Кейс проверяет добавление пользователя без поля "name"
@pytest.mark.parametrize("field, value, message", [('id', f.data_1_id, 'Wrong id value in response'),
                                                   ('method', 'add', 'Wrong method value in response'),
                                                   ('status', 'failure', 'Wrong status value in response')])
def test_add_negative_without_name_field(cleaner, field, value, message):
        result = f.add_kwargs(id=f.data_1_id, phone=f.data_1_phone, surname=f.data_1_surname, age=f.data_1_age)
        #print(result)
        assert result[field] == value, message


# Кейс проверяет добавление пользователя без поля "surname"
@pytest.mark.parametrize("field, value, message", [('id', f.data_1_id, 'Wrong id value in response'),
                                                   ('method', 'add', 'Wrong method value in response'),
                                                   ('status', 'failure', 'Wrong status value in response')])
def test_add_negative_without_surname_field(cleaner, field, value, message):
        result = f.add_kwargs(id=f.data_1_id, name=f.data_1_name, phone=f.data_1_phone, age=f.data_1_age)
        #print(result)
        assert result[field] == value, message


# Кейс проверяет добавление пользователя без поля "age"
@pytest.mark.parametrize("field, value, message", [('id', f.data_1_id, 'Wrong id value in response'),
                                                   ('method', 'add', 'Wrong method value in response'),
                                                   ('status', 'failure', 'Wrong status value in response')])
def test_add_negative_without_age_field(cleaner, field, value, message):
        result = f.add_kwargs(id=f.data_1_id, name=f.data_1_name, surname=f.data_1_surname, phone=f.data_1_phone)
        #print(result)
        assert result[field] == value, message


# Кейс проверяет добавление пользователя без поля "id"
@pytest.mark.parametrize("field, value, message", [('status', 'failure', 'Wrong status value in response')])
def test_add_negative_without_id_field(cleaner, field, value, message):
        result = f.add_kwargs(age=f.data_1_age, name=f.data_1_name, surname=f.data_1_surname, phone=f.data_1_phone)
        #print(result)
        assert result[field] == value, message


# Кейс проверяет добавление пользователя, который уже добавлен в базу
def test_add_already_existing_user(setup_cleaner):
        result = f.add(f.data_1_id, f.data_1_phone, f.data_1_name, f.data_1_surname, f.data_1_age)
        #print(result)
        assert result['status'] == 'failure', 'Wrong status value in response'


# Кейс проверяет добавление пользователя с невалидными данными поля "phone"
@pytest.mark.parametrize("value", ['', ' ', None])
def test_add_invalid_phone_value(value):
        result = f.add_kwargs(id=f.data_1_id, phone=value, name=f.data_1_name, surname=f.data_1_surname, age=f.data_1_age)
        #print(result)
        select_result = f.select_by_phone(f.data_1_id, value)
        #print(select_result)
        if 'users' in select_result.keys():
                f.delete(f.data_1_id, value)
        assert result['status'] == 'failure', 'Wrong status value in response'
        #assert 'users' not in select_result.keys(), 'Wrong status value in response'


# Кейс проверяет добавление пользователя с невалидными данными поля "age"
@pytest.mark.parametrize("value", ['', ' ', None, 'a', -5, 900])
def test_add_invalid_age_value(value):
        result = f.add_kwargs(id=f.data_1_id, phone=f.data_1_phone, name=f.data_1_name, surname=f.data_1_surname, age=value)
        #print(result)
        select_result = f.select_by_phone(f.data_1_id, f.data_1_phone)
        #print(select_result)
        if 'users' in select_result.keys():
                f.delete(f.data_1_id, value)
        assert result['status'] == 'failure', 'Wrong status value in response'
        #assert 'users' not in select_result.keys(), 'Wrong status value in response'
