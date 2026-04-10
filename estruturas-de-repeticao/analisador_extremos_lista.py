def pontos(n):
    pts = list(map(int, n.split()))
    pts_menor = pts.index(min(pts))
    print(min(pts), end=(" "))
    print(pts_menor)
    print(max(pts), end=(" "))
    pts_maior = pts.index(max(pts))
    print(pts_maior)
    print(n)

n = str(input())
pontos(n)