def main():
    # 7:30
    time = str(input("time:"))
    convert(time)

def convert(time):
    hours, minutes = time.split(":")
    # print(time.split(":"))

    if (19>= int(hours) >=18):
        print("dinner time")
    elif (13>= int(hours) >=12):
        print("lunch time")
    elif (8>= int(hours) >=7):
        print("breakfast time")
    
if __name__ == "__main__":
    main()