#-*-coding:utf8 -*-
#/usr/bin/python
import pandas as pd 
from sqlalchemy import create_engine
from pandas.io import sql

def to_xml(df, filename=None, mode='w', keys=None):
	def row_to_xml(row):
		xml = ['<item>']
		for field in row.index:
			xml.append('<field name="{0}"><![CDATA[{1}]]></field>'.format(field, row[field]))
		xml.append('</item>')
		return '\n'.join(xml)
	res = '<?xml version="1.0" encoding="ISO-8859-1"?>\n'+'<data>\n'+'\n'.join(df.apply(row_to_xml, axis=1))+'\n</data>'
	if filename is None:
		return res
	with open(filename, mode) as f:
	
		print res
		f.write(res)
pd.DataFrame.to_xml = to_xml

engine = create_engine('mysql://root:lifemaker1989@localhost/alterrefront', echo=True)
#cnx = engine.connect()
#query = "SELECT url, title, description, media, price, period, category, subcategory FROM ads LIMIT 100"
#results   = cnx.execute(query)
#fetchall  = results.fetchall()
df        = sql.read_sql_table("ads", con=engine) 
dataframe = out = df[df['location'].str.contains('^(.*rouen.*)$')]
#cnx.close()
keys = ["url", "title", "description", "media", "price", "period","category", "subcategory"]
dataframe.to_xml('flux.xml', keys=keys)
