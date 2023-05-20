class Logic():

  def sort(self,array):
    j = 0                                             #1, 2
    while j < len(array)-1:                           #3
      for i in range(len(array)-1,j,-1):              #4
        if array[i-1] > array[i]:                     #5
          array[i-1],array[i] = array[i],array[i-1]
      j += 1                                          #6
    return array

#1 比較を行う要素のインデックスの最小値
#2 この最小値を増やしていくことで、ソート済みの整数とは比較を行わないようにする
#3 最も右にある２つの整数のみが残り、最後の比較となるまで繰りかえす
#4 右の整数のインデックスをiとし、左にシフトして比較を行っていく
#5 左の整数の方が右の整数より大きければ順番を入れ替える
#6 １番左の整数をソート済みとし、比較を行う要素のインデックスの最小値を1増やす
