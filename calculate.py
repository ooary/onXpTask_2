pengeluaran = []
pemasukan = []

def inputMasukan(v) : 
    pemasukan.append(v)
    return pemasukan

def inputKeluaran(v) :
    pengeluaran.append(v)
    return pengeluaran

def sumMasukan() : 
    sum = 0 
    for i in pemasukan :
        sum += i 
    return sum

def sumKeluaran() :
    sum = 0
    for i in pengeluaran :
        sum += i
    return sum

while True:
    print("Welcome to Calculate onXp BootCamp Task")
    print("#######################################")
    print("List Uang Masuk : ", pemasukan)
    print("List Uang Keluar : ", pengeluaran)
    print("Choice your command : ")
    print("1. Input Uang Masuk")
    print("2. Input Uang Keluar")
    print("3. Total Uang Masuk")
    print("4. Total Uang Keluar")
    print("5. Sisa Uang (Pemasukan - Pengeluaran)")
    user_input = input("Enter a command: ")
    if user_input == "1":
        print("Total Jumlah Uang Masuk : " , sumMasukan())
        while True :
            v = int(input("Input Pemasukan : "))
            inputMasukan(v)
            print("Jumlah Uang Masuk : " , sumMasukan()) 
            continueInput = int(input("Apakah anda ingin Input kembali ? pilih 1 Ya / 2 Tidak : "))
            if continueInput != 1 :
                break
    elif user_input == "2":   
        print("Total Jumlah Uang Keluar : " , sumKeluaran())
        while True :
            v = int(input("Input Pengeluaran : "))
            inputKeluaran(v)
            print("Jumlah Uang Keluar : " , sumKeluaran()) 
            continueInput = int(input("Apakah anda ingin Input kembali ? pilih 1 Ya / 2 Tidak : "))
            if continueInput != 1 :
                break
    elif user_input == "3":
        while True: 
            print("Total Jumlah Uang Masuk : " , sumMasukan())
            continueInput = int(input("Kembali ke Menu awal? Ketik 1 : "))
            if continueInput == 1 :
                break
    elif user_input == "4":
         while True: 
            print("Total Jumlah Uang Keluar : " , sumKeluaran())
            continueInput = int(input("Kembali ke Menu awal? Ketik 1 : "))
            if continueInput == 1 :
                break
    elif user_input == "5":
        while True :
          print("Sisa Uang : " , sumMasukan() - sumKeluaran())
          continueInput = int(input("Kembali ke Menu awal? Ketik 1 : "))
          if continueInput == 1 :
            break
    else:
        print("Tidak ada dalam Menu!")





