from sqlalchemy import Column, Integer, Boolean


class Test(object):
    __tablename__ = 'test_result'
    id = Column(Integer, primary_key=True)
    solution_id = Column(Integer)
    test_id = Column(Integer)
    time = Column(Integer)
    result = Column(Boolean)  # OK or NOT OK
