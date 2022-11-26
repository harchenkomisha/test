import string 

class   Alpabet:
    def __init__(self,languege, latter_str:):
        self.lang = languege
        self.latters = list(letters_str)


    def letters_num(self):
        len(self.letters)

class EngAlhabet(Alpabet):
    __letters_num = 26
     
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self,letter):
        if letter.upper() in self.letters:
            return True
        return False

    def letters_num(self):
        return EngAlhabet.__letters_num


    @staticmethod
    def example():
        print("English Example:\nDon't judge a book by its cover.")



if __name__ == '__main__':
    eng_alhabet = EngAlhabet()
    eng_alhabet.print()
    print(eng_alhabet.letters_num())
    print(eng_alhabet.is_en_letter('F'))
    print(eng_alhabet.is_en_letter('Щ'))
    EngAlhabet.example()


    
