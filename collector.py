#17/05/2014
#faz download de arquivos do site wallbase.cc, ou de qualquer outro site.

from urllib.request import *
from threading import *

base_url = "http://wallpapers.wallbase.cc/rozne/wallpaper-%s.jpg"
download_folder = "C:/Users/Bruno Garcia/Desktop/wallbase collector/collection/"

def collect(start, final):
    
    for i in range(start, final):

        url = base_url % i

        try:
            request = urlopen(url)
        except:
	    #error 404
            continue    

        if(request.code == 200):

            with open(download_folder + str(i) + ".jpg" , "wb") as file:

                file.write(request.read())

                print(".")
				
#download de 1 milhao de imagens				
for i in range(2000000, 3000000, 100000):
    t = Thread(target = collect, args = (i, i + 100000)) 	
    t.start()

print("collect iniciado. \n ")       

