class Khoa:
	def __init__(self,MaKhoa,TenKhoa):
		self.MaKhoa = MaKhoa
		self.TenKhoa = TenKhoa
		

	def setMaKhoa(self,MaKhoa):
		self.MaKhoa = MaKhoa
	def getMaKhoa(self):
		return self.MaKhoa

	def setTenKhoa(self,TenKhoa):
		self.TenKhoa = TenKhoa
	def getTen(self):
		return self.TenKhoa

	def toString(self):
		print self.MaKhoa,self.TenKhoa
