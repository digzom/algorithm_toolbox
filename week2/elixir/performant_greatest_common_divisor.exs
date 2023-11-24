defmodule FindGcd do
  def calc(a, 0, _), do: a

  def calc(a, b) do
    calc(b, rem(a, b))
  end
end

FindGcd.calc(3918848080, 1653264) |> IO.puts()
