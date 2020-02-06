'''
Question 412: FizzBuzz: Easy 
URL: https://leetcode.com/problems/fizz-buzz/
'''
class Solution:
    def fizzBuzz(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]