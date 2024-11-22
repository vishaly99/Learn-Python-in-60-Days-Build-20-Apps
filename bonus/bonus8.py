# date=input("Enter today's date:=")
# mood=input("How do you rate your mood today from 1 to 10? ")
# journal=input("Let your thoughts flow: \n")
#
# with open(f"../file/{date}.txt","w") as file:
#     file.write(mood+"\n")
#     file.write(journal)
# file.close()

user_action="add 8"
if 'add' in user_action:
    text=int(user_action.replace("add","").strip(" "))
    print(text)
print("Hi Vishal")