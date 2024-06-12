from sqlalchemy import create_engine
from sqlalchemy.sql import text


class EmployeeTable:
    scripts = {
        "delete_employee": text("DELETE FROM employee "
                                "WHERE id = :new_employee_id"),
        "get_max_id": text("SELECT MAX(id) FROM employee"),
        "insert new": text("INSERT INTO employee(first_name, last_name, "
                           "phone, company_id, is_active) "
                           "VALUES (:first_name, :last_name, :phone, "
                           ":company_id, :is_active)")

    }

    def __init__(self, db_connection_string):
        self.db = create_engine(db_connection_string)

    def create(self, first_name, last_name, phone, company_id, is_active):
        new_employee = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "company_id": company_id,
            "is_active": is_active
        }
        self.db.execute(self.scripts["insert new"], new_employee)

    def get_max_id(self):
        return self.db.execute(self.scripts["get_max_id"]).fetchall()[0][0]

    def delete(self, id):
        self.db.execute(self.scripts["delete_employee"], new_employee_id=id)
