# 19 / 09 / 2023
# Day - 15
# Array & Linked List

# Array (list)
# ini_array = []

# ini_array.append("Brunch")
# print(f"Array: {ini_array}")
# ini_array.append("Bocce")
# print(f"Array: {ini_array}")
# ini_array.append("Tea")
# print(f"Array: {ini_array}")

# Linked List
# model data sekuensial yang saling berkait
# mirip dengan array, tetapi lebih fleksibel dan sedikit kompleks
# Null adalah tidak ada node lain dibelakang nya atau setelahnya


# Singly Linked List
# List : head,size
# Node : nextNode, element
# class List ini minimal memiliki 2 buah field
# head pada class List berfungsi untuk mencatat anggota pertama dari class List
# size pada class List digunakan untuk mencatat panjang dari class List / banyak nya anggota dari class List
# tiap anggota dari List itu akan direpresentasikan dengan Node
# class Node ini memiliki 2 buah field
# element pada class Node berfungsi untuk mencatat object atau isi dari list itu sendiri yaitu class Node
# nextNode pada class Node berfungsi untuk mencatat Node berikutnya atau anggota dari class List berikut nya
# List ini head nya hanya mencatat atau menunjuk ke Node yang pertama yaitu element nya 30
# Node yang berikutnya yang isi nya 20 ini dicatat nya itu oleh Node yang pertama
# jadi nextNode yang pertama ini dia akan menunjuk atau mencatat Node yang kedua
# dan nextNode yang kedua ini dia akan menunjuk atau mencatat Node yang ketiga
# dan nextNode dari Node yang ketiga ini akan berisi None
# dia tidak menunjuk apapun artinya adalah dia Node yang terakhir
# size itu sendiri menujukkan panjang atau ukuran List nya itu sendiri


# kita akan menunjukkan 2 buah fungsi yang akan kita implementasikan dalam singly linked list kita yaitu view yaitu fungsi yang kita gunakan untuk mengembalikan isi dari List yaitu 30,20,10
# lalu yang kedua adalah fungsi addFirst yaitu kita menambahkan element diawal dari List
# Jadi jika saya masukkan 40 di addFirst, si 40 itu
# akan masuk nya didepan bukan dibelakang
# jadi nanti isi dari List nya adalah 40,30,20


class SinglyLinkedList:
    # hanya bisa digunakan didalam class SinglyLinkedList
    # membuat Node / mendeklarasikan Node
    class _Node:
        def __init__(self, element, nextNode=None):
            self.element = element
            self.nextNode = nextNode

    # membuat constructor SinglyLinkedList
    def __init__(self):
        # membuat head
        self._head = None
        # membuat ukuran linked list nya
        self._size = 0

    # membuat method View_All atau mengembalikan semua nilai dari myList
    def __str__(self):
        result = ""
        # pointer menunjuk object yang sama dari object yang ditunjuk oleh head
        pointer = self._head
        # looping selama pointer tidak bernilai None
        while pointer != None:
            # menambahkan element nya ini ke dalam string bernama result
            result = result + str(pointer.element) + " "
            # pointer menunjuk nextNode element selanjutnya
            pointer = pointer.nextNode
        return result

    # Add_First dengan myList nya masih kosong menambahkan element diawal pada Node
    def add_first(self, element):
        # memasukkan element ke dalam Node yang baru dibuat
        newNode = self._Node(element)
        # nextNode menunjuk ke None
        # perintah dilakukan untuk jika head nya itu ternyata sudah ada element nya
        ## nextNode menunjuk yang sama dengan head yaitu Node yang berisi element
        newNode.nextNode = self._head
        # head menunjuk object yang dituju newNode
        ## head menunjuk object yang ditunjuk oleh newNode
        self._head = newNode
        # size nya ditambahkan 1
        self._size += 1

    # Add_last dengan myList nya sudah ada element nya menambahkan element diakhir pada Node
    def add_last(self, element):
        newNode = self._Node(element)
        # Node nya ada 2 kasus jika head nya kosong
        if self._head == None:
            self._head = newNode
        # Jika Node nya sudah ada isi nya
        else:
            pointer = self._head
            while pointer.nextNode != None:
                pointer = pointer.nextNode
            pointer.nextNode = newNode
        self._size += 1

    # Remove_First
    def remove_first(self):
        if self._size > 0:
            if self._size == 1:
                value = self._head.element
                self._head = None
                self._size -= 1
                return value
            else:
                pointer = self._head
                value = self._head.element
                self._head = pointer.nextNode
                pointer.nextNode = None
                self._size -= 1
                return value
        return None

    # Remove_Last
    def remove_last(self):
        if self._size > 0:
            if self._size == 1:
                value = self._head.element
                self._head = None
                self._size -= 1
                return value
            else:
                pointer = self._head
                while pointer.nextNode.nextNode != None:
                    pointer = pointer.nextNode
                value = pointer.nextNode.element
                pointer.nextNode = None
                self._size -= 1
                return value
        return None

    # method override size
    def __len__(self):
        return self._size


def main():
    myList = SinglyLinkedList()
    # myList.add_first(10)
    # myList.add_first(20)
    # myList.add_first(30)
    myList.add_last(10)
    myList.add_last(20)
    myList.add_last(30)
    print(str(myList))
    print(len(myList))
    # print("delete: ", myList.remove_first())
    # print("delete: ", myList.remove_first())
    # print("delete: ", myList.remove_first())
    # print("delete: ", myList.remove_first())
    print("delete: ", myList.remove_last())
    print("delete: ", myList.remove_last())
    print("delete: ", myList.remove_last())
    print("delete: ", myList.remove_last())
    print(str(myList))
    print(len(myList))


main()


# mendeklarasikan Node / membuat Node nya
# class Node:
#     def __init__(self, isi):
#         self._isi = isi
#         self._next = None


# membuat Linked List
# class Linked_List:
# mendeklarasikan head / membuat head
# def __init__(self):
#     self._head = None

# def add1(self, isi):
# membuat Node baru
# a = Node(isi)
# mengetahui posisi dari head nya pada Node
# if self._head == None:
#     self._head = a
# else:
# menunjuk Node yang baru ke Node head nya
# a._next = self._head
# memindahkan Node head ke Node yang baru
# self._head = a

# def cetak(self):
# Node head sudah pindah ke Node a
# a = self._head
# menyambungkan Node
# while a != None:
#     print(a._isi)
# mencetak Node berikutnya
# a = a._next


# my_linked_list = Linked_List()
# my_linked_list.add1("a")
# my_linked_list.add1("b")
# my_linked_list.add1("c")
# my_linked_list.cetak()
