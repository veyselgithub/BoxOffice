import requests
from bs4 import BeautifulSoup

url = "https://boxofficeturkiye.com/hafta/detay/2020-11"


r = requests.get(url,)
soup = BeautifulSoup(r.content,"lxml")

#ulasmak istedigimiz tablonun oldugu yere goturen kod
filmTablosu = soup.find("tbody",attrs={"class":"vertical-align-middle"}).select("td:nth-of-type(2)")
tablo = soup.select("tbody tr")
for row in tablo:
    deger = row.find_all("td")
    print(deger[7].text)


"""
for row in soup.select('tbody tr'):
    row_text = [x.text for x in row.find_all('td')]
    print(row_text[7])"""





"""
for i in range(1,48):
    filmAdi = filmTablosu[i].find("a",attrs={"class":"movie-link"}).text
    Seyirci = filmTablosu[i].find_all("td")
    print(Seyirci)
    print(filmAdi)"""
