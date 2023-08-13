import logging

logging.debug("Program debugged : Looks Fine should work")
logging.info("Program launched Successfully code execute 101")
logging.warning("No NetBios Connected")
logging.error("CrashHandeler failed to launch : error code 407")
logging.critical('''06/25/2021 11:10:11:950 -----------------------------------------------------------------
06/25/2021 11:10:11:950 NetpDoDomainJoin
06/25/2021 11:10:11:950 NetpDoDomainJoin: using new computer names
06/25/2021 11:10:11:950 NetpDoDomainJoin: NetpGetNewMachineName returned 0x0
06/25/2021 11:10:11:950 NetTapMachineDomainJoin: 'WINHP-GKPH9A5TJ'
06/25/2021 11:10:11:950 NetP Machinein: status: 0x0
06/25/2021 11:10:11:950 NetpJoinWorkgroup: joining computer 'WINHP-GKPH9A5TJ' to workgroup 'WORKGROUP'
06/25/2021 11:10:11:950 NetpValidateName: checking to see if 'WORKGROUP' is valid as type 2 name
06/25/2021 11:10:11:966 NetpCheckNetBiosNameNotInUse for 'WORKGROUP' [ Workgroup as MACHINE]  returned 0x0
06/25/2021 11:10:11:966 NetpValidateName: name 'WORKGROUP' is valid for type 2
06/25/2021 11:10:11:982 NetpJoinWorkgroup: status:  0x0
06/25/2021 11:10:11:982 NetpDoDomainJoin: status: 0x0''')

