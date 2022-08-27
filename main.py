from application.db.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    calculate_salary(2)
    get_employees('roman')