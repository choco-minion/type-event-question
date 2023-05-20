class Logic():

  def sort(self,x):
    m = len(x)//2
    while m >= 1:
      for i in range(m):
        j = i + m
        while j < len(x):
          n = x[j]
          for k in range(j-m,-1,-m):
            if x[k] > n:
              x[k+m] = x[k]
              if k < m:
                x[k] = n
            else:
              x[k+m] = n
              break
          j += m
      m //= 2
    return x
