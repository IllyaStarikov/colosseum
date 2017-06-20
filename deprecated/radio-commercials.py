def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

_, cost = [int(x) for x in input().split(' ')]
values = [int(x) - cost for x in input().split(' ')]

print(max_subarray(values))