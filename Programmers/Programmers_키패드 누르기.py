def solution(numbers, hand):
    answer = []

    left_key = [1, 4, 7, '*']
    right_key = [3, 6, 9, '#']
    center_key = [2, 5, 8, 0]
    
    left_p = '*'
    right_p = '#'
    
    
    for i in range(len(numbers)):
        if numbers[i] in left_key:
            left_p = numbers[i]
            answer.append("L")
        elif numbers[i] in right_key:
            right_p = numbers[i]
            answer.append("R")
            
        elif numbers[i] in center_key:
            if left_p in left_key:
                left_cha = abs(left_key.index(left_p) - center_key.index(numbers[i]))+1
            elif left_p in center_key:
                left_cha = abs(center_key.index(left_p) - center_key.index(numbers[i]))  
                
            if right_p in right_key:
                right_cha = abs(right_key.index(right_p) - center_key.index(numbers[i]))+1
            elif right_p in center_key:
                right_cha = abs(center_key.index(right_p) - center_key.index(numbers[i]))
            
                    
            print(i,numbers[i], left_p, left_cha, right_cha)
            if left_cha == right_cha:
                if hand == 'right':
                    answer.append('R')
                    right_p = numbers[i]
                if hand == 'left':
                    answer.append('L')
                    left_p = numbers[i]
                                
            elif left_cha < right_cha:
                answer.append('L')
                left_p = numbers[i]
            elif left_cha > right_cha:
                answer.append('R')
                right_p = numbers[i]
                
    answer = ''.join(answer)
    print(answer)
    return answer