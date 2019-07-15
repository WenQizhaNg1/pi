#encoding: utf-8
import RPi.GPIO as GPIO
import time
import picamera
from wxpy import *
print("请先登录微信！")
bot = Bot(console_qr=True)
def wx():
	my_friend = bot.friends().search('wenqi')
	my_friend.send('发现目标')
	my_friend.send_image('demo.jpg')

def camera():
	camera = picamera.PiCamera()
	camera.brightness = 60
	try:
		time.sleep(2)
		camera.capture('demo.jpg')
		camera.close()
		print("拍摄成功！")
	except:
		print("拍摄失败！")
def LED():
	GPIO.setup(21, GPIO.OUT)
	i = 0
	try:
		while True:

			if i > 10:

				break
			GPIO.output(21, True)
			time.sleep(0.1)
			GPIO.output(21, False)
			time.sleep(0.1)
			i += 1
	finally:
		GPIO.cleanup(21)
	return

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.IN)
bot.join()
try:
	p=1
	print("正在寻找人体红外光源...")
	while True :	
		if(GPIO.input(24)):
			print("红外感应器响应次数：%d" %p)
			LED()
			camera()
			try:
				wx()
				print("已发送到手机端")
			except:
				print("ERROR")
			p=p+1
			time.sleep(30)
		

except KeyboardInterrupt:
	GPIO.cleanup()
	print("意外终止。")

