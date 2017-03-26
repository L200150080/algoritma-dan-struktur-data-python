
print("%27s" %("Tabel KODE ASSCII")) ##agar string Tabel KODE ASCII berada ditengah
print("---------------------------------------")

## Nilai variabel kode akan berubah secara otomatis mulai dari 32 sampai 126

print("| %2s | %3s | %9s   | %6s |" %( "Simbol", "Kode","Binary" ,"Hex")) ##supaya tertata rapi
for kode in range(32,126):
    print("|%4c    | %4d | %10s  | %6s |" %( kode, kode, bin(kode), hex(kode) ) )
print("----------------------------------------")
print("Ragil Burhanudin Pamungkas\nL200150080")
    

    
