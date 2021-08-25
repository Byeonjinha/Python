import sys

n = int(sys.stdin.readline())
sorted_location = []
data_dict = []




for _ in range(n):
    x, y, z = list(map(int, sys.stdin.readline().split()))
    sorted_location.append((x, y, z))
sorted_location.sort()


def get_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2]-b[2]) ** 2


def solution(l, r):
    if l == r:
        return float('inf')
    else:
        m = (l + r) // 2
        min_dist = min(solution(l, m), solution(m + 1, r))
        target_list = []

        for i in range(m, l - 1, -1):
            if (sorted_location[i][0] - sorted_location[m][0]) ** 2 < min_dist:
                target_list.append(sorted_location[i])
            else:
                break

        for j in range(m + 1, r + 1):
            if (sorted_location[j][0] - sorted_location[m][0]) ** 2 < min_dist:
                target_list.append(sorted_location[j])
            else:
                break

        target_list.sort(key=lambda x: x[1])
        for i in range(len(target_list) - 1):
            for j in range(i + 1, len(target_list)):
                if (target_list[i][1] - target_list[j][1]) ** 2 < min_dist:
                    dist = get_dist(target_list[i], target_list[j])

                    if min_dist >= dist:
                        min_dist = dist
                        data_dict.append(str(dist) + str(target_list[i]) + str(target_list[j]))


                else:
                    break
        return (min_dist)


if len(sorted_location) != len(set(sorted_location)):
    print(0)
else:
    print((solution(0, len(sorted_location) - 1)))

P=[]
for AV in list(set(data_dict)):
    Ppp=int((AV.split("(")[0]))
    P.append(Ppp)
P.sort()
print(P.count(P[0]))
