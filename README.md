# shortest-path
## Deskripsi Singkat Program
## Penjelasan Singkat Algoritma A* yang Diimplementasikan
## Requirements dan Instalasi
### Instalasi
- Python 3
- Library matplotlib 
```shell 
pip install matplotlib
``` 
atau 
```bash
pip3 install matplotlib
```
- Library folium 
```bash 
pip install folium
``` 
atau
```
pip3 install folium
```
- Library networkx 
```
pip install networkx
``` 
atau 
```
pip3 install networkx
```
### Requirement
#### File requirement
```
jumlah node
(x1,y1)Kota X
(x2,y2)Kota Y
(x3,y3)Kota Z
0 0 1
0 0 0
1 0 0
```
**Note: koordinat sesuai dengan koordinat pada google map, dengan x adalah koordinat di sebelah kanan pada google map, dan y adalah koordinat di sebelah kiri pada google map. Pintu Depan ITB tertulis (-6.893164,107.610430) pada google map, maka ubahlah menjadi (107.610430,-6.893164) pada file input.**
#### Contoh File
```
15
(107.610430,-6.893164)Pintu Depan ITB
(107.611293,-6.893300)Masjid Salman ITB
(107.611949,-6.893594)Simpang3 Masjid Salman ITB
(107.611733,-6.894748)Jl Ciungwanara
(107.610154,-6.894768)Jl Gelap Nyawang
(107.609868,-6.893293)Jl Skanda
(107.608830,-6.894876)Jl Tamansari
(107.608441,-6.893875)Jl Tamansari 82
(107.608060,-6.891888)Kebun Binatang
(107.608095,-6.888586)Batan
(107.608332,-6.887800)Tikungan
(107.609947,-6.887704)Sabuga
(107.611456,-6.887379)Pintu Belakang ITB
(107.613555,-6.887409)Jl Dago
(107.612971,-6.893763)Jl Djuanda
0 1 0 0 0 1 0 0 0 0 0 0 0 0 0
1 0 1 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 1 0 0 0 0 0 0 0 0 0 0 1
0 0 1 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 1 1 0 0 0 0 0 0 0 0
1 0 0 0 1 0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 1 1 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0 1 0 1 0
0 0 0 0 0 0 0 0 0 0 0 0 1 0 1
0 0 1 0 0 0 0 0 0 0 0 0 0 1 0
```
## Cara Menggunakan Program
### Menjalankan melalui main.py
- Pastikan sudah berada di direktori src, kemudian ketikkan perintah berikut di terminal.
```
python3 main.py
```
atau
```
python main.py
```
- Kemudian masukkan input file.
- Pilih lokasi awal dan akhir.
- Pilih visualisasi (map atau graf).
- Jika memilih graf, gambar graf akan langsung dimunculkan.
- Apabila memilih map, gambar akan disimpan di map.html. Buka map.html di web browser.
### Contoh Input 
#### File
```
10
(107.641804,-6.946293)SAMSAT
(107.640250,-6.954075)Jl Margacinta
(107.641692,-6.954372)BRI
(107.647529,-6.954982)Jl Cipalago
(107.651788,-6.955439)BORMA
(107.655117,-6.955761)Samudra Bangunan
(107.643774,-6.944861)Universitas Islam Nusantara
(107.646891,-6.943967)Bengkel Motor
(107.648994,-6.944346)Cafe Resto
(107.648282,-6.950633)Jl Cijawura
0 1 0 0 0 0 1 0 0 0
1 0 1 0 0 0 0 0 0 0
0 1 0 1 0 0 0 0 0 0
0 0 1 0 1 0 0 0 0 1
0 0 0 1 0 1 0 0 0 0
0 0 0 0 1 0 0 0 0 0
1 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 1 0 1 0
0 0 0 0 0 0 0 1 0 1
0 0 0 1 0 0 0 0 1 0
```
#### Program
```
Lokasi awal	: Jl Margacinta
Lokasi tujuan	: Bengkel Motor
```
### Contoh Output
```
Jarak terdekat: 1.3613788178268975 km
Rute yang ditempuh:  Jl Margacinta -> SAMSAT -> Universitas Islam Nusantara -> Bengkel Motor
```
#### Graf
![Graf](https://github.com/mgstabrani/shortest-path/blob/main/img/graf.png)
#### Map
![Map](https://github.com/mgstabrani/shortest-path/blob/main/img/map.png)

## Author
- [M. Hilal Alhamdy (13519024)](https://github.com/hilalhmdy)
- [Mgs. Tabrani (13519122)](https://github.com/mgstabrani)
