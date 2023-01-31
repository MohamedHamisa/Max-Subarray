# O(n): iterate array only once, adding 
# max(prev + current, current) to sums array
# Add all positive numbers to subsequence total
# If no positive numbers, then subsequence = maxValue

def maxSubarray(arr):
    sums = [arr[0]] 
    subsequence = arr[0] if arr[0] > 0 else 0
    
    for idx in range(1, len(arr)):
        sums.append(max(sums[idx - 1] + arr[idx], arr[idx]))
        if arr[idx] > 0: subsequence += arr[idx]
    
    maxValue = max(sums)
    return [maxValue, subsequence if maxValue > 0 else maxValue]

