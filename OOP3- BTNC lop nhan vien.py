class SieuNhan:
    ten = str
    tuoi = int
    nangluc = str
    nhiem_vu_hoan_thanh = int 
    nhiem_vu_that_bai = int

    def __init__(self, ten, tuoi, nangluc, nhiem_vu_hoan_thanh, nhiem_vu_that_bai):
        self.ten = ten
        self.tuoi = tuoi
        self.nangluc = nangluc
        self.nhiem_vu_hoan_thanh = nhiem_vu_hoan_thanh
        self.nhiem_vu_that_bai = nhiem_vu_that_bai

    def __str__(self):
        return f"{self.ten} | {self.tuoi} | {self.nangluc} | {self.nhiem_vu_hoan_thanh} | {self.nhiem_vu_that_bai}"
    
danhsach = []
soluong = 0
while True:
    soluong += 1
    print("Nhap 'quit' de thoat")
    ten = input("Tên: ")
    if (ten.lower()== 'quit'):
        break
    tuoi = int(input("Tuổi: "))
    nangluc = input("Năng lực: ")
    nhiem_vu_hoan_thanh = int(input("Nhiệm vụ hoàn thành: "))
    nhiem_vu_that_bai = int(input("Nhiệm vụ thất bại: "))
    sieu_nhan = SieuNhan(ten, tuoi, nangluc, nhiem_vu_hoan_thanh, nhiem_vu_that_bai)
    danhsach.append(sieu_nhan)

for sn in danhsach:
    print (f"Danh sach cac sieu nhan la \n{sn}")