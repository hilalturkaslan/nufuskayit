from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import mysql.connector
class nufusKayit(QDialog):
    def __init__(self,parent=None):
        super(nufusKayit,self).__init__(parent)
        grid=QGridLayout()
        grid.addWidget(QLabel("Ad-Soyad"),0,0)
        grid.addWidget(QLabel("Sınıf"),1,0)
        grid.addWidget(QLabel("T.C. Kimlik No"),2,0)
        grid.addWidget(QLabel("Memleket"),3,0)
        grid.addWidget(QLabel("Cinsiyeti"),4,0)
        grid.addWidget(QLabel("Dogum Tarihi"),5,0)

        self.adi=QLineEdit()
        self.sinif=QLineEdit()
        self.kimlikNo=QLineEdit()
        self.memleket=QLineEdit()
        self.erkek=QRadioButton("Erkek")
        self.kadin=QRadioButton("Kadın")
        self.cinsiyet=QButtonGroup(self)
        self.cinsiyet.addButton(self.erkek)
        self.cinsiyet.addButton(self.kadin)
        self.tarih=QDateEdit(calendarPopup=True)
        temizle=QPushButton("Temizle")
        temizle.clicked.connect(self.temizle)
        kaydet=QPushButton("Kaydet")
        kaydet.clicked.connect(self.kaydet)
        kayitAktar=QPushButton("Kaydı Aktar")
        kayitAktar.clicked.connect(self.kayitAktar)

        grid.addWidget(self.adi,0,1)
        grid.addWidget(self.sinif,1,1)
        grid.addWidget(self.kimlikNo,2,1)
        grid.addWidget(self.memleket,3,1)
        grid.addWidget(self.erkek,4,1)
        grid.addWidget(self.kadin,4,2)
        grid.addWidget(self.tarih,5,1)
        grid.addWidget(temizle,6,0)
        grid.addWidget(kaydet,6,1)
        grid.addWidget(kayitAktar,0,3,5,1)

        grid.addWidget(QLabel("Ad-Soyad"),0,4)
        grid.addWidget(QLabel("Sınıf"),1,4)
        grid.addWidget(QLabel("T.C. Kimlik No"),2,4)
        grid.addWidget(QLabel("Memleket"),3,4)
        grid.addWidget(QLabel("Cinsiyeti"),4,4)
        grid.addWidget(QLabel("Doğum Tarihi"),5,4)

        self.adiLabel=QLabel()
        self.sinifLabel=QLabel()
        self.kimlikLabel=QLabel()
        self.memleketLabel=QLabel()
        self.cinsiyetLabel=QLabel()
        self.tarihLabel=QLabel()

        grid.addWidget(self.adiLabel,0,5)
        grid.addWidget(self.sinifLabel,1,5)
        grid.addWidget(self.kimlikLabel,2,5)
        grid.addWidget(self.memleketLabel,3,5)
        grid.addWidget(self.cinsiyetLabel,4,5)
        grid.addWidget(self.tarihLabel,5,5)

        oncekiKayit=QPushButton("Bir Önceki Kayıt")
        oncekiKayit.clicked.connect(self.oncekiKayit)
        sonrakiKayit=QPushButton("Bir sonraki Kayıt")
        sonrakiKayit.clicked.connect(self.sonrakiKayit)
        grid.addWidget(oncekiKayit,6,4)
        grid.addWidget(sonrakiKayit,6,5)
        self.setLayout(grid)
        self.setWindowTitle("Nüfus Kayıt Programı")
        self.resize(800,400)
    def temizle(self):
        self.adi.setText("")
        self.sinif.setText("")
        self.kimlikNo.setText("")
        self.memleket.setText("")
        self.tarih.clear()
    def kaydet(self):
        adi=self.adi.text()
        sinif=self.sinif.text()
        kimlikNo=self.kimlikNo.text()
        memleket=self.memleket.text()
        tarih=self.tarih.date()
        t=tarih.toPyDate()
        cinsiyet=""
        if self.erkek.isChecked()==True:
            cinsiyet="Erkek"
        elif self.kadin.isChecked()==True:
            cinsiyet="Kadın"
        baglanti=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="programlama2")
        isaretci=baglanti.cursor()
        isaretci.execute('''INSERT INTO nufusKayit(adSoyad,sinif,kimlikNo,memleket,cinsiyet,tarih)
VALUES ("%s","%s","%s","%s","%s","%s")'''%(adi,sinif,kimlikNo,memleket,cinsiyet,t))
        baglanti.commit()
        baglanti.close()
    def kayitAktar(self):
        adi=self.adi.text()
        sinif=self.sinif.text()
        kimlikNo=self.kimlikNo.text()
        memleket=self.memleket.text()
        cinsiyet=""
        if self.erkek.isChecked()==True:
            cinsiyet="Erkek"
        elif self.kadin.isChecked()==True:
            cinsiyet="Kadın"
        tarih=self.tarih.date()
        t=tarih.toPyDate()
        tarih=str(t)
        self.adiLabel.setText(adi)
        self.sinifLabel.setText(sinif)
        self.kimlikLabel.setText(kimlikNo)
        self.memleketLabel.setText(memleket)
        self.cinsiyetLabel.setText(cinsiyet)
        self.tarihLabel.setText(tarih)
    def oncekiKayit(self):
        if self.kimlikLabel.text():
            kimlikNo=self.kimlikLabel.text()
            baglanti=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="programlama2")
            isaretci=baglanti.cursor()
            isaretci.execute('''SELECT ID FROM nufusKayit WHERE kimlikNo="%s" '''%kimlikNo)
            row=isaretci.fetchall()#[[25]]
            for r in row:#[25]
                res=int(''.join(map(str,r)))#25
                res=res-1#24
                isaretci.execute('''SELECT * FROM nufusKayit WHERE ID="%s"'''%res)
                gelenler=isaretci.fetchall()#[[can,111,515,515]]
                for row in gelenler:#[can,111,515,515]
                    self.adiLabel.setText(row[1])#can
                    self.sinifLabel.setText(row[2])
                    self.kimlikLabel.setText(row[3])
                    self.memleketLabel.setText(row[4])
                    self.cinsiyetLabel.setText(row[5])
                    self.tarihLabel.setText(row[6])
            baglanti.close()
    def sonrakiKayit(self):
        if self.kimlikLabel.text():
            kimlikNo=self.kimlikLabel.text()
            baglanti=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="programlama2")
            isaretci=baglanti.cursor()
            isaretci.execute('''SELECT ID FROM nufusKayit WHERE kimlikNo="%s" '''%kimlikNo)
            row=isaretci.fetchall()#[[25]]
            for r in row:#[25]
                res=int(''.join(map(str,r)))#25
                res=res+1#24
                isaretci.execute('''SELECT * FROM nufusKayit WHERE ID="%s"'''%res)
                gelenler=isaretci.fetchall()#[[can,111,515,515]]
                for row in gelenler:#[can,111,515,515]
                    self.adiLabel.setText(row[1])#can
                    self.sinifLabel.setText(row[2])
                    self.kimlikLabel.setText(row[3])
                    self.memleketLabel.setText(row[4])
                    self.cinsiyetLabel.setText(row[5])
                    self.tarihLabel.setText(row[6])
            baglanti.close()
uyg=QApplication([])
pencere=nufusKayit()
pencere.show()
uyg.exec_()
