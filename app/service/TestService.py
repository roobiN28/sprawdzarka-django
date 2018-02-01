from app.models import Test

class TestService(object):

    def addTest(self, test):
        test.save();
        # dodawanie do bazy danych tego testu, ale to chyba bedzie obsługiwane bezposrednio przez formularz??

    def getTest(self,test_id):
        t = Test.objects.get(pk=test_id)
        return t

    def get_all_tests(self):
        return Test.objects.all()

