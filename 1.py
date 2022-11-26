class Soda:

    def __init__(self,ingreient):
        if isinstance(ingreient, str):
            self.ingreient = ingreient
        else:
            self.ingreient =   None



    def show_my_drink(self):
        if self.ingreient:
            print(f'Газировка и {self.ingreient}')
         
        else:
            print("Обычная газировка")