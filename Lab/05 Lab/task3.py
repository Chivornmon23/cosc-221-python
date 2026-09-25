class Node:
    def __init__(self, employee):
        self.employee = employee
        self.next = None

class EmployeeList:
    def __init__(self):
        self.head = None

    def add_employee(self, emp_no, name, salary, dept_no):
        # Check for duplicate employee numbers
        current = self.head
        while current is not None:
            if current.employee['emp_no'] == emp_no:
                return False
            current = current.next
        
        # Create dictionary and new node
        employee_dict = {
            'emp_no': emp_no,
            'name': name,
            'salary': salary,
            'dept_no': dept_no
        }
        new_node = Node(employee_dict)
        
        # Append to the list
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        return True

    def search_employee(self, emp_no):
        current = self.head
        while current is not None:
            if current.employee['emp_no'] == emp_no:
                return current.employee
            current = current.next
        return None

    def remove_employee(self, emp_no):
        current = self.head
        prev = None
        
        while current is not None:
            if current.employee['emp_no'] == emp_no:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def all_employees(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.employee)
            current = current.next
        return result