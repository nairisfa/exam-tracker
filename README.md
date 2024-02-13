
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