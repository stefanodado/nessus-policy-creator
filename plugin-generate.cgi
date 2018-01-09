#!/usr/bin/python

#classes
import os
import sys
from pprint import pprint
import cgi 
import sqlite3 as lite

dbconn = lite.connect('plugins.db')
query="SELECT name, id FROM Family ORDER BY name ASC"
cursor = dbconn.cursor()
cursor.execute(query)
results = cursor.fetchall()
file= open("plugin-list.html", "w")
print "Content-type: text/html\n\n"
for fam in results:
	textfilter=str(fam[0]+" ")
	lista=""
	query2="SELECT id, name FROM Plugin WHERE familyID='"+str(fam[1])+"' ORDER BY name"
	cursor.execute(query2)
	results2 = cursor.fetchall()
	for plu in results2:
		textfilter=textfilter+str(plu[0])+" "
		lista=lista+'<li data-icon="plus" data-filtertext="'+str(plu[0])+" "+'"> <a onclick="addplugin('+str(plu[0])+')" class="float-right" style="margin:0px;text-shadow:none;" role="button">'+str(plu[0])+" - "+str(plu[1])+'</a></li>'
	file.write('<div data-role="collapsible" data-filtertext="'+textfilter+'">')
	file.write('<h3>'+fam[0]+'</h3>')
	file.write('<ul data-role="listview" data-inset="false" data-split-icon="true">')
	file.write(lista)
	file.write('</ul></div>') 
file.close
print "Done"	
