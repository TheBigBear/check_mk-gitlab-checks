#!/bin/bash 

status=`curl -s https://localhost/-/health --insecure`

if [[ $status == *OK* ]]; then
	echo "0 Gitlab_Health - $status"  
	else 
	echo "2 Gitlab_Health - $status" 
fi 
