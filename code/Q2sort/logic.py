class Logic():

  def sort(self,array):
    j = 1                           #1
    while j < len(array):           #2
      m = array[j]                  #3
      for i in range(j-1,-1,-1):    #4
        if array[i] > m:            #5
          array[i+1] = array[i]
          if i == 0:                #6
            array[0] = m
        else:                       #7
          array[i+1] = m
          break
      j += 1
    return array

#1 代入を行う要素のインデックス
#2 最も右の整数の代入が終わるまで繰りかえす
#3 代入を行う整数の値を保存
#4 代入する整数と比較を行う整数のインデックスをiとし、左にシフトして比較を行っていく
#5 比較した整数の方が大きければ、その整数のインデックスを1増やす
#6 代入する値が最も小さければ配列の1番最初に代入する
#7 比較した整数の方が小さければ、その整数の後ろに代入する
