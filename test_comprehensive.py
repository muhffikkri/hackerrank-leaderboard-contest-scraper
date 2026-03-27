# Versi DIPERBAIKI dari fungsi SearchJadwal
def SearchJadwal(hari, awal, akhir) :
    if hari == "sen" :
        if akhir >= 13 and awal <= 15 :
            return "Dasar Pemrograman"
        else :
            return "Tidak ada"
    elif hari == "sel" :
        if akhir >= 13 and awal <= 15 :
            return "Aljabar Linier"
        else :
            return "Tidak ada"
    elif hari == "rab" :
        # Dasar Sistem: 7-10, Bahasa Inggris I: 15-16
        dasar_sistem = akhir >= 7 and awal <= 10
        bahasa_inggris = akhir >= 15 and awal <= 16
        
        if dasar_sistem and bahasa_inggris:
            return "Dasar Sistem & Bahasa Inggris I"
        elif dasar_sistem:
            return "Dasar Sistem"
        elif bahasa_inggris:
            return "Bahasa Inggris I"
        else:
            return "Tidak ada"
    elif hari == "kam" :
        # Pancasila: 7-9, Matematika I: 13-15
        pancasila = akhir >= 7 and awal <= 9
        matematika = akhir >= 13 and awal <= 15
        
        if pancasila and matematika:
            return "Pancasila & Matematika I"
        elif pancasila:
            return "Pancasila"
        elif matematika:
            return "Matematika I"
        else:
            return "Tidak ada"
    elif hari == "jum" :
        # Bahasa Indonesia: 7-9, Struktur Diskrit: 13-16
        bahasa_indonesia = akhir >= 7 and awal <= 9
        struktur_diskrit = akhir >= 13 and awal <= 16
        
        if bahasa_indonesia and struktur_diskrit:
            return "Bahasa Indonesia & Struktur Diskrit"
        elif bahasa_indonesia:
            return "Bahasa Indonesia"
        elif struktur_diskrit:
            return "Struktur Diskrit"
        else:
            return "Tidak ada"
    else :
        return "Tidak ada"

def test_jadwal():
    print("=== Testing SearchJadwal Function ===\n")
    
    # Test untuk Senin (Dasar Pemrograman: 13-15)
    print("SENIN (Dasar Pemrograman 13-15):")
    test_cases_sen = [
        ("sen", 13, 15),  # Tepat waktu kuliah
        ("sen", 12, 14),  # Overlapping dari sebelum
        ("sen", 14, 16),  # Overlapping dari sesudah  
        ("sen", 12, 16),  # Mencakup seluruh waktu
        ("sen", 13, 14),  # Sebagian waktu kuliah
        ("sen", 14, 15),  # Sebagian waktu kuliah
        ("sen", 10, 12),  # Sebelum waktu kuliah
        ("sen", 16, 18),  # Sesudah waktu kuliah
    ]
    
    for hari, awal, akhir in test_cases_sen:
        result = SearchJadwal(hari, awal, akhir)
        print(f"  {hari} {awal}-{akhir}: {result}")
    
    # Test untuk Selasa (Aljabar Linier: 13-15)
    print("\nSELASA (Aljabar Linier 13-15):")
    test_cases_sel = [
        ("sel", 13, 15),  # Tepat waktu kuliah
        ("sel", 12, 14),  # Overlapping
        ("sel", 14, 16),  # Overlapping
        ("sel", 10, 12),  # Sebelum waktu kuliah
    ]
    
    for hari, awal, akhir in test_cases_sel:
        result = SearchJadwal(hari, awal, akhir)
        print(f"  {hari} {awal}-{akhir}: {result}")
    
    # Test untuk Rabu (Dasar Sistem: 7-10, Bahasa Inggris I: 15-16)
    print("\nRABU (Dasar Sistem 7-10, Bahasa Inggris I 15-16):")
    test_cases_rab = [
        ("rab", 7, 10),   # Hanya Dasar Sistem
        ("rab", 15, 16),  # Hanya Bahasa Inggris I
        ("rab", 7, 16),   # Kedua mata kuliah
        ("rab", 8, 9),    # Sebagian Dasar Sistem
        ("rab", 15, 15),  # Sebagian Bahasa Inggris I (1 jam)
        ("rab", 6, 11),   # Overlapping Dasar Sistem
        ("rab", 14, 17),  # Overlapping Bahasa Inggris I
        ("rab", 6, 17),   # Overlapping keduanya
        ("rab", 11, 14),  # Gap di antara
        ("rab", 9, 15),   # Dari tengah DS sampai awal BI
        ("rab", 10, 15),  # Dari akhir DS sampai awal BI
        ("rab", 7, 15),   # Dari awal DS sampai awal BI
    ]
    
    for hari, awal, akhir in test_cases_rab:
        result = SearchJadwal(hari, awal, akhir)
        print(f"  {hari} {awal}-{akhir}: {result}")
    
    # Test untuk Kamis (Pancasila: 7-9, Matematika I: 13-15)
    print("\nKAMIS (Pancasila 7-9, Matematika I 13-15):")
    test_cases_kam = [
        ("kam", 7, 9),    # Hanya Pancasila
        ("kam", 13, 15),  # Hanya Matematika I
        ("kam", 7, 15),   # Kedua mata kuliah
        ("kam", 6, 10),   # Overlapping Pancasila
        ("kam", 12, 16),  # Overlapping Matematika I
        ("kam", 8, 14),   # Dari tengah Pancasila sampai awal Matematika I
        ("kam", 10, 12),  # Gap di antara
        ("kam", 9, 13),   # Dari akhir Pancasila sampai awal Matematika I
    ]
    
    for hari, awal, akhir in test_cases_kam:
        result = SearchJadwal(hari, awal, akhir)
        print(f"  {hari} {awal}-{akhir}: {result}")
    
    # Test untuk Jumat (Bahasa Indonesia: 7-9, Struktur Diskrit: 13-16)
    print("\nJUMAT (Bahasa Indonesia 7-9, Struktur Diskrit 13-16):")
    test_cases_jum = [
        ("jum", 7, 9),    # Hanya Bahasa Indonesia
        ("jum", 13, 16),  # Hanya Struktur Diskrit
        ("jum", 7, 16),   # Kedua mata kuliah
        ("jum", 6, 10),   # Overlapping Bahasa Indonesia
        ("jum", 12, 17),  # Overlapping Struktur Diskrit
        ("jum", 8, 14),   # Dari tengah BI sampai awal SD
        ("jum", 10, 12),  # Gap di antara
        ("jum", 9, 13),   # Dari akhir BI sampai awal SD
    ]
    
    for hari, awal, akhir in test_cases_jum:
        result = SearchJadwal(hari, awal, akhir)
        print(f"  {hari} {awal}-{akhir}: {result}")
    
    # Test untuk hari lain
    print("\nHARI LAIN:")
    test_cases_lain = [
        ("sab", 10, 12),
        ("min", 14, 16),
        ("", 7, 9),
    ]
    
    for hari, awal, akhir in test_cases_lain:
        result = SearchJadwal(hari, awal, akhir)
        print(f"  {hari} {awal}-{akhir}: {result}")

if __name__ == "__main__":
    test_jadwal()