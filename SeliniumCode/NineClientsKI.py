from SeleniumKI import selenium_KI_task

bitcoin_dog = "/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/div/table/tbody/tr[1]/td[1]/a/span"
presale_3 = "/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/div/table/tbody/tr[2]/td[1]/a/span"
bitbot_presale3 = "/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/div/table/tbody/tr[3]/td[1]/a/span"
memeinator_presale1 = "/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/div/table/tbody/tr[4]/td[1]/a/span"
crypto_monday_de = "/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/div/table/tbody/tr[5]/td[1]/a/span"
banks_less_times = "/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/div/table/tbody/tr[6]/td[1]/a/span"
coin_journal = "/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/div/table/tbody/tr[7]/td[1]/a/span"
invezz = "/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/div/table/tbody/tr[8]/td[1]/a/span"
presale4 = "/html/body/div[2]/div/div[2]/div/div/div[6]/div/div/div/table/tbody/tr[10]/td[1]/a/span"
kinetic_investments = "/html/body/div[2]/div/div/div/table/tbody/tr/td[1]/a/span/span"


list_items = [bitcoin_dog, presale_3, bitbot_presale3, memeinator_presale1, crypto_monday_de, banks_less_times, coin_journal, invezz, presale4]

for item in list_items:
    selenium_KI_task(item)

