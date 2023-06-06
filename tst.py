import os
here = os.path.dirname(os.path.abspath(__file__))
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

from pikepdf import Pdf
pdf = Pdf.open('111598007.pdf')
pages = pdf.pages
n = 1
for i in pages:
    output = Pdf.new()
    output.pages.append(i)
    output.save(f'{n}.pdf')    # 格式化檔案名稱
    n = n + 1                      # 編號加 1