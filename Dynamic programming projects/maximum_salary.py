def Maximum_salary():
    result = []
    n = int(input())
    digits = list(map(int, input().split()))
    
    while digits:
        
        best_possible = 0
        for digit in digits:
            
            if int(str(digit)[0]) == int(str(best_possible)[0]) and len(str(digit)) < len(str(best_possible)):      
                i = 1
                while i <= len(str(digit)) - 1:
                    if int(str(digit)[i]) > int(str(best_possible)[i]):
                        best_possible = digit
                        break
                    elif int(str(digit)[i]) < int(str(best_possible)[i]):
                        break
                    i += 1
                if i == len(str(digit)):
                    best_possible = digit
            elif int(str(digit)[0]) == int(str(best_possible)[0]) and len(str(digit)) > len(str(best_possible)):
                i = 1
                while i < len(str(best_possible)) - 1:
                    if int(str(digit)[i]) > int(str(best_possible)[i]):
                        best_possible = digit
                        break
                    elif int(str(digit)[i]) < int(str(best_possible)[i]):
                        break
                    i += 1
            elif digit > best_possible:
                best_possible = digit

        result.append(best_possible)
        digits.remove(best_possible)
    
    return "".join(list(map(str, result)))
print(Maximum_salary())
                