# given n, return 8n
def timesEight(n):
  return n << 3

def timesSeven(n):
  return (n << 3) - n

print timesEight(3)
print timesSeven(3)