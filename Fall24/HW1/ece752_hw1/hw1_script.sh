# ECE 752 HW 1
# The following is shell script to automate the running of all the 14 test cases#


## TO RUN ##
# $chmod +x hw1_script.sh
# $./hw1_script.sh

#!/bin/bash

# Print a message to indicate the script is starting
echo "Starting the script..."

echo "Starting Test Case1"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'TimingSimpleCPU' '1GHz' 'DDR3_1600_8x8' '500000'

echo "saving test case1"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_01.txt

echo "Starting Test Case2"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'TimingSimpleCPU' '2GHz' 'DDR3_1600_8x8' '500000'

echo "saving test case2"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_02.txt

echo "Starting Test Case3"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'TimingSimpleCPU' '4GHz' 'DDR3_1600_8x8' '500000'

echo "saving test case3"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_03.txt

echo "Starting Test Case4"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'MinorCPU' '1GHz' 'DDR3_1600_8x8' '500000'

echo "saving test case4"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_04.txt

echo "Starting Test Case5"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'MinorCPU' '2GHz' 'DDR3_1600_8x8' '500000'

echo "saving test case5"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_05.txt

echo "Starting Test Case6"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'MinorCPU' '4GHz' 'DDR3_1600_8x8' '500000'

echo "saving test case6"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_06.txt

echo "Starting Test Case7"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'TimingSimpleCPU' '4GHz' 'DDR3_2133_8x8' '500000'

echo "saving test case7"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_07.txt

echo "Starting Test Case8"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'TimingSimpleCPU' '4GHz' 'LPDDR2_S4_1066_1x32' '500000'

echo "saving test case8"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_08.txt

echo "Starting Test Case9"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'TimingSimpleCPU' '4GHz' 'HBM_1000_4H_1x64' '500000'

echo "saving test case9"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_09.txt

echo "Starting Test Case10"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'TimingSimpleCPU' '4GHz' 'HBM_2000_4H_1x64' '500000'

echo "saving test case10"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_10.txt

echo "Starting Test Case11"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'MinorCPU' '4GHz' 'DDR3_2133_8x8' '500000'

echo "saving test case3"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_11.txt

echo "Starting Test Case12"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'MinorCPU' '4GHz' 'LPDDR2_S4_1066_1x32' '500000'

echo "saving test case12"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_12.txt

echo "Starting Test Case13"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'MinorCPU' '4GHz' 'HBM_1000_4H_1x64' '500000'

echo "saving test case13"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_13.txt

echo "Starting Test Case14"
build/X86/gem5.opt configs/tutorial/part1/sieve-config.py --l2_size='1MB' --l1d_size='128kB' 'MinorCPU' '4GHz' 'HBM_2000_4H_1x64' '500000'

echo "saving test case14"
cp m5out/stats.txt ~/ece752/assignment/hw1/stats_folder/stats_14.txt

