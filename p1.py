Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def isIsomorphic(str1, str2):          
    dict_str1 = {}
    dict_str2 = {}
    
    for i, value in enumerate(str1):
        dict_str1[value] = dict_str1.get(value, []) + [i]
            
    for j, value in enumerate(str2):
        dict_str2[value] = dict_str2.get(value, []) + [j]
    
    if sorted(dict_str1.values()) == sorted(dict_str2.values()):
        return True
    else:
        return False

print(isIsomorphic("egg", "add"));         
print(isIsomorphic("foo", "bar"));      
print(isIsomorphic("paper", "title"));   
print(isIsomorphic("fry", "sky"));
print(isIsomorphic("apples", "apple"));