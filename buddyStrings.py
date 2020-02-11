# class Solution:
#     def buddyStrings(self, A, B):
        
#         if len(A) != len(B):
#             return False
        
#         if A == B and len(A) == 2 and A[0] == B[1]:
#             return True

#         str_a, str_b = [], []
#         for ch_a, ch_b in zip(A,B):
#             if ch_a == ch_b:
#                 continue
#             else:
#                 str_a.append(ch_a)
#                 str_b.append(ch_b)
        
#         return self.isReverse(str_a, str_b)
    
#     def isReverse(self, a, b):
#         if a[::-1] == b and len(a) == 2:
#             return True
#         return False

class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B) or set(A) != set(B):
            return False
        
        if A == B:
            return len(A) - len(set(A)) >= 1
        
        counter, indices = 0, []
        
        for i in range(len(A)):
            if A[i] != B[i]:
                indices.append(i)
                counter += 1
            
            if counter > 2:
                return False
            
        return A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]
        

        
        
        
        # for i in range(0, len(A)-1):
        #     for j in range(i+1, len(A)):
        #         A[i], A[j] = A[j], A[i]
        #         # print("{}<-->{}".format(A,B))
                
        #         if A == B:
        #             return True
        #         else:
        #             A[i], A[j] = A[j], A[i]
        
        # return False
            
    
    # def swap(self, list, a, b):
        
        
            
        


sn = Solution()
print(sn.buddyStrings(['a','a','a','a','a','a','c','b'], ['a','a','a','a','a','a','b','c']))