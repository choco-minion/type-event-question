class Logic():

  def sort(self,x):
    j = 0
    while j < len(x)-2:
      for i in range(len(x)-1,j,-1): 
        if x[i-1] > x[i]:
          x[i-1],x[i] = x[i],x[i-1]
      if x[j] == min(x[j:]):
        j += 1
    return x
