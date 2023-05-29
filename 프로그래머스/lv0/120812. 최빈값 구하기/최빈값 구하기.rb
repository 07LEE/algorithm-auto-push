def solution(array)
  count_hash = Hash.new(0)
  array.each do |num|
    count_hash[num] += 1
  end

  max_count = count_hash.values.max
  mode_values = count_hash.select { |_key, value| value == max_count }.keys
  return -1 if mode_values.length > 1
  return mode_values[0]
end