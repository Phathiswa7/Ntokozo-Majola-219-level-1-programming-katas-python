def triangle(triangle_size):
  
  if triangle_size > 0:
    for triangle_counter1 in range(1,triangle_size+1):
   
     print('#'*triangle_counter1)
  elif triangle_size < 0:
    for triangle_counter2 in range(triangle_size,0):
     print('#'*-triangle_counter2)