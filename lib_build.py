import sys
from os.path import join, realpath

Import("env")

print("PlatformIO-lwIP: building for PlatformIO-FreeRTOS")

# Add include directories to build:
env.Append(CPPPATH=[realpath("lwip/src/include")])
env.Append(CPPPATH=[realpath("arch")])

# lwIP core files:
env.Replace(SRC_FILTER=[
        "+<lwip/src/core>",
        "+<lwip/src/api>",
        "+<lwip/src/netif>",
        "+<arch>"
    ])

# lwIP application files - optional:
'''
    This functionality is not included yet! 
'''

# lwipopts.h is located in the project space, outside of the lib:
env.Append(CPPPATH=env.get("PROJECT_INCLUDE_DIR", []))
