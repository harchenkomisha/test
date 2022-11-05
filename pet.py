class Pet:
    """Виртуальный питомец"""

    total = 0
    @staticmethod   
    def status():
        print("Общее число зверюшек", Pet.total)

    def __init__(self, name, hunger = 0, boredom = 0):
            self.__name = name
            self.hunger = hunger
            self.boredom = boredom
            
        
    def talk(self):
        print("Меня зовут",self.__name,
             ",я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self, food = 4):
        print("Ммм....... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Уиии!")
        self.boredom -= fun
        if self.borendom < 0:
            self.borendom =0
        self.__pass_time()



    def __str__(self):
        ans = "Обьект класса Pet\n"
        ans += "имя: " + self.name + "\n"
        return ans
@property
def mood(self):
    unhappiness = self.hunger + self.borendom 
    if unhappiness < 5:
        m = 'прекрасно'
    elif 5 <= unhappiness <= 10:
        m = 'неплохо'
    elif 11 <= unhappiness <= 15:
        m = 'не сказать что хорошо'
    else:
        m = 'ужасно'
    return m

@property
def name(self):
    return self.__name

@name.setter
def main(self,new_name):
    if new_name == "":
        print("Имя зверюшки не может быть пустой строкой")
    else:
        self.__name = new_name
        print("Имя успешно изменено")

def  __pass_time(self):
    self.hunger += 1
    self.boredom += 1

def main():
    print('Создание зверюшек')
    pet1 = Pet('Зверюшка 1')
    pet2 = Pet('Зверюшка 2')
    pet3 = Pet('Зверюшка 3')
    
    Pet.status()

    print("Доступ к свойству обьекта:", pet1.mood)
    print(pet1.total)
main()

