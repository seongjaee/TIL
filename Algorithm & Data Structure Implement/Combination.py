def combination(arr, k):
    res = []
    temp = []

    def generate(level):
        if len(temp) == k:
            res.append(tuple(temp))
            return

        for i in range(level, len(arr) - (k - len(temp) - 1)):
            temp.append(arr[i])
            generate(i + 1)
            temp.pop()

    generate(0)
    return res


print("\n" + "#" * 30)
print("Combination")
print(combination([1, 2, 3, 4, 5, 6], 3))


def permuation(arr, k):
    res = []
    temp = []
    visited = [False] * len(arr)

    def generate():
        if len(temp) == k:
            res.append(tuple(temp))
            return

        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                temp.append(arr[i])
                generate()
                temp.pop()
                visited[i] = False

    generate()
    return res


print("\n" + "#" * 30)
print("Permuation")
print(permuation([1, 2, 3, 4, 5, 6], 2))


def combiantion_with_replacement(arr, k):
    res = []
    temp = []

    def generate(level):
        if len(temp) == k:
            res.append(tuple(temp))
            return

        for i in range(level, len(arr)):
            temp.append(arr[i])
            generate(i)
            temp.pop()

    generate(0)
    return res


print("\n" + "#" * 30)
print("Combiantion_with_replacement")
print(combiantion_with_replacement([1, 2, 3, 4, 5], 2))


def permutation_with_replacement(arr, k):
    res = []
    temp = []

    def generate():
        if len(temp) == k:
            res.append(tuple(temp))
            return

        for i in range(len(arr)):
            temp.append(arr[i])
            generate()
            temp.pop()

    generate()
    return res


print("\n" + "#" * 30)
print("Permutation_with_replacement")
print(permutation_with_replacement([1, 2, 3, 4], 2))


def subset(arr):
    res = []
    n = len(arr)
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if i & (1 << j):
                temp.append(arr[j])
        res.append(tuple(temp))

    return res


print("\n" + "#" * 30)
print("Subset")
print(subset(["a", "b", "c"]))
