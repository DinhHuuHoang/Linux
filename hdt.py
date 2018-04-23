class SinhVien:
	MSSV = '001'
	HoTen = 'Mai A'
	Khoa = '57'
	def __init__(self, MSSV, HoTen, Khoa):
		self.MSSV = MSSV
		self.HoTen = HoTen
		self.Khoa = Khoa
	def getMSSV(self):
		return self.MSSV
	def getHoTen(self):
		return self.HoTen
	def getKhoa(self):
		return self.Khoa
	def setMSSV(self,MSSV):
		self.MSSV = MSSV
	def setHoTen(self,HoTen):
		self.HoTen = HoTen
	def setKhoa(self, Khoa):
		self.Khoa =Khoa 
s=[]
s.append(SinhVien("001", "Mai A", "57"))
s.append(SinhVien("002", "Tran B", "58"))
s.append(SinhVien("003", "Le C", "57"))
s.append(SinhVien("004", "Pham Q", "58"))
s.append(SinhVien("005", "Nguyen N", "59"))
for i in range(1, len(s)):
	print(s[i].getMSSV())
	print(s[i].getHoTen())
	print(s[i].getKhoa()) 

class KH:
	MaKhoa = '56'
	TenKhoa = 'Khoa 56CNTT'
	def __init__(self, MaKhoa, TenKhoa):
		self.MaKhoa = MaKhoa
		self.TenKhoa = TenKhoa
	def getMaKhoa(self):
		return self.MaKhoa
	def getTenKhoa(self):
		return self.TenKhoa
	def setMaKhoa(self,MaKhoa):
		self.MaKhoa = MaKhoa
	def setTenKhoa(self, TenKhoa):
		self.TenKhoa = TenKhoa
s=[]
s.append(KH("56","Khoa 56CNTT"))
s.append(KH("57","Khoa 57CNTT"))
s.append(KH("58","Khoa 58CNTT"))
s.append(KH("59","Khoa 59CNTT"))
for i in range(1, len(s)):
	print(s[i].getMaKhoa()) 
	print(s[i].getTenKhoa())
		
