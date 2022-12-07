import xlrd
import re


class LoadLifuXlsx(object):

    def get_value(self, job, version):
        data=xlrd.open_workbook('../data/'+job+'.xlsx')
        table = data.sheets()[version]

        # rowx表示是获取第几行的数据
        # start_col表示从索引为多少开始，end_colx表示从索引为多少结束，
        # end_colx为None表示结束没有限制
        # 获取指定行中的数据并以列表的形式返回
        lifu_list = []
        # 获取指定edition所有行
        for i in range(0, table.nrows):
            table_list = table.row_values(rowx=i, start_colx=0, end_colx=None)
            #获取等级
            str = table_list[0]
            number = re.findall("\d+", str)
            num = "".join(number)
            table_list.insert(0, num)
            # 把单行添加到lifu_list
            lifu_list.append(table_list)

        return lifu_list


if __name__ == '__main__':
    LoadLifuXlsx().get_value('刻木匠', 5)
