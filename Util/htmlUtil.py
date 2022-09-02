# _*_ coding:UTF-8 _*_
# @time：2022/7/4  20:02
# @Author: 皓雪
# @file: htmlUtil.py
# @Software: PyCharm

import re,time
from Util import log
import logging
from conf.VarConfig import BASE_DIR



logger = log.Logger("google", CmdLevel=logging.DEBUG, FileLevel=logging.DEBUG)



def htmlreturn(step_row_nums,case_data):
    template = BASE_DIR + '\\conf' + '\\template.html'
    Reports = BASE_DIR + '\\Reports' + '\\Reports.html'

    test_date = 'test_date'
    test_result = step_row_nums-1

    test_version = 'V1.0'
    pass_count = 0
    fail_count = 0
    error_count = 0
    skip_count = 0
    for i in range(len(case_data)):
        if case_data[i]['test_result'] == 'Success':
            pass_count += 1
        elif case_data[i]['test_result'] == 'Fail':
            fail_count += 1
        elif case_data[i]['test_result'] == 'Error':
            error_count += 1
        else:
            skip_count += 1
    percent = pass_count/(pass_count+fail_count+error_count+skip_count)*100
    report_time = time.strftime('%Y-%m-%d',time.localtime())



    with open(template,'r',encoding='utf-8') as f :
        for line in f:
            line = line.replace('$test_date', str(eval('test_date')))
            line = line.replace('$pass_count',str(eval('pass_count')))
            line = line.replace('$test_version', str(eval('test_version')))
            line = line.replace('$fail_count', str(eval('fail_count')))
            line = line.replace('$error_count', str(eval('error_count')))
            line = line.replace('$skip_count', str(eval('skip_count')))
            line = line.replace('$percent', str(eval('percent')))
            line = line.replace('$report_time', str(eval('report_time')))
            line = line.replace('$skip_count', str(eval('skip_count')))
            with open(Reports,'a',encoding='utf-8') as f :
                f.write(line)
            if line == '\t$test_result\n':
                for i in range(0, test_result):
                    line_tmp = '''
                        	<tr >
                    		<td width="7%">ID</td>
                    		<td width="15%">Scene</td>
                    		<td width="7%">Executed</td>
                    		<td width="10%">Test_Result</td>
                    		<td width="12%">Run_time</td>
                    		<td width="12%">Error Msg</td>
                    		<td width="15%">Test_Log</td>
                    		<td width="20%">Test Screen</td>
                    	</tr>
                    	'''
                    ID = case_data[i]['id']
                    # print(ID)
                    Scene = case_data[i]['case_desc']
                    Executed = case_data[i]['is_need_run']
                    Test_Result = case_data[i]['test_result']
                    Run_time = case_data[i]['test_time']
                    Test_Log = logger.LogFileName

                    line_tmp = line_tmp.replace('ID',str(eval('ID')))
                    line_tmp = line_tmp.replace('Scene', str(eval('Scene')))
                    line_tmp = line_tmp.replace('Executed', str(eval('Executed')))

                    line_tmp = line_tmp.replace('Test_Result', str(eval('Test_Result')))
                    line_tmp = line_tmp.replace('Run_time', str(eval('Run_time')))
                    line_tmp = line_tmp.replace('Test_Log', str(eval('Test_Log')))

                    line = line_tmp

                    with open(Reports, 'a', encoding='utf-8') as f:
                        f.write(line)







if __name__ == '__main__':
    name = 'zgabf'
    a = '${name}'
    operate_value = eval(a[2:-1])
    print(operate_value)