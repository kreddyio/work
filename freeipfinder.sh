<<COMMENT
DESCRIPTION: This is a program to list all the free ip addresses in your local subnet.
I have used an array here so that the addresses may be used later for some other purposes.
USAGE: You can invoke this shell script by using bash or sh. You have to type "bash freeipfinder.sh subnetadress(10.3.8) startaddress endaddress"
AUTHOR: Kethu Harikishan Reddy
EMAIL: kishanreddy.kethu@gmail.com
COMMENT
#!/bin/bash
subnet=$1
start=$2
end=$3
c=0
while [ $start -le $end ]
do
   nmap -sP -v $subnet.$start|grep "down" > /dev/null
	if [ "$?" -eq 0 ]; then
	        list[$c]=$subnet.$start #This is my local subnet address in my hostelroom. Bits-Goa \m/.
	        c=`expr $c + 1`
	fi
start=`expr $start + 1`
done
for (( i = 0; i < c; i++ )); do
	echo ${list[$i]}
done
