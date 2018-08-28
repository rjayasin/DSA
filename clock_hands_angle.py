# given a string time, find the angle between the hands of a clock
# e.g.:
# 03:00 = 90
# 06:00 = 180

# find the degrees of each hand (out of 360) individually and subtract them
# minute hand is just minutes * 6
# hour hand is (hours % 12) * 30 + (30 * (minDegree / 360))

def time_angle(time):
    time = list(map(int, time.split(':')))
    min_degree = time[1] * 6
    h_degree = (time[0] % 12) * 30 + (30 * (min_degree / 360))
    ang = abs(min_degree - h_degree)
    return min(ang, 360 - ang)

if __name__ == '__main__':
    for h in range(1, 13):
        for m in range(0, 60):
            time = str(h) + ':' + str(m)
            print(time + " -> " +str(time_angle(time)))