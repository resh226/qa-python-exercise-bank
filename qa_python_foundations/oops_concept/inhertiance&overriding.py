class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_role(self):
        return f"{self.name}'s role is {self.role}"


class Manager(Employee):
    def __init__(self, name, role, department):
        super().__init__(name, role)
        self.department = department

    def get_role(self):
        # Call the base class's method using super()
        base_role = super().get_role()
        # Extend it with Manager-specific message
        override_role = f"{self.name} manages the {self.department} department."
        # Return both messages together
        return f"{base_role}\n{override_role}"

# ----- Main -----
if __name__ == "__main__":
    emp = Employee("John", "Technician")
    mgr = Manager("Manu", "Manager", "Sales")

    print(emp.get_role())
    print("\n---\n")
    print(mgr.get_role())
