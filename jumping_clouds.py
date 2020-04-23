# Jumping on the Clouds

#PseudoCode:
# 0. Initiate counter
# 1. If cloud.nextnext == True & cloud.nextnext == 0, jump
# 2. If cloud.next == True & cloud.next == 0, jump
# 3. If no cloud.next, end
# 4. Print counter results

def jumping3(arr):
    counter = 0
    print(len(arr))
    a = len(arr)
    b = 0
    while (a - b >= 0) == True:
        if a - b > 2:
            if arr[b + 2] == 0:
                b += 2
                counter += 1
            elif arr[b + 1] == 0:
                b += 1
                counter += 1
            else:
                pass
        elif a - b == 2:
            if arr[b + 1] == 0:
                b += 1
                counter += 1
            else:
                pass
        elif a - b == 1:
            break
        else:
            break
    print(counter)

arrayo = [0, 0, 1, 0, 1, 0, 0, 1]
arrayo_given = [0, 0, 1, 0, 0, 1, 0]
array_given = [0, 0, 0, 1, 0, 0]
jumping3(arrayo_given)



# def jumping(arr):
#     counter = 0
#     print(len(arr))
#     # a = len(arr)
#     while (a - b > 0) == True:
#         if len(arr) - i >= 2:
#             if arr[i + 2] == 0:
#                 print(f"Before jumping, I'm on i{i}")
#                 i += 2
#                 print(f'Double Jump! Now on i{i}')
#                 counter += 1
#                 print(f'Counter = {counter}')
#             elif arr[i + 1] == 0:
#                 print(f"Before jumping, I'm on i{i}")
#                 i += 1
#                 print(f'Single Jump! Now on i{i}')
#                 counter += 1
#                 print(f'Counter = {counter}')
#         elif len(arr) - i == 1:
#             if arr[i + 1] == 0:
#                 print(f"Before jumping, I'm on i{i}")
#                 i += 1
#                 print(f'Single Jump! Now on i{i}')
#                 counter += 1
#                 print(f'Counter = {counter}')
#             else:
#                 counter += 1
#                 print(f'Ended on {i}!')
#                 print(f'Counter = {counter}')
#                 break
#         elif len(arr)- i == 0:
#             break
#
#     print(counter)


# def jumping2(arr):
#     counter = 0
#     print(len(arr))
#     a = len(arr)
#     b = 0
#     while (a - b >= 0) == True:
#         # print('first')
#
#         if a - b > 2:
#             # print('second')
#             # print(f'{b}')
#             # print(f'{arr[b + 2]}')
#
#             if arr[b + 2] == 0:
#                 # print('third')
#
#             # if arr[b + 2] != 1:
#                 # print(f"Before jumping, I'm on i{b}")
#                 b += 2
#                 # print(f'Double Jump! Now on i{b}')
#                 counter += 1
#                 # print(f'Counter = {counter}')
#                 #
#                 # elif arr[b + 1] == 0:
#                 #     # print(f"Before jumping, I'm on i{b}")
#                 #     b += 1
#                 #     # print(f'Single Jump! Now on i{b}')
#                 #     counter += 1
#                 #     # print(f'Counter = {counter}')
#
#             elif arr[b + 1] == 0:
#                 # print(f"Before jumping, I'm on i{b}")
#                 b += 1
#                 # print(f'Single Jump! Now on i{b}')
#                 counter += 1
#                 # print(f'Counter = {counter}')
#             else:
#                 break
#         elif a - b == 2:
#             if arr[b + 1] == 0:
#                 # print(f"Before jumping, I'm on i{b}")
#                 b += 1
#                 # print(f'Single Jump! Now on i{b}')
#                 counter += 1
#                 # print(f'Counter = {counter}')
#
#
#             else:
#
#                 break
#         elif a - b == 1:
#             # print('fourth')
#             # print('here')
#             # print(a)
#             # print(b)
#             # print(b+1)
#             # print(arr[0])
#             # print(arr[b-1])
#             # print(arr[b])
#
#             # if arr[b + 1] == 0:
#             #     print(f"Before jumping, I'm on i{b}")
#             #     b += 1
#             #     print(f'Single Jump! Now on i{b}')
#             #     counter += 1
#             #     print(f'Counter = {counter}')
#             #     print('end')
#             break
#             # else:
#             #     break
#         else:
#             break
#
#     # print(f'Final count {counter}')
#     print(counter)


