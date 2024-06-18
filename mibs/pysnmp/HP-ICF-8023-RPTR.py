#
# PySNMP MIB module HP-ICF-8023-RPTR (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-8023-RPTR
# Produced by pysmi-0.3.4 at Mon Apr 29 19:20:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
hpicfRepeater, hpicfObjectModules, hpicf8023RptrTrapsPrefix, hp = mibBuilder.importSymbols("HP-ICF-OID", "hpicfRepeater", "hpicfObjectModules", "hpicf8023RptrTrapsPrefix", "hp")
rpMauIndex, rpMauPortIndex, rpMauMediaAvailable, rpMauGroupIndex = mibBuilder.importSymbols("MAU-MIB", "rpMauIndex", "rpMauPortIndex", "rpMauMediaAvailable", "rpMauGroupIndex")
rptrPortAutoPartitionState, = mibBuilder.importSymbols("SNMP-REPEATER-MIB", "rptrPortAutoPartitionState")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, Integer32, Gauge32, iso, Bits, Unsigned32, ModuleIdentity, Counter64, Counter32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Gauge32", "iso", "Bits", "Unsigned32", "ModuleIdentity", "Counter64", "Counter32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
hpicf8023RptrMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9))
hpicf8023RptrMib.setRevisions(('2000-11-03 22:10', '1998-07-16 20:27', '1996-09-10 02:19', '1994-02-25 00:00',))
if mibBuilder.loadTexts: hpicf8023RptrMib.setLastUpdated('200011032210Z')
if mibBuilder.loadTexts: hpicf8023RptrMib.setOrganization('Hewlett Packard Company, Network Infrastructure Solutions')
hpRptrBasic = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1))
hpRptrBasicGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1))
hpRptrEntityName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrEntityName.setStatus('deprecated')
hpRptrThinlanFault = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpRptrThinlanFault.setStatus('deprecated')
hpRptrSqeEnabled = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrSqeEnabled.setStatus('deprecated')
hpRptrRobustHealing = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpRptrRobustHealing.setStatus('deprecated')
hpRptrBasicGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2))
hpRptrBasicGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1), )
if mibBuilder.loadTexts: hpRptrBasicGroupTable.setStatus('deprecated')
hpRptrBasicGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1), ).setIndexNames((0, "HP-ICF-8023-RPTR", "hpRptrGrpGroupIndex"))
if mibBuilder.loadTexts: hpRptrBasicGroupEntry.setStatus('deprecated')
hpRptrGrpGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrGrpGroupIndex.setStatus('deprecated')
hpRptrGrpPortsAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrGrpPortsAdminStatus.setStatus('deprecated')
hpRptrGrpPortsSegStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrGrpPortsSegStatus.setStatus('deprecated')
hpRptrGrpPortsMediaAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrGrpPortsMediaAvailable.setStatus('deprecated')
hpRptrGrpPortsLinkbeatEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrGrpPortsLinkbeatEnabled.setStatus('deprecated')
hpRptrGrpPortsOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrGrpPortsOperStatus.setStatus('deprecated')
hpRptrBasicPort = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3))
hpRptrBasicPtTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1), )
if mibBuilder.loadTexts: hpRptrBasicPtTable.setStatus('current')
hpRptrBasicPtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1), ).setIndexNames((0, "HP-ICF-8023-RPTR", "hpRptrPtGroupIndex"), (0, "HP-ICF-8023-RPTR", "hpRptrPtPortIndex"))
if mibBuilder.loadTexts: hpRptrBasicPtEntry.setStatus('current')
hpRptrPtGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrPtGroupIndex.setStatus('current')
hpRptrPtPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrPtPortIndex.setStatus('current')
hpRptrPtLinkbeatEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpRptrPtLinkbeatEnable.setStatus('current')
hpRptrPtPolarityReversed = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrPtPolarityReversed.setStatus('current')
hpRptrPtSqeEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrPtSqeEnabled.setStatus('current')
hpRptrPtMediaAvailTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpRptrPtMediaAvailTrapEnable.setStatus('current')
hpRptrPtLongCableEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpRptrPtLongCableEnable.setStatus('current')
hpRptrMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2))
hpRptrMonitorGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1))
hpRptrMonCounters = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1))
hpRptrMonGlobalFrames = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalFrames.setStatus('deprecated')
hpRptrMonGlobalOctets = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalOctets.setStatus('deprecated')
hpRptrMonGlobalFCSErrors = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalFCSErrors.setStatus('deprecated')
hpRptrMonGlobalAlignmentErrors = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalAlignmentErrors.setStatus('deprecated')
hpRptrMonGlobalFrameTooLongs = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalFrameTooLongs.setStatus('deprecated')
hpRptrMonGlobalShortEvents = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalShortEvents.setStatus('deprecated')
hpRptrMonGlobalRunts = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalRunts.setStatus('deprecated')
hpRptrMonGlobalCollisions = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalCollisions.setStatus('deprecated')
hpRptrMonGlobalLateEvents = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalLateEvents.setStatus('deprecated')
hpRptrMonGlobalVeryLongEvents = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalVeryLongEvents.setStatus('deprecated')
hpRptrMonGlobalDataRateMismatches = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalDataRateMismatches.setStatus('deprecated')
hpRptrMonGlobalAutoPartitions = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalAutoPartitions.setStatus('deprecated')
hpRptrMonGlobalErrors = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalErrors.setStatus('deprecated')
hpRptrMonGlobalUcastPackets = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalUcastPackets.setStatus('deprecated')
hpRptrMonGlobalBcastPackets = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalBcastPackets.setStatus('deprecated')
hpRptrMonGlobalMcastPackets = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonGlobalMcastPackets.setStatus('deprecated')
hpRptrMonitorGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 2))
hpRptrMonitorPort = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3))
hpRptrMonPtTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1), )
if mibBuilder.loadTexts: hpRptrMonPtTable.setStatus('current')
hpRptrMonPtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1), ).setIndexNames((0, "HP-ICF-8023-RPTR", "hpRptrMonPtGroupIndex"), (0, "HP-ICF-8023-RPTR", "hpRptrMonPtPortIndex"))
if mibBuilder.loadTexts: hpRptrMonPtEntry.setStatus('current')
hpRptrMonPtGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonPtGroupIndex.setStatus('current')
hpRptrMonPtPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonPtPortIndex.setStatus('current')
hpRptrMonPtUcastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonPtUcastPackets.setStatus('current')
hpRptrMonPtBcastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonPtBcastPackets.setStatus('current')
hpRptrMonPtMcastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRptrMonPtMcastPackets.setStatus('current')
hpRpMauGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4))
hpRpMauTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1), )
if mibBuilder.loadTexts: hpRpMauTable.setStatus('current')
hpRpMauEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1), ).setIndexNames((0, "MAU-MIB", "rpMauGroupIndex"), (0, "MAU-MIB", "rpMauPortIndex"), (0, "MAU-MIB", "rpMauIndex"))
if mibBuilder.loadTexts: hpRpMauEntry.setStatus('current')
hpRpMauTypeList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 1), Bits().clone(namedValues=NamedValues(("bOther", 0), ("bAUI", 1), ("b10base5", 2), ("bFoirl", 3), ("b10base2", 4), ("b10baseT", 5), ("b10baseFP", 6), ("b10baseFB", 7), ("b10baseFL", 8), ("b10broad36", 9), ("b10baseTHD", 10), ("b10baseTFD", 11), ("b10baseFLHD", 12), ("b10baseFLFD", 13), ("b100baseT4", 14), ("b100baseTXHD", 15), ("b100baseTXFD", 16), ("b100baseFXHD", 17), ("b100baseFXFD", 18), ("b100baseT2HD", 19), ("b100baseT2FD", 20)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRpMauTypeList.setStatus('current')
hpRpMauAutoNegSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRpMauAutoNegSupported.setStatus('current')
hpRpMauAutoNegAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("autoNegotiate", 1), ("forceTo100TXHD", 2), ("forceTo10THD", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpRpMauAutoNegAdminStatus.setStatus('current')
hpRpMauAutoNegRemoteSignaling = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("detected", 1), ("notdetected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRpMauAutoNegRemoteSignaling.setStatus('current')
hpRpMauAutoNegConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("configuring", 2), ("complete", 3), ("disabled", 4), ("parallelDetectFail", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRpMauAutoNegConfig.setStatus('current')
hpRpMauAutoNegCapReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 6), Bits().clone(namedValues=NamedValues(("bOther", 0), ("b10baseT", 1), ("b10baseTFD", 2), ("b100baseT4", 3), ("b100baseTX", 4), ("b100baseTXFD", 5), ("b100baseT2", 6), ("b100baseT2FD", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpRpMauAutoNegCapReceived.setStatus('current')
hpRpMauAutoNegRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restart", 1), ("norestart", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpRpMauAutoNegRestart.setStatus('current')
hpicfLinkBeatTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0, 1)).setObjects(("MAU-MIB", "rpMauMediaAvailable"))
if mibBuilder.loadTexts: hpicfLinkBeatTrap.setStatus('deprecated')
hpicfPartitionTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0, 2)).setObjects(("SNMP-REPEATER-MIB", "rptrPortAutoPartitionState"))
if mibBuilder.loadTexts: hpicfPartitionTrap.setStatus('deprecated')
hpicfMediaAvailDetectTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0, 3)).setObjects(("MAU-MIB", "rpMauMediaAvailable"))
if mibBuilder.loadTexts: hpicfMediaAvailDetectTrap.setStatus('current')
hpicfMediaAvailLostTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0, 4)).setObjects(("MAU-MIB", "rpMauMediaAvailable"))
if mibBuilder.loadTexts: hpicfMediaAvailLostTrap.setStatus('current')
hpicfPortPartitionTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0, 5)).setObjects(("SNMP-REPEATER-MIB", "rptrPortAutoPartitionState"))
if mibBuilder.loadTexts: hpicfPortPartitionTrap.setStatus('current')
hpicfPortHealTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0, 6)).setObjects(("SNMP-REPEATER-MIB", "rptrPortAutoPartitionState"))
if mibBuilder.loadTexts: hpicfPortHealTrap.setStatus('current')
hpicf8023RptrConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1))
hpicf8023RptrCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 1))
hpicf8023RptrGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2))
hpicf8023RptrCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 1, 1)).setObjects(("HP-ICF-8023-RPTR", "hpicf8023RptrBasicGroup"), ("HP-ICF-8023-RPTR", "hpicf8023RptrMonitorGroup"), ("HP-ICF-8023-RPTR", "hpicf8023RptrNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023RptrCompliance = hpicf8023RptrCompliance.setStatus('deprecated')
hpicf8023RptrSlaveCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 1, 2)).setObjects(("HP-ICF-8023-RPTR", "hpicf8023RptrBasicSlaveGroup"), ("HP-ICF-8023-RPTR", "hpicf8023RptrMonitorSlaveGroup"), ("HP-ICF-8023-RPTR", "hpicf8023RptrNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023RptrSlaveCompliance = hpicf8023RptrSlaveCompliance.setStatus('deprecated')
hpicf8023MultiRptrCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 1, 3)).setObjects(("HP-ICF-8023-RPTR", "hpicf8023MultiRptrBasicGroup"), ("HP-ICF-8023-RPTR", "hpicf8023MultiRptrMonitorGroup"), ("HP-ICF-8023-RPTR", "hpicf8023MultiRptrNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023MultiRptrCompliance = hpicf8023MultiRptrCompliance.setStatus('current')
hpicf8023RptrAutoNegCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 1, 4)).setObjects(("HP-ICF-8023-RPTR", "hpicf8023MultiRptrBasicGroup"), ("HP-ICF-8023-RPTR", "hpicf8023MultiRptrMonitorGroup"), ("HP-ICF-8023-RPTR", "hpicf8023MultiRptrNotifyGroup"), ("HP-ICF-8023-RPTR", "hpicf8023RpMauAutoNegGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023RptrAutoNegCompliance = hpicf8023RptrAutoNegCompliance.setStatus('current')
hpicf8023RptrBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 1)).setObjects(("HP-ICF-8023-RPTR", "hpRptrEntityName"), ("HP-ICF-8023-RPTR", "hpRptrThinlanFault"), ("HP-ICF-8023-RPTR", "hpRptrSqeEnabled"), ("HP-ICF-8023-RPTR", "hpRptrRobustHealing"), ("HP-ICF-8023-RPTR", "hpRptrGrpGroupIndex"), ("HP-ICF-8023-RPTR", "hpRptrGrpPortsAdminStatus"), ("HP-ICF-8023-RPTR", "hpRptrGrpPortsSegStatus"), ("HP-ICF-8023-RPTR", "hpRptrGrpPortsMediaAvailable"), ("HP-ICF-8023-RPTR", "hpRptrGrpPortsLinkbeatEnabled"), ("HP-ICF-8023-RPTR", "hpRptrGrpPortsOperStatus"), ("HP-ICF-8023-RPTR", "hpRptrPtGroupIndex"), ("HP-ICF-8023-RPTR", "hpRptrPtPortIndex"), ("HP-ICF-8023-RPTR", "hpRptrPtLinkbeatEnable"), ("HP-ICF-8023-RPTR", "hpRptrPtPolarityReversed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023RptrBasicGroup = hpicf8023RptrBasicGroup.setStatus('deprecated')
hpicf8023RptrBasicSlaveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 2)).setObjects(("HP-ICF-8023-RPTR", "hpRptrEntityName"), ("HP-ICF-8023-RPTR", "hpRptrThinlanFault"), ("HP-ICF-8023-RPTR", "hpRptrSqeEnabled"), ("HP-ICF-8023-RPTR", "hpRptrGrpGroupIndex"), ("HP-ICF-8023-RPTR", "hpRptrGrpPortsAdminStatus"), ("HP-ICF-8023-RPTR", "hpRptrGrpPortsSegStatus"), ("HP-ICF-8023-RPTR", "hpRptrGrpPortsMediaAvailable"), ("HP-ICF-8023-RPTR", "hpRptrGrpPortsLinkbeatEnabled"), ("HP-ICF-8023-RPTR", "hpRptrGrpPortsOperStatus"), ("HP-ICF-8023-RPTR", "hpRptrPtGroupIndex"), ("HP-ICF-8023-RPTR", "hpRptrPtPortIndex"), ("HP-ICF-8023-RPTR", "hpRptrPtLinkbeatEnable"), ("HP-ICF-8023-RPTR", "hpRptrPtPolarityReversed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023RptrBasicSlaveGroup = hpicf8023RptrBasicSlaveGroup.setStatus('deprecated')
hpicf8023RptrMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 3)).setObjects(("HP-ICF-8023-RPTR", "hpRptrMonGlobalFrames"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalOctets"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalFCSErrors"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalAlignmentErrors"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalFrameTooLongs"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalShortEvents"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalRunts"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalCollisions"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalLateEvents"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalVeryLongEvents"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalDataRateMismatches"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalAutoPartitions"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalErrors"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalUcastPackets"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalBcastPackets"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalMcastPackets"), ("HP-ICF-8023-RPTR", "hpRptrMonPtGroupIndex"), ("HP-ICF-8023-RPTR", "hpRptrMonPtPortIndex"), ("HP-ICF-8023-RPTR", "hpRptrMonPtUcastPackets"), ("HP-ICF-8023-RPTR", "hpRptrMonPtBcastPackets"), ("HP-ICF-8023-RPTR", "hpRptrMonPtMcastPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023RptrMonitorGroup = hpicf8023RptrMonitorGroup.setStatus('deprecated')
hpicf8023RptrMonitorSlaveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 4)).setObjects(("HP-ICF-8023-RPTR", "hpRptrMonGlobalFrames"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalOctets"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalFCSErrors"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalAlignmentErrors"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalFrameTooLongs"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalShortEvents"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalRunts"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalCollisions"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalLateEvents"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalVeryLongEvents"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalDataRateMismatches"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalAutoPartitions"), ("HP-ICF-8023-RPTR", "hpRptrMonGlobalErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023RptrMonitorSlaveGroup = hpicf8023RptrMonitorSlaveGroup.setStatus('deprecated')
hpicf8023MultiRptrBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 5)).setObjects(("HP-ICF-8023-RPTR", "hpRptrPtGroupIndex"), ("HP-ICF-8023-RPTR", "hpRptrPtPortIndex"), ("HP-ICF-8023-RPTR", "hpRptrPtLinkbeatEnable"), ("HP-ICF-8023-RPTR", "hpRptrPtPolarityReversed"), ("HP-ICF-8023-RPTR", "hpRptrPtSqeEnabled"), ("HP-ICF-8023-RPTR", "hpRptrPtMediaAvailTrapEnable"), ("HP-ICF-8023-RPTR", "hpRptrPtLongCableEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023MultiRptrBasicGroup = hpicf8023MultiRptrBasicGroup.setStatus('current')
hpicf8023MultiRptrMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 6)).setObjects(("HP-ICF-8023-RPTR", "hpRptrMonPtGroupIndex"), ("HP-ICF-8023-RPTR", "hpRptrMonPtPortIndex"), ("HP-ICF-8023-RPTR", "hpRptrMonPtUcastPackets"), ("HP-ICF-8023-RPTR", "hpRptrMonPtBcastPackets"), ("HP-ICF-8023-RPTR", "hpRptrMonPtMcastPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023MultiRptrMonitorGroup = hpicf8023MultiRptrMonitorGroup.setStatus('current')
hpicf8023RptrNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 7)).setObjects(("HP-ICF-8023-RPTR", "hpicfLinkBeatTrap"), ("HP-ICF-8023-RPTR", "hpicfPartitionTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023RptrNotifyGroup = hpicf8023RptrNotifyGroup.setStatus('deprecated')
hpicf8023MultiRptrNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 8)).setObjects(("HP-ICF-8023-RPTR", "hpicfMediaAvailDetectTrap"), ("HP-ICF-8023-RPTR", "hpicfMediaAvailLostTrap"), ("HP-ICF-8023-RPTR", "hpicfPortPartitionTrap"), ("HP-ICF-8023-RPTR", "hpicfPortHealTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023MultiRptrNotifyGroup = hpicf8023MultiRptrNotifyGroup.setStatus('current')
hpicf8023RpMauAutoNegGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 9)).setObjects(("HP-ICF-8023-RPTR", "hpRpMauTypeList"), ("HP-ICF-8023-RPTR", "hpRpMauAutoNegSupported"), ("HP-ICF-8023-RPTR", "hpRpMauAutoNegAdminStatus"), ("HP-ICF-8023-RPTR", "hpRpMauAutoNegRemoteSignaling"), ("HP-ICF-8023-RPTR", "hpRpMauAutoNegConfig"), ("HP-ICF-8023-RPTR", "hpRpMauAutoNegCapReceived"), ("HP-ICF-8023-RPTR", "hpRpMauAutoNegRestart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023RpMauAutoNegGroup = hpicf8023RpMauAutoNegGroup.setStatus('current')
hpicf8023Rptr100BasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9, 1, 2, 10)).setObjects(("HP-ICF-8023-RPTR", "hpRptrPtGroupIndex"), ("HP-ICF-8023-RPTR", "hpRptrPtPortIndex"), ("HP-ICF-8023-RPTR", "hpRptrPtPolarityReversed"), ("HP-ICF-8023-RPTR", "hpRptrPtMediaAvailTrapEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicf8023Rptr100BasicGroup = hpicf8023Rptr100BasicGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-8023-RPTR", hpRpMauAutoNegRestart=hpRpMauAutoNegRestart, hpRptrMonGlobalFrames=hpRptrMonGlobalFrames, hpicf8023RptrBasicGroup=hpicf8023RptrBasicGroup, hpRpMauAutoNegAdminStatus=hpRpMauAutoNegAdminStatus, hpicf8023RptrCompliances=hpicf8023RptrCompliances, hpicfMediaAvailDetectTrap=hpicfMediaAvailDetectTrap, hpRptrMonPtGroupIndex=hpRptrMonPtGroupIndex, hpicf8023MultiRptrNotifyGroup=hpicf8023MultiRptrNotifyGroup, hpRptrMonitorGlobal=hpRptrMonitorGlobal, hpRptrMonitorPort=hpRptrMonitorPort, hpRptrGrpPortsSegStatus=hpRptrGrpPortsSegStatus, hpRptrMonCounters=hpRptrMonCounters, hpRptrMonGlobalBcastPackets=hpRptrMonGlobalBcastPackets, hpicf8023RptrBasicSlaveGroup=hpicf8023RptrBasicSlaveGroup, hpRptrPtLongCableEnable=hpRptrPtLongCableEnable, hpRptrPtGroupIndex=hpRptrPtGroupIndex, hpicf8023RptrSlaveCompliance=hpicf8023RptrSlaveCompliance, hpicf8023RptrConformance=hpicf8023RptrConformance, hpRpMauTypeList=hpRpMauTypeList, hpRptrMonPtEntry=hpRptrMonPtEntry, hpicfPortHealTrap=hpicfPortHealTrap, hpRpMauTable=hpRpMauTable, hpRptrMonGlobalErrors=hpRptrMonGlobalErrors, hpRptrMonGlobalRunts=hpRptrMonGlobalRunts, hpRpMauEntry=hpRpMauEntry, hpRptrRobustHealing=hpRptrRobustHealing, hpRptrMonGlobalFCSErrors=hpRptrMonGlobalFCSErrors, hpRptrBasicPort=hpRptrBasicPort, hpRptrPtPortIndex=hpRptrPtPortIndex, PYSNMP_MODULE_ID=hpicf8023RptrMib, hpRptrBasic=hpRptrBasic, hpRptrBasicGlobal=hpRptrBasicGlobal, hpicfPartitionTrap=hpicfPartitionTrap, hpRptrMonPtPortIndex=hpRptrMonPtPortIndex, hpRptrMonGlobalAutoPartitions=hpRptrMonGlobalAutoPartitions, hpRptrBasicGroup=hpRptrBasicGroup, hpRptrMonGlobalAlignmentErrors=hpRptrMonGlobalAlignmentErrors, hpicf8023RptrCompliance=hpicf8023RptrCompliance, hpRpMauAutoNegRemoteSignaling=hpRpMauAutoNegRemoteSignaling, hpRptrGrpPortsLinkbeatEnabled=hpRptrGrpPortsLinkbeatEnabled, hpRptrEntityName=hpRptrEntityName, hpRptrBasicPtEntry=hpRptrBasicPtEntry, hpRptrMonGlobalOctets=hpRptrMonGlobalOctets, hpRpMauGroup=hpRpMauGroup, hpRpMauAutoNegSupported=hpRpMauAutoNegSupported, hpRptrMonGlobalMcastPackets=hpRptrMonGlobalMcastPackets, hpRptrBasicGroupEntry=hpRptrBasicGroupEntry, hpRptrMonGlobalShortEvents=hpRptrMonGlobalShortEvents, hpRptrMonGlobalLateEvents=hpRptrMonGlobalLateEvents, hpicfLinkBeatTrap=hpicfLinkBeatTrap, hpicf8023RptrMib=hpicf8023RptrMib, hpRptrMonGlobalCollisions=hpRptrMonGlobalCollisions, hpicf8023RptrMonitorGroup=hpicf8023RptrMonitorGroup, hpRpMauAutoNegConfig=hpRpMauAutoNegConfig, hpRpMauAutoNegCapReceived=hpRpMauAutoNegCapReceived, hpRptrMonPtTable=hpRptrMonPtTable, hpRptrBasicGroupTable=hpRptrBasicGroupTable, hpRptrGrpPortsOperStatus=hpRptrGrpPortsOperStatus, hpicf8023MultiRptrMonitorGroup=hpicf8023MultiRptrMonitorGroup, hpRptrMonGlobalFrameTooLongs=hpRptrMonGlobalFrameTooLongs, hpicf8023RptrGroups=hpicf8023RptrGroups, hpicf8023RpMauAutoNegGroup=hpicf8023RpMauAutoNegGroup, hpRptrPtSqeEnabled=hpRptrPtSqeEnabled, hpicfMediaAvailLostTrap=hpicfMediaAvailLostTrap, hpicf8023RptrMonitorSlaveGroup=hpicf8023RptrMonitorSlaveGroup, hpRptrMonGlobalDataRateMismatches=hpRptrMonGlobalDataRateMismatches, hpRptrGrpPortsAdminStatus=hpRptrGrpPortsAdminStatus, hpRptrPtMediaAvailTrapEnable=hpRptrPtMediaAvailTrapEnable, hpRptrPtLinkbeatEnable=hpRptrPtLinkbeatEnable, hpicf8023RptrAutoNegCompliance=hpicf8023RptrAutoNegCompliance, hpicf8023RptrNotifyGroup=hpicf8023RptrNotifyGroup, hpRptrMonitorGroup=hpRptrMonitorGroup, hpRptrGrpPortsMediaAvailable=hpRptrGrpPortsMediaAvailable, hpRptrMonPtMcastPackets=hpRptrMonPtMcastPackets, hpRptrGrpGroupIndex=hpRptrGrpGroupIndex, hpicfPortPartitionTrap=hpicfPortPartitionTrap, hpRptrPtPolarityReversed=hpRptrPtPolarityReversed, hpRptrMonGlobalUcastPackets=hpRptrMonGlobalUcastPackets, hpicf8023Rptr100BasicGroup=hpicf8023Rptr100BasicGroup, hpRptrBasicPtTable=hpRptrBasicPtTable, hpRptrSqeEnabled=hpRptrSqeEnabled, hpRptrThinlanFault=hpRptrThinlanFault, hpRptrMonitor=hpRptrMonitor, hpRptrMonPtBcastPackets=hpRptrMonPtBcastPackets, hpicf8023MultiRptrBasicGroup=hpicf8023MultiRptrBasicGroup, hpRptrMonGlobalVeryLongEvents=hpRptrMonGlobalVeryLongEvents, hpRptrMonPtUcastPackets=hpRptrMonPtUcastPackets, hpicf8023MultiRptrCompliance=hpicf8023MultiRptrCompliance)
