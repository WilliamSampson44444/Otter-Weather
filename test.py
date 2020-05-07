

# class Student:
#     """A class to define a student"""
#     def __init__(self, otter_id, f_name, l_name):
#         self.otter_id = otter_id
#         self.f_name = f_name
#         self.l_name = l_name

#     def __str__(self):
#         return f'{self.l_name}, {self.f_name}'

#     def __eq__(self, other):
#         return self.otter_id == other.otter_id

# student_a = Student(76, 'Zora', 'Neale')

# student_b = Student(47, 'Zora', 'Neale')


amst_list = ["Amsterdam", "Netherlands", "books", "library", "museum"]

def wordist(s):
    if s[1] == s[4]:
        return True
    else:
        return False

result_list2 = list(filter(wordist, amst_list))

print(result_list2) 