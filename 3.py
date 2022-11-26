class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    
    def get_kg(self):
        return self.__kg

    @kg.setter
    def kg(self,new_kg):
        if isinstance(new_kg,(int,float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаються только числами')