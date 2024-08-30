#!bin/bash

#use from '/' directory, proc needs to be accessable.
echo > 1 /proc/sys/net/ipv4/ip_forward
echo "ip fowarding complete@"
