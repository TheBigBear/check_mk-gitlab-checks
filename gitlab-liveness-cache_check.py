curl -s https://localhost/-/liveness --insecure | \
sed -e 's/[{}]/''/g' | \
awk -v k="text" '{n=split($0,a,","); for (i=1; i<=n; i++) print a[i]}' | \
sed ':a;N;$!ba;s/\n/\t/g' | \
sed -e 's/[:]/\t/g' | \
sed -e 's/["]//g'
