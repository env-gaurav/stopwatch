import time 
def timer(n):
  while 0<n:
      time.sleep(2)
      print("Time left: ",n,"seconds left")
      n-=1
      
timer(10)