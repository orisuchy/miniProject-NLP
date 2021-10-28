import requests
import lxml.html as lh
from openpyxl import Workbook


def getBookDetails(bookNum):
    bookURL = "https://www.mgketer.org/tanach/" + str(bookNum)
    bookPage = requests.get(bookURL)
    pageContent = lh.fromstring(bookPage.content)
    title = pageContent.xpath('//u')[0].text_content()
    bookName = title.replace('תנ"ך -  ספר ', '')
    rows = pageContent.xpath('//h3')
    numOfPsukim = int(rows[3].text_content().split()[-1])
    return bookName, numOfPsukim


def putInExcel(num, name, psukim):
    sheet[f'A{num+1}'] = num
    sheet[f'B{num+1}'] = name
    sheet[f'C{num+1}'] = psukim


workbook = Workbook()
sheet = workbook.active
sheet['A1'] = 'מס"ד'
sheet['B1'] = 'ספר'
sheet['C1'] = 'מספר פסוקים'


for book in range(1, 40):
    name, psukim = getBookDetails(book)
    print(f'{name}\t{psukim}')
    putInExcel(book, name, psukim)

workbook.save(filename="biblePsukim.xlsx")
