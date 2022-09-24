import random

def random_carriage(coupe_ammout = 9):
    carriage = []
    coupe = {}
    for place in range(1,coupe_ammout * 4 + 1):
        coupe[place] = random.choice([None, 'м','ж'])
        if len(coupe) == 4:
            carriage.append(coupe)
            coupe = {}
    return carriage


def print_carriage(carriage):
    for  index, coupe in enumerate(carriage):
        print(index +1 ,':', coupe)
   

def empty_coupe_list(carriage):
    """ Список полностью свободных купе
    Args:
        carriage(int) = вагон

    Returns:
            Возвращает ответ
    """
    answer = {}
    for index, coupe in enumerate(carriage):
        if not any(coupe.values()):
            answer[index + 1] = coupe 
    return answer

def empty_place_list(carriage):
    """ Список полностью свободных купе
    Args:
        carriage(int) = вагон

    Returns:
            Возвращает ответ
    """
    answer = []
    for  coupe  in carriage:
        for place in coupe:
            if not coupe[place]:
                answer.append(place)
    return answer

def empty_lh_place_list(carriage, low = True):
    """ Список полностью свободных купе
    Args:
        carriage(int) = вагон

    Returns:
            Возвращает ответ
    """
    answer = []
    for coupe in carriage:
        for place in coupe:
            if not coupe[place] and place % 2 == int(low):
                if not coupe[place]:
                    answer.append(place)

    return answer
def empty_place_in_gender_coupe(carriage, gender):
    """ Список полностью свободных купе
    Args:
        carriage(int) = вагон
        gender(int) = купи

    Returns:
            Возвращает ответ
    """
    answer = []
    for coupe in carriage:
        answer1 = []
        for place in coupe:
            if not coupe[place]:
                answer1.append(place)
            elif coupe[place]  != gender:
                break
            
        else:
            if len(answer1) < 4:
                answer += answer1  
    return answer               

carriage = random_carriage()
print_carriage(carriage)


print('Список полностью свободных купе')
print(empty_coupe_list(carriage))
print('Список свободных мест в вагоне')
print(empty_place_list(carriage))
print('Список свободных мест нижних мест в вагоне')
print(empty_lh_place_list(carriage))
print('Список свободных мест верхих мест в вагоне')
print(empty_lh_place_list(carriage,False))
print('Список свободных мест в купе с мужской компнией')
print(empty_place_in_gender_coupe(carriage,'м'))
print('Список свободных мест в купе с женской компнией')
print(empty_place_in_gender_coupe(carriage,'ж'))
