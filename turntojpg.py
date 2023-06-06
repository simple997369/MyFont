# 导入这个库：python-office，简写为office
import office
import os
here = os.path.dirname(os.path.abspath(__file__))

# 一行代码，实现转换
# for i in range(138):
#     office.pdf.pdf2imgs(
#         pdf_path=str(i+1)+'.pdf',
#         out_dir=here+'/jpg'
#     )
# 参数说明：
# pdf_path = 你的PDF文件的地址 
# out_dir = 转换后的图片存放地址，可以不填，默认是PDF的地址

office.pdf.pdf2imgs(
    pdf_path='5.pdf',
    out_dir=here+'/jpg')