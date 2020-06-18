:warning: Kan zijn dat niet alles klopt!

## Forensic Analytics (zeker één vraag op 6 punten)

#### Stappen: 
* Checksum controlleren: $ md5sum image.dd  
                         $ cat image.dd.md5  (die oeten dezelfde resultaat geven. hetzelfde voor iender welke manier: sha1, sha512...)
* Wie:
* Wat:
* Waar:
* Wanneer:

:warning: Verschil tussen > en >> :
  $ echo hallo > hallo.txt                (hallo.txt: hallo)
  
  $ echo hallo weer > hallo.txt           (hallo.txt: hallo weer)
    
  $ echo nog een keer hallo >> hallo.txt  (hallo.txt: hallo weer
                                                      nog een keer hallo)
                                                      
    * tee writes output both on file and shows on terminal
                                                         
###### extended partitions:       disktype usbkey.dd                                             

###### non-DOS partition tables: mmls usbkey.dd

###### determine file system: disktype usbkey.dd  
                              (bijv --- usbkey.dd
Regular file, size 125.2 MiB (131252224 bytes)
DOS/MBR partition map
Partition 1: 125.1 MiB (131186688 bytes, 256224 sectors from 51)
  Type 0x3C (PartitionMagic recovery)
  Windows NTLDR boot loader
  NTFS file system
    Volume size 125.1 MiB (131186176 bytes, 256223 sectors)

###### File system information  (info used from disktype: file system and start sector) bijv fsstat usbkey.dd -f ntfs -o 51

:info:  Sector: Smallest Addressable Unit (mostly 512 bytes)
Cluster: Smallest Allocation Unit (equals to 1 or more sectors and the number of clusters depends on the file system).

###### Mounting file system read-only: 
                                       sudo mkdir /mnt/forensic  (sudo nodig als je werkt met /bestanden omdat die onder root zijn)
                                       sudo mount usbkey.dd /mnt/forensic -o loop,offset=$((51*512)) -r

###### Count regular files: find /mnt/forensic/ -type f | wc -l

###### Filesystem  Size  Used Avail Use% Mounted on: df -h /mnt/forensic

###### Search position of keywords: cat usbkey.dd | strings -td | egrep -i -f keywords.txt
                                    dd if=usbkey.dd skip=$((15393432/512)) count=1 | strings | grep Senor (lange nummer is offset van specifieke stuk dat we met vorige oneliner hebben gevonden)
                                    
###### Virusen : sudo clamscan -i -r /mnt/forensic/              
                                    
###### Rootkits: sudo rkhunter -r /mnt/forensic -c --report-warnings-only
