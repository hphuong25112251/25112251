class SieuNhan:
    ten = str
    vu_khi = str
    mau_sac = str

    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    def hien_thi(self):
        print(f"Siêu nhân: {self.ten} | Vũ khí: {self.vu_khi} | Màu sắc: {self.mau_sac}")
sieu_nhan_A = SieuNhan("A", "kiếm", "đỏ")
sieu_nhan_B = SieuNhan("B", "khiên", "xanh")
print("Thông tin siêu nhân đã tạo:")
sieu_nhan_A.hien_thi()
sieu_nhan_B.hien_thi()