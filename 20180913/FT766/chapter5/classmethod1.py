# 定義類別CoeffVar
class CoeffVar(object):
    coefficient = 1

    @classmethod  # 將方法mul指定為類別方法
    def mul(cls, fact):  # 第1引數為cls
        return cls.coefficient * fact


# 定義繼承類別Coeffvar的類別MulFive
class MulFive(CoeffVar):
    coefficient = 5


x = MulFive.mul(4)  # CoeffVar.mul(MulFive, 4) -> 20
