# f = open('newfile.txt', 'w')
# f.write('Hello')
# f.close()

'''
If we use 'w' and replace Hello with World, the file will be overriden

'''
# f = open('newfile.txt', 'w')
# f.write('World')
# f.close()

'''
To avoid overriding the file we need to use 'a' (from append) instead of 'w'
'''

# f = open('newfile.txt', 'a')
# f.write('World')
# f.close()

'''
But note that now of the words are added after each other without line break.. so we will need to add \n after each word 
'''

# f = open('newfile.txt', 'a')
# f.write('World\n')
# f.close()

'''
We can also use the method writelines() to add several strings
'''
# f = open('newfile.txt', 'a')
# lines = ["Hola","que","tal","stas?"]
# f.writelines(lines)
# f.close()

'''
Again we see that there are no breaks between words.. we can fix this by adding \n after each string
'''

# f = open('newfile.txt', 'a')
# lines = ["Hola\n","que\n","tal\n","stas?\n"]
# f.writelines(lines)
# f.close()

'''
But there is a better way to add line breaks
'''
f = open('newfile.txt', 'a')
lines = ["Hola","que","tal","stas?"]
text = '\n'.join(lines)
f.writelines(text)

f.close()