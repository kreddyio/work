<<COMMENT
DESCRIPTION: This is a program to check the ip address assigned to the given interface.
AUTHOR: Kethu Harikishan Reddy
EMAIL: kishanreddy.kethu@gmail.com
COMMENT
echo "Please enter the interface for which you wish to check the ip for: (eth0 for ethernet and wlan0 for wireless generally)"
echo "You can also type in virtual adapter addresses like eth0:1 etc."
read i
res=$(/sbin/ifconfig $i | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')
echo "The ip assigned for $i is " $res