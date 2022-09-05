from os import stat
from bottle import get, run, template, route, static_file


@get('/')
def homepage():
    return template('index')

# @route('/:name')
# def custompage(name):
#     return f'hello {name}'

@route('/:filename')
def getfile(filename):
    return static_file(filename, root='./')


@get('/upload')
def upload_get():
    return '''
    <html>

    '''


run(host='127.0.0.1', port=80) 


https://download.cncb.ac.cn/gsa/CRA005819/CRR365088/CRR365088_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365088/CRR365088_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365089/CRR365089_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365089/CRR365089_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365090/CRR365090_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365090/CRR365090_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365091/CRR365091_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365091/CRR365091_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365092/CRR365092_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365092/CRR365092_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365093/CRR365093_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365093/CRR365093_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365094/CRR365094_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365094/CRR365094_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365095/CRR365095_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365095/CRR365095_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365096/CRR365096_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365096/CRR365096_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365097/CRR365097_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365097/CRR365097_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365098/CRR365098_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365098/CRR365098_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365099/CRR365099_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365099/CRR365099_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365100/CRR365100_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365100/CRR365100_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365101/CRR365101_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365101/CRR365101_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365102/CRR365102_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365102/CRR365102_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365103/CRR365103_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365103/CRR365103_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365104/CRR365104_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365104/CRR365104_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365105/CRR365105_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365105/CRR365105_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365106/CRR365106_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365106/CRR365106_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365107/CRR365107_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365107/CRR365107_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365108/CRR365108_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365108/CRR365108_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365109/CRR365109_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365109/CRR365109_r2.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365110/CRR365110_f1.fq.gz
https://download.cncb.ac.cn/gsa/CRA005819/CRR365110/CRR365110_r2.fq.gz