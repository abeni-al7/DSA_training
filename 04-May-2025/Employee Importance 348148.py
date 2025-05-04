# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee = None
        importance = 0
        for i in range(len(employees)):
            if employees[i].id == id:
                employee = employees[i]
                importance += employee.importance
                for subordinate in employee.subordinates:
                    importance += self.getImportance(employees, subordinate)
                break
        return importance
        