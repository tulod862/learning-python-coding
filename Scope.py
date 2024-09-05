

name = "Pocky"
count = 1


def another():
    color = "pink"
    global count 
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "skyblue"
        print(color)
        print(name)
    
    greeting("Pocky")
another()
