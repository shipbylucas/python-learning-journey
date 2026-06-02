month = {
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}


def main():
    time = date_form()
    print(time)

def date_form():
    while True:
        date = input("Date: ")
        if "/" in date:
            try:
                m,d,y = date.strip().split("/")
                if 1 <= int(m) <= 12 and 1 <= int(d) <= 31 and 0 <= int(y) <= 9999:
                    return num_form(date)
            except: continue
        else:
            if "," in date:
                try:
                    o,p,q = date.strip().split(" ")
                    if 1 <= int(month[o]) <= 12 and 1 <= int(p.replace(",", "")) <= 31 and 0 <= int(q) <= 9999:
                        return text_form(date)
                except: continue
            else: continue

def num_form(r):
    m,d,y = r.strip().split("/")
    return (y + "-" + number(m) + "-" + number(d))

def text_form(u):
    m,d,y = u.strip().split(" ")
    return (y + "-" + month[m] + "-" + number(d.replace(",", "")))

def number(k):
    if int(k) < 10:
        return ("0" + k)
    else:
        return k

main()
