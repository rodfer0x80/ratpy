import os

os_info = os.uname()
#print(os_info)

print("name : ", os_info[0])
print("name of machine on network : ", os_info[1])
print("release : ", os_info[2])
print("version : ", os_info[3])
print("machine : ", os_info[4])

