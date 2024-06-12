from EmployeeApi import EmployeeApi
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable
from EmployeeTable import EmployeeTable


base_url = 'https://x-clients-be.onrender.com'
company_api = CompanyApi(base_url)
employee_api = EmployeeApi(base_url)

db_connection_string = ('postgresql://x_clients_db_3fmx_user:'
                        'mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@'
                        'dpg-cour99g21fec73bsgvug-a.oregon-postgres.'
                        'render.com/x_clients_db_3fmx')
company_table = CompanyTable(db_connection_string)
employee_table = EmployeeTable(db_connection_string)

# New company
name = 'NewCompany3'
description = 'My new company 2'

# New employee
# id = 1
first_name = "Ilya3"
last_name = "Ilin"
middle_name = "Ilich"
email = "new@test.com"
employee_url = "url1.com"
phone = "+79998887766"
birthdate = "2000-06-07T08:06:30.137Z"
is_active = True


def test_get_employee_list():
    # create new company in DB
    company_table.create(name, description)
    new_company_id = company_table.get_max_id()

    # create new employee in DB
    employee_table.create(first_name, last_name, phone, new_company_id,
                          is_active)
    new_employee_id = employee_table.get_max_id()

    # get employee list by API
    employee_list = employee_api.get_employee_list(new_company_id)

    # delete new employee and new company from DB
    employee_table.delete(new_employee_id)
    company_table.delete(new_company_id)

    assert employee_list[0]["id"] == new_employee_id, \
        "Employee's ID is not equal"


def test_create_employee():
    # create new company
    new_company = company_api.create_company(name, description)
    new_company_id = new_company["id"]

    # create new employee
    company_id = new_company_id
    new_employee = employee_api.add_employee(id, first_name, last_name,
                                             middle_name, company_id, email,
                                             employee_url, phone, birthdate,
                                             is_active)
    new_employee_id = new_employee["id"]
    assert type(new_employee_id) is int


def test_is_required_fist_name():
    # create new company
    new_company = company_api.create_company(name, description)
    new_company_id = new_company["id"]

    # create new employee
    company_id = new_company_id
    status_code = employee_api.add_employee_without_first_name(id,
                                                               last_name,
                                                               middle_name,
                                                               company_id,
                                                               email,
                                                               employee_url,
                                                               phone,
                                                               birthdate,
                                                               is_active)
    assert status_code == 400


def test_get_employee():
    # create new company
    new_company = company_api.create_company(name, description)
    new_company_id = new_company["id"]

    # create new employee
    company_id = new_company_id
    new_employee = employee_api.add_employee(id, first_name, last_name,
                                             middle_name, company_id, email,
                                             employee_url, phone, birthdate,
                                             is_active)
    new_employee_id = new_employee["id"]

    # get employee's info
    employee = employee_api.get_employee(new_employee_id)
    assert employee["id"] == new_employee_id
    assert employee["firstName"] == first_name
    assert len(employee) == 12


def test_change_employee():
    # create new company
    new_company = company_api.create_company(name, description)
    new_company_id = new_company["id"]

    # create new employee
    company_id = new_company_id
    new_employee = employee_api.add_employee(id, first_name, last_name,
                                             middle_name, company_id, email,
                                             employee_url, phone, birthdate,
                                             is_active)
    new_employee_id = new_employee["id"]
    new_email = "new_new@gmail.com"
    new_url = "url2.com"
    new_is_active = False
    patched_employee = employee_api.patch_employee(new_employee_id,
                                                   new_email, new_url,
                                                   new_is_active
                                                   )
    assert patched_employee["id"] == new_employee_id
    assert patched_employee["email"] == new_email
    assert patched_employee["url"] == new_url
    assert patched_employee["isActive"] == new_is_active


def test_is_required_token():
    # create new company
    new_company = company_api.create_company(name, description)
    new_company_id = new_company["id"]

    # create new employee
    company_id = new_company_id
    new_employee = employee_api.add_employee(id, first_name, last_name,
                                             middle_name, company_id, email,
                                             employee_url, phone, birthdate,
                                             is_active)
    new_employee_id = new_employee["id"]
    new_email = "new_new@gmail.com"
    new_url = "url2.com"
    new_is_active = False
    status_code = employee_api.patch_employee_without_token(new_employee_id,
                                                            new_email, new_url,
                                                            new_is_active)
    assert status_code == 401
