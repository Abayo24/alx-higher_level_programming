#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for i in names:
        if i[0] != '_':
            print(f"{i}")
=======
if __name__ == '__main__':
    import hidden_4
    names_list = dir(hidden_4)
    for name in names_list:
        if name[0] != '_':
            print("{}".format(name))
>>>>>>> master
