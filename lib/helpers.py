from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    return [print(employee) for employee in employees]


def find_employee_by_name():
    name = input('Enter employee name: ')
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f"Employee {name} does not exist")


def find_employee_by_id():
    id = input('Employee id :')
    employee = Employee.find_by_id(id=id_)
    print(employee) if employee else print(f"Employee {id_} not found")


def create_employee():
    name = input("Enter the employee's name: ")
    title = input("Enter the employee's job title: ")
    department_id = input("Enter the employee's department id: ")

    try:
        employee = Employee.create(name=name,
                                   job_title=title,
                                   department_id=int(department_id))
    except ValueError as e:
        print(f"Error creating employee: {e}")
    else:
        print(f"Success: {employee}")


def update_employee():
    pass


def delete_employee():
    pass


def list_department_employees():
    pass
