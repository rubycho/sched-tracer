#! /bin/bash
rosnode list |
	while read -r line
	do
		rosnode info $line | grep 'Pid'
	done
