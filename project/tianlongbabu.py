class ImpactEffect:
    #影响效果
    def impact(self):
        #影响效果，由技能释放器调用，由具体效果类实现
        raise NotImplementedError

class DamageEffect(ImpactEffect):
    def __init__(self,value):
        self.value=value
    def impact(self):
        print("伤害你%d生命"%self.value)
class LowerMoveSpeed(ImpactEffect):
    #降低移动速度
    def __init__(self,speed,time):
        self.speed=speed
        self.time=time
    def impact(self):
        print("降低速度为%d,持续时间%d"%(self.speed,self.time))

class SkillDeployer:
    #技能释放器
    def __init__(self,name):
        self.name=name
        self.__list_impact=self.__config_skill()
    #加载列表
    def __config_skill(self):
        #配置文件中，记录的信息
        dict_skill_config_info={
            "降龙十八掌":["LowerMoveSpeed(50,60)","DamageEffect(100)"],
            "金刚伏魔":["DamageEffect(100)"]
        }
        #返回技能列表
        list_skill_info= dict_skill_config_info[self.name]
        list_skill_instance=[]
        for item in list_skill_info:
            list_skill_instance.append(eval(item))
        return list_skill_instance
        # return [eval(item for item in list_skill_info]

    #释放技能
    def generate_skill(self):

        print("%s释放了"%self.name)
        for item in self.__list_impact:
            if not isinstance(item, ImpactEffect):
                raise TypeError()
            item.impact()

a=SkillDeployer("金刚伏魔")
a.generate_skill()
a=SkillDeployer("降龙十八掌")
a.generate_skill()

