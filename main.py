def get_input():
    print("Введите сумму денег")
    sum = float(input())
    print("Введите количество дней до заработной платы")
    days_left = int(input())
    return [sum, days_left]

def readfile(filename):
    f = open('meal_menu/' + filename, 'r')
    list = {}

    for line in f.readlines():
        list[line.split('|')[0]] = line.split('|')[1].strip()
    f.close()
    return list

def validate(sum):
    coffee = readfile('coffee')
    drinks = readfile('drinks')
    garnish = readfile('garnish')
    main = readfile('main')
    soups = readfile('soups')
    tea = readfile('tea')
    min_price = float(min(min(main.values()), min(soups.values())))
    max_price = float(max(max(main.values()), max(soups.values())))

    if sum < min_price:
        return 0
    if sum >= min_price and


print("Здравтсвуйте! Пожалуйста, ответьте на следующие вопросы")
input_res = get_input()

sum_per_consuption = input_res[0] / (input_res[1] * 2)
validation_code = validate(sum_per_consuption)
if validation_code == 0:
    print("К сожалению, мы не можем Вам предложить план питания: недостаточно денег")