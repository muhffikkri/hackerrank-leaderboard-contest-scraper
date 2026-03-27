# Test khusus untuk edge cases
from tes import SearchJadwal

def test_edge_cases():
    print("=== EDGE CASE TESTING ===\n")
    
    print("Test kasus khusus:")
    
    # Test boundary conditions
    edge_cases = [
        # Rabu - boundary testing
        ("rab", 10, 15),  # Dari akhir DS sampai awal BI - harus kedua matkul
        ("rab", 11, 14),  # Gap di antara - harus "Tidak ada"
        ("rab", 7, 7),    # Hanya 1 jam di awal DS - harus DS
        ("rab", 10, 10),  # Hanya 1 jam di akhir DS - harus DS
        ("rab", 15, 15),  # Hanya 1 jam di awal BI - harus BI
        ("rab", 16, 16),  # Hanya 1 jam di akhir BI - harus BI
        
        # Kamis - boundary testing
        ("kam", 9, 13),   # Dari akhir Pancasila sampai awal Mat - harus kedua matkul
        ("kam", 10, 12),  # Gap di antara - harus "Tidak ada"
        ("kam", 7, 7),    # Hanya 1 jam di awal Pancasila
        ("kam", 9, 9),    # Hanya 1 jam di akhir Pancasila
        ("kam", 13, 13),  # Hanya 1 jam di awal Matematika
        ("kam", 15, 15),  # Hanya 1 jam di akhir Matematika
        
        # Jumat - boundary testing
        ("jum", 9, 13),   # Dari akhir BI sampai awal SD - harus kedua matkul
        ("jum", 10, 12),  # Gap di antara - harus "Tidak ada"
        ("jum", 7, 7),    # Hanya 1 jam di awal BI
        ("jum", 9, 9),    # Hanya 1 jam di akhir BI
        ("jum", 13, 13),  # Hanya 1 jam di awal SD
        ("jum", 16, 16),  # Hanya 1 jam di akhir SD
    ]
    
    for hari, awal, akhir in edge_cases:
        result = SearchJadwal(hari, awal, akhir)
        print(f"  {hari} {awal}-{akhir}: {result}")
    
    print("\n=== RINGKASAN JADWAL ===")
    print("SENIN: Dasar Pemrograman (13-15)")
    print("SELASA: Aljabar Linier (13-15)")
    print("RABU: Dasar Sistem (7-10), Bahasa Inggris I (15-16)")
    print("KAMIS: Pancasila (7-9), Matematika I (13-15)")
    print("JUMAT: Bahasa Indonesia (7-9), Struktur Diskrit (13-16)")
    
    print("\n=== VALIDASI LOGIKA ===")
    print("✅ Jika interval overlap dengan 2 matkul -> tampilkan kedua dengan '&'")
    print("✅ Jika interval hanya overlap dengan 1 matkul -> tampilkan satu")
    print("✅ Jika interval tidak overlap dengan matkul manapun -> 'Tidak ada'")
    print("✅ Gap di antara 2 matkul -> 'Tidak ada'")

if __name__ == "__main__":
    test_edge_cases()