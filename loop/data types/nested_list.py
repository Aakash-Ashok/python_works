li=[
    [1,2],
    [4,50],
    [50,45],
    [5,6]
]

# for sbli in li:
#     for num in sbli:
#         print(num)


# for sbli in li:
    # for num in sbli:
    #     if num>5:
    #         print(num)

# all_num=[num for suli in li for num in suli]
# print(all_num)

# div_num=[num for suli in li for num in suli if num>5]
# print(div_num)
# for sbli in li:
#     for num in sbli:
#         if num>5:
#             print(num+1)
#         elif num<5:
#             print(num-1)
#         else:
#             print(num)



lii = [num+1 if num>5 else num-1 if num<5 else num for sbli in li for num in sbli]
print(lii)
