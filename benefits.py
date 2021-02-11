#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connect(host ="localhost", port = 3306 , user = "root", passwd="", db="finance")

cursor = conn.cursor()


def criptosQuery():
	cursor.execute("SELECT * from criptos")
	coins = cursor.fetchall()
	for n,shortName,name in coins:
		print(shortName,name)

def exchangesQuery():
	cursor.execute("SELECT * from exchange")
	exchange = cursor.fetchall()
	for n,exchangeName in exchange:
		print(exchangeName)

def purcharseQuery():
	cursor.execute("SELECT * from purchase")
	purchase = cursor.fetchall()
	for n,cripto,purchaseId,purchaseDate,cant,purchasePrice,totalPurchase,exchangeId in purchase:
		print(cripto,purchaseId,purchaseDate,cant,purchasePrice,totalPurchase,exchangeId)



criptosQuery();
exchangesQuery();
purcharseQuery();





















