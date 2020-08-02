
def prim_calc(n):
    min_num_ops = [n]*n
    min_num_ops[0] = 0
    ops = [1, 2, 3]
    
    for i in range(n-1):
        
        for op in ops:
            if op == 1:
                n_tmp = (i + 1) * 3
            elif op == 2:
                n_tmp = (i + 1) * 2
            elif op == 3:
                n_tmp = (i + 1) + 1
            
            num_ops = min_num_ops[i] + 1
            idx = n_tmp - 1
            if n_tmp <= n and num_ops < min_num_ops[idx]:
                min_num_ops[idx] = num_ops
                
    return min_num_ops

# print(prim_calc(28))