from machine import Pin
from utime import sleep

green = Pin(5, Pin.OUT)
yellow = Pin(4, Pin.OUT)
red = Pin(18, Pin.OUT)

while True:
  green.on()
  yellow.off()
  red.off()
  print("led verde, ligado!!")
  sleep(20.0)
  green.off()
  print("led verde, desligado...")
  sleep(0.5)
  yellow.on()
  print("led amarelo, ligado!!")
  sleep(10.0)
  yellow.off()
  print("led amarelo, desligado...")
  sleep(0.5)
  red.on()
  print("led vermelho, ligado!!")
  sleep(7.0)
  red.off()
  print("led vermelho, desligado...")
  sleep(0.5)