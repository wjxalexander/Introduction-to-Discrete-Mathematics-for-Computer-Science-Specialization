# Extended Euclid’s algorithm ax + by = d
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

def divide(a, b, n):
  assert n > 1 and a > 0 and extended_gcd(a, n)[0] == 1
  (d, t, s) = extended_gcd(a, n) 
  # nt + as = 1
  print(t, s)
  reverse_t = t % n
  print(reverse_t)
  # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
  return reverse_t * b % n
print(divide(2,7,9))
# divide(5,2,6)