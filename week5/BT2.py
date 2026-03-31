class NhanVien:
    Luong_co_ban = 5000000
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max):
        self.ma_nv= ma_nv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.he_so_luong = he_so_luong if he_so_luong > 0 else 0.1
        self.luong_max = luong_max

    def tinh_thu_nhap(self):
        thu_nhap = self.he_so_luong * self.LUONG_CO_BAN
        return min(thu_nhap, self.luong_max)

    def __str__(self):
        return f"Ma NV: {self.ma_nv}, Họ tên: {self.ho_ten}, Năm sinh: {self.nam_sinh}, Giới tính: {self.gioi_tinh}, Địa chỉ: {self.dia_chi}, Hệ số lương: {self.he_so_luong}"

class CongTacVien(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max, thoi_han_hop_dong, phu_cap_lao_dong_cong_them_thu_nhap):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max)
        if thoi_han_hop_dong not in ["3 tháng", "6 tháng", "1 năm"]:
            raise ValueError("Thời hạn hợp đồng phải là '3 tháng', '6 tháng' hoặc '1 năm'")
        self.thoi_han_hop_dong = thoi_han_hop_dong # "3 tháng ", " 6 tháng", " 1 năm"
        self.phu_cap_lao_dong_cong_them_thu_nhap = phu_cap_lao_dong_cong_them_thu_nhap

    def tinh_thu_nhap(self):
        thu_nhap_co_ban = super().tinh_thu_nhap()
        return thu_nhap_co_ban + self.phu_cap_lao_dong_cong_them_thu_nhap

class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max, vi_tri):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max)
        self.vi_tri = vi_tri
    def tinh_thu_nhap(self):
        return super().tinh_thu_nhap()

class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max, ngay_bat_dau_quan_ly, phu_cap_quan_ly_cong_them_thu_nhap):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_max)
        self.ngay_bat_dau_quan_ly = ngay_bat_dau_quan_ly
        self.phu_cap_quan_ly_cong_them_thu_nhap = phu_cap_quan_ly_cong_them_thu_nhap
    def tinh_thu_nhap(self):
        thu_nhap_co_ban = super().tinh_thu_nhap()
        return thu_nhap_co_ban + self.phu_cap_quan_ly_cong_them_thu_nhap
    
# Khởi tạo nhân viên
ctv = CongTacVien("NV01", "Nguyễn Diệu Linh", 2007, "Nữ", "Hanoi", 1.5, 20000000, "6 tháng", 2000000)
nvc = NhanVienChinhThuc("NV02", "Tạ Ngọc Huyền", 2007, "Nữ", "Hà Nội", 2.0, 30000000, "Kế toán")
tp = TruongPhong("NV03", "Nguyen Thị Thu Giang", 2007, "Nữ", "Sơn La", 2.5, 40000000, "17/08/2007", 5000000)    

print(ctv)
print(nvc)
print(tp)