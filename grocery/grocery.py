from sortedcontainers import SortedDict

def main():
    items = {}

    while(True):
        try:
            grocery = input().upper().strip()
            if grocery == "":
                for i in SortedDict(items.items()):
                    print(items[i], i, sep= " ")
                break

            item(grocery, items)

        except EOFError:
            for i in SortedDict(items.items()):
                print(items[i], i, sep= " ")
            return

        except KeyError:
            pass

def item(grocery, items):
    if grocery in items:
        items[grocery] = 1 + int(items[grocery])
    else:
        items[grocery] = 1
    return items

main()