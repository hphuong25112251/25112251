class CanBo():
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh  
        self.dia_chi = dia_chi
    def __str__(self):
        return f"Họ tên: {self.ho_ten}, Tuổi: {self.tuoi}, Giới tính: {self.gioi_tinh}, Địa chỉ: {self.dia_chi}"
    def hien_thi_thong_tin(self):
        print(self.__str__())   

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac
    def __str__(self):
        return super().__str__() + f", Bậc: {self.bac}"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao
    def __str__(self):
        return super().__str__() + f", Ngành đào tạo: {self.nganh_dao_tao}"
    
class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec
    def __str__(self):
        return super().__str__() + f", Công việc: {self.cong_viec}"
    
class QuanLyCanBo():
    def __init__(self):
        self.danh_sach_can_bo = []
    
    def them_moi_can_bo(self, can_bo):
        self.danh_sach_can_bo.append(can_bo)
    def tim_kiem_can_bo(self, ho_ten):
        self.ho_ten = ho_ten
        for can_bo in self.danh_sach_can_bo:
            if can_bo.ho_ten == self.ho_ten:
                return can_bo
        return None
    def hien_thi_danh_sach_can_bo(self):
        for can_bo in self.danh_sach_can_bo:
            print(can_bo)
    def thoat_chuong_trinh(self):
        print("Thoát chương trình") 

# Khởi tạo quản lý cán bộ
qlcb = QuanLyCanBo()
# Thêm cán bộ
qlcb.them_moi_can_bo(CongNhan("Nguyễn Văn Đinh", 30, "Nam", "Hà Nội", 5))
qlcb.them_moi_can_bo(KySu("Trần Thị HH", 28, "Nữ", "Hà Nội", "Công nghệ thông tin"))
qlcb.them_moi_can_bo(NhanVien("Lê Văn Ninh", 35, "Nam", "Hà Nội", "Nhân viên văn phòng"))
# Hiển thị danh sách cán bộ
print("Danh sách cán bộ:")
qlcb.hien_thi_danh_sach_can_bo()
# Tìm kiếm cán bộ
ho_ten_can_tim = "Lê Văn Ninh"
can_bo_tim_thay = qlcb.tim_kiem_can_bo(ho_ten_can_tim)
if can_bo_tim_thay:
    print(f"\nKết quả tìm kiếm cho '{ho_ten_can_tim}':")
    print(can_bo_tim_thay)
else: 
    print(f"\nKhông tìm thấy cán bộ với tên '{ho_ten_can_tim}'")
# Thoát chương trình
qlcb.thoat_chuong_trinh()
print("Chương trình kết thúc.")