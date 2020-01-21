def profession():
    sel_profession = str(input('请选择你的职业:\n        1:唐僧\n        2:白骨精'))
    if sel_profession == '1':
        print('恭喜你，你选择了又白又帅的唐僧，让我们开始冒险吧')
    elif sel_profession == '2':
        print('什么？你尽然选了白骨精，白不要脸了，作为正义的系统，当然要默认帮你选择唐僧来参加游戏')
    else:
        print('瞎JB输什么，快点重新选')
        profession()

profession()

def arms():
    sel_arms = str(input('请选择你要使用的武器：\n        1:板凳（攻击+10）\n        2:板砖（攻击+20）'))
    if sel_arms == '1':
        print('攻击+10')
    elif sel_arms == '2':
        print('攻击+20')
    else:
        print('瞎JB输什么，快点重新选')
        arms()
arms()
print('既然选择好了武器，那么，少年，开始战斗吧：')

def action():
    health = 0
    while True:
        sel_action = str(input('请选择你接下来的行动：\n        1:修炼神功\n        2:打白骨精\n        3:妖怪太厉害了，溜了溜了'))
        if sel_action == '1':
            health = health + 1 * 2
            print('恭喜你修炼有成！生命值+2，当前生命值等于',health)
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
action()