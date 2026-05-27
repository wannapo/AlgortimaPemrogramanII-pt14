def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - 1 - i):
            if arr[j].lower() > arr[j + 1].lower():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        if not swapped:
            break
            
    return arr

if __name__ == "__main__":
    nama_peserta = ["Rifqi", "Andi", "Citra", "Budi", "Dewi", "Eko", "Zaki", "Fahmi"]
    
    print(f"List asli: {nama_peserta}")
    
    sorted_list = bubble_sort(nama_peserta)
    
    print(f"List setelah diurutkan: {sorted_list}")
