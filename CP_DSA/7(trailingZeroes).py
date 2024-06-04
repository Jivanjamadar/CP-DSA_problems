def trail_Zero(n):
    count=0
    power_of_zero=5
    while n >= power_of_zero:
        count +=n//power_of_zero
        power_of_zero *=5
    return count
n=int(input())
print(trail_Zero(n))