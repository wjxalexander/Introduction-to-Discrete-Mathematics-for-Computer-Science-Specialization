import sys, threading
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
def ConvertToInt(message_str):
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]

def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
          return b
        else:
          return b * a % mod

def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

#which takes coprime integers aa and nn as inputs and returns integer bb such that ab = 1 mod n`
def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b

def Encrypt(message, modulo, exponent):
  # Fix this implementation
  return PowMod(ConvertToInt(message), exponent, modulo) # cipher = exp(m,e) mod n

def Decrypt(ciphertext, p, q, exponent):
  d = InvertModulo(exponent ,(p-1)*(q-1))
  return ConvertToStr(PowMod(ciphertext, d, p * q))  # exp(cipher, d) = m mod n
# a = 3
# b = 7
# c = InvertModulo(a, b)
# print(c)

# p = 1000000007
# q = 1000000009
# exponent = 23917
# modulo = p * q
# ciphertext = Encrypt("attack", modulo, exponent)
# message = Decrypt(ciphertext, p, q, exponent)
# print(message)

def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
  # Fix this implementation
  for message in potential_messages:
    if ciphertext == Encrypt(message, modulo, exponent):
      return potential_messages[0]
  return "don't know"

# small prime < 100000
def GetPrimes(n):
    #""" Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def DecipherSmallPrime(ciphertext, modulo, exponent):
  primes = GetPrimes(1000000)
  for prime in primes:
    if modulo % prime == 0:
      small_prime = prime
      big_prime = modulo // small_prime
      return Decrypt(ciphertext, small_prime, big_prime, exponent)
  return "don't know"

def IntSqrt(n):
  low = 1
  high = n
  iterations = 0
  while low < high and iterations < 5000:
    iterations += 1
    mid = (low + high + 1) // 2
    if mid * mid <= n:
      low = mid
    else:
      high = mid - 1
  return low

# sqrt(n) - r < p <sqart(n)
def DecipherSmallDiff(ciphertext, modulo, exponent):
  for number in range(IntSqrt(modulo)-5000, IntSqrt(modulo)+1):
    if(modulo % number == 0):
      small_prime = number
      big_prime = modulo // number
      break
  return Decrypt(ciphertext, small_prime, big_prime, exponent)


def GCD(a, b):
  if b == 0:
    return a
  return GCD(b, a % b)

def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent):
  # Fix this implementation to correctly decipher both messages in case
  # first_modulo and second_modulo share a prime factor, and return
  # a pair (first_message, second_message). The implementation below won't work
  # if the common_prime is bigger than 1000000.
  common_prime = GCD(first_modulo, second_modulo)
  q1 = first_modulo // common_prime
  q2 = second_modulo // common_prime
  return (Decrypt(first_ciphertext, common_prime, q1, first_exponent), Decrypt(second_ciphertext, common_prime, q2, second_exponent))
