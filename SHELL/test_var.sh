#!/bin/bash
echo "Ievadi Decimalo skaitli"
read dec
echo -n "Binarais skaitlis ir $dec="

echo "obase=2; ibase=10; $dec" | bc
