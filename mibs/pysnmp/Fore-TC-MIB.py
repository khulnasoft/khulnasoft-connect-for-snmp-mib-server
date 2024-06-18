#
# PySNMP MIB module Fore-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:04:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
asx, = mibBuilder.importSymbols("Fore-Common-MIB", "asx")
trapLogIndex, = mibBuilder.importSymbols("Fore-TrapLog-MIB", "trapLogIndex")
ifName, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifName", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Bits, iso, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, TimeTicks, Integer32, MibIdentifier, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Bits", "iso", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "TimeTicks", "Integer32", "MibIdentifier", "IpAddress", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
foreTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12))
if mibBuilder.loadTexts: foreTcMib.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: foreTcMib.setOrganization('FORE')
foreTcConfigTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1), )
if mibBuilder.loadTexts: foreTcConfigTable.setStatus('current')
foreTcConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: foreTcConfigEntry.setStatus('current')
foreTcConfigCellScrambling = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("scrambling", 1), ("noScrambling", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreTcConfigCellScrambling.setStatus('current')
foreTcConfigEmptyCell = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("unassigned", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreTcConfigEmptyCell.setStatus('current')
foreTcConfigLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tcNoLoop", 1), ("tcDiagLoop", 2), ("tcPayloadLoop", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreTcConfigLoopback.setStatus('current')
foreTcConfigFramingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tcFramingDirect", 1), ("tcFramingPlcp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreTcConfigFramingMode.setStatus('current')
foreTcConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 1, 1, 5), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcConfigStatus.setStatus('current')
foreTcTotalTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2), )
if mibBuilder.loadTexts: foreTcTotalTable.setStatus('current')
foreTcTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: foreTcTotalEntry.setStatus('current')
foreTcTotalLcdSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcTotalLcdSeconds.setStatus('current')
foreTcTotalCorrectableHcs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcTotalCorrectableHcs.setStatus('current')
foreTcTotalUncorrectableHcs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcTotalUncorrectableHcs.setStatus('current')
foreTcTotalTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcTotalTxCells.setStatus('current')
foreTcTotalRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcTotalRxCells.setStatus('current')
foreTcCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4), )
if mibBuilder.loadTexts: foreTcCurrentTable.setStatus('current')
foreTcCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: foreTcCurrentEntry.setStatus('current')
foreTcCurrentErrSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcCurrentErrSeconds.setStatus('current')
foreTcCurrentSevErrSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcCurrentSevErrSeconds.setStatus('current')
foreTcCurrentUnavailSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcCurrentUnavailSeconds.setStatus('current')
foreTcCurrentCorrectableHcs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcCurrentCorrectableHcs.setStatus('current')
foreTcCurrentUncorrectableHcs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcCurrentUncorrectableHcs.setStatus('current')
foreTcIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5), )
if mibBuilder.loadTexts: foreTcIntervalTable.setStatus('current')
foreTcIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "Fore-TC-MIB", "foreTcInterval"))
if mibBuilder.loadTexts: foreTcIntervalEntry.setStatus('current')
foreTcInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcInterval.setStatus('current')
foreTcIntervalErrSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcIntervalErrSeconds.setStatus('current')
foreTcIntervalSevErrSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcIntervalSevErrSeconds.setStatus('current')
foreTcIntervalUnavailSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcIntervalUnavailSeconds.setStatus('current')
foreTcIntervalCorrectableHcs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcIntervalCorrectableHcs.setStatus('current')
foreTcIntervalUncorrectableHcs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreTcIntervalUncorrectableHcs.setStatus('current')
foreTcLCDDetected = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreTcLCDDetected.setStatus('current')
foreTcLCDCleared = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 12, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: foreTcLCDCleared.setStatus('current')
mibBuilder.exportSymbols("Fore-TC-MIB", PYSNMP_MODULE_ID=foreTcMib, foreTcCurrentEntry=foreTcCurrentEntry, foreTcIntervalCorrectableHcs=foreTcIntervalCorrectableHcs, foreTcLCDDetected=foreTcLCDDetected, foreTcConfigCellScrambling=foreTcConfigCellScrambling, foreTcConfigTable=foreTcConfigTable, foreTcTotalRxCells=foreTcTotalRxCells, foreTcIntervalUnavailSeconds=foreTcIntervalUnavailSeconds, foreTcMib=foreTcMib, foreTcIntervalTable=foreTcIntervalTable, foreTcCurrentUnavailSeconds=foreTcCurrentUnavailSeconds, foreTcCurrentCorrectableHcs=foreTcCurrentCorrectableHcs, foreTcTotalTxCells=foreTcTotalTxCells, foreTcTotalUncorrectableHcs=foreTcTotalUncorrectableHcs, foreTcCurrentSevErrSeconds=foreTcCurrentSevErrSeconds, foreTcTotalCorrectableHcs=foreTcTotalCorrectableHcs, foreTcIntervalEntry=foreTcIntervalEntry, foreTcConfigFramingMode=foreTcConfigFramingMode, foreTcTotalEntry=foreTcTotalEntry, foreTcConfigLoopback=foreTcConfigLoopback, foreTcCurrentErrSeconds=foreTcCurrentErrSeconds, foreTcCurrentTable=foreTcCurrentTable, foreTcIntervalErrSeconds=foreTcIntervalErrSeconds, foreTcIntervalUncorrectableHcs=foreTcIntervalUncorrectableHcs, foreTcConfigEntry=foreTcConfigEntry, foreTcConfigStatus=foreTcConfigStatus, foreTcConfigEmptyCell=foreTcConfigEmptyCell, foreTcInterval=foreTcInterval, foreTcCurrentUncorrectableHcs=foreTcCurrentUncorrectableHcs, foreTcLCDCleared=foreTcLCDCleared, foreTcIntervalSevErrSeconds=foreTcIntervalSevErrSeconds, foreTcTotalTable=foreTcTotalTable, foreTcTotalLcdSeconds=foreTcTotalLcdSeconds)
