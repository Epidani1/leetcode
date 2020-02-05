'''
Question 929: Unique Email Addresses: Easy 
URL: https://leetcode.com/problems/unique-email-addresses/
'''
class Solution:
    def numUniqueEmails(self, emails):
        real = set()
        for email in emails:
            x= email.split('@')
            y = x[0].split('+')
            z = y[0].replace('.', '')
            real.add(z + '@' + x[1])
        return len(real)
            