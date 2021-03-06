## System states

##   state can change to next state in 2 ways:
##   - a process emits a GotoSystemState signal with state name to goto
##   - objects specified in EXIT_STATE_DEPEND have started
SYSTEM_STATES = [
    'BASE_APPS',
    'BMC_STARTING',
    'BMC_READY',
    'HOST_POWERING_ON',
    'HOST_POWERED_ON',
    'HOST_BOOTING',
    'HOST_BOOTED',
    'HOST_POWERED_OFF',
]

EXIT_STATE_DEPEND = {
    '<inventory_root>/system/chassis/motherboard/bmc' : { 'fru_type' : 'BMC','is_fru' : False, 'manufacturer' : 'ASPEED' },
    'BASE_APPS' : {
        '/xyz/openbmc_poroject/sensors': 0,
    },
    'BMC_STARTING' : {
        '/xyz/openbmc_project/control/chassis0': 0,
    },
}

FRU_INSTANCES = {
        '<inventory_root>/system/chassis/motherboard/bmc' : { 'fru_type' : 'BMC','is_fru' : False, 'manufacturer' : 'ASPEED' },
}

# I believe these numbers need to match the yaml file used to create the c++ ipmi map.
# the devices have types, but I don't believe that factors in here, I think these are
# just unique IDs.
ID_LOOKUP = {
    'FRU' : {},
    # The number at the end needs to match the FRU ID.
    # https://github.com/openbmc/skeleton/blob/master/pysystemmgr/system_manager.py#L143
    # The parameter for it is of type 'y' (unsigned 8-bit integer) presumably decimal?
    'FRU_STR' : {},
    'SENSOR' : {},
    'GPIO_PRESENT' : {}
}

PCH_CONFIG = {
    'i2c_bus' : '3'
}
