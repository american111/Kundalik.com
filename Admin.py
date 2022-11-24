class Admin: 
    def __init__(self,ism,familiya,parol): 
        self.ism = ism 
        self.familiya = familiya 
        self.parol = parol 
 
    
    def true(self): 
        import random 
        sinf = {'ona_tili':random.randint(2,5), 
                'matem':random.randint(2,5), 
                'english':random.randint(2,5), 
                'ruskiy':random.randint(2,5)} 
 
        s = input('Ismingizni kiriting: ').capitalize() 
        c = input('Familiyangizni kiriting: ').capitalize() 
        if s == self.ism and c == self.familiya: 
            d = int(input('Parolingizni kiriting: ')) 
            if d == self.parol: 
                print(f'Sizning baholaringiz\n{sinf}') 
            else: 
                print('Sizning parolingiz noto`g`ri') 
        else: 
            print('Bizda bunday shaxs yo`q') 
 
 
 
 
z = Admin('Bobur','Anvarjonov',1122) 
 
z.true()
