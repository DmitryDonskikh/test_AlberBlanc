import pytest
import constant_functions as f


# DELETE TESTS; кейсы проверяют работу функции удаления пользователя из базы данных
# Кейс проверяет корректность полей ответа при успешном удалении
@pytest.mark.parametrize("field, value, message", [('id', f.data_1_id, 'wrong id') ,
                                                   ('method', 'delete', 'wrong method'),
                                                   ('status', 'success', 'wrong status')])
def test_delete_positive(setup, field, value, message):
        result = f.delete(f.data_1_id, f.data_1_phone)
        assert result[field] == value, message


# Кейс провеярет отсутствие пользователя в базе данных при успешном удалении
def test_delete_positive_user(setup):
        f.delete(f.data_1_id, f.data_1_phone)
        select_result = f.select_by_phone(f.data_1_id, f.data_1_phone)
        assert 'users' not in select_result.keys(), 'note is existing yet'


# Кейс провеярет корректность ответа при удалении несуществующего пользователя
@pytest.mark.parametrize("response_field, value, error_message", [('id', f.data_1_id, 'wrong id') ,
                                                                  ('method', 'delete', 'wrong method'),
                                                                  ('status', 'failure', 'wrong status')])
def test_delete_negative_user_is_not_existing(setup, response_field, value, error_message):
        result = f.delete(f.data_1_id, f.data_2_phone)
        #print(result)
        assert result[response_field] == value, error_message
