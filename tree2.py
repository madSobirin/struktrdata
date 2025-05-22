class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        print(" " * (level * 4) + "|-- " + self.name)
        for child in self.children:
            child.print_tree(level + 1)

    def find_position(self, name, path=""):
        current_path = f"{path}/{self.name}"
        if self.name == name:
            return current_path
        for child in self.children:
            result = child.find_position(name, current_path)
            if result:
                return result
        return None


# Contoh penggunaan
if __name__ == "__main__":
    direktur = Node("Direktur")

    manajer1 = Node("Manajer 1")
    manajer1.add_child(Node("Supervisor A"))
    manajer1.add_child(Node("Supervisor B"))

    manajer2 = Node("Manajer 2")
    manajer2.add_child(Node("Supervisor C"))

    direktur.add_child(manajer1)
    direktur.add_child(manajer2)

    print("Struktur Organisasi:")
    direktur.print_tree()

    posisi = "Supervisor C"
    hasil = direktur.find_position(posisi)
    if hasil:
        print(f"\nPosisi '{posisi}' ditemukan di jalur: {hasil}")
    else:
        print(f"\nPosisi '{posisi}' tidak ditemukan.")
