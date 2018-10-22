"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        def takeid(employee):
            return employee.id

        employees.sort(key=takeid)
        self.dict = {}
        self.list = []
        self.importance = 0
        for i in employees:
            self.dict[i.id] = i.importance
            if i.id == id:
                self.list = i.subordinates
                self.importance = i.importance
            if i.id in self.list:
                self.list += i.subordinates
        for i in self.list:
            self.importance += self.dict[i]
        return self.importance
