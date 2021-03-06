#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np

def solve_linear_equation(A, b):
    Arank=np.linalg.matrix_rank(A)
    Combine=np.hstack((A,b))
    Combinerank=np.linalg.matrix_rank(Combine)
    if (Arank!=Combinerank):
       return -1
    elif(Arank==Combinerank):
        if (Arank==3):
            return 1
        else:
            return 0

def flag_to_message(flag):
   if flag == 1:
     print('The linear system Ax=b has only one solution.')
   elif flag == 0:
     print('The linear system Ax=b has infinitely many solutions.')
   elif flag == -1:
     print('The linear system Ax=b has no solutions.')
   else:
     print('Unknown flag!')

def get_input_data(input_id):
   if input_id == 'case1': 
     A = np.array([[3, 2, -1], [6, -1, 3], [1, 10, -2]])
     b = np.array([[-7], [-4], [2]])
   elif input_id == 'case2':
     A = np.array([[4, -1, 3], [21, -4, 18], [-9, 1, -9]])
     b = np.array([[5], [7], [-8]])
   elif input_id == 'case3':
     A = np.array([[7, -4, 1], [3, 2, -1], [5, 12, -5]])
     b = np.array([[-15], [-5], [-5]])
   return A, b

if __name__ == '__main__':
   for case in ['case1', 'case2', 'case3']:
     A, b = get_input_data(case)
     print(case)
     print('A =', A, 'b =', b.T)
     flag = solve_linear_equation(A, b)
     flag_to_message(flag)
     if flag == 1:
       print('The solution is ', np.linalg.solve(A, b))
     print()


# In[1]:


# Can we use np.linalg.solve() to determine whether ðð±=ð is consistent? Explain the reason for your answer. (5%)
# Write down your answer here.
ç¡æ³ï¼å çºç¡è§£èç¡éå¤è§£å¤æ·ä¸åºä¾ï¼åªè½å¤æ·åºå®ä¸è§£çç­æ¡


# In[ ]:


# Given matrix ð of dimension (m,n). If rank(ð)=ð, can we infer that ðð±=ð is consistent? Explain the reason for your answer. (5%)
# Write down your answer here.
åæ±ºæ¼m>n or m<n å®ç´RANK(A)=nç¡æ³å¤æ·æ¯å¦æè§£

