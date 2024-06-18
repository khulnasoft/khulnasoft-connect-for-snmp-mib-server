#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-FCPOOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-FCPOOL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:59:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, CiscoNetworkAddress, CiscoAlarmSeverity, CiscoInetAddressMask, Unsigned64 = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec", "CiscoNetworkAddress", "CiscoAlarmSeverity", "CiscoInetAddressMask", "Unsigned64")
CucsManagedObjectDn, ciscoUnifiedComputingMIBObjects, CucsManagedObjectId = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "CucsManagedObjectDn", "ciscoUnifiedComputingMIBObjects", "CucsManagedObjectId")
CucsFcpoolInitiatorPurpose, CucsFcpoolBootTargetType, CucsPolicyPolicyOwner, CucsFcpoolInitiatorsMaxPortsPerNode, CucsFcpoolInitiatorEpPurpose, CucsAddressWWNMask, CucsFcpoolInitiatorsPurpose, CucsPoolElementOwner, CucsFcpoolInitiatorsAssignmentOrder = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsFcpoolInitiatorPurpose", "CucsFcpoolBootTargetType", "CucsPolicyPolicyOwner", "CucsFcpoolInitiatorsMaxPortsPerNode", "CucsFcpoolInitiatorEpPurpose", "CucsAddressWWNMask", "CucsFcpoolInitiatorsPurpose", "CucsPoolElementOwner", "CucsFcpoolInitiatorsAssignmentOrder")
InetAddressIPv4, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressIPv6")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, ObjectIdentity, MibIdentifier, TimeTicks, NotificationType, IpAddress, Bits, Counter32, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "ObjectIdentity", "MibIdentifier", "TimeTicks", "NotificationType", "IpAddress", "Bits", "Counter32", "Unsigned32", "ModuleIdentity")
TimeInterval, MacAddress, DateAndTime, TextualConvention, DisplayString, TruthValue, RowPointer, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "MacAddress", "DateAndTime", "TextualConvention", "DisplayString", "TruthValue", "RowPointer", "TimeStamp")
cucsFcpoolObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21))
if mibBuilder.loadTexts: cucsFcpoolObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsFcpoolObjects.setOrganization('Cisco Systems Inc.')
cucsFcpoolAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1), )
if mibBuilder.loadTexts: cucsFcpoolAddrTable.setStatus('current')
cucsFcpoolAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolAddrInstanceId"))
if mibBuilder.loadTexts: cucsFcpoolAddrEntry.setStatus('current')
cucsFcpoolAddrInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsFcpoolAddrInstanceId.setStatus('current')
cucsFcpoolAddrDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolAddrDn.setStatus('current')
cucsFcpoolAddrRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolAddrRn.setStatus('current')
cucsFcpoolAddrAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolAddrAssigned.setStatus('current')
cucsFcpoolAddrAssignedToDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolAddrAssignedToDn.setStatus('current')
cucsFcpoolAddrId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 6), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolAddrId.setStatus('current')
cucsFcpoolAddrOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 7), CucsPoolElementOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolAddrOwner.setStatus('current')
cucsFcpoolAddrGlobalAssignedCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolAddrGlobalAssignedCnt.setStatus('current')
cucsFcpoolAddrGlobalDefinedCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolAddrGlobalDefinedCnt.setStatus('current')
cucsFcpoolBlockTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2), )
if mibBuilder.loadTexts: cucsFcpoolBlockTable.setStatus('current')
cucsFcpoolBlockEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolBlockInstanceId"))
if mibBuilder.loadTexts: cucsFcpoolBlockEntry.setStatus('current')
cucsFcpoolBlockInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsFcpoolBlockInstanceId.setStatus('current')
cucsFcpoolBlockDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolBlockDn.setStatus('current')
cucsFcpoolBlockRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolBlockRn.setStatus('current')
cucsFcpoolBlockFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2, 1, 4), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolBlockFrom.setStatus('current')
cucsFcpoolBlockTo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 2, 1, 5), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolBlockTo.setStatus('current')
cucsFcpoolBootTargetTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3), )
if mibBuilder.loadTexts: cucsFcpoolBootTargetTable.setStatus('current')
cucsFcpoolBootTargetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolBootTargetInstanceId"))
if mibBuilder.loadTexts: cucsFcpoolBootTargetEntry.setStatus('current')
cucsFcpoolBootTargetInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsFcpoolBootTargetInstanceId.setStatus('current')
cucsFcpoolBootTargetDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolBootTargetDn.setStatus('current')
cucsFcpoolBootTargetRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolBootTargetRn.setStatus('current')
cucsFcpoolBootTargetLun = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolBootTargetLun.setStatus('current')
cucsFcpoolBootTargetType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1, 5), CucsFcpoolBootTargetType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolBootTargetType.setStatus('current')
cucsFcpoolBootTargetWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 3, 1, 6), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolBootTargetWwn.setStatus('current')
cucsFcpoolFormatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4), )
if mibBuilder.loadTexts: cucsFcpoolFormatTable.setStatus('current')
cucsFcpoolFormatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolFormatInstanceId"))
if mibBuilder.loadTexts: cucsFcpoolFormatEntry.setStatus('current')
cucsFcpoolFormatInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsFcpoolFormatInstanceId.setStatus('current')
cucsFcpoolFormatDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolFormatDn.setStatus('current')
cucsFcpoolFormatRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolFormatRn.setStatus('current')
cucsFcpoolFormatFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4, 1, 4), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolFormatFormat.setStatus('current')
cucsFcpoolFormatMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 4, 1, 5), CucsAddressWWNMask()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolFormatMask.setStatus('current')
cucsFcpoolInitiatorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5), )
if mibBuilder.loadTexts: cucsFcpoolInitiatorTable.setStatus('current')
cucsFcpoolInitiatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolInitiatorInstanceId"))
if mibBuilder.loadTexts: cucsFcpoolInitiatorEntry.setStatus('current')
cucsFcpoolInitiatorInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsFcpoolInitiatorInstanceId.setStatus('current')
cucsFcpoolInitiatorDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorDn.setStatus('current')
cucsFcpoolInitiatorRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorRn.setStatus('current')
cucsFcpoolInitiatorAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorAssigned.setStatus('current')
cucsFcpoolInitiatorAssignedToDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorAssignedToDn.setStatus('current')
cucsFcpoolInitiatorDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorDescr.setStatus('current')
cucsFcpoolInitiatorId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 7), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorId.setStatus('current')
cucsFcpoolInitiatorName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorName.setStatus('current')
cucsFcpoolInitiatorPoolableDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorPoolableDn.setStatus('current')
cucsFcpoolInitiatorPrevAssignedToDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorPrevAssignedToDn.setStatus('current')
cucsFcpoolInitiatorPurpose = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 5, 1, 11), CucsFcpoolInitiatorPurpose()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorPurpose.setStatus('current')
cucsFcpoolInitiatorEpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9), )
if mibBuilder.loadTexts: cucsFcpoolInitiatorEpTable.setStatus('current')
cucsFcpoolInitiatorEpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolInitiatorEpInstanceId"))
if mibBuilder.loadTexts: cucsFcpoolInitiatorEpEntry.setStatus('current')
cucsFcpoolInitiatorEpInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsFcpoolInitiatorEpInstanceId.setStatus('current')
cucsFcpoolInitiatorEpDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorEpDn.setStatus('current')
cucsFcpoolInitiatorEpRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorEpRn.setStatus('current')
cucsFcpoolInitiatorEpId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1, 4), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorEpId.setStatus('current')
cucsFcpoolInitiatorEpInitiatorDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorEpInitiatorDn.setStatus('current')
cucsFcpoolInitiatorEpPurpose = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 9, 1, 6), CucsFcpoolInitiatorEpPurpose()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorEpPurpose.setStatus('current')
cucsFcpoolInitiatorsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6), )
if mibBuilder.loadTexts: cucsFcpoolInitiatorsTable.setStatus('current')
cucsFcpoolInitiatorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolInitiatorsInstanceId"))
if mibBuilder.loadTexts: cucsFcpoolInitiatorsEntry.setStatus('current')
cucsFcpoolInitiatorsInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsFcpoolInitiatorsInstanceId.setStatus('current')
cucsFcpoolInitiatorsDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorsDn.setStatus('current')
cucsFcpoolInitiatorsRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorsRn.setStatus('current')
cucsFcpoolInitiatorsAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorsAssigned.setStatus('current')
cucsFcpoolInitiatorsDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorsDescr.setStatus('current')
cucsFcpoolInitiatorsIntId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorsIntId.setStatus('current')
cucsFcpoolInitiatorsName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorsName.setStatus('current')
cucsFcpoolInitiatorsPurpose = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 8), CucsFcpoolInitiatorsPurpose()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorsPurpose.setStatus('current')
cucsFcpoolInitiatorsSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorsSize.setStatus('current')
cucsFcpoolInitiatorsAssignmentOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 10), CucsFcpoolInitiatorsAssignmentOrder()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorsAssignmentOrder.setStatus('current')
cucsFcpoolInitiatorsMaxPortsPerNode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 11), CucsFcpoolInitiatorsMaxPortsPerNode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorsMaxPortsPerNode.setStatus('current')
cucsFcpoolInitiatorsPolicyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorsPolicyLevel.setStatus('current')
cucsFcpoolInitiatorsPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 6, 1, 13), CucsPolicyPolicyOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolInitiatorsPolicyOwner.setStatus('current')
cucsFcpoolPoolableTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7), )
if mibBuilder.loadTexts: cucsFcpoolPoolableTable.setStatus('current')
cucsFcpoolPoolableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolPoolableInstanceId"))
if mibBuilder.loadTexts: cucsFcpoolPoolableEntry.setStatus('current')
cucsFcpoolPoolableInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsFcpoolPoolableInstanceId.setStatus('current')
cucsFcpoolPoolableDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolPoolableDn.setStatus('current')
cucsFcpoolPoolableRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolPoolableRn.setStatus('current')
cucsFcpoolPoolableId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7, 1, 4), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolPoolableId.setStatus('current')
cucsFcpoolPoolablePoolDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 7, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolPoolablePoolDn.setStatus('current')
cucsFcpoolUniverseTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 8), )
if mibBuilder.loadTexts: cucsFcpoolUniverseTable.setStatus('current')
cucsFcpoolUniverseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 8, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", "cucsFcpoolUniverseInstanceId"))
if mibBuilder.loadTexts: cucsFcpoolUniverseEntry.setStatus('current')
cucsFcpoolUniverseInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 8, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsFcpoolUniverseInstanceId.setStatus('current')
cucsFcpoolUniverseDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 8, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolUniverseDn.setStatus('current')
cucsFcpoolUniverseRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 21, 8, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsFcpoolUniverseRn.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-FCPOOL-MIB", cucsFcpoolUniverseInstanceId=cucsFcpoolUniverseInstanceId, cucsFcpoolInitiatorsMaxPortsPerNode=cucsFcpoolInitiatorsMaxPortsPerNode, cucsFcpoolAddrRn=cucsFcpoolAddrRn, cucsFcpoolInitiatorAssigned=cucsFcpoolInitiatorAssigned, cucsFcpoolObjects=cucsFcpoolObjects, cucsFcpoolPoolableDn=cucsFcpoolPoolableDn, cucsFcpoolBootTargetType=cucsFcpoolBootTargetType, cucsFcpoolBlockDn=cucsFcpoolBlockDn, cucsFcpoolInitiatorsAssignmentOrder=cucsFcpoolInitiatorsAssignmentOrder, cucsFcpoolAddrTable=cucsFcpoolAddrTable, cucsFcpoolInitiatorEntry=cucsFcpoolInitiatorEntry, cucsFcpoolUniverseTable=cucsFcpoolUniverseTable, PYSNMP_MODULE_ID=cucsFcpoolObjects, cucsFcpoolAddrOwner=cucsFcpoolAddrOwner, cucsFcpoolAddrGlobalDefinedCnt=cucsFcpoolAddrGlobalDefinedCnt, cucsFcpoolBootTargetTable=cucsFcpoolBootTargetTable, cucsFcpoolBootTargetInstanceId=cucsFcpoolBootTargetInstanceId, cucsFcpoolInitiatorsInstanceId=cucsFcpoolInitiatorsInstanceId, cucsFcpoolInitiatorsEntry=cucsFcpoolInitiatorsEntry, cucsFcpoolBlockFrom=cucsFcpoolBlockFrom, cucsFcpoolInitiatorPurpose=cucsFcpoolInitiatorPurpose, cucsFcpoolInitiatorsDn=cucsFcpoolInitiatorsDn, cucsFcpoolInitiatorEpDn=cucsFcpoolInitiatorEpDn, cucsFcpoolUniverseDn=cucsFcpoolUniverseDn, cucsFcpoolInitiatorAssignedToDn=cucsFcpoolInitiatorAssignedToDn, cucsFcpoolPoolableRn=cucsFcpoolPoolableRn, cucsFcpoolUniverseEntry=cucsFcpoolUniverseEntry, cucsFcpoolBlockTable=cucsFcpoolBlockTable, cucsFcpoolInitiatorInstanceId=cucsFcpoolInitiatorInstanceId, cucsFcpoolInitiatorEpInitiatorDn=cucsFcpoolInitiatorEpInitiatorDn, cucsFcpoolInitiatorsDescr=cucsFcpoolInitiatorsDescr, cucsFcpoolFormatRn=cucsFcpoolFormatRn, cucsFcpoolPoolablePoolDn=cucsFcpoolPoolablePoolDn, cucsFcpoolBootTargetWwn=cucsFcpoolBootTargetWwn, cucsFcpoolInitiatorsPurpose=cucsFcpoolInitiatorsPurpose, cucsFcpoolBlockRn=cucsFcpoolBlockRn, cucsFcpoolPoolableInstanceId=cucsFcpoolPoolableInstanceId, cucsFcpoolBlockEntry=cucsFcpoolBlockEntry, cucsFcpoolBootTargetEntry=cucsFcpoolBootTargetEntry, cucsFcpoolAddrGlobalAssignedCnt=cucsFcpoolAddrGlobalAssignedCnt, cucsFcpoolFormatFormat=cucsFcpoolFormatFormat, cucsFcpoolInitiatorName=cucsFcpoolInitiatorName, cucsFcpoolInitiatorsIntId=cucsFcpoolInitiatorsIntId, cucsFcpoolFormatDn=cucsFcpoolFormatDn, cucsFcpoolBootTargetDn=cucsFcpoolBootTargetDn, cucsFcpoolAddrAssigned=cucsFcpoolAddrAssigned, cucsFcpoolFormatMask=cucsFcpoolFormatMask, cucsFcpoolFormatEntry=cucsFcpoolFormatEntry, cucsFcpoolAddrDn=cucsFcpoolAddrDn, cucsFcpoolInitiatorEpEntry=cucsFcpoolInitiatorEpEntry, cucsFcpoolBlockTo=cucsFcpoolBlockTo, cucsFcpoolFormatTable=cucsFcpoolFormatTable, cucsFcpoolInitiatorId=cucsFcpoolInitiatorId, cucsFcpoolInitiatorDn=cucsFcpoolInitiatorDn, cucsFcpoolInitiatorEpRn=cucsFcpoolInitiatorEpRn, cucsFcpoolInitiatorsName=cucsFcpoolInitiatorsName, cucsFcpoolInitiatorsPolicyOwner=cucsFcpoolInitiatorsPolicyOwner, cucsFcpoolInitiatorRn=cucsFcpoolInitiatorRn, cucsFcpoolPoolableTable=cucsFcpoolPoolableTable, cucsFcpoolInitiatorDescr=cucsFcpoolInitiatorDescr, cucsFcpoolInitiatorEpId=cucsFcpoolInitiatorEpId, cucsFcpoolBlockInstanceId=cucsFcpoolBlockInstanceId, cucsFcpoolInitiatorEpPurpose=cucsFcpoolInitiatorEpPurpose, cucsFcpoolBootTargetLun=cucsFcpoolBootTargetLun, cucsFcpoolInitiatorTable=cucsFcpoolInitiatorTable, cucsFcpoolInitiatorPoolableDn=cucsFcpoolInitiatorPoolableDn, cucsFcpoolFormatInstanceId=cucsFcpoolFormatInstanceId, cucsFcpoolInitiatorsTable=cucsFcpoolInitiatorsTable, cucsFcpoolAddrAssignedToDn=cucsFcpoolAddrAssignedToDn, cucsFcpoolInitiatorPrevAssignedToDn=cucsFcpoolInitiatorPrevAssignedToDn, cucsFcpoolInitiatorsSize=cucsFcpoolInitiatorsSize, cucsFcpoolPoolableEntry=cucsFcpoolPoolableEntry, cucsFcpoolInitiatorsPolicyLevel=cucsFcpoolInitiatorsPolicyLevel, cucsFcpoolInitiatorsAssigned=cucsFcpoolInitiatorsAssigned, cucsFcpoolAddrEntry=cucsFcpoolAddrEntry, cucsFcpoolBootTargetRn=cucsFcpoolBootTargetRn, cucsFcpoolAddrId=cucsFcpoolAddrId, cucsFcpoolInitiatorsRn=cucsFcpoolInitiatorsRn, cucsFcpoolAddrInstanceId=cucsFcpoolAddrInstanceId, cucsFcpoolInitiatorEpInstanceId=cucsFcpoolInitiatorEpInstanceId, cucsFcpoolPoolableId=cucsFcpoolPoolableId, cucsFcpoolInitiatorEpTable=cucsFcpoolInitiatorEpTable, cucsFcpoolUniverseRn=cucsFcpoolUniverseRn)
