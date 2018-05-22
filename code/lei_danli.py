
# 类继承的单例模式
class SingTon:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            org  = super(SingTon, cls)
            # 继承SingTon的boy类
            print(org)
            cls._instance = org.__new__(cls, *args, **kwargs)
        return cls._instance



class Boy(SingTon):
    def __init__(self):
        pass



c = Boy()