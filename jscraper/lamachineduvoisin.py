import dryscrape
import time

start_url="http://www.lamachineduvoisin.fr/fr/find/"
search_term = 'douai'

ads = []
# set up a web scraping session
sess = dryscrape.Session(base_url = start_url)
print sess

# we don't need images
sess.set_attribute('auto_load_images', False)

# visit homepage and search for a term
sess.visit(start_url)
q = sess.at_xpath('/html/body/div[2]/div[3]/div[1]/div/div/div[1]/div[1]/div/div/input')
print q
q.set(search_term)
button = sess.at_xpath('/html/body/div[2]/div[3]/div[1]/div/div/div[1]/div[3]/a')
button.click()

time.sleep(10)
# extract all links
count = 0
for sel in sess.xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div[3]/h4'):
	print sel.text()
# save a screenshot of the web page
sess.render('lamachineduvoisin.png')
print "Screenshot written to 'lamachineduvoisin.png'"
