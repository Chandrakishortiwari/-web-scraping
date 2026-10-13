import requests
from bs4 import BeautifulSoup

web = requests.get("url")


# html parssing and pritty
soup = BeautifulSoup(web.content, "html.parser")

print(soup.prettify())

# print(soup.h1) soup.tag name and return tag frist elemet 

# naviagteable string tag ke annder ki sting findig
# tag = soup.p.string

# find and find all method 
# find method find frist value in finding

# tag name 
# tag_p = soup.find("p")

# class name 
class_name = soup.find('div', class_name ="")

# id name
id_name = soup.find("div", id= "")





# allfind method find all value in finding

# tag name 
# tag_p = soup.find_all("p")

# class name 
# class_name = soup.find_all('div', class_name ="")

# id name
# id_name = soup.find_all("div", id= "")