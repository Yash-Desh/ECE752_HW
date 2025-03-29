"""
CS/ECE 752: Advanced Computer Architecture HW 1

This file is the Python configuration file for running the sieve.cpp program using gem5. 

The configuration script is designed to simulate the execution of the C++ program `sieve.cpp` using the gem5 simulator. The script sets up various parameters for the simulation environment, including CPU type, CPU clock speed, and DRAM memory type.

The file can accept the following command-line arguments:
    - `n` : The number for the C++ program, which will be passed as an argument to the `sieve` executable.
    - `CPU type` : Specifies the type of CPU to be used in the simulation. For example, it could be a simple or more advanced CPU model.
    - `CPU clock speed` : Defines the clock speed of the CPU in GHz.
    - `DRAM memory type` : Indicates the type of DRAM memory to be used, such as DDR3, DDR4, etc.

The code has been written with reference to gem5 examples provided on their GitHub repository (https://github.com/gem5/gem5) and the "Learning Gem5" section of the gem5 documentation.

Note: Ensure that the executable `sieve` is compiled and accessible from the script's path.

"""
# import necessary libraries

import argparse
import os

import m5
from m5.objects import *
# Add the common scripts to the path
m5.util.addToPath("../../")

# import the cache
from caches import *
# import the SimpleOpts module
from common import SimpleOpts

from ruby import Ruby

# grab the specific path to the binary
thispath = os.path.dirname(os.path.realpath(__file__))
# Contains the folder directory of where binary file is located for the cpp program
default_binary = os.path.join(
    thispath,
    "../../../",
    "tests/test-progs/sieve/bin/x86/linux/sieve",
)

# Binary to execute
SimpleOpts.add_option("binary", nargs="?", default=default_binary)
#CPU Type -->to define the type of CPU 
SimpleOpts.add_option("CPU", type=str, default="TimingSimpleCPU", help="Type of CPU")
#CPU Clock
SimpleOpts.add_option("CPUClock", type=str, default="4GHz", help="CPU clock")
# Memory Type
SimpleOpts.add_option("memtype", type=str, default = "DDR3_1600_8x8", help="The type of DDR memory")
#Number N for the sieve program 
SimpleOpts.add_option("nvalue", type = int, default = 100000, help="sieve program n")

# Finalize the arguments and grab the args so we can pass it on to objects
args = SimpleOpts.parse_args()

# creating the system
system = System()

# Setting the clock frequency of the system (and all of its children)
system.clk_domain = SrcClockDomain()
# Using the arguement from the command line to set up the clock frequency
system.clk_domain.clock = args.CPUClock
system.clk_domain.voltage_domain = VoltageDomain()

# Setting up the system
system.mem_mode = "timing"  # Use timing accesses
system.mem_ranges = [AddrRange("512MB")]  # Creating an address range

# Creating a simple CPU, using conditional statments to set different CPU type to the system based on command line input
if args.CPU == "MinorCPU" :
    system.cpu = X86MinorCPU()
elif args.CPU == "TimingSimpleCPU" :
    system.cpu = X86TimingSimpleCPU()
else :
    # The program quits if the CPU type isn't suppported
    print("ERROR: CPU Type not supported")
    sys.exit(1)

# Creating the memory bus
system.membus = SystemXBar()

# Creating an L1 instruction and data cache, passing the arguements to the cache file that was written 
system.cpu.icache = L1ICache(args)
system.cpu.dcache = L1DCache(args)

# Connecting the instruction and data caches to the CPU
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

# Creating a memory bus, a coherent crossbar, in this case
system.l2bus = L2XBar()

# Hooking the CPU ports up to the l2bus
system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

# Creating an L2 cache and Connecting it to the l2bus, and send the command line arguement to L2Cache object
system.l2cache = L2Cache(args)
system.l2cache.connectCPUSideBus(system.l2bus)

# Connect the L2 cache to the membus
system.l2cache.connectMemSideBus(system.membus)

# Creating the interrupt controller for the CPU
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

# Connecting the system up to the membus
system.system_port = system.membus.cpu_side_ports

# Creating a DDR3 memory controller
system.mem_ctrl = MemCtrl()
if args.memtype == "DDR3_1600_8x8" : 
    system.mem_ctrl.dram = DDR3_1600_8x8()
elif args.memtype == "DDR3_2133_8x8":
    system.mem_ctrl.dram = DDR3_2133_8x8()
elif args.memtype == "LPDDR2_S4_1066_1x32":
    system.mem_ctrl.dram = LPDDR2_S4_1066_1x32()
elif args.memtype == "HBM_1000_4H_1x64":
    system.mem_ctrl.dram = HBM_1000_4H_1x64()
elif args.memtype == "HBM_2000_4H_1x64":
    system.mem_ctrl.dram == "HBM_2000_4H_1x64"
else :
    print("ERROR: DRAM Type not supported")
    sys.exit(1)

system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

system.workload = SEWorkload.init_compatible(args.binary)

# Creating a process for a simple "Hello World" application
process = Process()
# Set the command
# cmd is a list which begins with the executable (like argv)
process.cmd = [args.binary, args.nvalue]
# Set the cpu to use the process as its workload and Creating thread contexts
system.cpu.workload = process
system.cpu.createThreads()

# set up the root SimObject and start the simulation
root = Root(full_system=False, system=system)
# instantiate all of the objects we've created above
m5.instantiate()

print(f"Beginning simulation!")
exit_event = m5.simulate()
print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")
