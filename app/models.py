from django.db import models


class Algorithm(models.Model):
    name = models.CharField('Nazwa', max_length=100)
    description = models.CharField('Opis', max_length=10000)


class Solution(models.Model):
    program_code = models.CharField('Kod programu napisany w Python', max_length=800000)
    add_date = models.DateTimeField('Data dodania', auto_now_add=True)
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)

    def allTestPassed(self):
        return all(testResult.result == "ok" for testResult in self.testresult_set.all())


class Test(models.Model):
    test_name = models.CharField(max_length=30)  # czy potrzebujemy????
    input_data = models.CharField('Dane wejściowe', max_length=800000)
    output_data = models.CharField('Dane wyjściowe', max_length=800000)
    add_date = models.DateTimeField('Data dodania', auto_now_add=True)
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)


class TestResult(models.Model):
    time = models.IntegerField()
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
