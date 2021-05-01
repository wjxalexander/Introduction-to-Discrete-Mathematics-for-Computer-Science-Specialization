
def FastModularExponentiation2K(b, k, m):
  # your code here
  if(k == 0): return b % m
  ret = FastModularExponentiation(b, k -1, m)
  return ret * ret % m #b^k-1 * b^k-1 mod m


def decimalToBinary(n):
  return bin(n).replace("0b", "")
  
def generateModTable(length, b, m):
  ret = [b%m]
  while(length > 1):
    ret.append(ret[-1] * ret[- 1] % m)
    length -=1
  return ret
    
def reverse(string):
    string = string[::-1]
    return string

def FastModularExponentiation(b, e, m):
  # your code here
  binary_string = decimalToBinary(e)
  binary_string_length = len(binary_string)
  factor_two_mod_table = generateModTable(binary_string_length,b,m)
  revere_binary_string = reverse(binary_string)
  ret = 1
  for i in range(len(revere_binary_string)):
    if(revere_binary_string[i] == '1'): 
      ret *= factor_two_mod_table[i]
  return ret % m

print(FastModularExponentiation(7,1,11))
