nums1 = [12,7,5,64,-14]
print("Original numbers in the list: ",nums1)
nums2 = [12,14,-95,3]
print("Original numbers in the list: ",nums2)
new_nums1=list(filter(lambda x: x>0,nums1))
new_nums2=list(filter(lambda x: x>0,nums2))
print("positive numbers in the list",new_nums1)
print("positive numbers in the list",new_nums2)
