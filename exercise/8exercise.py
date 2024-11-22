"""with open('bear.txt', 'r') as file:
    todos=file.read()

print(todos)"""


"""with open('essay.txt', 'r') as file:
    content=file.read()
nr_chars = len(content)
print(nr_chars)"""

"""file = open('file.txt', 'w')
file.write('snail')
file.close()

with open('file.txt', 'w') as file:
    file.write('snail')"""

"""languages = ['English', 'German', 'Spanish']
text = ""
for language in languages:
    text = f"the content of the file {language}.txt should be {language}"
    with open(f"../file/{language}.txt", "w") as file:
        file.write(text)

file.close()"""

"""text="";
with open('story.txt','r') as file:
    text=file.read()
    file.close()
with open('story_copy.txt','w') as file:
    file.write(text)
    file.close()"""