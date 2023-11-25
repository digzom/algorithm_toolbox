defmodule Gcd do
  def find(a, 0), do: a

  def find(a, b) do
    a_reminder = rem(a, b)
    find(b, a_reminder)
  end
end

Gcd.find(357, 234) |> IO.puts()
