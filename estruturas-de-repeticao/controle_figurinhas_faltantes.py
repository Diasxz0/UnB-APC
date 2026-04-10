total = int(input())
have = int(input())

fig = []

for i in range(have):
    fig.append(int(input()))

conjunto = set(fig)



print(f"{total-(len(conjunto))}")
