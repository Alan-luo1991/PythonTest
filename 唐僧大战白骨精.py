# 公式： 扣血 = 攻击-防御

import logging

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

file_hander = logging.FileHandler("battle.log")
file_hander.setLevel(logging.DEBUG)

console_hander = logging.StreamHandler()
console_hander.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s")
console_hander.setFormatter(formatter)
file_hander.setFormatter(formatter)

logger.addHandler(file_hander)
logger.addHandler(console_hander)


class Creature:
    def __init__(self, hp=0, damage=0, armor=0):
        """
        初始化生物
        :param hp: 血量
        :param damage: 攻击
        :param armor: 防御力
        """
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def add_damage(self, weapon):
        """
        增加攻击力
        :param weapon: 攻击力
        :return:
        """
        self.damage += weapon

    def add_hp(self, practice):
        """
        增加生命值
        :param practice:
        :return:
        """
        self.defence += practice

    def attack(self):
        """
        攻击，预留
        :return:
        """
        pass

    def defence(self, enemy_damage):
        """
        防守
        :param enemy_damage:
        :return:
        """
        if enemy_damage > self.armor and self.hp > 0:
            self.hp -= enemy_damage - self.armor
            logger.debug("Current HP = %s" % self.hp)
        else:
            logger.debug("Armor is enough, not change")


def profession():
    sel_profession = str(input('请选择你的职业:\n        1:唐僧\n        2:白骨精\n'))
    while sel_profession != "1":
        if sel_profession == '2':
            print('什么？你竟然选了白骨精，太不要脸了，作为正义的系统，当然要默认帮你选择唐僧来参加游戏\n')
            return 0
        else:
            print('瞎JB输什么，快点重新选')
        sel_profession = str(input('请选择你的职业:\n        1:唐僧\n        2:白骨精\n'))
    print('恭喜你，你选择了又白又帅的唐僧，让我们开始冒险吧\n')


def selection():
    while True:
        sel_profession = str(input('请选择你的职业:\n        1:唐僧\n        2:白骨精\n'))
        if sel_profession == '1':
            print('恭喜你，你选择了又白又帅的唐僧，让我们开始冒险吧\n')
            break
        elif sel_profession == '2':
            print('什么？你竟然选了白骨精，太不要脸了，作为正义的系统，当然要默认帮你选择唐僧来参加游戏\n')
            break
        else:
            print('瞎JB输什么，快点重新选')


def arms():
    """
    选择武器
    :return: 返回增加的攻击力
    """
    while True:
        sel_arms = str(input('请选择你要使用的武器：\n        1:板凳（攻击+10）\n        2:板砖（攻击+20）\n'))
        if sel_arms == '1':
            print('攻击+10')
            return 10
        elif sel_arms == '2':
            print('攻击+20')
            return 20
        else:
            print('瞎JB输什么，快点重新选')


def action(health):
    while True:
        sel_action = str(input('请选择你接下来的行动：\n        1:修炼神功\n        2:打白骨精\n        3:妖怪太厉害了，溜了溜了\n'))
        if sel_action == '1':
            health = health + 2
            print('恭喜你修炼有成！生命值+2，当前生命值等于', health)
        elif sel_action == '2':
            if health >= 10:
                print('恭喜你，你战胜了白骨精')
                break
            else:
                print('你被干死了，再练练再来吧')
        elif sel_action == '3':
            print('溜你嘛B，回来继续干')
        else:
            print('瞎JB选，重新选')

# print(Creature.__init__.__doc__)
if __name__ == '__main__':
    character = Creature(10, 5, 5)  # 初始化唐僧的数据
    monster = Creature(100, 10, 8)  # 初始化白骨精的数据
    selection()
    character.add_damage(arms())
    logger.debug("当前攻击力:%s" % character.damage)
    action(character.hp)
