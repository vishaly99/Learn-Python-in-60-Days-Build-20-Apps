member=input("Add a new member:=")

file=open("../file/members.txt",'r')
existing_members=file.readlines()
print(existing_members)
file.close()

existing_members.append(member +"\n")

file=open("../file/members.txt",'w')
existing_members=file.writelines(existing_members)
file.close()

