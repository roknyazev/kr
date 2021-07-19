apt-get update
apt-get install net-tools
apt-get install python3 -y
apt install python3-pip -y
pip3 install requests
apt-get install build-essential -y
DEBIAN_FRONTEND='noninteractive' apt-get install cmake -y


pip3 install requests


fuser -k 10000/tcp
fuser -k 7070/tcp

for ((i=8000;i<8207;i++))
do 
fuser -k $i/tcp
done

cd router
sh start_router.sh
cd ../
cd hubs
sh start_hubs.sh

