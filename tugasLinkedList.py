class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularQueue:
    def __init__(self):
        self.tail = None
        self.size = 0

    def tambah_pelanggan(self, nama):
        new_node = Node(nama)
        if not self.tail:
            self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"> Tambah: {nama}")

    def layani_pelanggan(self):
        if not self.tail:
            print("> Antrian kosong")
            return
        head = self.tail.next
        print(f"> Layani pelanggan: {head.nama}")
        if self.tail == head:
            self.tail = None
        else:
            self.tail.next = head.next
        self.size -= 1

    def tampilkan_antrian(self):
        if not self.tail:
            print("> Antrian kosong")
            return
        hasil = []
        current = self.tail.next
        while True:
            hasil.append(current.nama)
            current = current.next
            if current == self.tail.next:
                break
        print("> Antrian: " + " -> ".join(hasil) + " -> (kembali ke head)")

    def cari_pelanggan(self, nama):
        if not self.tail:
            print("> Antrian kosong")
            return False
        current = self.tail.next
        while True:
            if current.nama == nama:
                print(f"> Pelanggan ditemukan: {nama}")
                return True
            current = current.next
            if current == self.tail.next:
                break
        print(f"> Pelanggan tidak ditemukan: {nama}")
        return False

    def jumlah_pelanggan(self):
        print(f"> Jumlah pelanggan: {self.size}")

# Contoh penggunaan
antrian = CircularQueue()
antrian.tambah_pelanggan("Andi")
antrian.tambah_pelanggan("Budi")
antrian.tambah_pelanggan("Citra")
antrian.tampilkan_antrian()
antrian.layani_pelanggan()
antrian.tampilkan_antrian()
antrian.cari_pelanggan("Citra")
antrian.jumlah_pelanggan()
