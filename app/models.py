from django.db import models

# Create your models here.
class TestResult(models.Model):
    # id = models.IntegerField(primary_key=True)
    # solution_id = models.ForeignKey(Solution,on_delete=models.CASCADE)
    # test_id = models.ForeignKey(Test,on_delete=models.CASCADE)
    # pub_time = models.DateTimeField('data published')
    result = models.BooleanField()

    # def __str__(self):
    #     return self.pub_time
    # def __bool__(self):
    #     return self.result


class Solution(models.Model):
    # id = models.IntegerField(primary_key=True)
    program_code = models.CharField(max_length=800000)
    add_data = models.DateField('date published')
    test_id = models.ForeignKey('app.Test', related_name='id_test', on_delete=models.CASCADE)
    testResult_id = models.ForeignKey('app.TestResult', related_name='id_testResult',on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.program_code
    # def __str__(self):
    #     return self.add_data
    # def __int__(self):
    #     return self.test_id
    # def __int__(self):
    #     return self.testResult_id


class Test(models.Model):
    test_name = models.CharField(max_length=30)
    input_data = models.CharField(max_length=800000)
    output_data = models.CharField(max_length=800000)
    # solution_id = ArrayField(models.ForeignKey('Solution',on_delete=models.CASCADE))
    # solution_id = models.ForeignKey('app.Solution', related_name='id_Solution',on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.test_name
    # def __str__(self):
    #     return self.input_data
    # def __str__(self):
    #     return self.output_data
    # def __str__(self):
    #     return self.solution_id