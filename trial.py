

with open('kohanpic.jpg','rb') as rf:
   with open('image.jpg','wb') as wf: 
        size_to_read = 4096
        rf_contents = rf.read(size_to_read)

        while len(rf_contents) > 0:
            wf.write(rf_contents)
            rf_contents = rf.read(size_to_read)


