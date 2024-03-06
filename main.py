from sense_hat import SenseHat
from time import sleep

s = SenseHat()
s.set_rotation(270, False)
s.low_light == True

# Set up the colour sensor
s.color.gain = 60 # Set the sensitivity of the sensor
s.color.integration_cycles = 64 # The interval at which the reading will be taken

orange = (255,85,14)
white = (235,235,235)
black = (0,0,0)
green= (0,153,0)

K = orange
W = white
O = black
G = green

count = 0
turn = 0
while count < 29 and turn < 2:
  
  img1 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,K,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img2 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,W,
  O,O,O,O,O,O,K,W,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img3 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,W,W,
  O,O,O,O,O,K,W,W,
  O,O,O,O,O,O,O,W,
  O,O,O,O,O,O,O,W,
  O,O,O,O,O,O,O,W,
  O,O,O,O,O,O,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img4 =[
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,W,W,O,
  O,O,O,O,K,W,W,O,
  O,O,O,O,O,O,W,O,
  O,O,O,O,O,O,W,W,
  O,O,O,O,O,O,W,W,
  O,O,O,O,O,O,O,K,
  G,G,G,G,G,G,G,G,
  ] 
  img5 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,W,W,O,O,
  O,O,O,K,W,W,O,O,
  O,O,O,O,O,W,O,O,
  O,O,O,O,O,W,O,O,
  O,O,O,O,O,W,W,W,
  O,O,O,O,O,O,K,O,
  G,G,G,G,G,G,G,G,
  ]
  img6 = [
  O,O,O,O,O,O,O,O,
  O,O,O,W,W,O,O,O,
  O,O,K,W,W,O,O,O,
  O,O,O,O,W,O,O,W,
  O,O,O,O,W,W,W,W,
  O,O,O,O,W,W,W,W,
  O,O,O,O,O,K,O,K,
  G,G,G,G,G,G,G,G,
  ]
  img7 = [
  O,O,O,O,O,O,O,O,
  O,O,W,W,O,O,O,O,
  O,K,W,W,O,O,O,O,
  O,O,O,W,O,O,W,O,
  O,O,O,W,W,W,W,O,
  O,O,O,W,W,W,W,O,
  O,O,O,O,K,O,K,O,
  G,G,G,G,G,G,G,G,
  ]
  img8 = [
  O,O,O,O,O,O,O,O,
  O,W,W,O,O,O,O,O,
  K,W,W,O,O,O,O,O,
  O,O,W,O,O,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,O,K,O,K,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img9 = [
  O,O,O,O,O,O,O,O,
  O,W,W,O,O,O,O,O,
  K,W,W,O,O,O,O,O,
  O,O,W,O,O,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,O,K,O,K,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img10 = [
  O,O,O,O,O,O,O,O,
  O,W,W,O,O,O,O,O,
  K,W,W,O,O,O,O,O,
  O,O,W,O,O,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,O,K,O,K,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img11 = [
  O,O,O,O,O,O,O,O,
  O,O,W,W,O,O,O,O,
  O,O,W,W,K,O,O,O,
  O,O,W,O,O,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,O,K,O,K,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img12 = [
  O,O,O,O,O,O,O,O,
  O,O,W,W,O,O,O,O,
  O,O,W,W,K,O,O,O,
  O,O,W,O,O,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,O,K,O,K,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img13 = [
  O,O,O,O,O,O,O,O,
  O,O,W,W,O,O,O,O,
  O,O,W,W,K,O,O,O,
  O,O,W,O,O,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,O,K,O,K,O,O,
  G,G,G,G,G,G,G,G
  ]
  img14 = [
  O,O,O,O,O,O,O,O,
  O,W,W,O,O,O,O,O,
  K,W,W,O,O,O,O,O,
  O,O,W,O,O,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,W,W,W,W,O,O,
  O,O,O,K,O,K,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img15 = [
  O,O,O,O,O,O,O,O,
  W,W,O,O,O,O,O,O,
  W,W,O,O,O,O,O,O,
  O,W,O,O,W,O,O,O,
  O,W,W,W,W,O,O,O,
  O,W,W,W,W,O,O,K,
  O,O,K,O,K,O,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img16 = [
  O,O,O,O,O,O,O,O,
  W,O,O,O,O,O,O,O,
  W,O,O,O,O,O,O,O,
  W,O,O,W,O,O,O,O,
  W,W,W,W,O,O,O,O,
  W,W,W,W,O,O,K,W,
  O,K,O,K,O,O,O,W,
  G,G,G,G,G,G,G,G,
  ]
  img17 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,W,O,O,O,O,O,
  W,W,W,O,O,O,O,O,
  W,W,W,O,O,K,W,W,
  K,O,K,O,O,O,W,W,
  G,G,G,G,G,G,G,G,
  ]
  img18 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,W,O,O,O,O,O,O,
  W,W,O,O,O,O,O,O,
  W,W,O,O,K,W,W,O,
  K,O,K,O,O,W,W,O,
  G,G,G,G,G,G,G,G,
  ]
  img19 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  W,O,O,O,O,O,O,O,
  W,O,O,O,O,O,O,O,
  W,O,O,K,W,W,O,K,
  K,O,O,O,W,W,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img20 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,K,W,W,O,K,W,
  O,O,O,W,W,O,O,W,
  G,G,G,G,G,G,G,G,
  ]
  img21 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,K,W,W,O,K,W,W,
  O,O,W,W,O,O,W,W,
  G,G,G,G,G,G,G,G,
  ]
  img22 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  K,W,W,O,K,W,W,O,
  O,W,W,O,O,W,W,O,
  G,G,G,G,G,G,G,G,
  ]
  img23 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  W,W,O,K,W,W,O,O,
  W,W,O,O,W,W,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img24 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  W,O,K,W,W,O,O,O,
  W,O,O,W,W,O,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img25 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,K,W,W,O,O,O,O,
  O,O,W,W,O,O,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img26 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  K,W,W,O,O,O,O,O,
  O,W,W,O,O,O,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img27 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  W,W,O,O,O,O,O,O,
  W,W,O,O,O,O,O,O,
  G,G,G,G,G,G,G,G,
  ]
  img28 = [
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  O,O,O,O,O,O,O,O,
  W,O,O,O,O,O,O,O,
  W,O,O,O,O,O,O,O,
  G,G,G,G,G,G,G,G,
  ]

  images = [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,
  img13,img14,img15,img16,img17,img18,img19,img20,img21,img22,img23,img24,
  img25,img26,img27,img28]
  
  rgb = s.color # get the colour from the sensor
  O = (rgb.red, rgb.green, rgb.blue)
  
  s.set_pixels(images[count%len(images)])

  count += 1
  sleep(0.5)
  if count == 28:
    turn += 1
    count = 0
  
s.clear()
