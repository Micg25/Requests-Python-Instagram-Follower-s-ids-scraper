# Requests-Python-Instagram-Follower-s-ids-scraper
instagram Followers' IDs scraper bot made with python-requests 

ITALIAN:
Spieghiamo due cose, il file "Standard-Requests IDs scraper for instagram" è la versione più a basso livello per fare scraping di follower da un profilo di instagram,
essa molto semplicemente fa richieste all'endpoint api del profilo stesso aggiornando il max_id (ovvero il valore dell'id massimo dalla quale dovrà cominciare il fetch successivo, ovvero la chiamata api successiva), il max id nel caso del codice "Standard" viene preso direttamente dai valori di risposta alla richiesta, ovvero nel json. Facendo però le chiamate in modo "normale" ho notato che non vengono presi tutti i follower di un profilo ma ne vengono saltati un numero variabile, ad esempio ho provato a fare scraping da un profilo con 389 follower, ne venivano fetchati in totale solo 340, ma a volte 339 o anche meno. Insomma, un numero variabile, ho notato che questo accadeva probabilmente perchè in chiamate differenti alcuni follower venivano ripetuti (anche qui non so il perchè). 
Per cercare di risolvere questo problema ho scritto l'altro codice che trovate nella repository, ovvero: "Requests IDs scraper for instagram" dove ho aggiunto il fatto che i follower vengono calcolati in due set di chunk differenti, in due modi differenti ovvero, nella seconda iterazione del ciclo for vengono presi come nella versione standard, mentre nella prima iterazione cambia il modo in cui il "max_id" viene calcolato, viene infatti, piuttosto che preso direttamente dalla risposta dell'api, cambiato con il valore della lunghezza corrente del nostro set, in modo tale da saltare meno follower possibili. Pure le condizioni di break del ciclo for sono differenti in base al set di chunk che stiamo prendendo. 
Cosi cambiando il codice sono riuscito a prendere più follower possibili da un profilo di quanto abbia fatto con tanti altri metodi (che potete trovare nel mio profilo se siete interessati, ho utilizzato: selenium, browsermob-proxy e instagrapi), purtroppo però non vengono ancora presi tutti, ne rimangono fuori circa 10, che in confronto ai 40+ di prima è una vittoria. Se avete trovato soluzioni che risolvono completamente il problema fatelo sapere!

Pacchetti necessari per avviare il codice: pip install requests

PS. Per fare funzionare il codice fare attenzione ad assegnare i vostri valori personali alle variabili contrassegnate con i commenti.



ENGLISH:
The file "Standard-Requests IDs scraper for Instagram" is the lower-level version used for scraping followers from an Instagram profile. It simply makes requests to the profile's API endpoint, updating the max_id (the maximum ID value from which the next fetch should start, i.e., the next API call). In the "Standard" code, the max_id is taken directly from the values in the API response JSON. However, when making requests in a "normal" manner, I noticed that not all followers from a profile were fetched; a variable number were skipped. For example, when trying to scrape a profile with 389 followers, only 340 were fetched in total—sometimes 339 or even fewer. The number varied.

I observed that this issue likely occurred because in different calls, some followers were repeated (although I'm not sure why). To try to resolve this problem, I wrote another script found in the repository called "Requests IDs scraper for Instagram". In this version, I adjusted how followers are collected in two sets of chunks using two different methods. In the second iteration of the for loop, followers are collected as in the standard version. In the first iteration, however, I changed how the max_id is calculated. Instead of being taken directly from the API response, it is changed to the current set length value to skip as few followers as possible.
I also modified the break conditions for the for loop based on which set of chunks we are collecting. By changing the code this way, I managed to collect more followers from a profile than with many other methods I've tried (which you can find in my profile if you're interested, including using Selenium, BrowserMob Proxy, and InstaGrapi). Unfortunately, however, not all followers are yet collected—about 10 are still left out, compared to more than 40 previously. It's a step forward.
If you have found solutions that completely solve this problem, please let me know!

Required packages to run the code: pip install requests

PS. Make sure to assign your own personal values to the variables marked with comments to make the code work.
