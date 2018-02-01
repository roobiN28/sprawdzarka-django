from app.models import TestResult

class TestResultServices(object):

    def get_test_result(self, id):
        return TestResult.objects.get(pk=id)

    def get_all_lists_tests_resut(self):
        return TestResult.objects.all()

    def get_result_is_false(self):
        return TestResult.objects.filter(result=False)

    def get_result_is_true(self):
        return TestResult.objects.filter(result=True)