def permute(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms

print("*** Fun with permute ***")
num_list = [int(e) for e in input("input : ").split(',')]
print("Original Cofllection:  " + str(num_list))
print("Collection of distinct numbers:\n",permute(num_list))
