#
# PySNMP MIB module ASCEND-SPARING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-SPARING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
sparingGroup, = mibBuilder.importSymbols("ASCEND-MIB", "sparingGroup")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, ModuleIdentity, Gauge32, TimeTicks, Counter32, MibIdentifier, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Gauge32", "TimeTicks", "Counter32", "MibIdentifier", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Counter64", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sparingGlobalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 30, 1))
sparingSlotGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 30, 2))
sparingIfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 30, 3))
sparingSlotMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 30, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("disable", 2), ("manual", 3), ("automatic", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingSlotMode.setStatus('mandatory')
sparingSlotTable = MibTable((1, 3, 6, 1, 4, 1, 529, 30, 2, 2), )
if mibBuilder.loadTexts: sparingSlotTable.setStatus('mandatory')
sparingSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1), ).setIndexNames((0, "ASCEND-SPARING-MIB", "sparingSlotPrimaryIndex"), (0, "ASCEND-SPARING-MIB", "sparingSlotSparingIndex"))
if mibBuilder.loadTexts: sparingSlotEntry.setStatus('mandatory')
sparingSlotPrimaryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingSlotPrimaryIndex.setStatus('mandatory')
sparingSlotSparingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingSlotSparingIndex.setStatus('mandatory')
sparingSlotStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("standby", 1), ("fault", 2), ("active", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingSlotStatus.setStatus('mandatory')
sparingSlotLastStatusChange = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingSlotLastStatusChange.setStatus('mandatory')
sparingSlotLastChangeReason = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("manual", 2), ("automatic", 3), ("test", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingSlotLastChangeReason.setStatus('mandatory')
sparingSlotStatusChangeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 30, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingSlotStatusChangeCount.setStatus('mandatory')
sparingIfTable = MibTable((1, 3, 6, 1, 4, 1, 529, 30, 3, 2), )
if mibBuilder.loadTexts: sparingIfTable.setStatus('mandatory')
sparingIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1), ).setIndexNames((0, "ASCEND-SPARING-MIB", "sparingIfPrimaryIndex"), (0, "ASCEND-SPARING-MIB", "sparingIfSparingIndex"))
if mibBuilder.loadTexts: sparingIfEntry.setStatus('mandatory')
sparingIfPrimaryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingIfPrimaryIndex.setStatus('mandatory')
sparingIfSparingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingIfSparingIndex.setStatus('mandatory')
sparingIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("standby", 1), ("fault", 2), ("active", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingIfStatus.setStatus('mandatory')
sparingIfLastStatusChange = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingIfLastStatusChange.setStatus('mandatory')
sparingIfLastChangeReason = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("manual", 2), ("automatic", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingIfLastChangeReason.setStatus('mandatory')
sparingIfStatusChangeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 30, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparingIfStatusChangeCount.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-SPARING-MIB", sparingSlotMode=sparingSlotMode, sparingIfSparingIndex=sparingIfSparingIndex, sparingIfLastChangeReason=sparingIfLastChangeReason, sparingSlotEntry=sparingSlotEntry, sparingSlotTable=sparingSlotTable, sparingSlotPrimaryIndex=sparingSlotPrimaryIndex, sparingIfEntry=sparingIfEntry, sparingIfPrimaryIndex=sparingIfPrimaryIndex, sparingSlotStatus=sparingSlotStatus, sparingGlobalGroup=sparingGlobalGroup, sparingSlotSparingIndex=sparingSlotSparingIndex, sparingSlotLastChangeReason=sparingSlotLastChangeReason, sparingSlotStatusChangeCount=sparingSlotStatusChangeCount, sparingIfStatus=sparingIfStatus, sparingIfStatusChangeCount=sparingIfStatusChangeCount, sparingIfLastStatusChange=sparingIfLastStatusChange, sparingSlotLastStatusChange=sparingSlotLastStatusChange, sparingIfGroup=sparingIfGroup, sparingSlotGroup=sparingSlotGroup, sparingIfTable=sparingIfTable)
