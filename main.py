import tkinter as tk
from tkinter import ttk

columns = [
    'Model', 'Marka', 'Fiyat', 'Vites', 'Yakıt', 'Motor Hacmi', 'Aktarma', 'Horsepower',
    'Rehin', 'Haciz', 'Muayene', 'Yıl', 'Km', 'Kullanım Alanı', 'Renk', 'Son Hız',
    'Bagaj Hacmi', '0-100', 'Max Tork', 'Silindir', 'Depo', 'Tüketim', 'Sübap','Hasar Bilgi'
]
def open_detail_page(car):
    # Ayrı bir pencere oluştur
    detail_window = tk.Toplevel()
    detail_window.title("Araç Detayları")

    # Araç hakkındaki bilgileri pencereye ekle
    for key, value in car.items():
        label = tk.Label(detail_window, text=f"{key}: {value}")
        label.pack()

    detail_window.mainloop()
# Verileri okuma ve filtreleme fonksiyonu
def filter_by_year():
    selected_year = year_var.get()  # Seçilen yılı al

    # Seçilen yıla göre filtreleme
    filtered_cars = [car for car in data if car['yıl'] == selected_year]

    # UI temizleme
    for i in treeview.get_children():
        treeview.delete(i)

    # Filtrelenmiş verileri sütun halinde göster
    for car in filtered_cars:
        values = [car.get(col.replace(' ', '_').lower(), '') for col in columns]  # Her sütun için değerleri al
        treeview.insert('', 'end', values=values)  # Sütunlara ekleme
        button = ttk.Button(treeview, text="İncele", command=lambda event=None, car=car: open_detail_page(car))
        button.grid(row=treeview.index('end'), column=12, sticky='w')
        button.winfo_width()
        button.winfo_height()

        
        
       
    


# Verileri metin dosyasından okuma ve düzgünce sözlük oluşturma
with open('output.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

data = []
for line in lines:
    parts = line.strip().split(';')
    

    car = {
        'model': parts[0],
        'marka': parts[1],
        'fiyat': parts[2],
        'vites': parts[3],
        'yakıt': parts[4],
        'motor_hacmi': parts[5],
        'aktarma': parts[6],
        'horsepower': parts[7],
        'rehin': parts[8],
        'haciz': parts[9],
        'muayene': parts[10],
        'yıl': parts[11],
        'km': parts[12],
        'kullanım_alanı': parts[13],
        'renk': parts[14],
        'son_hız': parts[15],
        'bagaj_hacmi': parts[16],
        '0-100': parts[17],
        'max_tork': parts[18],
        'silindir': parts[19],
        'depo': parts[20],
        'tüketim': parts[21],
        'sübap': parts[22]
    }
    #print(car)  # Oluşturulan sözlükleri kontrol etmek için
    data.append(car)


# TKinter penceresi oluşturma
root = tk.Tk()
root.title("Araç Filtreleme")

# Sütun başlıkları


# Yıl dropdown menüsü oluşturma
years = list(set(car['yıl'] for car in data))  # Verilerden yılları al
year_var = tk.StringVar(root)
year_var.set(years[0])  # Başlangıçta ilk yılı seçili yap

year_label = tk.Label(root, text="Filtreleme Yılı:")
year_label.pack()

year_dropdown = tk.OptionMenu(root, year_var, *years)
year_dropdown.pack()

# Filtreleme düğmesi
filter_button = tk.Button(root, text="Filtrele", command=filter_by_year)
filter_button.pack()

# Veri görüntüleme widget'ı oluşturma (Treeview kullanacağız)
treeview = ttk.Treeview(root, columns=columns, show='headings')

# Sütun başlıklarını ayarlama
for col in columns:
    treeview.heading(col, text=col)
    
treeview.pack()

root.mainloop()
