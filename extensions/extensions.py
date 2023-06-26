
x = str(input("File: ")).strip().lower().replace(",","")

# find position "."
location_point = x.find('.')
# print (location_point)
# print al string final
# print(x[location_point:len(x)])

y = x[location_point+1:len(x)]
# print (y)

while (y.count(".") >= 1):
    location_point = y.find('.')
    y = y[location_point+1:len(x)]

match y:
    case "gif":
        print("image/gif")
    case "jpg"|"jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
