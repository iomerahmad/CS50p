def main():
    items = {}

    while True:
        try:
            item = input().upper()
            items[item] = items.get(item, 0) + 1 
            
            
        except EOFError:
            sorted_items = sorted(items)  
            for item in sorted_items:     
                print(items[item], item)
            break
    
main()
