gender = input("What is your gender?")
weight = input("What is your weight in lb?")
height = input("What is your height?")
sizes = {
    (130, "5'5") : "XS",
    (150, "5'9") : "XS",
    (151, "5'5") : "S",
    (160, "5'9") : "S",
    (161, "5'5") : "M",
    (170, "5'9") : "M", 
    (171, "5'6") : "L",
    (180, "5'8") : "L", 
    (171, "5'9") : "M",
    (180, "6'") : "M", 
    (181, "5'7") : "L",
    (190, "6'1") : "L", 
}
def height_to_inches(height):
    return (int(height.split("'")[0])*12) + int(height.split("'")[1])

def size(height, weight, gender):
    height = height_to_inches(height)
    for i in sizes:
        if (height_to_inches(i[1]) <= height) and (i[0] <= weight):
            if (height_to_inches(i[1]) + 3 > height) and (i[0] + 9 > weight):
                return sizes[i]

print(size("5'10", 180, "male"))
