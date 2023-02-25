import string

def access_to_file(fileName):
    try:
      file = open(fileName)
    except IOError as e:
        print(u'Error opening file!')
    file = open(fileName, 'r')
    read_file = file.read().lower()
    words_in_file = read_file.split() 
    return words_in_file

def text_clear(text):
    for p in string.punctuation + '\n':
        if p in text:
            text = text.replace(p, '')
    return text

def counter(list_element):
    count = {}
    for element in list_element:
        if count.get(element, None):
            count[element] += 1
        else:
            count[element] = 1
    sorted_values = sorted(count.items(), key=lambda tpl: tpl[1], reverse=True)
    return dict(sorted_values)



print("Enter file location or name of file: ")
file = input()
text = access_to_file(file)
list_of_words = text_clear(text)
print('\nList of words in file "', file, '": ')
final_dict = counter(list_of_words)
for item in final_dict:
    print(f"'{item}': {final_dict[item]}")
