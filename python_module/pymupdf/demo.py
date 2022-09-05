
import fitz 



# 打开文档 
doc = fitz.open('a.pdf')

pno = 1
page = doc.load_page(pno) # loads page number 'pno' of the document (0-based)
# page = doc[pno] # the short form
    

# ## 呈现页面 
pix = page.get_pixmap(dpi=600)
pix.save(f"{pno}.png") 


# ## 提取页面信息 
# text = page.get_text('text')
# print(text)
    

## 信息搜索 
areas = page.search_for('both')
print(areas)
    



