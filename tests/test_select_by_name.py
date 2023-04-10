import pytest
import constant_functions as f


# SELECT BY NAME TESTS: кейсы проверяют выдачу полдьзователей по параметру name
# кейс проверяет поле method ответа при выдаче существующего пользователя
def test_select_by_name_positive_method(setup_cleaner):
        result = f.select_by_name(f.data_1_id, f.data_1_name)
        assert result['method'] == 'select', 'Wrong method'


# кейс проверяет поле id ответа при выдаче существующего пользователя
def test_select_by_name_positive_id(setup_cleaner):
        result = f.select_by_name(f.data_1_id, f.data_1_name)
        assert result['id'] == f.data_1_id, 'Wrong Id'


# кейс проверяет поле status ответа при выдаче существующего пользователя
def test_select_by_name_positive_status(setup_cleaner):
        result = f.select_by_name(f.data_1_id, f.data_1_name)
        assert result['status'] == 'success', 'Wrong status'


# кейс проверяет поле users ответа при выдаче существующего пользователя
def test_select_by_name_positive_users(setup_cleaner):
        result = f.select_by_name(f.data_1_id, f.data_1_name)
        #print(result)
        assert len(result['users']) == 1, 'note is not exist'


# кейс проверяет поле phone ответа при выдаче существующего пользователя
def test_select_by_name_positive_users_phone(setup_cleaner):
        result = f.select_by_name(f.data_1_id, f.data_1_name)
        #print(result)
        assert result['users'][0]['phone'] == f.data_1_phone, 'wrong phone in db'


# кейс проверяет поле name ответа при выдаче существующего пользователя
def test_select_by_name_positive_users_name(setup_cleaner):
        result = f.select_by_name(f.data_1_id, f.data_1_name)
        assert result['users'][0]['name'] == f.data_1_name, 'wrong name in db'


# кейс проверяет поле surname ответа при выдаче существующего пользователя
def test_select_by_name_positive_users_surname(setup_cleaner):
        result = f.select_by_name(f.data_1_id, f.data_1_name)
        assert result['users'][0]['surname'] == f.data_1_surname, 'wrong surname in db'


# кейс проверяет поле age ответа при выдаче существующего пользователя
def test_select_by_name_positive_users_age(setup_cleaner):
        result = f.select_by_name(f.data_1_id, f.data_1_name)
        assert result['users'][0]['age'] == f.data_1_age, 'wrong age in db'


# кейс проверяет корректность полей ответа при запросе несуществующего пользователя
@pytest.mark.parametrize("response_field, value, error_message", [('id', f.data_2_id, 'wrong id') ,
                                                                  ('method', 'select', 'wrong method'),
                                                                  ('status', 'failure', 'wrong status')])
def test_select_by_name_user_is_not_existing_fields(setup_cleaner, response_field, value, error_message):
        result = f.select_by_name(f.data_2_id, f.data_2_name)
        #print(result)
        assert result[response_field] == value, error_message


# кейс проверяет наличие пустного поля users в ответе при запросе несуществующего пользователя
def test_select_by_name_user_is_not_existing_users(setup_cleaner):
        result = f.select_by_name(f.data_2_id, f.data_2_name)
        #print(result)
        assert 'users' in result.keys(), 'note is exist yet'


# кейс проверяет выдачу при наличии двух пользователей с одинаковым именем
def test_select_by_name_several_users(setup_cleaner):
        f.add(f.data_3_id, f.data_3_phone, f.data_3_name, f.data_3_surname, f.data_3_age)
        f.add(f.data_4_id, f.data_4_phone, f.data_4_name, f.data_4_surname, f.data_4_age)
        result = f.select_by_name(f.data_1_id, f.data_1_name)
        #print(result)
        f.delete(f.data_3_id, f.data_3_phone)
        f.delete(f.data_4_id, f.data_4_phone)
        assert 'users' in result.keys(), 'note is existing yet'
        assert len(result['users']) == 2, 'Wrong amount of users'


# кейс проверяет корректность полей выдачи при наличии двух пользователей с одинаковым именем
def test_select_by_name_several_users_fields(setup_cleaner):
        f.add(f.data_3_id, f.data_3_phone, f.data_3_name, f.data_3_surname, f.data_3_age)
        f.add(f.data_4_id, f.data_4_phone, f.data_4_name, f.data_4_surname, f.data_4_age)
        result = f.select_by_name(f.data_1_id, f.data_1_name)
        #print(result)
        f.delete(f.data_3_id, f.data_3_phone)
        f.delete(f.data_4_id, f.data_4_phone)
        assert result['users'][0]['name'] == f.data_1_name, 'wrong name in db'
        assert result['users'][1]['name'] == f.data_3_name, 'wrong name in db'

