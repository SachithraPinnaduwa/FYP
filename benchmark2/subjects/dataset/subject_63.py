def entrance(n, cache = {}):
  # if the number is in the cache, return it
  if n in cache:
    return cache[n]
  # base case
  elif n <= 1:
    value = n
  # recursive case
  else:
    value = entrance(n-1, cache) + entrance(n-2, cache)
  # store the value in the cache before returning it
  cache[n] = value
  return value