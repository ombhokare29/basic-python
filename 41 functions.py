def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p

mar = [85,75,98,56]
percentage1=percent(mar)

marks2 = [98,95,96,98]
percentage2=percent(marks2)

print(percentage1,percentage2)


