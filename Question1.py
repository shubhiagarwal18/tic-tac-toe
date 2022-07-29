from operator import itemgetter

total_info = []
while True:
    per_person_info = input("Enter the values of name, age and height(comma seperated): ")

    if per_person_info == "":
        break
    else:
        print(per_person_info)
        total_info.append(tuple((per_person_info.split(","))))
        print(total_info)
total_info.sort(key =  itemgetter(0, 1, 2))       
print(total_info)