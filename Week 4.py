#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
class NhanVien {
private:
    string tenNhanVien;
    double luongCoBan;
    double heSoLuong;
public:
    static const double LUONG_MAX;
    // Constructor
    NhanVien(string ten, double lcb, double hsl) {
        tenNhanVien = ten;
        luongCoBan = lcb;
        heSoLuong = hsl;
    }
    // ── Getter ────────────────────────────────────────
    string getTenNhanVien() { return tenNhanVien; }
    double getLuongCoBan() { return luongCoBan; }
    double getHeSoLuong() { return heSoLuong; }
    // ── Setter ────────────────────────────────────────
    void setTenNhanVien(string value) {
        tenNhanVien = value;
    } 
    void setLuongCoBan(double value) {
        if (value < 0) {
            cout << "Luong co ban khong duoc am!" << endl;
            return;
        }
        luongCoBan = value;
    }
    void setHeSoLuong(double value) {
        if (value <= 0) {
            cout << "He so luong phai lon hon 0!" << endl;
            return;
        }
        heSoLuong = value;
    }
    // ── Phương thức nghiệp vụ ─────────────────────────
    double tinhLuong() {
        return luongCoBan * heSoLuong;
    }
    void inTTin() {
        cout << "========== THONG TIN NHAN VIEN ==========" << endl;
        cout << " Ten NV : " << tenNhanVien << endl;
        cout << fixed << setprecision(0);
        cout << " Luong CB : " << luongCoBan << " VND" << endl;
        cout << setprecision(1);
        cout << " He so : " << heSoLuong << endl;
        cout << setprecision(0);
        cout << " Luong TT : " << tinhLuong() << " VND" << endl;
        cout << "==========================================" << endl;
   }
    bool tangLuong(double delta) {
        double heSoMoi = heSoLuong + delta;
        double luongMoi = luongCoBan * heSoMoi;
        if (luongMoi > LUONG_MAX) {
            cout << fixed << setprecision(0);
            cout << "Luong moi (" << luongMoi
                 << ") vuot LUONG_MAX (" << LUONG_MAX
                 << "). Khong tang!" << endl;
            return false;
        }
        heSoLuong = heSoMoi;
            cout << fixed << setprecision(0);
            cout << "Da tang he so luong! Luong moi: "
                 << tinhLuong() << " VND" << endl;
            return true;
        }
};
// Khởi tạo hằng số static bên ngoài class
const double NhanVien::LUONG_MAX = 50000000;
// ──── Demo ────────────────────────────────────────────
int main() {
    NhanVien nv("Nguyen Van A", 10000000, 2.0);
nv.inTTin();
cout << "\n--- Test tangLuong ---" << endl;
nv.tangLuong(0.5); // he so 2.0 -> 2.5, luong 25M < 50M -> OK
nv.inTTin();
nv.tangLuong(3.0); // he so 2.5 -> 5.5, luong 55M > 50M -> Canh bao
cout << "\n--- Test getter/setter ---" << endl;
cout << "Ten: " << nv.getTenNhanVien() << endl;
nv.setLuongCoBan(12000000);
cout << fixed << setprecision(0);
cout << "Luong CB moi: " << nv.getLuongCoBan() << endl;
cout << "Luong TT moi: " << nv.tinhLuong() << endl;
return 0;
}