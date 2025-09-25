# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 2. Running Total with Reset
# Track a running total of values. If a negative number is added, reset the total to 0.
# Input: [5, 7, -1, 3, 2]
# Output: [5, 12, 0, 3, 5]

def running_total_with_reset(nums):
    result = []
    total = 0
    for num in nums:
        if num < 0:
            total = 0
        else:
            total += num
        result.append(total)
    return result



print(running_total_with_reset([5, 7, -1, 3, 2]))   
print(running_total_with_reset([]))                 
print(running_total_with_reset([10]))               
print(running_total_with_reset([-5]))               
print(running_total_with_reset([1, 2, 3]))          
print(running_total_with_reset([2, -1, 2, -1, 2]))

# For this challenge I decided to use a list to store the running totals as I went through each number in the input. A list is a good choice because it allows me to collect the results in order and then return them exactly as required. Adding values to a list is very fast, and it keeps the solution simple and easy to understand. I only needed to keep track of the current total and update it as I moved through the numbers.

# The thirty minute time limit shaped the way I approached this problem. I knew that I needed to find the most direct solution without overthinking it. My main focus was to write something clear that would work for normal cases and edge cases. Because of the time pressure I avoided more advanced structures and stuck with the most straightforward method that I was comfortable with. This gave me more time to test different inputs and make sure the output was correct.

# There were some trade-offs in this approach. The function works well for lists of numbers but it does not handle situations where the input might include other data types or be given in the wrong format. If I had more time I could add checks to make the function safer and more flexible. Another limitation is that it only resets when it sees a negative number, which is exactly what the problem asked for, but it may not be useful if the rules changed. Overall I balanced speed and correctness, and I think the solution shows how to stay focused under a strict time limit.
