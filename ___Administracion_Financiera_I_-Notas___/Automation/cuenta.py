from yaml import full_load, dump

def remove_accents(s:str):
    return s.lower().replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("é","e")

class cuenta: 
    def __init__(self,name:str,cant1:float,cant2:float,db):
        self.name = remove_accents(name)
        self.cant1 = cant1
        self.cant2 = cant2
        # [activo, pasivo, capital]
        self.category = [False, False, False] 
        self.is_circulante = None
        self.db = db
    def sort_category(self):
        if (self.name in [remove_accents(i) for i in self.db["activo"]]):
            self.category[0] = True
        elif (self.name in [remove_accents(i) for i in self.db["pasivo"]]):
            self.category[1] = True
        elif (self.name in [remove_accents(i.lower()) for i in self.db["capital"]]):
            self.category[2] = True 
        else:
            choice = input(f"\"{self.name}\" es activo? (a,p,c,n): ")
            if choice == "a": 
                self.category[0] = True
                self.db["activo"].append(self.name)
            elif choice == "p":
                self.category[1] = True
                self.db["pasivo"].append(self.name)
            elif choice == "c": 
                self.category[2] = True
                self.db["capital"].append(self.name)
            else: 
                print("It's not a valid account.")
    def circulante(self):
        """ sort_category() needs to be executed before this. """
        if (self.category == [False,False,True]):
            self.is_circulante = None
        elif (self.category == [False,False,False]):
            self.is_circulante = None
        else: 
            if (self.name in [remove_accents(i) for i in self.db["circulantes"]]):
                self.is_circulante = True 
            elif (self.name in [remove_accents(i) for i in self.db["no_circulantes"]]):
                self.is_circulante = False
            else: 
                choice = input(f"\"{self.name}\" es circulante? (y,n,nan): ")
                if (choice == "y"):
                    self.is_circulante = True 
                    self.db["circulantes"].append(self.name)
                elif (choice == "n"): 
                    self.is_circulante = False
                    self.db["no_circulantes"].append(self.name)
                else: 
                    pass
    def get_name(self):
        return self.name
    def get_cant1(self):
        return self.cant1
    def get_cant2(self):
        return self.cant2
    def get_category(self):
        return self.category
    def get_is_circulante(self):
        return self.is_circulante
    def __str__(self):
        if (self.category == [1,0,0]):
            s = "activo"
        elif (self.category == [0,1,0]):
            s = "pasivo"
        else: 
            s = "capital"
        return f"{self.name}: {s}, {'circulante' if self.circulante else 'no circulante'}, cant1: {self.cant1}, cant2: {self.cant2}"



