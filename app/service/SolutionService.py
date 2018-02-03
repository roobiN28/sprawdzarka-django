from app.models import Solution

class SolutionService(object):

    def addSolution(self, program_code,add_data,test_id,testResult_id):
        solution =Solution(program_code,add_data,test_id,testResult_id)
        solution.save();

    def get_all_slution(self):
        return Solution.objects.all()

    def get_concrete_solution_by_id(self, solution_id):
        return Solution.objects.get(pk = solution_id)

    def get_lists_solution_by_test_id(self,id):
        return Solution.objects.all().filter(test_id = id)

    def get_lists_solution_by_test_result_id(self,id):
        return Solution.Objects.all().filter(testResult_id = id)

