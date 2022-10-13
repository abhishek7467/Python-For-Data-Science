
def formatList(items):
    if len(items) == 0:
        return "<empty>"
    if len(items) == 1:
        return str(items[0])
    result = ""
    for i in range(0, len(items) - 2):
        result = result + str(items[i]) + ", "

    result = result + str(items[len(items) - 2]) + " and "
    result = result + str(items[len(items) - 1])
    return result

def main():
    items = []
    line = input("Enter an item (blank to quit): ")
    while line != "":
        items.append(line)
        line = input("Enter an item (blank to quit): ")
    print("The items are ",  formatList(items),' . ')

if  __name__   == "__main__":
   main() 
