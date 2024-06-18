#
# PySNMP MIB module NETSCREEN-NSRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-NSRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:10:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
netscreenNsrp, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenNsrp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, iso, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, MibIdentifier, Integer32, Counter64, TimeTicks, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "iso", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "MibIdentifier", "Integer32", "Counter64", "TimeTicks", "IpAddress", "Unsigned32")
DisplayString, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "PhysAddress")
netscreenNsrpMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 6, 0))
netscreenNsrpMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-14 00:00', '2003-06-04 00:00', '2001-01-08 00:00',))
if mibBuilder.loadTexts: netscreenNsrpMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenNsrpMibModule.setOrganization('Juniper Networks, Inc.')
netscreenNsrpGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 6, 1))
nsrpGeneralClusterId = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpGeneralClusterId.setStatus('current')
nsrpGeneralLocalUnitId = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpGeneralLocalUnitId.setStatus('current')
nsrpGeneralEncrypEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpGeneralEncrypEnable.setStatus('current')
nsrpGeneralAuthEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpGeneralAuthEnable.setStatus('current')
nsrpGeneralIfMonitor = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpGeneralIfMonitor.setStatus('current')
nsrpGeneralGratArps = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpGeneralGratArps.setStatus('current')
netscreenNsrpVSD = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 6, 2))
nsrpVsdGroupTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1), )
if mibBuilder.loadTexts: nsrpVsdGroupTable.setStatus('current')
nsrpVsdGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1), ).setIndexNames((0, "NETSCREEN-NSRP-MIB", "nsrpVsdGroupID"))
if mibBuilder.loadTexts: nsrpVsdGroupEntry.setStatus('current')
nsrpVsdGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupID.setStatus('current')
nsrpVsdGroupPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupPriority.setStatus('current')
nsrpVsdGroupPreempt = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupPreempt.setStatus('current')
nsrpVsdGroupHoldDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupHoldDownTime.setStatus('current')
nsrpVsdGroupNumberOfUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupNumberOfUnit.setStatus('current')
nsrpVsdGroupCntStateChange = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupCntStateChange.setStatus('current')
nsrpVsdGroupCntToInit = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupCntToInit.setStatus('current')
nsrpVsdGroupCntToMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupCntToMaster.setStatus('current')
nsrpVsdGroupCntToPBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupCntToPBackup.setStatus('current')
nsrpVsdGroupCntToBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupCntToBackup.setStatus('current')
nsrpVsdGroupCntToIneligible = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupCntToIneligible.setStatus('current')
nsrpVsdGroupCntToInoperable = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupCntToInoperable.setStatus('current')
nsrpVsdGroupCntMasterConflict = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupCntMasterConflict.setStatus('current')
nsrpVsdGroupCntPbConfilict = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupCntPbConfilict.setStatus('current')
nsrpVsdGroupCntHeartbeatTx = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupCntHeartbeatTx.setStatus('current')
nsrpVsdGroupCntHeartbeatRx = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGroupCntHeartbeatRx.setStatus('current')
nsrpVsdMemberTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 6, 2, 2), )
if mibBuilder.loadTexts: nsrpVsdMemberTable.setStatus('current')
nsrpVsdMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 6, 2, 2, 1), ).setIndexNames((0, "NETSCREEN-NSRP-MIB", "nsrpVsdMemberGroupId"), (0, "NETSCREEN-NSRP-MIB", "nsrpVsdMemberUnitId"))
if mibBuilder.loadTexts: nsrpVsdMemberEntry.setStatus('current')
nsrpVsdMemberGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdMemberGroupId.setStatus('current')
nsrpVsdMemberUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdMemberUnitId.setStatus('current')
nsrpVsdMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("undefined", 0), ("init", 1), ("master", 2), ("primary-backup", 3), ("backup", 4), ("ineligible", 5), ("inoperable", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdMemberStatus.setStatus('current')
nsrpVsdMemberPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdMemberPriority.setStatus('current')
nsrpVsdMemberPreempt = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdMemberPreempt.setStatus('current')
nsrpVsdInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3), )
if mibBuilder.loadTexts: nsrpVsdInterfaceTable.setStatus('current')
nsrpVsdInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1), ).setIndexNames((0, "NETSCREEN-NSRP-MIB", "nsrpVsdIfIndex"))
if mibBuilder.loadTexts: nsrpVsdInterfaceEntry.setStatus('current')
nsrpVsdIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfIndex.setStatus('current')
nsrpVsdIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("down", 0), ("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfStatus.setStatus('current')
nsrpVsdIfGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfGroupId.setStatus('current')
nsrpVsdIfIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfIp.setStatus('current')
nsrpVsdIfNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfNetmask.setStatus('current')
nsrpVsdIfGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfGateway.setStatus('current')
nsrpVsdIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfName.setStatus('current')
nsrpVsdIfVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfVLAN.setStatus('current')
nsrpVsdIfMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 9), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfMAC.setStatus('current')
nsrpVsdIfVSys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfVSys.setStatus('current')
nsrpVsdIfMngTelnet = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfMngTelnet.setStatus('current')
nsrpVsdIfMngSCS = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfMngSCS.setStatus('current')
nsrpVsdIfMngWEB = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfMngWEB.setStatus('current')
nsrpVsdIfMngSSL = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfMngSSL.setStatus('current')
nsrpVsdIfMngSNMP = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfMngSNMP.setStatus('current')
nsrpVsdIfMngGlobal = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfMngGlobal.setStatus('current')
nsrpVsdIfMngGlobalPro = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfMngGlobalPro.setStatus('current')
nsrpVsdIfMngPing = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfMngPing.setStatus('current')
nsrpVsdIfMngIdentReset = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdIfMngIdentReset.setStatus('current')
nsrpVsdGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 6, 2, 4))
nsrpVsdGeneralInitHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 2, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGeneralInitHoldTime.setStatus('current')
nsrpVsdGeneralHbInterval = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 2, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGeneralHbInterval.setStatus('current')
nsrpVsdGeneralHbLostThres = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 2, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpVsdGeneralHbLostThres.setStatus('current')
netscreenNsrpRTO = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 6, 3))
nsrpRtoGroupTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 6, 3, 1), )
if mibBuilder.loadTexts: nsrpRtoGroupTable.setStatus('current')
nsrpRtoGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 6, 3, 1, 1), ).setIndexNames((0, "NETSCREEN-NSRP-MIB", "nsrpRtoGroupId"))
if mibBuilder.loadTexts: nsrpRtoGroupEntry.setStatus('current')
nsrpRtoGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoGroupId.setStatus('current')
nsrpRtoNumOfUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoNumOfUnit.setStatus('current')
nsrpRtoUnitTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 6, 3, 2), )
if mibBuilder.loadTexts: nsrpRtoUnitTable.setStatus('current')
nsrpRtoUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1), ).setIndexNames((0, "NETSCREEN-NSRP-MIB", "nsrpRtoUnitGroupId"), (0, "NETSCREEN-NSRP-MIB", "nsrpRtoUnitId"))
if mibBuilder.loadTexts: nsrpRtoUnitEntry.setStatus('current')
nsrpRtoUnitGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoUnitGroupId.setStatus('current')
nsrpRtoUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoUnitId.setStatus('current')
nsrpRtoUnitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("undefined", 0), ("set", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoUnitStatus.setStatus('current')
nsrpRtoUnitDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("out", 1), ("in", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoUnitDirection.setStatus('current')
nsrpRtoUnitLostHeartbeat = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoUnitLostHeartbeat.setStatus('current')
nsrpRtoUnitToActive = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoUnitToActive.setStatus('current')
nsrpRtoUnitToSet = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoUnitToSet.setStatus('current')
nsrpRtoUnitLostPeer = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoUnitLostPeer.setStatus('current')
nsrpRtoUnitGroupDetach = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoUnitGroupDetach.setStatus('current')
nsrpRtoCounter = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 6, 3, 3))
nsrpRtoCounterPakForwarded = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoCounterPakForwarded.setStatus('current')
nsrpRtoCounterPakReceived = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoCounterPakReceived.setStatus('current')
nsrpRtoCounterTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3), )
if mibBuilder.loadTexts: nsrpRtoCounterTable.setStatus('current')
nsrpRtoCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3, 1), ).setIndexNames((0, "NETSCREEN-NSRP-MIB", "nsrpRtoCounterIdx"))
if mibBuilder.loadTexts: nsrpRtoCounterEntry.setStatus('current')
nsrpRtoCounterIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoCounterIdx.setStatus('current')
nsrpRtoCounterName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoCounterName.setStatus('current')
nsrpRtoCounterSend = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoCounterSend.setStatus('current')
nsrpRtoCounterReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoCounterReceive.setStatus('current')
nsrpRtoCounterDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoCounterDrop.setStatus('current')
nsrpRtoGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 6, 3, 4))
nsrpRtoGeneralHbInterval = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 3, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoGeneralHbInterval.setStatus('current')
nsrpRtoGeneralHbLostThres = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 3, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoGeneralHbLostThres.setStatus('current')
nsrpRtoGeneralSessSyncEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 3, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpRtoGeneralSessSyncEnable.setStatus('current')
netscreenNsrpTrack = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 6, 4))
nsrpTrackEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackEnable.setStatus('current')
nsrpTrackThreshold = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackThreshold.setStatus('current')
nsrpTrackFailoverEnalble = MibScalar((1, 3, 6, 1, 4, 1, 3224, 6, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackFailoverEnalble.setStatus('current')
nsrpTrackTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4), )
if mibBuilder.loadTexts: nsrpTrackTable.setStatus('current')
nsrpTrackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1), ).setIndexNames((0, "NETSCREEN-NSRP-MIB", "nsrpTrackIpIndex"))
if mibBuilder.loadTexts: nsrpTrackEntry.setStatus('current')
nsrpTrackIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackIpIndex.setStatus('current')
nsrpTrackIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackIpAddr.setStatus('current')
nsrpTrackIpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("success", 0), ("fail", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackIpStatus.setStatus('current')
nsrpTrackIpTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackIpTimestamp.setStatus('current')
nsrpTrackIpInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackIpInterval.setStatus('current')
nsrpTrackIpThreshhold = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackIpThreshhold.setStatus('current')
nsrpTrackIpMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ping", 0), ("arp", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackIpMethod.setStatus('current')
nsrpTrackIpWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackIpWeight.setStatus('current')
nsrpTrackIpIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackIpIfName.setStatus('current')
nsrpTrackIpTotalCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackIpTotalCheck.setStatus('current')
nsrpTrackIpTotalFailedCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpTrackIpTotalFailedCheck.setStatus('current')
netscreenNsrpCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 6, 5))
nsrpClusterTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 6, 5, 1), )
if mibBuilder.loadTexts: nsrpClusterTable.setStatus('current')
nsrpClusterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 6, 5, 1, 1), ).setIndexNames((0, "NETSCREEN-NSRP-MIB", "nsrpClusterTblIndex"))
if mibBuilder.loadTexts: nsrpClusterEntry.setStatus('current')
nsrpClusterTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpClusterTblIndex.setStatus('current')
nsrpClusterUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpClusterUnitId.setStatus('current')
nsrpClusterUnitCtrlMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 5, 1, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpClusterUnitCtrlMac.setStatus('current')
nsrpClusterUnitDataMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 5, 1, 1, 4), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpClusterUnitDataMac.setStatus('current')
netscreenNsrpLinkInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 6, 6))
nsrpLinkInfoTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 6, 6, 1), )
if mibBuilder.loadTexts: nsrpLinkInfoTable.setStatus('current')
nsrpLinkInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 6, 6, 1, 1), ).setIndexNames((0, "NETSCREEN-NSRP-MIB", "nsrpLinkInfoIndex"))
if mibBuilder.loadTexts: nsrpLinkInfoEntry.setStatus('current')
nsrpLinkInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpLinkInfoIndex.setStatus('current')
nsrpLinkInfoLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("control", 0), ("data", 1), ("unused", 2), ("hapath2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpLinkInfoLinkType.setStatus('current')
nsrpLinkInfoChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 6, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpLinkInfoChannel.setStatus('current')
nsrpLinkInfoMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 6, 1, 1, 4), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpLinkInfoMac.setStatus('current')
nsrpLinkInfoState = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 6, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsrpLinkInfoState.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-NSRP-MIB", nsrpRtoUnitGroupId=nsrpRtoUnitGroupId, nsrpGeneralAuthEnable=nsrpGeneralAuthEnable, nsrpVsdIfMngTelnet=nsrpVsdIfMngTelnet, nsrpVsdGroupCntToInoperable=nsrpVsdGroupCntToInoperable, nsrpClusterUnitId=nsrpClusterUnitId, nsrpVsdGeneralHbLostThres=nsrpVsdGeneralHbLostThres, nsrpVsdMemberEntry=nsrpVsdMemberEntry, nsrpVsdIfGateway=nsrpVsdIfGateway, PYSNMP_MODULE_ID=netscreenNsrpMibModule, nsrpVsdGeneral=nsrpVsdGeneral, nsrpRtoUnitDirection=nsrpRtoUnitDirection, nsrpRtoUnitToSet=nsrpRtoUnitToSet, nsrpTrackIpTotalFailedCheck=nsrpTrackIpTotalFailedCheck, nsrpTrackIpIfName=nsrpTrackIpIfName, nsrpTrackIpTotalCheck=nsrpTrackIpTotalCheck, nsrpTrackIpAddr=nsrpTrackIpAddr, nsrpVsdInterfaceEntry=nsrpVsdInterfaceEntry, nsrpVsdGroupEntry=nsrpVsdGroupEntry, nsrpRtoUnitLostPeer=nsrpRtoUnitLostPeer, nsrpVsdIfMngWEB=nsrpVsdIfMngWEB, nsrpVsdGroupPriority=nsrpVsdGroupPriority, nsrpRtoGeneralHbLostThres=nsrpRtoGeneralHbLostThres, netscreenNsrpLinkInfo=netscreenNsrpLinkInfo, nsrpVsdIfMngIdentReset=nsrpVsdIfMngIdentReset, nsrpRtoUnitStatus=nsrpRtoUnitStatus, nsrpLinkInfoLinkType=nsrpLinkInfoLinkType, nsrpTrackIpWeight=nsrpTrackIpWeight, nsrpVsdIfMAC=nsrpVsdIfMAC, nsrpVsdMemberTable=nsrpVsdMemberTable, nsrpGeneralLocalUnitId=nsrpGeneralLocalUnitId, nsrpGeneralEncrypEnable=nsrpGeneralEncrypEnable, nsrpVsdGroupPreempt=nsrpVsdGroupPreempt, nsrpTrackIpThreshhold=nsrpTrackIpThreshhold, nsrpLinkInfoIndex=nsrpLinkInfoIndex, netscreenNsrpCluster=netscreenNsrpCluster, nsrpVsdIfStatus=nsrpVsdIfStatus, nsrpLinkInfoState=nsrpLinkInfoState, nsrpVsdIfMngSSL=nsrpVsdIfMngSSL, nsrpVsdGroupCntToIneligible=nsrpVsdGroupCntToIneligible, nsrpVsdMemberStatus=nsrpVsdMemberStatus, nsrpVsdIfMngSCS=nsrpVsdIfMngSCS, nsrpTrackEnable=nsrpTrackEnable, nsrpGeneralGratArps=nsrpGeneralGratArps, nsrpGeneralIfMonitor=nsrpGeneralIfMonitor, nsrpRtoGroupEntry=nsrpRtoGroupEntry, nsrpVsdGeneralHbInterval=nsrpVsdGeneralHbInterval, nsrpVsdIfVSys=nsrpVsdIfVSys, nsrpVsdGroupID=nsrpVsdGroupID, nsrpVsdGroupCntPbConfilict=nsrpVsdGroupCntPbConfilict, nsrpRtoCounterReceive=nsrpRtoCounterReceive, nsrpVsdGroupHoldDownTime=nsrpVsdGroupHoldDownTime, nsrpVsdGroupCntHeartbeatRx=nsrpVsdGroupCntHeartbeatRx, nsrpLinkInfoTable=nsrpLinkInfoTable, nsrpVsdIfMngPing=nsrpVsdIfMngPing, nsrpClusterUnitDataMac=nsrpClusterUnitDataMac, nsrpRtoCounterPakForwarded=nsrpRtoCounterPakForwarded, netscreenNsrpTrack=netscreenNsrpTrack, nsrpRtoCounterTable=nsrpRtoCounterTable, nsrpVsdIfMngGlobalPro=nsrpVsdIfMngGlobalPro, nsrpVsdMemberPreempt=nsrpVsdMemberPreempt, nsrpVsdGroupCntToInit=nsrpVsdGroupCntToInit, nsrpRtoCounterIdx=nsrpRtoCounterIdx, nsrpVsdIfIp=nsrpVsdIfIp, nsrpVsdGroupCntStateChange=nsrpVsdGroupCntStateChange, nsrpRtoUnitLostHeartbeat=nsrpRtoUnitLostHeartbeat, nsrpVsdIfMngGlobal=nsrpVsdIfMngGlobal, nsrpVsdInterfaceTable=nsrpVsdInterfaceTable, nsrpRtoGroupTable=nsrpRtoGroupTable, nsrpRtoUnitEntry=nsrpRtoUnitEntry, nsrpTrackThreshold=nsrpTrackThreshold, nsrpTrackIpIndex=nsrpTrackIpIndex, nsrpVsdMemberUnitId=nsrpVsdMemberUnitId, nsrpLinkInfoChannel=nsrpLinkInfoChannel, nsrpVsdMemberGroupId=nsrpVsdMemberGroupId, nsrpRtoNumOfUnit=nsrpRtoNumOfUnit, nsrpRtoCounter=nsrpRtoCounter, nsrpVsdGroupCntHeartbeatTx=nsrpVsdGroupCntHeartbeatTx, nsrpVsdIfIndex=nsrpVsdIfIndex, nsrpVsdIfVLAN=nsrpVsdIfVLAN, nsrpVsdGroupCntToMaster=nsrpVsdGroupCntToMaster, netscreenNsrpGeneral=netscreenNsrpGeneral, nsrpVsdMemberPriority=nsrpVsdMemberPriority, nsrpClusterUnitCtrlMac=nsrpClusterUnitCtrlMac, nsrpRtoGeneralSessSyncEnable=nsrpRtoGeneralSessSyncEnable, nsrpGeneralClusterId=nsrpGeneralClusterId, nsrpClusterTable=nsrpClusterTable, nsrpLinkInfoEntry=nsrpLinkInfoEntry, nsrpVsdGeneralInitHoldTime=nsrpVsdGeneralInitHoldTime, nsrpTrackEntry=nsrpTrackEntry, nsrpVsdIfNetmask=nsrpVsdIfNetmask, nsrpVsdGroupCntToPBackup=nsrpVsdGroupCntToPBackup, nsrpRtoCounterPakReceived=nsrpRtoCounterPakReceived, nsrpRtoGeneralHbInterval=nsrpRtoGeneralHbInterval, nsrpTrackIpMethod=nsrpTrackIpMethod, nsrpVsdIfMngSNMP=nsrpVsdIfMngSNMP, nsrpVsdGroupTable=nsrpVsdGroupTable, nsrpVsdIfGroupId=nsrpVsdIfGroupId, nsrpClusterTblIndex=nsrpClusterTblIndex, nsrpRtoCounterEntry=nsrpRtoCounterEntry, nsrpTrackFailoverEnalble=nsrpTrackFailoverEnalble, nsrpLinkInfoMac=nsrpLinkInfoMac, nsrpTrackIpInterval=nsrpTrackIpInterval, nsrpRtoCounterSend=nsrpRtoCounterSend, nsrpRtoGeneral=nsrpRtoGeneral, nsrpVsdIfName=nsrpVsdIfName, nsrpRtoUnitId=nsrpRtoUnitId, nsrpRtoUnitGroupDetach=nsrpRtoUnitGroupDetach, nsrpVsdGroupCntMasterConflict=nsrpVsdGroupCntMasterConflict, netscreenNsrpVSD=netscreenNsrpVSD, nsrpTrackIpStatus=nsrpTrackIpStatus, nsrpRtoCounterDrop=nsrpRtoCounterDrop, nsrpTrackTable=nsrpTrackTable, nsrpVsdGroupNumberOfUnit=nsrpVsdGroupNumberOfUnit, netscreenNsrpMibModule=netscreenNsrpMibModule, nsrpRtoUnitToActive=nsrpRtoUnitToActive, nsrpVsdGroupCntToBackup=nsrpVsdGroupCntToBackup, nsrpTrackIpTimestamp=nsrpTrackIpTimestamp, nsrpRtoGroupId=nsrpRtoGroupId, nsrpRtoUnitTable=nsrpRtoUnitTable, nsrpClusterEntry=nsrpClusterEntry, netscreenNsrpRTO=netscreenNsrpRTO, nsrpRtoCounterName=nsrpRtoCounterName)
