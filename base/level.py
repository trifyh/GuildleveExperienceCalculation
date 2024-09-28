import xlrd


TABLE = []


class Level(object):

    def __init__(self):
        data = xlrd.open_workbook(r'../data/level.xlsx')
        table = data.sheets()[0]
        global TABLE
        TABLE = table.col_values(colx=1, start_rowx=0, end_rowx=None)
        # colx表示是获取第几列的数据
        # start_rowx表示从索引为多少开始，end_rowx表示从索引为多少结束，
        # end_rowx为None表示结束没有限制
        # 获取指定列中的数据并以列表的形式返回


Level()


class Exp(object):

    def __init__(self, lva, lvb):
        self.lva = lva
        self.lvb = lvb
        self.lvlist = []
        self.exp = 0
        for i in range(lva, lvb + 1):
            self.lvlist.append(i)

    def expcal_all(self, overflow_exp, add_exp):
        """
        经验计算

        :param (overflow_exp, add_exp)
        overflow_exp:当前有的经验值
        add_exp:新增的经验值

        :return: [缴纳理符后的当前等级，当前等级下经验，当前升级所需经验，进度条百分比0-99]
        """
        exp_list = []
        for i in self.lvlist:
            e = TABLE[i-1]
            exp_list.append(e)

        current_level = self.lvlist[0]   # 当前等级
        overflow_exp += add_exp    # 总获取经验
        i = 0
        current_need_exp = exp_list[i]  # 当前升级所需经验值

        while True:

            if self.lva >= self.lvb-1 and overflow_exp - current_need_exp >= 0:
                return [self.lvb, 0, 0, 100]

            elif overflow_exp < current_need_exp:    # 如果当前等级不够升级，跳过

                rounda = round(overflow_exp/current_need_exp * 100, 2)
                return [current_level, overflow_exp, current_need_exp, rounda]

            elif overflow_exp >= current_need_exp:       # 如果可以升级
                overflow_exp = overflow_exp - current_need_exp   # 溢出经验计算
                i += 1
                current_level = self.lvlist[i]
                current_need_exp = exp_list[i]
            else:
                return [100, 0, 0, 100]


if __name__ == '__main__':
    print(Exp(1, 99).expcal_all(int(0), float(225730000.0)))
