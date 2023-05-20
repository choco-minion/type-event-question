class Logic():

  def sort(self,x):
    j = 1
    while j < len(x):
      m = x[j]
      for i in range(j-1,-1,-1): 
        if x[i] > m:
          x[i+1] = x[i]
          if i == 0:
            x[0] = m
        else:
          x[i+1] = m
          break
      j += 1
    return x
