#!/bin/bash 

#alias echo='{ save_flags="$-"; set +x;} 2> /dev/null; echo_and_restore'
#echo_and_restore() {
#        builtin echo "$*"
#        case "$save_flags" in
#         (*x*)  set -x
#        esac
#}
# 

status=`curl -s https://localhost/-/health --insecure`

if [[ $status == *OK* ]]; then
	echo "0 Gitlab_Health - $status"  
	else 
	echo "2 Gitlab_Health - $status" 
fi 
