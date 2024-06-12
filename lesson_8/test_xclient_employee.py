from EmployeeApi import EmployeeApi
from CompanyApi import CompanyApi


base_url = 'https://x-clients-be.onrender.com'
company_api = CompanyApi(base_url)
employee_api = EmployeeApi(base_url)

# New company
name = 'New Company'
description = 'My new company'

# New employee
id = 1
first_name = "Ilya"
last_name = "Ilin"
middle_name = "Ilich"
email = "new@gmail.com"
employee_url = "url1.com"
phone = "+79998887766"
birthdate = "2000-06-07T08:06:30.137Z"
is_active = True


def test_get_employee_list():
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

    # get employee list
    employee_list = employee_api.get_employee_list(company_id)
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
