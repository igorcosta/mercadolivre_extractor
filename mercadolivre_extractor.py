#!/usr/bin/python
# -*- encoding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
from lxml import html
import json
import uuid
import lxml.html
import time
import os
from product import Product
import re
import sys
#Extrair anuncios do Mercado livre 
#Author Igor Costa
#E-mail igorcosta AT google mail DOT com

url = 'http://eshops.mercadolivre.com.br/LEDGREEN+ILUMINACAO' 
# url = "http://eshops.mercadolivre.com.br/chedas+som"

class Printer():
    """Print things to stdout on one line dynamically"""
    def __init__(self,data):
        sys.stdout.write("\r"+data.__str__())
        sys.stdout.flush()

# Main Function
def grab():
	# print 'Digita a lista de um vendedor do Mercado Livre:',
	# url = raw_input()
	# print 'A url esta certa? *y/n) \n' + url
	# if raw_input() is not 'y':
	# 	sys.exit(0)
	links = []
	products =[]
	print 'pegando dados da paginacao'
	pages = getPagination()
	print 'pegando links'
	for page in pages:
		for link in getPaginationList(page):
			links.append(link)
	print 'Total Links ' + str(len(links))
	print 'Gerando dados dos produtos'
	counter = 0
	for url in links:
		products.append(getProductDetails(url))
		counter+=1
		output = 'Produto %d de %d' %(counter,len(links))
		Printer(output)

	return products

def getProductDetails(url):
	page = requests.get(url)
	tree = html.fromstring(page.text)
	prod = Product()
	prod.name = tree.xpath('/html/body/div[2]/header[1]/h1/text()')
	prod.price =  tree.xpath('//*[@id="productInfo"]/fieldset[1]/article/strong/text()')[0]
	image_url = tree.xpath('//div[@class="first-image"]//a/@href')
	image_path = ''
	for image in image_url:
		image_path = image
		prod.image = saveImage(image_path)
	itens=''
	for p in tree.xpath('//div[@id="itemDescription"]'):
		itens += lxml.html.tostring(p)
	soup = BeautifulSoup(itens, 'lxml')
 	prod.desc =  soup.get_text().encode('utf-8')
 	prod.original_url = url
 	return prod

def getPagination():
	xpath_rule = '//*[@id="inner-main"]/div[3]/div[4]/ul/li/a/@href'
	page = requests.get(url)
	tree = html.fromstring(page.text)
	crumbs = tree.xpath(xpath_rule)
	return crumbs

def getPaginationList(url):
	xpath_rule ='//*[@id="searchResults"]/li/a/@href'
	page = requests.get(url)
	tree = html.fromstring(page.text)
	links = tree.xpath(xpath_rule)
	return links

def saveImage(path):
	directory = directory = os.path.dirname(os.path.realpath(__file__)) + '\images_ml'
	if not os.path.exists(directory):
		os.makedirs(directory)
	image_file = str(uuid.uuid1()) +'.jpg'
	f = open( directory + '\\' + image_file,'wb')
	content = requests.get(path).content
	f.write(content)
	f.close()
	return image_file
 


def exportJSON():
	#Save the json file
	f_json = open("itens.json",'wb')
	with open("itens.json", "a") as myfile:
		myfile.write(json.dumps(grab(),sort_keys=False))
	myfile.close()

def exportSQL():
	# Generate SQL
	data = ''
	counter = 0
	print 'Gerando arquivo SQL'
	with open('itens.json') as data_file:
		data = json.load(data_file)
	while counter < len(data):
		counter +=1
		line = 'Rows %d' %counter
	print line,
	print '\n'
	fsql = open('itens.sql','wb')
	fsql.write(insert_sql('produtos',data,["name","price","desc","image","original_url"]))
	fsql.close()
	print 'Arquivo SQL gerado'

def clean(str):
	# str = str.replace('\t','')
	# str = str.replace('[','')
	# str = str.replace(']','')
	str = str.replace('["',"'")
	str = str.replace('"]',"'")
	str = str.replace('[','')
	tr = str.replace('[','')
	tr = str.replace("['",'')
	tr = str.replace("']",'')
	tr = str.replace("u'",'')
	return str.encode('utf-8').strip()

def insert_sql(table,source,fields):
	table_fields = ''
	sql = ''
	for field in fields:
		table_fields += '"'+field+'"'+','
	table_fields = table_fields[:-1]
	prefix = 'insert into %s (%s) ' %(table,table_fields)
	for item in source:
		value = ''
		for field in fields:
			value +='"' + item[clean(field)] +'"'+ ','
		sql += prefix  + ' values ('+clean(value[:-1]) +')'+'\n'	
	return sql

#exportSQL()
#exportJSON()


