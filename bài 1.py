import array as arr
a = [1, 1, 2, 6, 8, 9, 4, 5, 6, 45, 34, 66, 44, 37, 78]
b = []
print("câu A:")
for i in a:
    if(i < 30):
        print(i)
print("câu B:")
c = int(input("Nhap 1 so: "))
d = []
for i in a:
    if i < c:
        print(i)