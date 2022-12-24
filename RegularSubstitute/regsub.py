import re,sys
sublist=[['<span class="MuiChip-label MuiChip-labelMedium css-.+?">','【'],
['</span></div></div>','】'],
['<.+?>',''],
['\n',''],
['\r',''],
['【','\n【'],
['】','】\n'],
['\r1 - ','1 - '],
['&gt;','>'],
['&lt;','<']
]
def sub(filename):
    string=''
    f = open(filename,'r',encoding='utf-8')
    for i in f.readlines():
        string += i
    for i in sublist:
        string = re.sub(i[0],i[1], string)
    f.close()
    f = open(filename,'w',encoding='utf-8')
    f.write(string)
    f.close()
if __name__ == '__main__':
    for i in sys.argv[1:len(sys.argv)]:
        sub(i)
    print('Done successfully.')