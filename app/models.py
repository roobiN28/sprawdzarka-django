from django.db import models


class Solution(models.Model):
    program_code = models.CharField('Kod programu napisany w Python', max_length=800000)
    add_date = models.DateTimeField('Data dodania', auto_now_add=True)

    def allTestPassed(self):
        return all(testResult.result == "ok" for testResult in self.testresult_set.all())


class Test(models.Model):
    test_name = models.CharField(max_length=30)  # czy potrzebujemy????
    input_data = models.CharField('Dane wejściowe', max_length=800000)
    output_data = models.CharField('Dane wyjściowe', max_length=800000)
    add_date = models.DateTimeField('Data dodania', auto_now_add=True)


class TestResult(models.Model):
    time = models.IntegerField()
    # result = models.BooleanField()  # TODO: {OK, FAIL, IN-PROGRESS, ERROR}
    result = models.CharField(max_length=10)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    @classmethod
    def create(cls, time, result, solution, test):
        testResult = cls(time=time,
                         result=result,
                         solution=solution,
                         test=test)

        return testResult
