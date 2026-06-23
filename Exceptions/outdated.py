months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

while True:
    try:
        date = input("Date: ")
        if date[0].isalpha():
            m, d, y = date.split(" ")
            m = months[m]
            m = m.zfill(2)
            d = d.replace(",", "")
            d = d.zfill(2)
            print(f"{y}-{m}-{d}") 
        else:
            m, d, y = date.split("/")
            m = m.zfill(2)
            d = d.zfill(2)
            print(f"{y}-{m}-{d}")

    except ValueError:
        pass
