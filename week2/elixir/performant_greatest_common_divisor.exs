defmodule Gcd do
  def find(a, 0), do: a

  def find(a, b) do
    a_reminder = rem(a, b)
    find(b, a_reminder)
  end
end

time_before = Time.utc_now()

Gcd.find(3918848080, 1653264) |> IO.puts()

time_after = Time.utc_now()

Time.diff(time_after, time_before, :millisecond) |> IO.puts()
