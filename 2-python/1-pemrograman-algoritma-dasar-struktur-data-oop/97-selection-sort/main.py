# 12 / 10 / 2023
# Day - 27
# Selection Sort
# Selection Sort adalah pengurutan dengan konsep memilih element dengan nilai paling rendah dan menukar element tersebut dengan element ke-i

angka = [3, 6, 1, 8, 9, 12, 33, 43, 15, 91, 43]


def selection_sort(data):
    print("data awal\n{}".format(data))
    langkah = 0
    for i in range(len(data) - 1, 0, -1):
        print("langkah ke-{}".format(langkah))
        # step nilai awal
        m = 0
        for j in range(1, i + 1):
            if data[j] > data[m]:
                m = j
        # data dipindahkan atau diswap
        temp = data[i]
        data[i] = data[m]
        data[m] = temp
        langkah += 1
        print(data)


selection_sort(angka)
