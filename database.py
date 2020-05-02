"""

Author: TUMMALA VISWANTH SAI

Purpose: Module acts as SUBJECT code in SUBJECT-OBSERVER Design pattern for a simple CRM application. Typical uses cases
         in SUBJECT-OBSERVER pattern like a) registering new user, delete users and and provide info about all users are
         to be developed

Usage:
    Script is trigger by Control code (crmapp_view). Serves as Model in MVC pattern
    from database import EmployeeDatabase
"""
class EmployeeDataBase:
    """
    Represent the interface to data( model - MVC). Can read data from json file
    """

    def __init__(self, pathtodb):
        """Method to initialize the variable

        	Args:
        		pathtodb: Path to the JSON database is provided as input

        """

        import json
        with open(pathtodb, mode='rt') as file:
            self.data = json.load(file)

        #import yaml
        #with open(pathtodb, mode='rt') as file:
        #    self.data = yaml.safe_load(file)

    def activebacklog(self, employeeid):
        """Method to find the active backlog of an employee

        	Args:
        		employeeid: Employee ID is provided as input

        	Returns:
        		Based on the employee ID provided, function returns a tuple of name and active cases of the employee
        """

        name = self.data[employeeid][0]
        activecases = self.data[employeeid][1]["Backlog"] - self.data[employeeid][1]["ClosedCases"]
        return name, activecases

    #    def __init__(self):
    #        self.data = {
    #            "632132": ["Tummala Viswanth Sai", {"Backlog": 12, "ClosedCases": 3}],
    #            "632133": ["Nikhil Prabhu", {"Backlog": 15, "ClosedCases": 1}],
    #            "632134": ["Mohammed Naseef", {"Backlog": 9, "ClosedCases": 0}],
    #            "632135": ["Dinesh Singh", {"Backlog": 0, "ClosedCases": 0}],
    #        }
    # This is static data initialization for Testing
