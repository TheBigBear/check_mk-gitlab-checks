#!/bin/bash
 
status=`curl -s https://localhost/-/health --insecure`

if [[ $status == *OK* ]]; then
	echo "0 gitlab-health_check - $status" 2> /dev/null
	else 
	echo "2 gitlab-health_check - $status" 2> /dev/null
fi 

