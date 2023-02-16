# Задача 2 (24). В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем 
# кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на 
# грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система 
# автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого 
# куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод, которое 
# может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле 
# грядки.

# Пример:
# 4 -> 1 2 3 4
# 9 


N = int(input('Введите количество кустов на Вашей грядке: '))
yrozai = [int(input(f'Введите урожай на {i+1} кусте: ')) for i in range (N)]

# ----------------- 1 вариант ---------------------------------
# sbor_1 = [sum(yrozai[i:i+3]) for i in range (N)]
# print (f'{N} -> ',end='')
# print(*yrozai)
# print (max(sbor_1))

# ----------------- 2 вариант ---------------------------------
# max_cbor = 0
# for i in range(N):
#     count_max = sum(yrozai[i:i+3])
#     if count_max > max_cbor:
#         max_cbor = count_max
# if yrozai[0] + yrozai[-1] + yrozai[-2] > max_cbor:
# 	max_cbor = yrozai[0] + yrozai[-1] + yrozai[-2]
# if yrozai[0] + yrozai[1] + yrozai[-1] > max_cbor:
# 	max_cbor = yrozai[0] + yrozai[1] + yrozai[-1]
# print (f'{N} -> ',end='')
# print(*yrozai)
# print(max_cbor)