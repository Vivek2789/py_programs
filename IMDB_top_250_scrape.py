import urllib2
from bs4 import BeautifulSoup

import sqlite3





url = 'http://www.imdb.com/chart/top'

page = urllib2.urlopen(url)

soup = BeautifulSoup(page,'html.parser')
table = soup.find('table',class_='chart full-width') #Identify the table which contains the list of movies, use find() to get all the children of the table tag 


	 
#Used inspect element on the webpage to identify the tag which contains the required data	 
	 
a_tags = table.select(".lister-list .titleColumn a")  #gets you the anchor tag inside the tag which has class = titleColumn which is inside class = lister-list
movie_list = [muvie.get_text() for muvie in a_tags]   # get_text() returns the text attribute of a tag

span_tags = table.select(".lister-list  strong")
rating_list = [rating.get_text() for rating in span_tags]

secondary_info = table.select(".lister-list .titleColumn span")
year_list = [year.get_text() for year in secondary_info]



# create the  sql connection

conn = sqlite3.connect('IMDB_test.db')
cur = conn.cursor()

#create the new table
cur.execute('CREATE TABLE IMDB_250 (Movie VARCHAR(150), Rating VARCHAR(20), Year VARCHAR(20))')

for movie,ratn,yr in zip(movie_list,rating_list,year_list) :
    
	#execute the Insert query 
    cur.execute('INSERT INTO IMDB_250 (Movie, Rating, Year) VALUES (?,?,?)',(movie, ratn, yr))
	
conn.commit()
cur.close()






#tbody = table.find('tbody',class_ = 'lister-list')
#tr = tbody.find('tr')
#td = tr.find_all('td',class_ = 'titleColumn')
#x = td[0]
#print x.find('a').get_text()


#print soup.find('td',class_='titleColumn').find('a').get_text()