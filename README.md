<div align="center">
    <h1>HTML Checker dengan Pushdown Automata (PDA)</h1>
    <h3>Tugas Pemrograman IF2124 Teori Bahasa Formal dan Otomata</h3>
    <p>oleh Kelompok satepadarman</p>
    
![Example screenshot](./logokelompok.png)
    <br/>
    <br/>
</div>

Sama seperti bahasa pada umumnya, HTML juga memiliki sintaks tersendiri dalam penulisannya yang dapat menimbulkan error jika tidak dipenuhi. Meskipun web browser modern seperti Chrome dan Firefox cenderung tidak menghiraukan error pada HTML memastikan bahwa HTML benar dan terbentuk dengan baik masih penting untuk beberapa alasan seperti Search Engine Optimization (SEO), aksesibilitas, maintenance yang lebih baik, kecepatan render, dan profesionalisme. 
Dibutuhkan sebuah program pendeteksi error untuk HTML. Oleh sebab itu, implementasikan sebuah program yang dapat memeriksa kebenaran HTML dari segi nama tag yang digunakan serta attribute yang dimilikinya. Pada tugas pemrograman ini, gunakanlah konsep Pushdown Automata (PDA) dalam mencapai hal tersebut yang diimplementasikan dalam bahasa Python. 

## Cara kompilasi program

Buka folder projek ini pada terminal lalu ketik command berikut:
```shell
python main.py pda.txt
```

**Note**: Apabila pada content tag div terdapat teks, ketik command dengan file PDA yang berbeda, yaitu:
```shell
python main.py pdaDivFormText.txt
```

## Dibuat oleh:
| NIM | Nama | Linkedin |
| :---: | :---: | :---: |
| 13522122 | Maulvi Ziadinda Maulana | [LinkedIn](https://www.linkedin.com/in/maulvizm/) |
| 13522161 | Mohamad Akmal Ramadan | [LinkedIn](https://www.linkedin.com/in/akmalrmn/) |
| 13522163 | Atqiya Haydar Luqman | [LinkedIn](https://www.linkedin.com/in/atqiyahaydar/) |
