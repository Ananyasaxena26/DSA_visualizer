def quick_sort_steps(arr):
    steps = []
    a = arr.copy()

    def partition(l, r):
        pivot = a[r]
        i = l - 1
        for j in range(l, r):
            steps.append((a.copy(), j, r))  # show comparison with pivot
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                steps.append((a.copy(), i, j))  # show swap
        a[i + 1], a[r] = a[r], a[i + 1]
        steps.append((a.copy(), i + 1, r))  # pivot swap
        return i + 1

    def qs(l, r):
        if l >= r:
            return
        p = partition(l, r)
        qs(l, p - 1)
        qs(p + 1, r)

    qs(0, len(a) - 1)
    return steps
