"""change names"""

def change_names(name):
    name = name.split()
    renamed = ""
    for elements in name:
        if "." not in elements:
            if elements != "of":
                renamed += elements + " "
            if elements == "of":
                break        
    name = renamed
    print(name)
    
change_names("Maria A. G. Italia H. Rodrigez")
change_names("Pythagoras of Samos")