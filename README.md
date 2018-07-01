# Ip-adresses-range-by-country
Sqlite3 database containing all the known IP ranges with the registration country 

You can use this database for searching some ip ranges and get the country of origin. 



![alt text](https://github.com/HAL68000/Ip-adresses-range-by-country/blob/master/Screenshot.jpg)

Note:
Before begin unpack ipdatabaseipv4.zip in the same directory 

Utility included 
----------------------------------------------------------------------------------------------------------------------------
ipdb.py 

Ip Database filler utility v1.0

-------------------------------------------------------------------------------------------------------------
Fill the database with whois information
-------------------------------------------------------------------------------------------------------------
Example usage
ipdb.py -ip 200. -country US (scan all the US ip address starting with 200.)
Note: You can also use a more narrow range like 200.62.21. 
ipdb.py -country US  (scan all the US ip ranges... Maybe a bad idea)
ipdb.py -country ALL -ip 200 -sleep 5 (scan all the ip starting with 200. and wait 5 seconds between requests)
ipdb.py -country ALL (scan all the ip ranges... This will take it forever :P )

You can use this tool to fill the database with the whois public information. 

This code will need python 2.7
The following libraries are necessary: 


dataset   https://dataset.readthedocs.io/en/latest/         pip install dataset

stuf      https://pypi.org/project/stuf/                    pip install stuf

ipwhois   https://github.com/secynic/ipwhois                pip install ipwhois

argparse  https://pypi.org/project/argparse/                pip install argparse

-----------------------------------------------------------------------------------------------------------------------------
Donate:

Bitcoin       1NKNbzm3tkCsosg4U9hsg291RpYo8UiTpf

Bitcoin Cash  qprdq7rwat0flqplcyuxkvq2jsvnta09tglsq9379u

Litecoin      Lc8ccuUcScFZTvZL5WMEewREDwnZ4X89yV

Contact me at hal68000@protonmail.com

Use this with absolutely no warranty.
Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and I am are not responsible for any damage or data loss incurred with their use.
