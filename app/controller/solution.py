import datetime
import random

from django.shortcuts import render

from app.entity.Solution import Solution
from app.entity.TestResult import TestResult


def add(request):
    if request.method == "POST":
        # dodanie do bazy i zwrócenie
        s = createMockSolution()
        return render(request, 'view/solution/added_solution.html', {'solution': s})

    else:
        return render(request, 'view/solution/add_solution.html')


def showAll(request):
    list = []
    s = Solution()
    s.id = 1
    s.add_date = datetime.datetime.now()
    s.program_code = "code1"
    list.append(s)
    s1 = Solution()
    s1.id = 2
    s1.add_date = datetime.datetime.now()
    s1.add_date = s1.add_date.replace(hour=6)
    s1.program_code = "code2"
    list.append(s1)
    return render(request, 'view/solution/solutions.html', {"solutions": list})


def details(request, id):
    solution = createMockSolution()
    return render(request, 'view/solution/solution.html', {'solution': solution})


def createMockSolution():
    solution = Solution()
    solution.id = random.randint(0, 1000)
    solution.add_date = datetime.datetime.now()
    solution.program_code = '''import datetime
import random

from django.shortcuts import render

from app.entity.Solution import Solution
from app.entity.TestResult import TestResult


def add(request):
    if request.method == "POST":
        return render()
    return render(request, 'view/add_solution.html')


def showAll(request):
    list = []
    s = Solution()
    s.id = 1
    s.add_date = datetime.datetime.now()
    s.program_code = "code1"
    list.append(s)
    s1 = Solution()
    s1.id = 2
    s1.add_date = datetime.datetime.now()
    s1.add_date = s1.add_date.replace(hour=6)
    s1.program_code = "code2"
    list.append(s1)
    return render(request, 'view/solutions.html', {"solutions": list})


def details(request, id):
    solution = createMockSolution()
    return render(request, 'view/solution.html', {'solution': solution})


def createMockSolution():
    solution = Solution()
    solution.id = random.randint(0, 1000)
    solution.add_date = datetime.datetime.now()
    solution.program_code = "To jest kod programu xxx"
    solution.testResults = []
    solution.testResults.append(createMockTestResult())
    solution.testResults.append(createMockTestResult())
    solution.testResults.append(createMockTestResult())
    return solution


def createMockTestResult():
    t = TestResult()
    t.id = random.randint(0, 1000)
    t.solution_id = 1
    t.test_id = 1
    t.time = random.randint(0, 1000)
    t.result = True
    return t
'''
    solution.program_code = '<br/>'.join(solution.program_code.splitlines())
    solution.testResults = []
    solution.testResults.append(createMockTestResult())
    solution.testResults.append(createMockTestResult())
    solution.testResults.append(createMockTestResult())
    return solution


def createMockTestResult():
    t = TestResult()
    t.id = random.randint(0, 1000)
    t.solution_id = 1
    t.test_id = 1
    t.time = random.randint(0, 1000)
    t.result = True
    return t
