class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia

    def __str__(self):
        return f"Ma hang: {self.ma_hang}, Ten hang: {self.ten_hang}, Nha san xuat: {self.nha_sx}, Gia: {self.gia}"

class DienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, thoi_gian_bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.thoi_gian_bao_hanh = thoi_gian_bao_hanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat
    def __str__(self):
        return super().__str__() + f", Bảo hành: {self.thoi_gian_bao_hanh} tháng, Điện áp: {self.dien_ap}V, Công suất: {self.cong_suat}W"
    
class SanhSu(HangHoa):
    def  __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyen_lieu = loai_nguyen_lieu    
    def __str__(self):
        return super().__str__() + f", Loại nguyên liệu: {self.loai_nguyen_lieu}"

class ThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_san_xuat, ngay_het_han_dung):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_san_xuat = ngay_san_xuat
        self.ngay_het_han_dung = ngay_het_han_dung
    def __str__(self):
        return super().__str__() + f", Ngày sản xuất: {self.ngay_san_xuat}, Ngày hết hạn: {self.ngay_het_han_dung}"

# Khởi tạo đối tượng (Lưu ý truyền đủ tham số gia cho DienMay)
dm = DienMay("DM01", "Tủ lạnh", "Samsung", 150000000, "24 tháng", 220, 150)
ss = SanhSu("SS01", "Bình hoa", "Bát Tràng", 500000, "Gốm")
tp = ThucPham("TP01", "Sữa tươi", "Vinamilk", 30000, "20/03/2024", "20/03/2025")

print(dm)
print(ss)   
print(tp)