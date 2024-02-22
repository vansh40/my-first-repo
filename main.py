from functools import lru_cache 

@lru_cache(maxsize = 1000)
def recursive_fibonacci(n):
  if(type(n) != int):
      raise TypeError("n should be of integer datatype")
  if(n <= 0):
      raise ValueError("n should be a positive number")
  if n == 1:
      return 1
  elif n == 2:
     return 1
  elif n > 2:
      return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)  

for i in range(1, 1000): 
    print(i, ":", recursive_fibonacci(i+1) / recursive_fibonacci(i)) 

# 1.6180 => Golden Ratio 

    
    # recur(5) => recur(4) + recur(3)
    #          => recur(3) + recur(2) + recur(2) + recur(1)
    #          => recur(2) + recur(1) + recur(2) + recur(2) + recur(1)
    #          => 1 + 1 + 1 + 1 + 1 
    #          => 5
    
