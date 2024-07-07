import sqlite3

# Veritabanı bağlantısı oluşturma
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Users tablosunu oluşturma
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Örnek veri ekleme
cursor.execute("INSERT INTO users (name, email) VALUES ('admin', 'admin@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('user', 'user@example.com')")

# Değişiklikleri kaydetme ve bağlantıyı kapatma
conn.commit()
conn.close()

print("Veritabanı ve tablo başarıyla oluşturuldu.")
