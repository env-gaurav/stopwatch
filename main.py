import time

def timer(n):
  while 0<n:
      time.sleep(1)
      print("Time left:",n,"seconds left")
      n-=1
  print("Time's Up")
      
try:
   seconds=int(input("Enter Number In Seconds: "))
   timer(seconds)
except:
   print("Invalid Input")