#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-PROC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-PROC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:00:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoAlarmSeverity, TimeIntervalSec, Unsigned64, CiscoInetAddressMask, CiscoNetworkAddress = mibBuilder.importSymbols("CISCO-TC", "CiscoAlarmSeverity", "TimeIntervalSec", "Unsigned64", "CiscoInetAddressMask", "CiscoNetworkAddress")
ciscoUnifiedComputingMIBObjects, CucsManagedObjectDn, CucsManagedObjectId = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIBObjects", "CucsManagedObjectDn", "CucsManagedObjectId")
CucsProcStatAdminState, = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsProcStatAdminState")
InetAddressIPv4, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressIPv6")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Counter32, IpAddress, TimeTicks, NotificationType, Unsigned32, MibIdentifier, ModuleIdentity, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Counter32", "IpAddress", "TimeTicks", "NotificationType", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Gauge32", "Integer32")
MacAddress, TimeInterval, DateAndTime, DisplayString, TruthValue, TimeStamp, TextualConvention, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TimeInterval", "DateAndTime", "DisplayString", "TruthValue", "TimeStamp", "TextualConvention", "RowPointer")
cucsProcObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40))
if mibBuilder.loadTexts: cucsProcObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsProcObjects.setOrganization('Cisco Systems Inc.')
cucsProcDoerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1), )
if mibBuilder.loadTexts: cucsProcDoerTable.setStatus('current')
cucsProcDoerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcDoerInstanceId"))
if mibBuilder.loadTexts: cucsProcDoerEntry.setStatus('current')
cucsProcDoerInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsProcDoerInstanceId.setStatus('current')
cucsProcDoerDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcDoerDn.setStatus('current')
cucsProcDoerRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcDoerRn.setStatus('current')
cucsProcDoerId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcDoerId.setStatus('current')
cucsProcDoerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcDoerName.setStatus('current')
cucsProcManagerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 2), )
if mibBuilder.loadTexts: cucsProcManagerTable.setStatus('current')
cucsProcManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcManagerInstanceId"))
if mibBuilder.loadTexts: cucsProcManagerEntry.setStatus('current')
cucsProcManagerInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsProcManagerInstanceId.setStatus('current')
cucsProcManagerDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcManagerDn.setStatus('current')
cucsProcManagerRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcManagerRn.setStatus('current')
cucsProcPrtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3), )
if mibBuilder.loadTexts: cucsProcPrtTable.setStatus('current')
cucsProcPrtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcPrtInstanceId"))
if mibBuilder.loadTexts: cucsProcPrtEntry.setStatus('current')
cucsProcPrtInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsProcPrtInstanceId.setStatus('current')
cucsProcPrtDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcPrtDn.setStatus('current')
cucsProcPrtRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcPrtRn.setStatus('current')
cucsProcPrtId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcPrtId.setStatus('current')
cucsProcPrtName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcPrtName.setStatus('current')
cucsProcPrtCountsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4), )
if mibBuilder.loadTexts: cucsProcPrtCountsTable.setStatus('current')
cucsProcPrtCountsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcPrtCountsInstanceId"))
if mibBuilder.loadTexts: cucsProcPrtCountsEntry.setStatus('current')
cucsProcPrtCountsInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsProcPrtCountsInstanceId.setStatus('current')
cucsProcPrtCountsDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcPrtCountsDn.setStatus('current')
cucsProcPrtCountsRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcPrtCountsRn.setStatus('current')
cucsProcPrtCountsDbtxs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcPrtCountsDbtxs.setStatus('current')
cucsProcPrtCountsTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcPrtCountsTotal.setStatus('current')
cucsProcPrtCountsCachenospc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcPrtCountsCachenospc.setStatus('current')
cucsProcPrtCountsLargetxs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcPrtCountsLargetxs.setStatus('current')
cucsProcPrtCountsPersistTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 8), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcPrtCountsPersistTime.setStatus('current')
cucsProcStimulusCountsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5), )
if mibBuilder.loadTexts: cucsProcStimulusCountsTable.setStatus('current')
cucsProcStimulusCountsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcStimulusCountsInstanceId"))
if mibBuilder.loadTexts: cucsProcStimulusCountsEntry.setStatus('current')
cucsProcStimulusCountsInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsProcStimulusCountsInstanceId.setStatus('current')
cucsProcStimulusCountsDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcStimulusCountsDn.setStatus('current')
cucsProcStimulusCountsRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcStimulusCountsRn.setStatus('current')
cucsProcStimulusCountsBulked = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcStimulusCountsBulked.setStatus('current')
cucsProcStimulusCountsFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcStimulusCountsFailed.setStatus('current')
cucsProcStimulusCountsRetried = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcStimulusCountsRetried.setStatus('current')
cucsProcStimulusCountsSingleton = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcStimulusCountsSingleton.setStatus('current')
cucsProcStimulusCountsSuccessfull = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcStimulusCountsSuccessfull.setStatus('current')
cucsProcStimulusCountsTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcStimulusCountsTotal.setStatus('current')
cucsProcStimulusCountsAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 10), CucsProcStatAdminState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcStimulusCountsAdminState.setStatus('current')
cucsProcSvcTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7), )
if mibBuilder.loadTexts: cucsProcSvcTable.setStatus('current')
cucsProcSvcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcSvcInstanceId"))
if mibBuilder.loadTexts: cucsProcSvcEntry.setStatus('current')
cucsProcSvcInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsProcSvcInstanceId.setStatus('current')
cucsProcSvcDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcSvcDn.setStatus('current')
cucsProcSvcRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcSvcRn.setStatus('current')
cucsProcSvcId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcSvcId.setStatus('current')
cucsProcSvcName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcSvcName.setStatus('current')
cucsProcTxCountsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6), )
if mibBuilder.loadTexts: cucsProcTxCountsTable.setStatus('current')
cucsProcTxCountsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcTxCountsInstanceId"))
if mibBuilder.loadTexts: cucsProcTxCountsEntry.setStatus('current')
cucsProcTxCountsInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsProcTxCountsInstanceId.setStatus('current')
cucsProcTxCountsDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcTxCountsDn.setStatus('current')
cucsProcTxCountsRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcTxCountsRn.setStatus('current')
cucsProcTxCountsBulked = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcTxCountsBulked.setStatus('current')
cucsProcTxCountsFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcTxCountsFailed.setStatus('current')
cucsProcTxCountsRetried = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcTxCountsRetried.setStatus('current')
cucsProcTxCountsSingleton = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcTxCountsSingleton.setStatus('current')
cucsProcTxCountsSuccessfull = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcTxCountsSuccessfull.setStatus('current')
cucsProcTxCountsTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcTxCountsTotal.setStatus('current')
cucsProcTxCountsAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 10), CucsProcStatAdminState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsProcTxCountsAdminState.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-PROC-MIB", cucsProcDoerEntry=cucsProcDoerEntry, cucsProcStimulusCountsTotal=cucsProcStimulusCountsTotal, cucsProcPrtCountsTable=cucsProcPrtCountsTable, cucsProcPrtCountsPersistTime=cucsProcPrtCountsPersistTime, cucsProcDoerRn=cucsProcDoerRn, cucsProcStimulusCountsEntry=cucsProcStimulusCountsEntry, cucsProcSvcId=cucsProcSvcId, cucsProcTxCountsRetried=cucsProcTxCountsRetried, cucsProcStimulusCountsSingleton=cucsProcStimulusCountsSingleton, cucsProcPrtDn=cucsProcPrtDn, cucsProcTxCountsTotal=cucsProcTxCountsTotal, cucsProcTxCountsFailed=cucsProcTxCountsFailed, cucsProcDoerDn=cucsProcDoerDn, cucsProcManagerDn=cucsProcManagerDn, cucsProcTxCountsDn=cucsProcTxCountsDn, cucsProcDoerName=cucsProcDoerName, cucsProcPrtTable=cucsProcPrtTable, cucsProcPrtRn=cucsProcPrtRn, cucsProcPrtId=cucsProcPrtId, cucsProcTxCountsInstanceId=cucsProcTxCountsInstanceId, cucsProcManagerTable=cucsProcManagerTable, cucsProcPrtEntry=cucsProcPrtEntry, cucsProcPrtCountsRn=cucsProcPrtCountsRn, cucsProcSvcTable=cucsProcSvcTable, cucsProcSvcName=cucsProcSvcName, cucsProcDoerTable=cucsProcDoerTable, cucsProcSvcRn=cucsProcSvcRn, cucsProcManagerRn=cucsProcManagerRn, cucsProcStimulusCountsAdminState=cucsProcStimulusCountsAdminState, cucsProcPrtCountsTotal=cucsProcPrtCountsTotal, cucsProcTxCountsSingleton=cucsProcTxCountsSingleton, cucsProcPrtCountsEntry=cucsProcPrtCountsEntry, cucsProcPrtCountsDn=cucsProcPrtCountsDn, cucsProcStimulusCountsRetried=cucsProcStimulusCountsRetried, cucsProcStimulusCountsFailed=cucsProcStimulusCountsFailed, cucsProcPrtName=cucsProcPrtName, cucsProcManagerInstanceId=cucsProcManagerInstanceId, cucsProcPrtCountsDbtxs=cucsProcPrtCountsDbtxs, cucsProcStimulusCountsDn=cucsProcStimulusCountsDn, cucsProcStimulusCountsTable=cucsProcStimulusCountsTable, cucsProcPrtCountsInstanceId=cucsProcPrtCountsInstanceId, cucsProcSvcInstanceId=cucsProcSvcInstanceId, cucsProcTxCountsAdminState=cucsProcTxCountsAdminState, cucsProcDoerInstanceId=cucsProcDoerInstanceId, cucsProcSvcDn=cucsProcSvcDn, cucsProcTxCountsBulked=cucsProcTxCountsBulked, cucsProcObjects=cucsProcObjects, cucsProcPrtCountsCachenospc=cucsProcPrtCountsCachenospc, cucsProcStimulusCountsInstanceId=cucsProcStimulusCountsInstanceId, PYSNMP_MODULE_ID=cucsProcObjects, cucsProcDoerId=cucsProcDoerId, cucsProcStimulusCountsSuccessfull=cucsProcStimulusCountsSuccessfull, cucsProcPrtCountsLargetxs=cucsProcPrtCountsLargetxs, cucsProcStimulusCountsRn=cucsProcStimulusCountsRn, cucsProcSvcEntry=cucsProcSvcEntry, cucsProcTxCountsTable=cucsProcTxCountsTable, cucsProcTxCountsSuccessfull=cucsProcTxCountsSuccessfull, cucsProcStimulusCountsBulked=cucsProcStimulusCountsBulked, cucsProcPrtInstanceId=cucsProcPrtInstanceId, cucsProcManagerEntry=cucsProcManagerEntry, cucsProcTxCountsRn=cucsProcTxCountsRn, cucsProcTxCountsEntry=cucsProcTxCountsEntry)
