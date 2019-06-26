def power(N, K): 
  
    if (K == 0): return 1
    elif (int(K % 2) == 0): 
        return (power(N, int(K / 2)) *
               power(N, int(K / 2))) 
    else: 
        return (N * power(N, int(K / 2)) *
                   power(N, int(K / 2))) 
  
# Driver Code 
N = 2; K = 3
print(power(N, K)) 
  
