Capitalized = {"1":"壹", "2":"贰", "3":"叁", "4":"肆", "5":"伍","6":"陆", "7":"柒", "8":"捌", "9":"玖", "0":"零", ".":""}
MonetaryUnit = ["分", "角", "", "元", "拾", "佰", "千", "万", "拾", "佰", "仟", "亿", "拾"]


number = input("请输入想要转换为大写的金额：")
list_money = []
str_money = ""
Unitlenth = len(number) -1
for key, value in enumerate(number):
    Chinese = Capitalized.get(value)
    list_money.append(Chinese)
    list_money.append(MonetaryUnit[Unitlenth])
    Unitlenth = Unitlenth -1
for i in list_money:
    str_money += i
print(str_money)



# import logzero
# import logging
# from logzero import logger
#
# logzero.loglevel(logging.ERROR)
#
# number = {"1": "壹", "2": "贰", "3": "叁", "4": "肆", "5": "伍", "6": "陆", "7": "柒", "8": "捌", "9": "玖", "0": "零", }
# unit = ["元", "拾", "佰", "千", "万", "拾", "佰", "仟", "亿", "拾"]


# class Dollor():
#     def __init__(self):
#         self.money = input("请输入金额：\n")
#         try:
#             self.money = float(self.money)
#         except:
#             raise Exception("输入有误，只能输入数字")
#         float_no = str(self.money).split(".")
#         self.integer, self.decimal = float_no[0], float_no[1]
#         logger.debug("整数部分：%s" % self.integer)
#         logger.debug("小数部分：%s" % self.decimal)
#
#     def translate(self):
#         output = ""
#         # 整数部分处理
#         unit_part = (unit[:len(self.integer)])[::-1]
#         logger.debug("unit_part: %s" % unit_part)
#         for index, i in enumerate(self.integer):
#             if i == "0" and output[-1] != "零":
#                 output += "零"
#                 continue
#             elif i == "0" and output[-1] == "零":
#                 continue
#             output = output + number.get(i) + unit_part[index]
#
#         # 小数部分处理
#         if self.decimal == "0":
#             output += "整"
#             logger.debug("无小数为%s" % output)
#         else:
#             list_decimal = ["角", "分"]
#             for index, j in enumerate(self.decimal):
#                 if index < 2:
#                     output = output + number.get(j) + list_decimal[index]
#                 else:
#                     break
#         return output
#
#
# if __name__ == '__main__':
#     d = Dollor()
#     print(d.translate())
























# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print('/n')
# nums = [2, 4, 5, 7]
# target = 9
# list: int = len(nums)
#
# for i in range(list):
#     print(i)

