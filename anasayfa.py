from Ui_MainWindow import Ui_AnaSayfa_

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time

cred = credentials.Certificate("serverkey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


class AnaSayfa(QMainWindow):
    def __init__(self):
        super(AnaSayfa, self).__init__()
        self.ui = Ui_AnaSayfa_()
        self.ui.setupUi(self)
        #köşeleri kaldır.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        
        #kapat, küçült, indir işlemleri
        self.ui.btn_maximize_restore.clicked.connect(self.pencereBuyut)
        self.ui.btn_close.clicked.connect(self.pencereKapat)
        self.ui.btn_minimize.clicked.connect(self.pencereIndir)
        
        #Pencere Sürükle Fonksiyon
        def pencereKaydir(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos()- self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        #Pencere Sürükle
        self.ui.label_title_bar_top.mouseMoveEvent = pencereKaydir
        ####### menüler arası geçiş #########
        #Sayfa Stok
        self.ui.btn_stokPaneli.clicked.connect(self.stokPanel)
        #Sayfa Home
        self.ui.btn_home.clicked.connect(self.anasayfa)
        #Sayfa Satış

        #işlem buton event
        self.ui.btn_satisPaneli.clicked.connect(self.satisYap)
        self.ui.btn_hizliSil.clicked.connect(self.HizliUrunSil)
        self.ui.btn_stokKaydiTamamla.clicked.connect(self.urunEkle)
        self.ui.btn_satisEkle.clicked.connect(self.satisEkle)
        self.ui.btn_satisTamam.clicked.connect(self.satisTamamla)
        
        self.ui.btn_stokUrunSil.clicked.connect(self.stokUrunSil)
        self.ui.btn_stokUrunGuncelle.clicked.connect(self.urunGuncelle)
        self.ui.cmb_guncellenecekBilgi.addItems(['Ürün Adı Bilgisi','Marka Bilgisi','Fiyat Bilgisi','Adet Bilgisi','Barkod Bilgisi'])
        self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_kullaniciAyar))
        
        #yüklemeler
        self.anasayfa()
        self.urunListele()

        
        
        
        #Hızlı erişime yüklenme aşamasında veri aktarımı
        #self.ui.tbl_hizliErisim.resizeRowsToContents()
    def anasayfa(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_hizliErisim)
        try:
            docs = db.collection("Urunler").get()
            self.ui.tbl_hizliErisim.setRowCount(len(docs))
            self.ui.tbl_hizliErisim.setColumnCount(6)
            self.ui.tbl_hizliErisim.setHorizontalHeaderLabels(('Ürün Adı','Marka','Fiyat','Adet','Barkod','Yüklenme Tarihi'))
            rowIndex =0
            for doc in docs:
                self.ui.tbl_hizliErisim.setItem(rowIndex,0,QTableWidgetItem(doc.to_dict()['urun_adi']))
                self.ui.tbl_hizliErisim.setItem(rowIndex,1,QTableWidgetItem(doc.to_dict()['marka']))
                self.ui.tbl_hizliErisim.setItem(rowIndex,2,QTableWidgetItem(str(doc.to_dict()['fiyat'])))
                self.ui.tbl_hizliErisim.setItem(rowIndex,3,QTableWidgetItem(str(doc.to_dict()['adet'])))
                self.ui.tbl_hizliErisim.setItem(rowIndex,4,QTableWidgetItem(doc.to_dict()['barkod']))
                self.ui.tbl_hizliErisim.setItem(rowIndex,5,QTableWidgetItem(str(doc.to_dict()['yuklenme_tarih'])))
                rowIndex+=1
        except Exception as e:
            print("Yüklenirken bir hata oluştu", e)
    def satisYap(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_satisPanel)
        self.ui.label_top_info.setText("Satış Paneli | Buradan satış işlemlerinizi halledebilirsiniz") 

    def urunListele(self):
        docs = db.collection("Urunler").get()
        self.ui.tbl_stok.setRowCount(len(docs))
        self.ui.tbl_stok.setColumnCount(6)
        self.ui.tbl_stok.setHorizontalHeaderLabels(('Ürün Adı','Marka','Fiyat','Adet','Barkod','Yüklenme Tarihi'))
        #Hızlı erişime yüklenme aşamasında veri aktarımı
        rowIndex =0
        for doc in docs:
            self.ui.tbl_stok.setItem(rowIndex,0,QTableWidgetItem(doc.to_dict()['urun_adi']))
            self.ui.tbl_stok.setItem(rowIndex,1,QTableWidgetItem(doc.to_dict()['marka']))
            self.ui.tbl_stok.setItem(rowIndex,2,QTableWidgetItem(str(doc.to_dict()['fiyat'])))
            self.ui.tbl_stok.setItem(rowIndex,3,QTableWidgetItem(str(doc.to_dict()['adet'])))
            self.ui.tbl_stok.setItem(rowIndex,4,QTableWidgetItem(doc.to_dict()['barkod']))
            self.ui.tbl_stok.setItem(rowIndex,5,QTableWidgetItem(str(doc.to_dict()['yuklenme_tarih'])))
            rowIndex+=1


        
    ############  Pencere işlemleri ###########
    #pencere büyütme
    def pencereBuyut(self):
        self.showMaximized()
    #pencere kapat
    def pencereKapat(self):
        self.close()
    #pencere indir
    def pencereIndir(self):
        self.showMinimized()     
    ##Uygulama için fonksiyonlar
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    #####Veritabanı işlemleri ###############33
    def urunEkle(self):
        try:
            ts=time.ctime(1424233311.771502)
            datas = {
                "urun_adi": self.ui.ln_stokAdEkle.text(),
                "marka": self.ui.ln_stokMarkaEkle.text(),
                "fiyat": int(self.ui.ln_stokFiyatEkle.text()),
                "adet": int(self.ui.sp_stokAdetEkle.text()),
                "barkod": self.ui.ln_stokBarkodEkle.text(),
                "yuklenme_tarih": str(ts)
        }
        #alınan verileri veritabanına yollar
            db.collection('Urunler').add(datas)
        except Exception as e:
            print("Veritabanı hatası: ",e)
        self.urunListele()
        self.ui.ln_stokAdEkle.clear()
        self.ui.ln_stokMarkaEkle.clear()
        self.ui.ln_stokFiyatEkle.clear()
        self.ui.sp_stokAdetEkle.clear()
        self.ui.ln_stokBarkodEkle.clear()
    def HizliUrunSil(self):
        for i in self.ui.tbl_hizliErisim.selectedItems():
            data = i.text()
            row = i.row()
        #self.ui.tbl_hizliErisim.removeRow(row) #ürünü tablodan manuel
        print(data)
        field ="urun_adi"
        try:
            docs = db.collection('Urunler').where(field, "==", data).get()
            for doc in docs:
                key=doc.id
                db.collection('Urunler').document(key).delete()          
        except Exception as e:
            print("ürün güncellerken hata oluştu hata kodu:", e)   
          
    def urunGuncelle(self):
        data = self.ui.ln_stokGuncelleAd.text()
        if data.isnumeric():
            field= "barkod"
        else:
            field ="urun_adi"
        bilgi = self.ui.cmb_guncellenecekBilgi.currentText()
        yeni_bilgi = self.ui.ln_stokYeniBilgi.text()

        if bilgi == "Ürün Adı Bilgisi":
            value = "urun_adi" 
        elif bilgi == "Marka Bilgisi":
            value = "marka"
        elif bilgi == "Fiyat Bilgisi":
            value = "fiyat"
            yeni_bilgi = int(yeni_bilgi)
        elif bilgi == "Adet Bilgisi":
            value = "adet"
            yeni_bilgi = int(yeni_bilgi)
        elif bilgi == "Barkod Bilgisi":
            value = "barkod"
        else:
            print("eşleşme bulunamadı")
        try:
            docs = db.collection('Urunler').where(field, "==", data).get()
            for doc in docs:
                key=doc.id
                db.collection('Urunler').document(key).update({value:yeni_bilgi})
            print("Güncelleme işlem tamam ")
        except Exception as e:
            print("ürün güncellerken hata oluştu hata kodu:", e)
        self.urunListele()
        self.ui.ln_stokYeniBilgi.clear()
        self.ui.ln_stokGuncelleAd.clear()
    def stokPanel(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_stokPanel)
        self.ui.label_top_info.setText("Stok Paneli | Buradan girdi-çıktı işlemlerinizi halledebilirsiniz")
        self.urunListele()
    def stokUrunSil(self):
        if self.ui.ln_stokSilAd.textChanged:
            field = "urun_adi"
            data = self.ui.ln_stokSilAd.text()
        else:
            field = "barkod"
            data = self.ui.ln_stokSil.text()
        try:
            docs = db.collection('Urunler').where(field, "==", data).get()
            for doc in docs:
                key=doc.id
                db.collection('Urunler').document(key).delete() 
            print("işlem tamam")        
        except Exception as e:
            print("ürün güncellerken hata oluştu hata kodu:", e)
        self.ui.ln_stokSilAd.clear()
        self.ui.ln_stokSil.clear()
        self.urunListele()
    def satisEkle(self):
        adet = self.ui.spin_adet.text()
        indirimOrani = self.ui.cmb_indirim.currentText()
        field ="barkod"
        data = self.ui.ln_satis_barkod.text()
        
        try:    
            satilacaklar = db.collection('Urunler').where(field, "==", data).get()
            #self.ui.tbl_satis_listele.setRowCount(len(satilacaklar))
            rowCount = self.ui.tbl_satis_listele.rowCount()
            for sat in satilacaklar:
                urunAdi=sat.to_dict()['urun_adi']
                fiyat=sat.to_dict()['fiyat']
            total = 0
            total = fiyat + total
            self.ui.ln_fiyat_goster.setText(str(total))
            print(urunAdi)
            print(fiyat)
            if urunAdi and adet is not None:
                if str(adet) =="2":
                    fiyat = fiyat *2
                elif str(adet) =="3":
                    fiyat = fiyat * 3
                    self.ui.tbl_satis_listele.setItem(rowCount,2,QTableWidgetItem(str(fiyat)))

                self.ui.tbl_satis_listele.insertRow(rowCount)
                self.ui.tbl_satis_listele.setItem(rowCount,0,QTableWidgetItem(urunAdi))
                self.ui.tbl_satis_listele.setItem(rowCount,1,QTableWidgetItem(str(adet)))
                self.ui.tbl_satis_listele.setItem(rowCount,2,QTableWidgetItem(str(fiyat)))
                self.ui.tbl_satis_listele.setItem(rowCount,3,QTableWidgetItem(indirimOrani))
        except Exception as e:
            print("hata var",e)
    def satisTamamla(self):

        rowCount = self.ui.tbl_satis_listele.rowCount()
        for i in range(rowCount):

            self.ui.tbl_satis_listele.setItem(i,0,QTableWidgetItem(""))
            self.ui.tbl_satis_listele.setItem(i,1,QTableWidgetItem(""))
            self.ui.tbl_satis_listele.setItem(i,2,QTableWidgetItem(""))
            self.ui.tbl_satis_listele.setItem(i,3,QTableWidgetItem(""))
        self.ui.ln_fiyat_goster.clear()
        self.ui.spin_adet.clear()
        self.ui.cmb_indirim.clear()
        self.ui.ln_satis_barkod.clear()


    

