
# Exam Tracker

Nama: Naila Nursa Krisnazulfa

NPM: 2306275071

Kelas: PBP A

Url proyek: http://naila-nursa-examtracker.pbp.cs.ui.ac.id/

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### [ ] Membuat sebuah proyek Django baru.

Siapkan sebuah folder baru bernama exam-tracker. Buat folder tersebut menjadi virtual environment (python -m venv env). Install module-module yang diperlukan terutama Django dengan pip install "nama module" atau dengan menggunakan sebuah file txt dan menggunakan perintah pip install -r "nama file". Setelah module berhasil diinstall, jalankan perintah "django-admin startproject exam_tracker .".

### [ ] Membuat aplikasi dengan nama main pada proyek tersebut.

Buat aplikasi main dengan perintah "python manage.py startapp main"

### [ ] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

Tambahkan aplikasi main pada list INSTALLED_APPS di file settings.py. Kemudian include "main.urls" pada urls.py agar aplikasi main terhubung dengan proyek exam_tracker.

### [ ] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.

Buat file models.py untuk menambahkan model pada aplikasi. Model harus berupa class yang meng-inherit class models.Model dari Django. Setelah itu tambahkan class attribute untuk menambahkan kolom baru, name yang berupa objek class CharField, grade yang berupa objek class IntegerField, dan description yang berupa objek class TextField.

### [ ] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

Siapkan sebuah template file html misal: main.html pada folder templates (buat baru jika belum ada) yang digunakan untuk menampilkan nama dan kelas. Agar nama dan kelas dapat kita ubah-ubah, gunakan ekspresi "{{ <expression> }}" agar Django dapat mengubah isi file html kita sesuai konteks yang diberikan. Setelah itu, buatlah sebuah fungsi yang menerima satu parameter "request" dan mereturn render(< nama file >.html)

### [ ] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

Di dalam urls.py, tambahkan sebuah pattern url dengan method path milik django. Parameter pertama berisi string yang berupa pattern untuk user mengakses laman yang kita inginkan, parameter kedua berisi fungsi yang merespons / mengontrol apa yang akan dikembalikan pada user, parameter setelahnya dapat kita isi untuk menambahkan informasi tambahan seperti parameter "name".

### [ ] Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Buatlah akun dan proyek baru di PWS. Inisiasi git pada folder di komputer kita untuk menjadikannya local git repository. Setelah itu lakukan add dan commit pada project tersebut, dan cocokkan branch utama menjadi branch master (jika branch utama belum bernama master) dengan perintah "git branch -M master". Lalu, lakukan push untuk mendeploy proyek ke PWS.
## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan](https://i.ibb.co/gwTcf5f/tugaspbp-drawio-2.png)


## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Agar setiap proyek yang kita buat dapat terisolasi dari proyek lain. Tujuannya, jika kita ingin membuat proyek baru dengan module yang telah diupdate, perubahan tersebut tidak akan memengaruhi proyek lama kita karena setiap module sudah terisolasi pada proyek tersebut. Seringkali, perubahan versi pada module yang lebih baru bisa saja menghilangkan fitur yang terdapat pada versi lawas, hal ini dapat menggangg fungsionalitas kode kita karena mungkin saja kita menggunakan fitur tersebut.
## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC: Model, View, Controller

Desain arsitektur web yang membagi fungsionalitas web menjadi tiga bagian: model, view, dan controller.

Model mengelola data aplikasi, termasuk menambah (create), mengambil (read), mengubah (update), dan menghapus (delete).
View mengelola tampilan yang akan diberikan pada user.
Controller mengelola apa yang akan ditampilkan pada pengguna.

MVT: Model, View, Template

Desain arsitektur web yang membagi fungsionalitas web menjadi tiga bagian: model, view, dan template.

Model mengelola data aplikasi, termasuk menambah (create), mengambil (read), mengubah (update), dan menghapus (delete).
View mengelola apa yang akan ditampilkan pada pengguna.
Template mengelola tampilan yang akan diberikan pada user.

MVVM: Model, View, ViewModel

Desain arsitektur web yang membagi fungsionalitas web menjadi tiga bagian: model, view, dan viewmodel.

Model mengelola data aplikasi, termasuk menambah (create), mengambil (read), mengubah (update), dan menghapus (delete).
View mengelola apa yang akan ditampilkan pada pengguna.
ViewModel menghubungkan / menjembatani antara view dengan model, sehingga interaksi yang terjadi pada view dapat berefek pada model.

Perbedaan antara MVC dan MVT hanya terletak pada penamaan. Sementara antara MVC dan MVT dengan MVVM terletak pada cara kedua desain mengatur hubungan antara model dengan tampilan. Jika pada MVC dan MVT controller atau view hanya memberikan informasi dan tidak berinteraksi langsung dengan model ataupun tampilan, pada MVVM viewmodel ter-bind langsung dengan view (tampilan) dan model.


# Tugas 5

## 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
#### Selektor Tunggal (elementname):
Manfaat: memilih semua elemen yang sesuai namanya.

Waktu yang tepat untuk digunakan: menerapkan style tertentu pada semua elemen di kode

#### Selektor Kelas (.classname):

Manfaat: memilih semua elemen yang memiliki value dari atribut class yang sama.

Waktu yang tepat untuk digunakan: saat ingin menerapkan style yang sama pada beberapa elemen yang sama, tetapi tidak semua elemen.

#### Selektor ID (#idname):
Manfaat: memilih elemen tertentu secara spesifik. Selektor ini memilih elemen dengan ID yang cocok.

Waktu yang tepat untuk digunakan: saat ingin menerapkan style tertentu pada suatu elemen spesifik.

##### Selektor Universal (*):
Manfaat: memilih semua elemen dalam dokumen.

Waktu yang tepat untuk digunakan:saat ingin menerapkan base style pada kode

#### Selektor Grup (,):
Manfaat: membuat beberapa selektor menjadi satu aturan CSS

Waktu yang tepat untuk digunakan: menerapkan style yang sama pada elemen yang berbeda
 

## 2. Jelaskan HTML5 Tag yang kamu ketahui
#### header: 
Digunakan untuk menentukan bagian atas dari sebuah halaman web.

#### section: 
digunakan unuk mengelompokkan section yang berhubungan.

#### footer: 
Menandakan bagian paling bawah dari sebuah halaman web. 

#### div:
digunakan untuk menegelompokkan konten dalam dokumen HTML. 

#### main: 
Menunjukkan konten yang utama dari web.

#### body:
menunjukkan isi konten web

## 3. Jelaskan perbedaan antara margin dan padding
Margin menentukan ruang yang berada di luar batas elemen, seperti mengontrol jarak antara elemen dengan elemen lainnya.Sementara itu, padding menentukan ruang yang berapa di antara batas elemen dan konten yang ada di dalamnya, seperti mengatur jarak antara konten dengan batas elemen. .

## 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
komponen tailwind lebih spesifik, tidak siap pakai seperti bootstrap. Bootstrap cocok untuk prototyping. bootstrap berdasarkan functionality, sedangkan tailwind berdasarkan karakterisitik dan jauh lebih bebas. Bootstrap Bootstrap lebih cocok untuk proyek yang berdasarkan prototyping ada menginginkan style yang konsisten, sedangkan tailwind cocok digunakan untuk design yang lebih spesifik dan bebas. 

# Tugas 6

### 1.  Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
Synchronous programming mengeksekusi program secara brurutan,. setiap tugas yang ada akan berjalan berurutan menunggu tugas sebelumnya selesai berjalan yang dapat menyebabkan program terblokir saat menunggu operasi Input/Output selesai. Sedangkan, asynchronous programming memungkinkan eksekusi tugas-tugas yang membutuhkan waktu lama untuk dilakukan secara non-blokir, memungkinkan program untuk melanjutkan eksekusi tugas-tugas lain sementara menunggu hasil operasi Input/Output, sehingga membuat program lebih responsif dan efisien. 

### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini

Event-driven programming adalah sebuah paradigma pemrograman dimana flow program ditentukan oleh event eksternal. Program akan berjalan dan bereaksi sesuai event yang ditrigger oleh user / API, sehingga program akan berjalan lebih dinamis sesuai data yang didapat. Penerapan dari event-driven programming pada tugas ini adalah dalam penggunaan AJAX untuk melakukan CRUD data dari database. Pemanggilan fetch dalam program merupakan salah satu bentuk event-driven programming karena web akan berubah sesuai data yang diterima, jika user menambahkan data baru tampilan web akan berubah.

### 3. Jelaskan penerapan asynchronous programming pada AJAX.

Dalam penggunaan di program ini, konsep AJAX yang digunakan menggunakan Promise dan async-await. Penerapan konsep asynchronous dalam program yaitu terdapat dalam fetching data dari database (GET) dan penulisan data ke database (POST). Pemanggilan data dari database menggunakan fungsi fetch yang ditaruh didalam fungsi async, kemudian menggunakan keyword then untuk mengeksekusi data jika fetch telah mengembalikan data. Dalam penampilan data tsb, kita menggunakan keyword await agar program menunggu jika fetch telah mengambil data. Dalam penulisan data baru, program akan menggunakan fungsi fetch dengan method POST, dan akan menggunakan keyword then kembali untuk memanggil fungsi callback agar menampilkan data yang telah diupdate.

### 4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

jQuery merupakan sebuah library yang dibangun untuk mempermudah developer dalam melakukan pengolahan DOM dan pemanggilan API. Sementara, Fetch API merupakan fungsi bawaan dari javascript agar devoper dapat memanggil API dari dalam program. Kelebihan teknologi jQuery adalah kemudahan yang ditawarkannya karena library tersebut telah melakukan banyak abstraksi sehingga developer tidak perlu mengatur banyak konfigurasi untuk memanggil API. Sementara fetch dari bawaan javascript memiliki kelebihan lebih cepat dan efisien, tetapi kekurangannya sistem fetch memerlukan konfigurasi lebih banyak dan pemahaman akan asynchronous programming agar dapat melakukan pemanggilan API dengan baik.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.

##### AJAX GET
Agar dapat mendukung Ajax GET, kita harus mengubah kode pada yang sebelumnya menggunakan for bawaan django menjadi menggunakan JavaScript. Card tersebut pertama-tama harus kita buat menggunakan createElement dan menambahkan class serta innerHTML sesuai dengan html sebelumnya yang terdapat pada file. Kemudian kita me-wrap html tersebut dengan forEach loop menggunakan data yang telah diambil. Setelah card dibuat, kita mengappendChild card tersebut ke div yang memang digunakan untuk menjadi container dari cards tersebut.

##### AJAX POST
Agar dapat mendukung Ajax POST, kita harus mengimplementasi fungsi baru yang terdapat fungsi fetch didalamnya. Didalam fungsi fetch tersebut, kita menambahkan parameter method=POST agar method yang digunakan dalam pemanggilan API adalah POST. Setelah itu, kita akan menambahkan form baru yang terdapat di dalam halaman, berupa modal yang nantinya dapat digunakan oleh user untuk menambahkan data baru. Setelah itu kita hubungkan modal dengan menambahkan callback onclick pada button di modal tsb.

#### Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.

Kita dapat menambahkan view baru tersebut ke views.py. Dalam fungsi view tersebut, kita harus mengecek apakah request yang diberikan bermethod POST atau bukan, setelah itu kita ambil data dari form yang diberikan dan kemudian nantinya kita buat instance baru dari data dan melakukan save. Kemudian kita akan mengembalikan HttpResponse yang sesuai.

#### Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.

Tambahkan path baru pada urls.py kemudian hubungkan dengan view yang baru kita buat dengan mengimportnya.

#### Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/

Telah dijelaskan di bab AJAX POST.

#### Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.

Kita dapat menggunakan method then pada fungsi fetch untuk menambahkan callback function jika data berhasil ditambahkan. Fungsi callback tersebut dapat kita isi menggunakan fungsi refresh data yang telah kita buat sebelumnya ketika mengimplementasi AJAX GET.