
"""menu:
    1-İsme göre arama yap, roket isminin sonuçlarını getir
    2-Tarihe göre arama yap, tarih aralığı veya yıl içinde olan tüm roket fırlatmalarını getir
    3-Başarı durumuna göre arama yap:
        3-1: Launch success olan roketler
        3-2: Landing success olan roketler
        3-3: Reuse success olan roketler

#kullanılacak bilgiler:
    flight_number: 1-66 arası
    mission_name: fırlatma ismi
    land_success: karaya iniş başarısı
    reused: tekrar kullanılmış mı
    reuse parts: hangi bölümleri yeniden kullanılabilmiş
    launch_date_unix: timestamp olarak fırlatma tarihi
    launch_date_utc: greenwich zamanına göre fırlatma
    launch_date_local: yerel zaman göre fırlatma

# fonksiyonlar
    load(): api dan verileri çağırma işlemi
    search (): arama fonksiyonu, sçeilen işleme göre hangi value hangi key de aranmalı
            örneğin isim seçildiyse mission_name
            tarih seçildiyse launch_date
            başarı seçildiyse
                    1- launch success
                    2- land success
                    3- reuse success

    sonuc_goster(): işleme göre sonucu gösterme fonksiyonu
                    belki başarılı ise kutlamalı, başarısız ise üzgün surat falan olabilir.



log olarak kaydedilecek kısım:
    kullanıcının seçtiği işlem
    çağrılan veri
    gösterilen veri
"""

import requests
import json
import sys

class SpaceX():
    rocket_name = None
    launch_year = None
    launch_success = None
    rockets_list = []
    data = []

    def __init__(self):
        self.session = requests.session()
        while True:
            self.menu()

    def menu(self):
        print("Welcome")
        menu = self.kontrol(input("""Please select your operation.
                        1-Search by the rocket name 
                        2- Search by the launch year 
                        3-Search by the launch success    
                        4-for exit           
                          """))

        if menu == "1":
            rocket_name = input("Please write the rocket name you want to search")
            self.name_search(rocket_name)
        elif menu == "2":
            launch_year = input("Please write the year you want to search")
            self.year_search(launch_year)
        elif menu == "3":
            success_type = self.kontrol(input("""
                        1- Show rockets with launch success
                        2- Show rockets with land success
                        3- Show rockets with reuse success
                        """))
            self.rocket_success(success_type)
        elif menu == "4":
            #burada ne yaparsak while True calismayi birakir ?
            sys.exit("Byeeee")
        else:
            print("Error")


    def kontrol(self, key):
        if int(key.isnumeric()) and int(key)<5 and int(key)>=0 :
            return key
        else:
            key = input("Try again: ")
            return self.kontrol(key)

    def load(self):

        self.data = self.session.get('https://api.spacexdata.com/v2/launches/')
        content = self.data.content.decode("utf-8")
        self.data = json.loads(content)
        return self.data

    def name_search(self,keyword):
        self.load()
        exists = False
        for i in self.data:
            if i["mission_name"] == keyword:
                self.show_result(i)
                exists=True
        if exists ==False:
            print("No results found")


    def year_search(self,keyword):

        self.load()
        exists= False
        for year in self.data:
            if year['launch_year'] == keyword:
                self.show_result(year)
                exists=True
        if exists ==False:
            print("No results found")




    def show_result(self,i):

        value = i['flight_number']
        value2=i["mission_name"]
        value3=i["launch_year"]
        value4=i["rocket"]["rocket_name"]
        print(
            "flight number: {}  mission name: {} launch year: {} rocket name: {} ".format(value, value2, value3,
                                                                                          value4))
        #print(self.rockets_list)
        #self.rockets_list.append("flight number: {}  mission name: {} launch year: {} rocket name: {} ".format(value,value2,value3,value4))
        #print(self.rockets_list)

    #bu fonksiyona neden gerek duyduk ?
    def get_result(self):
        return self.data()


    #find land_success = True
    def success_control1(self, rocket):
        #ic ice liste ve sozluk oldugu icin rocket sozlugunun first_stage listesinde bir sozluk keyi olan land_successe ulasamadim, devam edicem
        ls=rocket.get("rocket").get("first_stage").get("cores")
        for roc in ls:
            icic = roc.get("land_success")
            if icic == True:
                return roc

    # find reused = True
    def success_control2(self, rocket):
        ls = rocket.get("rocket").get("first_stage").get("cores")
        for roc in ls:
            icic = roc.get("reused")
            if icic == True:
                return roc

    def rocket_success(self, success_type):
        self.load()
        if success_type == '1':
            print(list(filter(lambda rocket: rocket.get(ctype) == True, self.data)))

        elif success_type == '2':
            sonuc =list(filter(
                self.success_control1,
                self.data
            ))
            for all in sonuc:
                self.show_result(all)

        elif success_type == '3':
            sonuc = list(filter(
                self.success_control2,
                self.data
            ))
            for all in sonuc:
                self.show_result(all)


space = SpaceX()


# space.load()
# space.show_result()
# space.menu()
# space.load()

