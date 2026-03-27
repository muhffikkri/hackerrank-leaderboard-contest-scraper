# Test untuk input ekstrem dan tidak valid
from tes import SearchJadwal

def test_invalid_inputs():
    print("=== TESTING INPUT EKSTREM ===\n")
    
    # Test dengan nilai waktu ekstrem
    extreme_cases = [
        ("sen", 0, 24),   # Seluruh hari
        ("rab", 0, 24),   # Seluruh hari - harus kedua matkul
        ("kam", 0, 24),   # Seluruh hari - harus kedua matkul
        ("jum", 0, 24),   # Seluruh hari - harus kedua matkul
        ("sen", 15, 13),  # Waktu terbalik (akhir < awal)
        ("rab", 20, 5),   # Waktu terbalik ekstrem
        ("sen", 13, 13),  # Waktu sama (1 jam tepat)
        ("sen", 14, 14),  # Waktu sama di tengah matkul
        ("rab", 8, 8),    # 1 jam di tengah Dasar Sistem
        ("rab", 15, 15),  # 1 jam tepat Bahasa Inggris I
    ]
    
    print("Test input ekstrem:")
    for hari, awal, akhir in extreme_cases:
        result = SearchJadwal(hari, awal, akhir)
        print(f"  {hari} {awal}-{akhir}: {result}")
    
    print("\n=== FINAL VALIDATION ===")
    
    # Validasi bahwa semua skenario bekerja dengan benar
    correct_cases = [
        ("rab", 7, 16, "Dasar Sistem & Bahasa Inggris I"),  # Overlap kedua
        ("rab", 11, 14, "Tidak ada"),                       # Gap
        ("kam", 7, 15, "Pancasila & Matematika I"),         # Overlap kedua
        ("kam", 10, 12, "Tidak ada"),                       # Gap
        ("jum", 7, 16, "Bahasa Indonesia & Struktur Diskrit"), # Overlap kedua
        ("jum", 10, 12, "Tidak ada"),                       # Gap
    ]
    
    print("Validasi kasus penting:")
    all_correct = True
    for hari, awal, akhir, expected in correct_cases:
        result = SearchJadwal(hari, awal, akhir)
        status = "✅" if result == expected else "❌"
        print(f"  {status} {hari} {awal}-{akhir}: {result} (expected: {expected})")
        if result != expected:
            all_correct = False
    
    print(f"\n{'🎉 SEMUA TEST PASSED!' if all_correct else '⚠️ ADA TEST YANG FAILED!'}")

if __name__ == "__main__":
    test_invalid_inputs()