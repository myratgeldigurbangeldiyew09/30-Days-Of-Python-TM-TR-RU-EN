# 2. Gün - Değişkenler ve Yerleşik Fonksiyonlar

# Değişken tanımlama
first_name = 'Myrat'
last_name = 'Gurbangeldiýew'
country = 'Turkmenistan'
age = 17
is_married = False
skills = ['Python', 'C++', 'C#']

# Tek satırda birden fazla değişken tanımlama
name, year, is_student = 'Myrat', 2026, True

# Yerleşik fonksiyon kullanımı
print('İsim:', first_name)
print('İsmin Uzunluğu:', len(first_name))
print('Yetenekler:', skills)

# Tip Dönüşümü (Type Casting)
num_str = '10'
num_int = int(num_str)
print('Dönüşüm:', type(num_str), '->', type(num_int))

# Float'ı Int'e dönüştürme
gravity = 9.81
print('Tam Sayı Hali:', int(gravity))  # Çıktı: 9
