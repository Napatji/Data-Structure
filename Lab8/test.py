# if not root:
#             return
#         left = root.left
#         right = root.right
#         if self.checkChild(left) == False and self.checkChild(right) == False:
#             temp_L = left.data
#             temp_R = right.data
#             root.data = int(min(temp_L,temp_R))
#             left.data = int(temp_L) - int(min(temp_L,temp_R))
#             right.data = int(temp_R) - int(min(temp_L,temp_R))
#         if self.checkChild(left) == True and self.checkChild(right) == True:
#             left = self.subtract(left)
#             right = self.subtract(right)
#             temp_L = left.data
#             temp_R = right.data
#             root.data = int(min(temp_L,temp_R))
#             left.data = int(temp_L) - int(min(temp_L,temp_R))
#             right.data = int(temp_R) - int(min(temp_L,temp_R))
#         if self.checkChild(left) == True and self.checkChild(right) == False:
#             left = self.subtract(left)
#             temp_L = left.data
#             temp_R = right.data
#             root.data = int(min(temp_L,temp_R))
#             left.data = int(temp_L) - int(min(temp_L,temp_R))
#             right.data = int(temp_R) - int(min(temp_L,temp_R))
#         if self.checkChild(left) == False and self.checkChild(right) == True:
#             right = self.subtract(right)
#             temp_L = left.data
#             temp_R = right.data
#             root.data = int(min(temp_L,temp_R))
#             left.data = int(temp_L) - int(min(temp_L,temp_R))
#             right.data = int(temp_R) - int(min(temp_L,temp_R))
#         # else:
#         #     if self.checkChild(left) == True:
#         #         self.subtract(left)
#         #     if self.checkChild(right) == True:
#         #         self.subtract(right)
#         return root