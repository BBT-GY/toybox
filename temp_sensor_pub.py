#!/usr/bin/env python


import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import ds18b20
import segment
import time
from datetime import datetime
import ambient
from os import getenv
import mysql.connector

broker_address = "test.mosquitto.org"     #MQTT broker_address :192.168.0.31
Topic = "yahatapiper"

print("creating new instance")
client = mqtt.Client() #create new instance

print("connecting to broker")
client.connect(broker_address) #connect to broker


channelID = your ambient channelID
writeKey = 'your ambient channelID writeKey'

def setup():
	segment.TM1638_init()

def destory():
	GPIO.cleanup()
	cnn.close()

def loop():
	tmp = 0.0
	while True:
		datetime_dat = datetime.now()
		time_str = datetime_dat.strftime('%Y/%m/%d')
		tmp = ds18b20.ds18b20Read()
		segment.numberDisplay_dec(tmp)
		print("Publishing message: %s to topic: %s" % (tmp, Topic))
		client.publish(Topic, tmp)
		am = ambient.Ambient(channelID, writeKey)
		r = am.send({'d1': tmp})
		dateappend = datetime_dat
		temperature = tmp
		cnn = mysql.connector.connect(host='yourmysqlhost',
                                  port=mysqlport,
                                  db='yourdbname',
                                  user='yourusername',
                                  passwd='yourpasswd',
                                  charset="utf8")
		cur = cnn.cursor()
		cur.execute("""INSERT INTO yoursensortablename (DateAppend, Temperature)
  		 	VALUES (%s, %s)""",  (dateappend, temperature))

		cnn.commit()
		time.sleep(60)

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destory()
