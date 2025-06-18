"""
CSE212 
(c) BYU-Idaho
01-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def rotate_list_right(data, amount):
   result = []
   element_index= data.index(amount)
   previous_numbers = data[:element_index]
   following_numbers = data[element_index:]

   result.append(data[element_index])

   for index in range(1, len(following_numbers)):

      result.append(following_numbers[index])

   for index in range(1, len(previous_numbers)):
      result.append(previous_numbers[index])
   
   return result

      

  

print(rotate_list_right([1,2,3,4,5,6,7,8,9],1)) # [9, 1, 2, 3, 4, 5, 6, 7, 8]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],5)) # [5, 6, 7, 8, 9, 1, 2, 3, 4]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],9)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
