#   * * * * * * *
#   *           *
#   *           *
#   * * * * * * *

for  i in range(4):
    for j in range(7):
        if i==0 or i==3 or j==0 or j==6:
            print('*',end=' ')
        else:
            print(" ", end=" ")

    print()


# for i in range(4):
#     for j in range(7):
#         if i==0 or i==3 or j==0 or j==6:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#         X-axis (j)
#      0  1  2  3  4  5  6
#    ┌───────────────────────
# Y 0│  *  *  *  *  *  *  *
#   1│  *  *  *  *  *  *  *
#   2│  *  *  *  *  *  *  *
#   3│  *  *  *  *  *  *  *
#    ↓

# for i in range(4):
#     for j in range(7):
#         if i == 0 or i == 3 or j == 0 or j == 6:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()