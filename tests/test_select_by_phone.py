import pytest
import constant_functions as f


# SELECT BY PHONE TESTS: кейсы проверяют выдачу полдьзователей по параметру phone
# кейс проверяет поле method ответа при выдаче существующего пользователя
def test_select_by_phone_positive_method(setup_cleaner):
        result = f.select_by_phone(f.data_1_id, f.data_1_phone)
        assert result['method'] == 'select', 'Wrong method'


# кейс проверяет поле id ответа при выдаче существующего пользователя
def test_select_by_phone_positive_id(setup_cleaner):
        result = f.select_by_phone(f.data_1_id, f.data_1_phone)
        assert result['id'] == f.data_1_id, 'Wrong Id'


# кейс проверяет поле status ответа при выдаче существующего пользователя
def test_select_by_phone_positive_status(setup_cleaner):
        result = f.select_by_phone(f.data_1_id, f.data_1_phone)
        assert result['status'] == 'success', 'Wrong status'


# кейс проверяет поле users ответа при выдаче существующего пользователя
def test_select_by_phone_positive_users(setup_cleaner):
        result = f.select_by_phone(f.data_1_id, f.data_1_phone)
        #print(result)
        assert len(result['users']) == 1, 'Wrong amount of users in select'


# кейс проверяет поле phone ответа при выдаче существующего пользователя
def test_select_by_phone_positive_users_phone(setup_cleaner):
        result = f.select_by_phone(f.data_1_id, f.data_1_phone)
        #print(result)
        assert result['users'][0]['phone'] == f.data_1_phone, 'Wrong phone'


# кейс проверяет поле name ответа при выдаче существующего пользователя
def test_select_by_phone_positive_users_name(setup_cleaner):
        result = f.select_by_phone(f.data_1_id, f.data_1_phone)
        assert result['users'][0]['name'] == f.data_1_name, 'Wrong name'


# кейс проверяет поле surname ответа при выдаче существующего пользователя
def test_select_by_phone_positive_users_surname(setup_cleaner):
        result = f.select_by_phone(f.data_1_id, f.data_1_phone)
        assert result['users'][0]['surname'] == f.data_1_surname, 'Wrong surname'


# кейс проверяет поле age ответа при выдаче существующего пользователя
def test_select_by_phone_positive_users_age(setup_cleaner):
        result = f.select_by_phone(f.data_1_id, f.data_1_phone)
        assert result['users'][0]['age'] == f.data_1_age, 'Wrong age'


# кейс проверяет корректность полей ответа при попытке запросить информацию о несуществующем пользователе
@pytest.mark.parametrize("response_field, value, error_message", [('id', f.data_2_id, 'Wrong id') ,
                                                                  ('method', 'select', 'Wrong method'),
                                                                  ('status', 'failure', 'Wrong status')])
def test_select_by_phone_user_is_not_existing_fields(setup_cleaner, response_field, value, error_message):
        result = f.select_by_phone(f.data_2_id, f.data_2_phone)
        #print(result)
        assert result[response_field] == value, error_message


# кейс проверяет пустую выдачу поля users, при попытке выдать информацтю о несуществующем пользователе
def test_select_by_phone_user_is_not_existing_users(setup_cleaner):
        result = f.select_by_phone(f.data_2_id, f.data_2_phone)
        #print(result)
        assert 'users' in result.keys(), 'There are not users field in response'
