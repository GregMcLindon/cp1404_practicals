names = ["Jack", "Jill", "Harry"]
dobs = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
dob_dict = dict(zip(names, dobs))
while len(dob_dict) < 5:
    name_add = input("Name: ")
    dob_add = input("DOB (dd/mm/yyyy): ")
    dob_dict[name_add] = dob_add.split("/")
for name, dob in dob_dict.items():
    print("{}'s birth date is {}/{}/{}".format(name, dob[0], dob[1], dob[2]))

