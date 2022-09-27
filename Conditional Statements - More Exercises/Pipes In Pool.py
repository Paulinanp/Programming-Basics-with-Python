volume_in_meters = int(input())
p1 = int(input())
p2 = int(input())
hours_missing = float(input())

p1_full_for_h = p1 * hours_missing
p2_full_for_h = p2 * hours_missing

total_volume = p1_full_for_h + p2_full_for_h

if total_volume <= volume_in_meters:
    total_volume_in_percent = total_volume / volume_in_meters * 100
    p1_in_percent = p1_full_for_h / total_volume * 100
    p2_in_percent = p2_full_for_h / total_volume * 100

    print(f"The pool is {total_volume_in_percent:.2f}% full."
          f"Pipe 1: {p1_in_percent:.2f}%. Pipe 2: {p2_in_percent:.2f}%.")
else:
    overflow = total_volume - volume_in_meters
    print(f"For {hours_missing} hours the pool overflows "
          f"with {overflow:.2f} liters.")