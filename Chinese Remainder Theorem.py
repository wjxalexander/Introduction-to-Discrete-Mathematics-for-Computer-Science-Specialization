# Implement the algorithm to construct the number from the Chinese Remainder Theorem.
def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)
    
def ChineseRemainderTheorem(n1, r1, n2, r2):
  (x, y) = ExtendedEuclid(n1, n2)
  # 𝑛 = 𝑟𝑎⋅ 𝑏𝑦 + 𝑟𝑏⋅ 𝑎x
  print(x,y)
  x0 = r1 * n2 * y + r2 * n1 *x
  product_m_n = n1 * n2 
  print(x0 % product_m_n)
  return (x0 % product_m_n + product_m_n) % product_m_n

print(ChineseRemainderTheorem(686579304, 295310485, 26855093, 8217207))
# print(ChineseRemainderTheorem(7, 1, 10, 3))
