# --*-- encoding:utf-8 --*--
import sys
import difflib
def read_file(filename):
    try:
        with open(filename,'r') as f:
            return f.readlines()
    except IOError:
        print "ERROR：没有找到文件%d或%d文件读取失败!" %filename

def compare_file(file1,file2,outfile):
    file1_content = read_file('file1')
    file2_content = read_file('file2')
    d = difflib.HtmlDiff
    result = d.make_file(file1_content,file2_content)
    with open(outfile,'w') as f:
        f.readlines(result)

if __name__ == '__main__':
    compare_file(r'D:/file1',r'D:/file2',r'D:/result.html')


