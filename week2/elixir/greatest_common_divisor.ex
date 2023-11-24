a = 3918848
b = 1653264

best = Enum.find((a + b)..1, fn d -> rem(a, d) == 0 and rem(b, d) == 0 end)

IO.puts(best)

