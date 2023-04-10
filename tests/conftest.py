
import pytest
import constant_functions as f


@pytest.fixture()
def setup_cleaner():
        f.add(f.data_1_id, f.data_1_phone, f.data_1_name, f.data_1_surname, f.data_1_age)
        yield
        f.delete(f.data_1_id, f.data_1_phone)

@pytest.fixture()
def cleaner():
        yield
        f.delete(f.data_1_id, f.data_1_phone)

@pytest.fixture()
def setup():
        f.add(f.data_1_id, f.data_1_phone, f.data_1_name, f.data_1_surname, f.data_1_age)
