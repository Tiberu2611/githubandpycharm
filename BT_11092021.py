file_object = open('BT1', mode= 'w')
file_object.write('Chao moi nguoi')
file_object.close()
# Bai 2 Viết chương trình thực hiện các yêu cầu sau:
# - Nhập tên tập tin từ bàn phím
# - Đọc nội dung tập tin và in ra màn hình
file_object1 = open('BT1', mode= 'r')
data = file_object1.read()
file_object1.close()
print(data)
# Bài 3: Viết chương trình thực hiện các yêu cầu sau:
# - Nhập tên tập tin từ bàn phím
# - Nhập một chuỗi kí tự vào từ bàn phím
# - Ghi chuỗi kí tự này vào cuối tập tin ở trên
file_object_2 = open('BT1', mode='a+')
file_object_2.write('\nBai tap lap trinh 3')
file_object_2.close()
# Bài 4: Viết chương trình thực hiện các yêu cầu sau:
# - Đọc tập tin ở bài 3 và ghi kết quả ra màn hình
file_object3 = open('BT1', 'r')
data2 = file_object3.read()
file_object3.close()
print(data2)