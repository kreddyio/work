<<COMMENT
DESCRIPTION: This is a program to list all the free ip addresses in your local subnet.
I have used an array here so that the addresses may be used later for some other purposes.
USAGE: You can invoke this shell script by using bash. You have to type "bash freeipfinder.sh startaddress endaddress"
AUTHOR: Kethu Harikishan Reddy
EMAIL: kishanreddy.kethu@gmail.com
COMMENT
#!/bin/bash
start=$1
end=$2
c=0
ip=$(/sbin/ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')
for (( i = 1; i < 4; i++ )); do
	sub[$i]=${ip%%.*}
	ip=${ip#*.*}
done
subnet=${sub[1]}.${sub[2]}.${sub[3]}
while [ $start -le $end ]
do
   nmap -sP -v $subnet.$start|grep "down" > /dev/null
	if [ "$?" -eq 0 ]; then
	        list[$c]=$subnet.$start #This is my local subnet address in my hostelroom. Bits-Goa \m/.
	        c=`expr $c + 1`
	fi
start=`expr $start + 1`
done
echo "Free ip's in your subnet are:"
for (( i = 0; i < c; i++ )); do
	echo ${list[$i]}
done
