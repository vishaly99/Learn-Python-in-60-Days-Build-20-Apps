contents=["All carrots are to be sliced longitudinally.","The carrots were reportdely sliced","The slicing process was well presentation"]
filenames=["doc.txt","report.txt","presentation.txt"]

for content, filename in zip(contents,filenames):
    file=open(f"../file/{filename}","w")
    file.write(content)

