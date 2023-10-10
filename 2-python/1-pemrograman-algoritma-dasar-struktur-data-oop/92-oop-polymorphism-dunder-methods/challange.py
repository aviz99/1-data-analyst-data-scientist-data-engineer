# Buatlah sebuah class dengan nama RekeningBank
# Kemudian class ini memiliki beberapa method seperti mencetak saldo, menabung, dan menarik uang
# Jika rekeningnya kurang, maka akan menunjukkan keterangan bahwa saldo tidak bisa ditarik karena tidak mencukupi


class Rekening_Bank:
    def __init__(self, tabungan):
        self.tabungan = tabungan

    def cek_saldo(self):
        print(f"Jumlah saldo anda adalah:\nRP. {self.tabungan}")

    def deposit(self):
        menabung = int(input("Masukkan jumlah yang anda ingin ditabungkan:\nRP. "))
        self.tabungan += menabung

    def tarik_tunai(self):
        tarik = int(input("Masukkan jumlah yang anda ingin diambil:\nRP "))
        if self.tabungan < tarik:
            print(
                f"Maaf saldo anda tidak mencukupi untuk\nSaldo anda saat ini adalah:\nRP. {self.tabungan}"
            )
        else:
            self.tabungan -= tarik
            return f"Saldo berhasil diambil\nSaldo anda saat ini adalah:\nRP. {self.tabungan}"


tabunganku = Rekening_Bank(100000)
tabunganku.cek_saldo()
tabunganku.deposit()
tabunganku.cek_saldo()
tabunganku.tarik_tunai()
tabunganku.cek_saldo()
