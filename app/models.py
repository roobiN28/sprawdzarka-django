from django.db import models
from app.static import TestResultChoices


class Solution(models.Model):
    program_code = models.CharField('Kod programu napisany w Python', max_length=800000)
    add_date = models.DateTimeField('Data dodania', auto_now_add=True)


class Test(models.Model):
    test_name = models.CharField(max_length=30)  # czy potrzebujemy????
    input_data = models.CharField('Dane wejściowe', max_length=800000)
    output_data = models.CharField('Dane wyjściowe', max_length=800000)
    add_date = models.DateTimeField('Data dodania', auto_now_add=True)


class TestResult(models.Model):
    time = models.IntegerField()
    result = models.BooleanField()  # TODO: {OK, FAIL, IN-PROGRESS, ERROR}
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    @classmethod
    def create(cls, time, result, solution, test):
        testResult = cls(time=time,
                         result=result,
                         solution=solution,
                         test=test)

        return testResult
