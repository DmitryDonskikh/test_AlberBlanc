import pytest
import constant_functions as f


# UPDATE TESTS: кейсы проверяют работу функции обновления данных пользователей
# кейс проверяет корректность значения поля id ответа, при успешном обновлении
def test_update_positive_id(setup_cleaner):
        result = f.update(f.data_2_id, f.data_1_phone, f.data_2_name, f.data_2_surname, f.data_2_age)
        #print(result)
        assert result['id'] == f.data_2_id, 'Wrong id value in response'


# кейс проверяет корректность значения поля method ответа, при успешном обновлении
def test_update_positive_method(setup_cleaner):
        result = f.update(f.data_2_id, f.data_1_phone, f.data_2_name, f.data_2_surname, f.data_2_age)
        #print(result)
        assert result['method'] == 'update', 'Wrong method value in response'


# кейс проверяет корректность значения поля status ответа, при успешном обновлении
def test_update_positive_status(setup_cleaner):
        result = f.update(f.data_2_id, f.data_1_phone, f.data_2_name, f.data_2_surname, f.data_2_age)
        #print(result)
        assert result['status'] == 'success', 'Wrong status value in responses'


# кейс проверяет корректность обновленного значения поля name в базе данных, при успешном обновлении
def test_update_positive_user_name(setup_cleaner):
        result = f.update(f.data_2_id, f.data_1_phone, f.data_2_name, f.data_2_surname, f.data_2_age)
        select_result = f.select_by_phone(f.data_2_id, f.data_1_phone)
        assert select_result['users'][0]['name'] == f.data_2_name, 'Wrong name value in response'


# кейс проверяет корректность обновленного значения поля surname в базе данных, при успешном обновлении
def test_update_positive_user_surname(setup_cleaner):
        result = f.update(f.data_2_id, f.data_1_phone, f.data_2_name, f.data_2_surname, f.data_2_age)
        select_result = f.select_by_phone(f.data_2_id, f.data_1_phone)
        assert select_result['users'][0]['surname'] == f.data_2_surname, 'Wrong surname value in response'


# кейс проверяет корректность обновленного значения поля age в базе данных, при успешном обновлении
def test_update_positive_user_age(setup_cleaner):
        result = f.update(f.data_2_id, f.data_1_phone, f.data_2_name, f.data_2_surname, f.data_2_age)
        select_result = f.select_by_phone(f.data_2_id, f.data_1_phone)
        assert select_result['users'][0]['age'] == f.data_2_age, 'Wrong age value in response'


# кейс проверяет обновление данныхз несуществующего пользователя
@pytest.mark.parametrize("response_field, value, error_message", [('id', f.data_2_id, 'Wrong id value in response') ,
                                                                  ('method', 'update', 'Wrong method value in response'),
                                                                  ('status', 'failure', 'Wrong status value in response')])
def test_update_negative_user_is_not_existing(setup_cleaner, response_field, value, error_message):
        result = f.update(f.data_2_id, f.data_2_phone, f.data_2_name, f.data_2_surname, f.data_2_age)
        #print(result)
        assert result[response_field] == value, error_message
