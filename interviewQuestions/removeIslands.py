input = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1], 
]
def removeIslands(matrix):
  # 1 -> black
  # 0 -> white
  # 'XY' -> X = col idx, Y = row idx
  # [true, ['03', '13']] -> '03' is connected to '13', all connected to edge
  # [false, ['11']] -> '11' isnt connected to edge

  adj_list = []

  for i, row in enumerate(matrix):
    for j, col in enumerate(row):
      print(i)
      print(j)

removeIslands(input)
