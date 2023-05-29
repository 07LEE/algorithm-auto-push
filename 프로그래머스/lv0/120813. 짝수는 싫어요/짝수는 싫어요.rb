def solution(n)
  result = []
  (1..n).step(2) do |num|
    result << num
  end

  return result
end
