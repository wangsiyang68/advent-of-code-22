f = open("input.txt")
text = f.read().split('\n\n')
nested_list = [i.split('\n') for i in text][:-1]
calorie_sum = [sum(int(calorie) for calorie in gnome_calories) for gnome_calories in nested_list]
print(max(calorie_sum))