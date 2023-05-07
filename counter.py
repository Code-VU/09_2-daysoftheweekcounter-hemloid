def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    han = open(file_name)
    
    content_list = dict()

    for line in han:
        if line.startswith('From '):
            new_line = line.split()
            days = new_line[2]

            content_list[days] = content_list.get(days,0) + 1

            print(content_list)




## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
