# -*- coding: utf-8 -*- 
# @Time : 2022-06-19 21:53 
# @Author : kunp
# @File : ReportUtil.py 
# @Software: PyCharm
import time

from conf.VarConfig import template_path, report_dir_path, testDataPath
from Util.ExcelUtil import ExcelUtil


class Reporter(object):
    """根据模板生成测试报告"""

    def __init__(self, filename):
        self.excel = ExcelUtil()
        self.excel.load_workbook(filename)

        self.sheet = self.excel.get_sheet_by_name('case')
        # 这边定义一个 get_all_rows_values() 方法来获取excel case sheet 中的所有数据
        self.all_values = self.excel.get_all_rows_values(self.sheet)

    def generate_report(self, test_version):
        test_count = 0
        pass_count = 0
        fail_count = 0
        skip_count = 0
        # TODO
        error_count = 0

        for one in self.all_values:
            result = one.get("test_result")
            if result == 'pass':
                pass_count += 1
            elif result == 'fail':
                fail_count += 1
            elif result == 'skip':
                skip_count += 1
            test_count += 1
        percent = str(round(pass_count/(test_count-skip_count), 4)*100) if pass_count != 0 else "0"

        content = ''
        for one in self.all_values:
            test_count += 1

            content += '\n<tr height="40">'
            content += '\n<td width="7%%">%d</td>' % one.get('id')
            content += '\n<td width="15%%">%s</td>' % one.get('case_desc')
            content += '\n<td width="7%%">%s</td>' % one.get('is_need_run')

            tmp = one.get('test_result')
            if tmp == 'pass':
                color = "darkseagreen"
            elif tmp == 'fail':
                color = "red"
            else:
                color = "yellow"
            content += '\n<td width="10%%" bgcolor="%s">%s</td>' % (color, tmp)

            content += '\n<td width="13%%">%s</td>' % one.get('test_time')         # runtime
            # TODO
            content += '\n<td width="12%%" bgcolor="#b8860b">%s</td>' % "To be added"         # error msg
            content += '\n<td width="12%%" bgcolor="#b8860b">%s</td>' % "To be added"         # test log
            content += '\n<td width="20%%" bgcolor="#b8860b">%s</td>' % "To be added"         # test img
            content += '\n</tr>'

        # 打开模板文件，并替换模板变量
        with open(template_path, encoding='utf-8') as file:
            template = file.read()

        now = time.strftime("%Y%m%d_%H%M%S")

        template = template.replace('$test-date', time.strftime("%Y%m%d"))
        template = template.replace('$test-version', test_version)
        template = template.replace('$pass-count', str(pass_count))
        template = template.replace('$fail-count', str(fail_count))
        template = template.replace('$error-count', str(error_count))
        template = template.replace('$skip-count', str(skip_count))
        template = template.replace('$percent', percent)
        template = template.replace('$report-time', now)
        template = template.replace('$test-result', content)

        filename = report_dir_path + "/" + time.strftime(f"{now}.html")
        with open(filename, mode='w+', encoding='utf-8') as file:
            file.write(template)


if __name__ == '__main__':
    filename = testDataPath + "/test_1.xlsx"
    report = Reporter(filename)
    report.generate_report('2.0')