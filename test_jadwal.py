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
        if akhir >= 7 and awal <= 10 and akhir <= 10:
            return "Dasar Sistem"
        elif akhir >= 15 and awal <= 16 and awal >= 15:   
            return "Bahasa Inggris I"
        elif akhir >= 7 and awal <= 16 :
            return "Dasar Sistem & Bahasa Inggris I"
        else :
            return "Tidak ada"
    elif hari == "kam" :
        if akhir >= 7 and awal <= 9 and akhir <= 9:
            return "Pancasila"
        elif akhir >= 13 and awal <= 15 and awal >= 13:
            return "Matematika I"
        elif akhir >= 7 and awal <= 15 : 
            return "Pancasila & Matematika I"
        else :
            return "Tidak ada"
    elif hari == "jum" :
        if akhir >= 7 and awal <= 9  and akhir <= 9:
            return "Bahasa Indonesia"
        elif akhir >= 13 and awal <= 16 and awal >= 13:
            return "Struktur Diskrit"
        elif akhir >= 7 and awal <= 16 :
            return "Bahasa Indonesia & Struktur Diskrit"
        else :
            return "Tidak ada"
    else :
        return "Tidak ada"

def test_all_scenarios():
    print("=== TESTING FUNGSI SearchJadwal ===\n")
    
    # Test cases untuk setiap hari
    test_cases = [
        # Senin - Dasar Pemrograman (13-15)
        ("sen", 13, 15, "Dasar Pemrograman"),
        ("sen", 12, 14, "Dasar Pemrograman"),
        ("sen", 14, 16, "Dasar Pemrograman"),
        ("sen", 10, 12, "Tidak ada"),
        ("sen", 16, 18, "Tidak ada"),
        
        # Selasa - Aljabar Linier (13-15)  
        ("sel", 13, 15, "Aljabar Linier"),
        ("sel", 12, 14, "Aljabar Linier"),
        ("sel", 14, 16, "Aljabar Linier"),
        ("sel", 10, 12, "Tidak ada"),
        ("sel", 16, 18, "Tidak ada"),
        
        # Rabu - Dasar Sistem (7-10) dan Bahasa Inggris I (15-16)
        ("rab", 7, 10, "Dasar Sistem"),
        ("rab", 8, 9, "Dasar Sistem"),
        ("rab", 15, 16, "Bahasa Inggris I"),
        ("rab", 7, 16, "Dasar Sistem & Bahasa Inggris I"),
        ("rab", 6, 11, "Dasar Sistem & Bahasa Inggris I"),  # Ini yang bermasalah
        ("rab", 14, 17, "Bahasa Inggris I"),
        ("rab", 11, 14, "Tidak ada"),
        ("rab", 17, 18, "Tidak ada"),
        
        # Kamis - Pancasila (7-9) dan Matematika I (13-15)
        ("kam", 7, 9, "Pancasila"),
        ("kam", 8, 8, "Pancasila"),
        ("kam", 13, 15, "Matematika I"),
        ("kam", 14, 14, "Matematika I"),
        ("kam", 7, 15, "Pancasila & Matematika I"),
        ("kam", 6, 16, "Pancasila & Matematika I"),  # Ini yang bermasalah
        ("kam", 10, 12, "Tidak ada"),
        ("kam", 16, 18, "Tidak ada"),
        
        # Jumat - Bahasa Indonesia (7-9) dan Struktur Diskrit (13-16)
        ("jum", 7, 9, "Bahasa Indonesia"),
        ("jum", 8, 8, "Bahasa Indonesia"),
        ("jum", 13, 16, "Struktur Diskrit"),
        ("jum", 14, 15, "Struktur Diskrit"),
        ("jum", 7, 16, "Bahasa Indonesia & Struktur Diskrit"),
        ("jum", 6, 17, "Bahasa Indonesia & Struktur Diskrit"),  # Ini yang bermasalah
        ("jum", 10, 12, "Tidak ada"),
        ("jum", 17, 18, "Tidak ada"),
        
        # Hari tidak valid
        ("sab", 10, 12, "Tidak ada"),
        ("min", 10, 12, "Tidak ada"),
        ("", 10, 12, "Tidak ada"),
    ]
    
    failed_tests = []
    
    for i, (hari, awal, akhir, expected) in enumerate(test_cases, 1):
        result = SearchJadwal(hari, awal, akhir)
        status = "✓" if result == expected else "✗"
        
        print(f"Test {i:2d}: {hari} {awal:2d}-{akhir:2d} -> {result}")
        print(f"         Expected: {expected}")
        print(f"         Status: {status}")
        print()
        
        if result != expected:
            failed_tests.append((i, hari, awal, akhir, expected, result))
    
    print(f"\n=== SUMMARY ===")
    print(f"Total tests: {len(test_cases)}")
    print(f"Passed: {len(test_cases) - len(failed_tests)}")
    print(f"Failed: {len(failed_tests)}")
    
    if failed_tests:
        print(f"\n=== FAILED TESTS ===")
        for test_num, hari, awal, akhir, expected, actual in failed_tests:
            print(f"Test {test_num}: {hari} {awal}-{akhir}")
            print(f"  Expected: {expected}")
            print(f"  Actual: {actual}")
            print()

if __name__ == "__main__":
    test_all_scenarios()