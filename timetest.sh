#!/bin/bash
# despite trying to make it POSIX, it won't work with dash: "test_time.sh: 3: time: not found"
# as time is a builtin

# time1="$( { time -p sleep 0.01; } 2>&1)"
# time2="$( { time -p sleep 0.01; } 2>&1)"
# time3="$( { time -p sleep 0.01; } 2>&1)"

#r1="$(printf '%s' "$time1" | grep -oP 'real \K.*')"
#u1="$(printf '%s' "$time1" | grep -oP 'user \K.*')"
#s1="$(printf '%s' "$time1" | grep -oP 'sys \K.*')"
#r2="$(printf '%s' "$time2" | grep -oP 'real \K.*')"
#u2="$(printf '%s' "$time2" | grep -oP 'user \K.*')"
#s2="$(printf '%s' "$time2" | grep -oP 'sys \K.*')"
#r3="$(printf '%s' "$time3" | grep -oP 'real \K.*')"
#u3="$(printf '%s' "$time3" | grep -oP 'user \K.*')"
#s3="$(printf '%s' "$time3" | grep -oP 'sys \K.*')"
#
#printf '%s\n' "sum real=$(printf '%s\n' "$r1+$r2+$r3" |bc)"
#echo $r1
#echo $r2
#echo $r3

shopt -s expand_aliases

for i in {1..5}
do
  time_op="$( { time alice-cli pay alice --auth alice_password --amount 200000 --to http://charlie-node:7770/accounts/charlie/spsp; } 2>&1)"
  echo $time_op
done

