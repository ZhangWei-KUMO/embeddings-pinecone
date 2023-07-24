# 表格抽取

pdfplumber对表格检测的方法在很大程度上借鉴了Anssi Nurminen的硕士论文，并受到Tabula的启发。其工作原理如下：

对于给定的PDF页面，找到明确定义的线条和/或通过页面上单词的对齐来暗示的线条。合并重叠或几乎重叠的线条。找到所有这些线条的交点。
找到使用这些交点作为顶点的最精细的矩形集（即单元格）。将连续的单元格分组成表格。表格提取方法`pdfplumber.Page`对象可以调用以下表格方法：

```py
pdf = pdfplumber.open("path/to/my.pdf")
page = pdf.pages[0]
# 返回一个Table对象的列表。Table对象提供对.cells、.rows和.bbox属性的访问，以及.extract(x_tolerance=3, y_tolerance=3)方法的访问。
page.find_tables(table_settings={})
# 类似于.find_tables(...)，但返回页面上最大的表格，以Table对象的形式。如果有多个表格大小相同（通过单元格数量测量），则此方法返回距离页面顶部最近的表格。
page.find_table(table_settings={})	
# 返回从页面上找到的所有表格提取的文本，以列表的形式表示，列表中包含列表和列表，结构为表格 -> 行 -> 单元格。
page.extract_tables(table_settings={})	
# 返回从页面上找到的最大的表格提取的文本，以列表的形式表示，列表中包含列表和列表，结构为表格 -> 行 -> 单元格。
page.extract_table(table_settings={})	
```