import random

users = [
    {'nama': 'Erlangga Adhya', 'username': 'erlanggaadhya', 'password': '1234', 'saldo': 200},
    {'nama': 'Seza Setyohadi','username': 'sezasetyohadi', 'password': '1234', 'saldo': 200},
    {'nama': 'Tiara Yoga','username': 'tiaraYoga', 'password': '1234', 'saldo': 200},
    {'nama': 'Yohanes Kevin','username': 'yohaneskevin', 'password': '1234', 'saldo': 200},
    {'nama': 'Dummy','username': 'a', 'password': '1', 'saldo': 200},
]


auth = {}

def init():
    onBoarding()

def title(title):
    print("".center(50,"-"))
    print(title.center(50))
    print("".center(50,"-"))

def body(text):
    print(text)

def alert(text):
    print(f" {text} ".center(50,"-"))
def onBoarding():
    title("🔥 Gachapon Force 🔥")
    body("Selamat Datang di Gachapon Force, Silahkan Login Terlebih Dahulu !")
    body("[1] Login\n[2] Registrasi\n[0] Exit")

    try :
        op = int(input("Masukan Pilihan [1/2/0]:"))
        if op == 1:
            login()
        elif op == 2:
            registrasi()
        elif op == 0:
            alert("⭐ Permainan Telah Berakhir⭐ ")
            exit()
        else:
            alert("Ketik [1/2/0]")
            onBoarding()
    except ValueError:
        alert("Input harus berupa angka. Silakan coba lagi.")
        onBoarding()

def login():
    global auth

    title("Login")

    username = input("Username : ")
    password = input("Password : ")

    for user in users :
        if (username == user['username']) & (password == user['password']):
            alert("Login Berhasil")
            auth = user
            dashboard()
            break

    else:
        alert("Login Gagal")
        onBoarding()

def registrasi():
    title("Registrasi")

    nama = input("Nama: ")
    username = input("Username : ")
    password = input("Password : ")

    for user in users:
        if username == user['username']:
            alert("Username Sudah Ada")
            return registrasi()

    users.append({
        'username': username,
        'password': password,
        'nama': nama,
        'saldo' : 50
    })
    alert("Registrasi berhasil, saldo gratis 50")
    login()

def dashboard():
  title("🔥 Gachapon Force 🔥")
  body(f"Selamat Datang {auth['nama']} di Gachapon Force")
  body("[1] Situs Gachapon\n[2] Tebak Berhadiah\n[3] Info Akun\n[0] Logout")

  op = int(input("Masukan Pilihan [1/2/3/0]:"))

  try :
    if op == 1:
        slot_gacor()
    elif op == 2:
        tebak_berhadiah()
    elif op == 3:
        info_akun()
    elif op == 0:
        onBoarding()
  except ValueError:
    alert("Input harus berupa angka. Silakan coba lagi.")
    dashboard()


def info_akun():
  title("Info Akun")

  body(f"Nama : {auth['nama']}\nUsername : {auth['username']}\nSaldo : {auth['saldo']}")
  body("[1] Deposit\n[2] Penarikan\n[0] Kembali")
  op = int(input("Masukan Pilihan [1/2/0]:"))
  if op == 1:
      jum = int(input("Masukkan nominal deposit: "))
      deposit(jum)
  elif op == 2:
      jum = int(input("Masukkan nominal penarikan: "))
      penarikan(jum)
  elif op == 0:
      dashboard()
  else :
      alert("input tidak valid")
      info_akun()

def deposit(jumlah):
    global auth
    auth['saldo'] += jumlah
    alert("Berhasil melakukan deposit")
    info_akun()

def penarikan(jumlah):
    if jumlah > auth['saldo']:
        alert("Saldo tidak mencukupi")
    else:
        auth['saldo'] -= jumlah
        print("Berhasil melakukan penarikan")
    info_akun()

SIMBOL = ["🍒", "🍉", "🍋"]
PELUANG = [0.4, 0.3, 0.3]

def putar_slot():

    a = random.choices(SIMBOL, PELUANG)[0]
    b = random.choices(SIMBOL, PELUANG)[0]
    c = random.choices(SIMBOL, PELUANG)[0]

    hasil = [a, b, c]
    print(hasil)
    return hasil

def cek_slot(hasil, taruhan):
    if hasil.count("🍒") == 3:
        return taruhan * 2
    elif hasil.count("🍉") == 3:
        return taruhan * 3
    elif hasil.count("🍋") == 3:
        return taruhan * 5
    else:
        return 0

def setelah_gacor():
    while True:
      body("[1] Coba lagi\n[2] Beralih tebak berhadiah\n[3] Info akun\n[0] Selesai")
      op = int(input("Masukan Pilihan [1/2/3/0]:"))
      if op == 1:
        slot_gacor()
      elif op == 2:
        alert("Anda beralih ke tebak berhadiah")
        tebak_berhadiah()
      elif op == 3:
        info_akun()
      elif op == 0:
        alert("Permainan slot diakhiri")
        dashboard()
        break
      else:
        alert("Lu salah input")

def slot_gacor():
    global auth

    title("🍋🍉🍒 Situs Gachapon 🍒🍉🍋")
    body(f"🍋🍉🍒 Selamat Datang di Situs Gachapon {auth['nama']} 🍒🍉🍋")
    body("Masukan taruhan untuk main, ketik 0 untuk kembali")

    while True:
      try:
        taruhan = int(input("Masukkan taruhan anda : "))
        break
      except ValueError:
        alert("Masukan harus angka!")

    if taruhan > auth['saldo']:
        alert("Saldo tidak cukup! Isi saldo dulu!")
        setelah_gacor()
    elif taruhan < 0:
        print("Minimal taruhan adalah 1!")
        return
    elif taruhan == 0:
      alert("minimal taruhan 1")
      slot_gacor()
    else:
        hasil = putar_slot()

        bonus = cek_slot(hasil, taruhan)

        if  bonus > 0:
            auth['saldo'] += bonus
            print(f"Selamat anda memenangkan {bonus}")
            setelah_gacor()

        else:
            auth['saldo'] -= taruhan
            print("Sayang anda kurang beruntung")
            print(f"Saldo anda sekarang {auth['saldo']} ")
            setelah_gacor()

def tebak_berhadiah():

    teams = ["Napoli", "AC Milan", "Chelsea", "Liverpool", "AS Roma", "Juventus"]
    leagues = ["Serie A", "Premier League"]
    matches = ["Napoli vs AC Milan",
            "Chelsea vs Liverpool",
            "AC Milan vs AS Roma",
            "AC Milan vs Juventus",
            "AS Roma vs Napoli"]

    random.shuffle(matches)
    title("🤔 Tebak Berhadiah")
    body(f"Selamat datang di Situs Tebak Berhadiah {auth['nama']}")

    body("Match List:")
    for i,match in enumerate(matches[:5]):
        print(f"[{i+1}] {match}")

    pick = int(input("Pilih Match: "))
    if pick > 0 and pick <= len(matches):

        match_parts = matches[pick-1].split(" vs ")

        taruhan = int(input(f"Masukkan jumlah taruhan: "))

        if taruhan <= auth['saldo']:
            auth['saldo'] -= taruhan

        elif taruhan > auth['saldo']:
            alert("Saldo tidak cukup! Isi saldo dulu!")
            setelah_nebak()

        body(f"Tebak siapa yang menang [1] {match_parts[0]} vs [2] {match_parts[1]} : ")

        while True:
          guess = int(input(f"Pilih [1/2] : "))

          winner = random.choice([1, 2])
          if guess == winner:
            alert(f"Selamat! Tim {match_parts[winner - 1]} menang!")
            auth['saldo'] += 2 * taruhan
            body(f"Saldo Anda sekarang: {auth['saldo']}")
            setelah_nebak()
            break

          else:
            alert(f"Sayang, pemenangnya adalah Tim {match_parts[winner - 1]}")
            body(f"Saldo Anda sekarang: {auth['saldo']}")
            setelah_nebak()
            break

        else:
          alert("Tim yang Anda pilih tidak valid")
          return

    else:
        alert("Nomor match tidak valid")
        tebak_berhadiah()

def setelah_nebak():
    while True:
        body("[1] Tebak Liga Lain\n[2] Beralih Permainan Gachapon\n[3] Info Akun\n[0] Kembali")
        op = int(input("Pilih [1/2/3/0]: "))

        if op == 1:
            tebak_berhadiah()
        elif op == 2:
            slot_gacor()
        elif op == 3:
            info_akun()
        elif op == 0:
            alert("Permainan Tebakan diakhiri")
            dashboard()
            break
        else:
            alert("Lu salah input")
            return
init()