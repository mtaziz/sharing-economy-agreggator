import tornado.ioloop
import tornado.web
import json
import os
import psycopg2

class HousetripResults(tornado.web.RequestHandler):
	def get(self):
		conn = psycopg2.connect("host=localhost dbname=scrape user=postgres password=lifemaker1989")
		cur = conn.cursor()
		results = []
		cur.execute("select * from housetripdeals")
		for record in cur:
			results.append(record)
		cur.close()
		conn.close()

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(results))


application = tornado.web.Application([
	(r"/housetrip", HousetripResults),

])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()