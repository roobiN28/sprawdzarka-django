import subprocess

import os
import time
from app.models import Test
from app.models import TestResult


class TestService(object):

    def __init__(self, solution):
        self._solution = solution
        self._testSolutionFileName = 'testSolution.py'
        self._command = ['python', self._testSolutionFileName]


    def createFile(self, code):
        with open(self._testSolutionFileName, "w") as text_file:
            print(code, file=text_file)


    def removeFile(self):
        try:
            os.remove(self._testSolutionFileName)
        except OSError:
            pass


    def convertArgsToBytes(self, args):
        return ((str(args).replace(' ', '\n')).encode())


    def checkResult(self, obtainedResult, expectedResult):
        return True if (int(obtainedResult) == int(expectedResult)) else False


    def calculateExecutionTime(self,startTime):
        return round((time.time() - startTime) * 1000)


    def doTest(self):
        for test in Test.objects.filter(algorithm__id=self._solution.algorithm.id):
            testResult = TestResult().create(-1, "inprogress", self._solution, test)
            testResult.save()
            self.createFile(self._solution.program_code)
            startTime = time.time()
            try:
                out = subprocess.check_output(self._command, input=self.convertArgsToBytes(test.input_data), timeout=20)
                executionTime = self.calculateExecutionTime(startTime)
                validationResult = "ok" if self.checkResult(out, test.output_data) else "fail"
            except subprocess.TimeoutExpired:
                validationResult = self.calculateExecutionTime(startTime)
                executionTime = -2
            except subprocess.SubprocessError:
                validationResult = "error"
                executionTime = -3

            testResult.time = executionTime
            testResult.result = validationResult
            testResult.save()

            self.removeFile()

