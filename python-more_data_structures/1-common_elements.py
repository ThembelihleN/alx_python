#set_1 = { "Python", "C", "Javascript" }
#set_2 = { "Bash", "C", "Ruby", "Perl" }

def common_elements(set_1, set_2):
     element = set_1.intersection(set_2)
     return element
