import requests
import lxml.html as lh


def getBookDetails(bookNum):
    bookURL = "https://www.mgketer.org/tanach/" + str(bookNum)
    bookPage = requests.get(bookURL)
    pageContent = lh.fromstring(bookPage.content)
    title = pageContent.xpath('//u')[0].text_content()
    bookName = title.replace('תנ"ך -  ספר ', '')
    rows = pageContent.xpath('//h3')
    numOfPsukim = int(rows[3].text_content().split()[-1])
    return bookName, numOfPsukim

for book in range(1,40):
    name, psukim = getBookDetails(book)
    print(f'{name}\t{psukim}')