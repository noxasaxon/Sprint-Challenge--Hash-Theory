def get_indices_of_item_weights(weights, limit):
  packages = {}
  for weight in weights:
    packages[weight] = weight
  
  newLimit = limit
  for weight in packages:
    newLimit -= weight
    if newLimit in packages: return (weights.index(newLimit), weights.index(weight))
    else: newLimit = limit
  return ()

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print(get_indices_of_item_weights([4, 6, 10, 15, 16], 21))