#
# PySNMP MIB module ChrComPmAtmATM-CELL-Interval-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmAtmATM-CELL-Interval-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmAtm, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmAtm")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, iso, Counter64, IpAddress, NotificationType, ModuleIdentity, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "iso", "Counter64", "IpAddress", "NotificationType", "ModuleIdentity", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComPmAtmATM_CELL_IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2), ).setLabel("chrComPmAtmATM-CELL-IntervalTable")
if mibBuilder.loadTexts: chrComPmAtmATM_CELL_IntervalTable.setStatus('current')
chrComPmAtmATM_CELL_IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1), ).setLabel("chrComPmAtmATM-CELL-IntervalEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmAtmATM-CELL-Interval-MIB", "chrComPmAtmIntervalNumber"))
if mibBuilder.loadTexts: chrComPmAtmATM_CELL_IntervalEntry.setStatus('current')
chrComPmAtmIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmIntervalNumber.setStatus('current')
chrComPmAtmSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmSuspectedInterval.setStatus('current')
chrComPmAtmElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmElapsedTime.setStatus('current')
chrComPmAtmSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmSuppressedIntrvls.setStatus('current')
chrComPmAtmOCDS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmOCDS.setStatus('current')
chrComPmAtmHECCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmHECCells.setStatus('current')
chrComPmAtmCorrectableHECCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmCorrectableHECCells.setStatus('current')
chrComPmAtmDiscardedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedCells.setStatus('current')
chrComPmAtmReceivedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmReceivedCells.setStatus('current')
chrComPmAtmTransmittedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmTransmittedCells.setStatus('current')
chrComPmAtmDiscardedIngCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedIngCells.setStatus('current')
chrComPmAtmDiscardedIngHighPrCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 12), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedIngHighPrCells.setStatus('current')
chrComPmAtmDiscardedEgCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedEgCells.setStatus('current')
chrComPmAtmDiscardedEgHighPrCells = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 14), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedEgHighPrCells.setStatus('current')
chrComPmAtmDiscardedUPC = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 15), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmDiscardedUPC.setStatus('current')
chrComPmAtmTaggedUPC = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 2, 1, 16), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmAtmTaggedUPC.setStatus('current')
mibBuilder.exportSymbols("ChrComPmAtmATM-CELL-Interval-MIB", chrComPmAtmSuppressedIntrvls=chrComPmAtmSuppressedIntrvls, chrComPmAtmDiscardedUPC=chrComPmAtmDiscardedUPC, chrComPmAtmElapsedTime=chrComPmAtmElapsedTime, chrComPmAtmHECCells=chrComPmAtmHECCells, chrComPmAtmReceivedCells=chrComPmAtmReceivedCells, chrComPmAtmATM_CELL_IntervalEntry=chrComPmAtmATM_CELL_IntervalEntry, chrComPmAtmDiscardedEgHighPrCells=chrComPmAtmDiscardedEgHighPrCells, chrComPmAtmCorrectableHECCells=chrComPmAtmCorrectableHECCells, chrComPmAtmOCDS=chrComPmAtmOCDS, chrComPmAtmDiscardedIngHighPrCells=chrComPmAtmDiscardedIngHighPrCells, chrComPmAtmDiscardedIngCells=chrComPmAtmDiscardedIngCells, chrComPmAtmSuspectedInterval=chrComPmAtmSuspectedInterval, chrComPmAtmDiscardedEgCells=chrComPmAtmDiscardedEgCells, chrComPmAtmTaggedUPC=chrComPmAtmTaggedUPC, chrComPmAtmATM_CELL_IntervalTable=chrComPmAtmATM_CELL_IntervalTable, chrComPmAtmDiscardedCells=chrComPmAtmDiscardedCells, chrComPmAtmIntervalNumber=chrComPmAtmIntervalNumber, chrComPmAtmTransmittedCells=chrComPmAtmTransmittedCells)
