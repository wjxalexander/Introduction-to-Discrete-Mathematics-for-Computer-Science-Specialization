def extended_gcd(a, b): 
    # Base Case 
    if a == 0 :  
        return b,0,1
             
    (gcd,x1,y1) = extended_gcd(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 

    return (gcd,x,y)

def diophantine(a, b, c):
  assert c % extended_gcd(a, b)[0] == 0
  # return (x, y) such that a * x + b * y = c
  (d, x_0, y_0) = extended_gcd(a,b)
  p = c / d
  print(p)
  return (p * x_0, p * y_0)
