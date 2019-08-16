"""用于统计在某个文件中，某些字段出现的次数，如统计访问web日志的同一ip次数排名"""
import re

class CountPatt:
    def __init__(self,fname,patt):
        self.fname = fname
        self.patt = patt

    def count_patt(self):        #提供文件和匹配模式，即可算出符合模式的数量
        result = {}                   #使用字典保存结果
        cpatt = re.compile(self.patt)     #使用正则编译，以便提高匹配效率
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)      #逐行匹配
                if m:
                    key = m.group()         #将成功匹配的进行内容提取
                    result[key] = result.get(key,0) + 1     #对匹配的结果进行累计，不能直接使用+=，因为前提字典key要存在
        return result


if __name__ == '__main__':

    fname = 'access_log'
    ip = '^(\d+\.){3}(\d+)'    #正则模糊匹配IP地址
    cp = CountPatt(fname,ip)
    ips_dict = cp.count_patt()
    ips_list = list(ips_dict.items())
    print(ips_dict)
    print(ips_list)

    # 取出数量最多的前10位
    ips_list.sort(key=lambda item:item[-1],reverse=True)    #倒序排序，key参数指定一个在进行比较之前作用在每个列表元素上的函数
    for i in range(10):
        print(ips_list[i])

    #用于统计其他数据的数量
    cp2 = CountPatt('/etc/passwd','bash$|nologin$')
    print(cp2.count_patt())