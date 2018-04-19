from sinhvien import SinhVien

sv = SinhVien(Ten,NamSinh,Khoa)
print("Nhap ten: ")
Ten=input()
print("Nhap nam sinh: ")
sv.NamSinh=input()
print("Nhap khoa: ")
sv.Khoa=input()

print("----------------------")

print(sv.toString())
