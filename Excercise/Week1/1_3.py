import math

hour_in, minute_in, hour_out, minute_out = [int(e) for e in input().split()]
cost = 0

duration = ((hour_out - hour_in) * 60) + (minute_out - minute_in)
duration_hour = math.ceil(duration/60)

if (7 <= hour_in <= 23 and 7 <= hour_out <= 23) and hour_out >= hour_in:
    if duration <= 15:
        cost = 0
    elif duration_hour < 4:
        cost = math.ceil(duration/60) * 10
    elif duration_hour < 6:
        cost = 30 + ((duration_hour - 3) * 20)
    elif duration >= 360:
        cost = 200
    print(cost)