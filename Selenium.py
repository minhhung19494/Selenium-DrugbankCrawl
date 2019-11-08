from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

Lst_Co_so = []
Lst_Dia_chi = []
Lst_giay_phep = []
Lst_Loai_hinh = []
Lst_Pham_vi_KD = []
Trang = []
# code for install web driver: ChromeDriverManager().install()
#for lopp for change page
for page in range(1251,2055):
	driver = webdriver.Chrome('C:/Users/Min/.wdm/chromedriver/77.0.3865.40/win32/chromedriver.exe')
	driver.get('https://drugbank.vn/danh-sach/co-so-kinh-doanh?page=%d&size=20&sort=id,desc' %(page))

	L_Co_so = []
	L_Dia_chi = []
	L_giay_phep = []	
	L_Loai_hinh = []
	L_Pham_vi_KD = []
	
#Crawl table in 1 page
	for i in range(1,21):
		Co_so = driver.find_elements_by_xpath('/html/body/jhi-main/jhi-danh-sach/div[2]/div/div/table/tbody/tr[%d]/td[1]' %(i))
		Dia_chi = driver.find_elements_by_xpath('/html/body/jhi-main/jhi-danh-sach/div[2]/div/div/table/tbody/tr[%d]/td[2]' %(i))
		Giay_phep = driver.find_elements_by_xpath('/html/body/jhi-main/jhi-danh-sach/div[2]/div/div/table/tbody/tr[%d]/td[3]' %(i))
		Loai_hinh = driver.find_elements_by_xpath('/html/body/jhi-main/jhi-danh-sach/div[2]/div/div/table/tbody/tr[%d]/td[4]' %(i))
		Pham_vi_KD = driver.find_elements_by_xpath('/html/body/jhi-main/jhi-danh-sach/div[2]/div/div/table/tbody/tr[%d]/td[5]' %(i))
		L_Co_so += Co_so
		L_Dia_chi += Dia_chi
		L_giay_phep += Giay_phep
		L_Loai_hinh += Loai_hinh
		L_Pham_vi_KD += Pham_vi_KD
#Transform selenium into text and append to list
	num_item = len(L_Co_so)
	for a in range(num_item):
		Lst_Co_so.append(L_Co_so[a].text)
		Lst_Dia_chi.append(L_Dia_chi[a].text)
		Lst_giay_phep.append(L_giay_phep[a].text)
		Lst_Loai_hinh.append(L_Loai_hinh[a].text)
		Lst_Pham_vi_KD.append(L_Pham_vi_KD[a].text)
		Trang.append(str(num_item) + "-" + str(page))

	driver.close()
#List to dict
Final = {}

Final['Co_so'] = Lst_Co_so
Final['Dia_chi'] = Lst_Dia_chi
Final['Giay_phep'] = Lst_giay_phep
Final['Loai_hinh'] = Lst_Loai_hinh
Final['Pham_vi_KD'] = Lst_Pham_vi_KD
Final['Num_item'] = Trang
#dict to dataframe to file csv
df_Final = pd.DataFrame(Final)
df_Final.to_csv('output3.csv', encoding = 'utf-8')

