def print_employee_hierarchy(input_str):
    # Parse input and create employee dictionary
    employees = {}
    for employee in input_str.split(', '):
        id_, name, manager_id = employee.split(':')
        employees[id_] = {
            'name': name,
            'manager_id': manager_id,
            'subordinates': []
        }
    print(employees)
    # Build hierarchy by linking subordinates to managers
    root = None
    for id_, emp in employees.items():
        if emp['manager_id'] == '0':
            root = id_
        else:
            employees[emp['manager_id']]['subordinates'].append(id_)
    print(employees)

    # Helper function to print tree recursively
    def print_tree(employee_id, level=0):
        result = []
        # Add current employee with proper indentation
        prefix = '- ' * level if level > 0 else ''
        result.append(prefix + employees[employee_id]['name'])

        # Sort subordinates by name for consistent output
        sorted_subordinates = sorted(
            employees[employee_id]['subordinates'],
            key=lambda x: employees[x]['name']
        )

        # Recursively print all subordinates
        for subordinate_id in sorted_subordinates:
            result.extend(print_tree(subordinate_id, level + 1))

        return result

    # Print the hierarchy starting from root
    return '\n'.join(print_tree(root))

if __name__ == '__main__':

    # Test the function
    input_str = "1:Max:4, 4:Ann:0, 2:Jim:4, 3:Tom:1"
    print(print_employee_hierarchy(input_str))
