import os

from whoosh.filedb.filestore import FileStorage
from whoosh.fields import *  
from jieba.analyse import ChineseAnalyzer
import json  

from whoosh.qparser import QueryParser
from whoosh.filedb.filestore import FileStorage


def method():
    pass 



schema = Schema(title = TEXT(stored=True, analyzer=ChineseAnalyzer()),
                dynasty = ID(stored=True),
                poet = ID(stored=True),
                content = TEXT(stored=True, analyzer=ChineseAnalyzer())
                )


schema = Schema(title = TEXT(stored=True),
                dynasty = ID(stored=True),
                poet = ID(stored=True),
                content = TEXT(stored=True)
                )




# storage = FileStorage('./index')
# if not os.path.exists('./index'):
#     os.mkdir('./index')
#     ix = storage.create_index(schema)
# else:
#     ix = storage.open_index()
    
# writer = ix.writer()

# with open('poem.csv', 'r', encoding='utf-8') as fr:
#     for line in fr:
#         linelist = line.strip('\n').split(',')
#         title,dynasty,poet,content = linelist
        
#         writer.add_document(title=title, dynasty=dynasty, poet=poet, content=content)
# writer.commit()


# # 查询  比如我们想要查询content中含有明月的诗句，可以输入以下代码：
storage = FileStorage('./index')
ix = storage.open_index()
with ix.searcher() as searcher:
    results = searcher.find('content', '君自故乡来')
    for res in results:
        print(res)  
        
        
        