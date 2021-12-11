#Function of getting input
def get_input():
    print("Введите сумму денег")
    sum = float(input())
    print("Введите количество дней до заработной платы")
    days_left = int(input())
    return [sum, days_left]

#Function of file reading
def readfile(filename):
    f = open('meal_menu/' + filename, 'r')
    list = {}

    for line in f.readlines():
        list[line.split('|')[0]] = line.split('|')[1].strip()
    f.close()
    return list

#Function of choosing the method to apply
def validate(sum):
    main = readfile('main')
    soups = readfile('soups')
    min_price_main = float(min(main.values()))
    min_price_soups = float(min(soups.values()))
    max_price_main = float(max(main.values()))
    max_price_soups = float(max(soups.values()))

    if sum < min_price_main + min_price_soups:
        return 0
    if (sum >= min_price_main + min_price_soups) and (sum < max_price_main + max_price_soups):
        return 1
    if sum >= max_price_main + min_price_soups:
        return 2

def get_minimal_meal(data):
    min_key = ""
    min = float(list(data.values())[0])
    for i in data.keys():
        curr = float(data[i])
        if curr < min:
            print(i)
            min_key = i
            min = curr

    return [min_key, min]


def start_providing(mode):
    if mode != 1 and mode != 2:
        return -1

    coffee = readfile('coffee')
    drinks = readfile('drinks')
    garnish = readfile('garnish')
    main = readfile('main')
    soups = readfile('soups')
    tea = readfile('tea')

    if mode == 1:
        resulting_menu = {}
        tmp_meal = get_minimal_meal(main)
        resulting_menu[tmp_meal[0]] = tmp_meal[1]
        tmp_meal = get_minimal_meal(soups)
        resulting_menu[tmp_meal[0]] = tmp_meal[1]
        return resulting_menu

#Start of the program
print("Здравтсвуйте! Пожалуйста, ответьте на следующие вопросы")
input_res = get_input()
sum_per_consuption = input_res[0] / (input_res[1] * 2)
val = validate(sum_per_consuption)
if val == 0:
    print("К сожалению, мы не можем Вам предложить план питания: недостаточно денег")
    exit()
elif val == 1:
    print("К сумме, указанной Вами, предлагаем следующий вариант")
elif val == 2:
    print("Выберите из предложенных вариантов")

menu = start_providing(val)
if menu == -1:
    print("Bad option")
    exit()
print(menu)

