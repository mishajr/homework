# with open("test.txt","r") as File1:
#     lines_file1 = set(File1.readlines())
    
# with open("text.txt","r") as File2:
#     lines_file2 = set(File2.readlines())
    



# line_file1 = lines_file1 - lines_file2
# line_file2 = lines_file2 - lines_file1

# if line_file1 == line_file2:
#     print("Рядки у файлів співпадають.")
# else:
#     print("Рядки, які не співпадають у першому файлі:")
#     print("\n".join(line for line in line_file1))

#     print("\nРядки, які не співпадають у другому файлі:")
#     print("\n".join(line for line in line_file2))

# =============================================================================================================





# def calculate_statistics(text):

#     num_characters = len(text)


#     num_lines = len(text.split('\n'))


#     vowels = "aiouAIOU"
#     num_vowels = sum(1 for char in text if char in vowels)

#     consonants = "bcdfghjklmnpqrstvwxyBCDFGHJKLMNPQRSTVWXY"
#     num_consonants = sum(1 for char in text if char in consonants)


#     num_digits = sum(1 for char in text if char.isdigit())

#     return num_characters, num_lines, num_vowels, num_consonants, num_digits



# with open("test.txt","r+") as File1:
#     text_content = File1.read()
#     statistics = calculate_statistics(text_content)

    
# with open("text.txt","w+") as File2:

#     File2.write(f"Number of characters: {statistics[0]}\n")
#     File2.write(f"Number of lines: {statistics[1]}\n")
#     File2.write(f"Number of vowels:{statistics[2]}\n")
#     File2.write(f"The number of consonant letters: {statistics[3]}\n")
#     File2.write(f"Number of digits: {statistics[4]}\n")


# =============================================================================================================





# with open("test.txt","r") as File1:
#     lines = File1.readlines()
#     lines.pop()     
    
    
# with open("text.txt","w") as File2:
#     File2.writelines(lines)
    
    
    

# =============================================================================================================

# with open("test.txt","r+") as File1:
#     lines = File1.readlines()
#     print(max(len(i) for i in lines))
        

    
# =============================================================================================================

# words = input("enter your words :")



# with open("test.txt","r+") as File1:
#     contents_split =  File1.read().split(" ")


# print(contents_split.count(words))

        
# =============================================================================================================



# with open("test.txt","r+") as File1:
#     content = File1.read().lower()
    


# words_SEARCH = input("enter your words search :")
# words_replace = input("enter your words replace :")

# print(content.replace(words_SEARCH,words_replace))