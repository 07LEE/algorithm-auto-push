def solution(array)
  sorted_array = array.sort
  mid_index = sorted_array.length / 2
  return sorted_array[mid_index]
end