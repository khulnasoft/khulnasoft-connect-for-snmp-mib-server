#
# PySNMP MIB module AC-PM-ATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AC-PM-ATM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:54:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, NotificationType, iso, Integer32, ObjectIdentity, ModuleIdentity, Counter64, IpAddress, TimeTicks, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "NotificationType", "iso", "Integer32", "ObjectIdentity", "ModuleIdentity", "Counter64", "IpAddress", "TimeTicks", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
audioCodes = MibIdentifier((1, 3, 6, 1, 4, 1, 5003))
acRegistrations = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 7))
acGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 8))
acProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9))
acPerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10))
acPMAtm = ModuleIdentity((1, 3, 6, 1, 4, 1, 5003, 10, 12))
if mibBuilder.loadTexts: acPMAtm.setLastUpdated('200601261643Z')
if mibBuilder.loadTexts: acPMAtm.setOrganization('AudioCodes Ltd')
acPMAtmConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 12, 1))
acPMAtmConfigurationPeriodLength = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 894780))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acPMAtmConfigurationPeriodLength.setStatus('current')
acPMAtmConfigurationResetTotalCounters = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("resetCountersDone", 1), ("resetTotalCounters", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acPMAtmConfigurationResetTotalCounters.setStatus('current')
acPMAtmCellAttributes = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 31))
acPMAtmCellAttributesTxHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 31, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acPMAtmCellAttributesTxHighThreshold.setStatus('current')
acPMAtmCellAttributesTxLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 31, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acPMAtmCellAttributesTxLowThreshold.setStatus('current')
acPMAtmCellAttributesRxHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 31, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acPMAtmCellAttributesRxHighThreshold.setStatus('current')
acPMAtmCellAttributesRxLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 12, 1, 31, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acPMAtmCellAttributesRxLowThreshold.setStatus('current')
acPMAtmData = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2))
acPMAtmDataAcPMAtmTimeFromStartOfInterval = MibScalar((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmDataAcPMAtmTimeFromStartOfInterval.setStatus('current')
acPMAtmCellTxTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21), )
if mibBuilder.loadTexts: acPMAtmCellTxTable.setStatus('current')
acPMAtmCellTxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1), ).setIndexNames((0, "AC-PM-ATM-MIB", "acPMAtmCellTxInterface"), (0, "AC-PM-ATM-MIB", "acPMAtmCellTxInterval"))
if mibBuilder.loadTexts: acPMAtmCellTxEntry.setStatus('current')
acPMAtmCellTxInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMAtmCellTxInterface.setStatus('current')
acPMAtmCellTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMAtmCellTxInterval.setStatus('current')
acPMAtmCellTxAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellTxAverage.setStatus('current')
acPMAtmCellTxMax = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellTxMax.setStatus('current')
acPMAtmCellTxMin = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellTxMin.setStatus('current')
acPMAtmCellTxVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellTxVolume.setStatus('current')
acPMAtmCellTxTimeBelowLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellTxTimeBelowLowThreshold.setStatus('current')
acPMAtmCellTxTimeBetweenThresholds = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellTxTimeBetweenThresholds.setStatus('current')
acPMAtmCellTxTimeAboveHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellTxTimeAboveHighThreshold.setStatus('current')
acPMAtmCellTxFullDayAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 21, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellTxFullDayAverage.setStatus('current')
acPMAtmCellRxTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22), )
if mibBuilder.loadTexts: acPMAtmCellRxTable.setStatus('current')
acPMAtmCellRxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1), ).setIndexNames((0, "AC-PM-ATM-MIB", "acPMAtmCellRxInterface"), (0, "AC-PM-ATM-MIB", "acPMAtmCellRxInterval"))
if mibBuilder.loadTexts: acPMAtmCellRxEntry.setStatus('current')
acPMAtmCellRxInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMAtmCellRxInterface.setStatus('current')
acPMAtmCellRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMAtmCellRxInterval.setStatus('current')
acPMAtmCellRxAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellRxAverage.setStatus('current')
acPMAtmCellRxMax = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellRxMax.setStatus('current')
acPMAtmCellRxMin = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellRxMin.setStatus('current')
acPMAtmCellRxVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellRxVolume.setStatus('current')
acPMAtmCellRxTimeBelowLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellRxTimeBelowLowThreshold.setStatus('current')
acPMAtmCellRxTimeBetweenThresholds = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellRxTimeBetweenThresholds.setStatus('current')
acPMAtmCellRxTimeAboveHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellRxTimeAboveHighThreshold.setStatus('current')
acPMAtmCellRxFullDayAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 22, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellRxFullDayAverage.setStatus('current')
acPMAtmCellDiscardedTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 23), )
if mibBuilder.loadTexts: acPMAtmCellDiscardedTable.setStatus('current')
acPMAtmCellDiscardedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 23, 1), ).setIndexNames((0, "AC-PM-ATM-MIB", "acPMAtmCellDiscardedInterface"), (0, "AC-PM-ATM-MIB", "acPMAtmCellDiscardedInterval"))
if mibBuilder.loadTexts: acPMAtmCellDiscardedEntry.setStatus('current')
acPMAtmCellDiscardedInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 23, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMAtmCellDiscardedInterface.setStatus('current')
acPMAtmCellDiscardedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 23, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2)))
if mibBuilder.loadTexts: acPMAtmCellDiscardedInterval.setStatus('current')
acPMAtmCellDiscardedVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 10, 12, 2, 23, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acPMAtmCellDiscardedVal.setStatus('current')
mibBuilder.exportSymbols("AC-PM-ATM-MIB", acPMAtmCellRxInterval=acPMAtmCellRxInterval, acPMAtmCellRxTimeBelowLowThreshold=acPMAtmCellRxTimeBelowLowThreshold, acPMAtmConfigurationPeriodLength=acPMAtmConfigurationPeriodLength, acPMAtmCellTxFullDayAverage=acPMAtmCellTxFullDayAverage, acPerformance=acPerformance, acPMAtmConfiguration=acPMAtmConfiguration, acPMAtmData=acPMAtmData, acPMAtmCellTxTable=acPMAtmCellTxTable, acPMAtmCellTxAverage=acPMAtmCellTxAverage, acPMAtmCellDiscardedTable=acPMAtmCellDiscardedTable, acPMAtmDataAcPMAtmTimeFromStartOfInterval=acPMAtmDataAcPMAtmTimeFromStartOfInterval, acPMAtmCellTxTimeBetweenThresholds=acPMAtmCellTxTimeBetweenThresholds, acPMAtmCellRxAverage=acPMAtmCellRxAverage, acPMAtmCellRxVolume=acPMAtmCellRxVolume, acPMAtmCellRxMax=acPMAtmCellRxMax, acPMAtmCellAttributesTxLowThreshold=acPMAtmCellAttributesTxLowThreshold, PYSNMP_MODULE_ID=acPMAtm, acPMAtmCellRxTimeBetweenThresholds=acPMAtmCellRxTimeBetweenThresholds, acPMAtmCellRxTimeAboveHighThreshold=acPMAtmCellRxTimeAboveHighThreshold, acPMAtmCellTxTimeAboveHighThreshold=acPMAtmCellTxTimeAboveHighThreshold, acProducts=acProducts, acPMAtmCellDiscardedVal=acPMAtmCellDiscardedVal, acGeneric=acGeneric, acPMAtmCellTxEntry=acPMAtmCellTxEntry, acPMAtmCellRxFullDayAverage=acPMAtmCellRxFullDayAverage, acPMAtmCellRxMin=acPMAtmCellRxMin, acPMAtmConfigurationResetTotalCounters=acPMAtmConfigurationResetTotalCounters, acPMAtmCellAttributesTxHighThreshold=acPMAtmCellAttributesTxHighThreshold, acPMAtmCellRxTable=acPMAtmCellRxTable, acPMAtmCellTxTimeBelowLowThreshold=acPMAtmCellTxTimeBelowLowThreshold, acPMAtmCellTxMin=acPMAtmCellTxMin, acPMAtmCellTxMax=acPMAtmCellTxMax, acPMAtmCellAttributes=acPMAtmCellAttributes, acPMAtmCellAttributesRxLowThreshold=acPMAtmCellAttributesRxLowThreshold, acPMAtmCellAttributesRxHighThreshold=acPMAtmCellAttributesRxHighThreshold, acPMAtmCellTxVolume=acPMAtmCellTxVolume, acRegistrations=acRegistrations, acPMAtmCellTxInterval=acPMAtmCellTxInterval, acPMAtmCellRxInterface=acPMAtmCellRxInterface, acPMAtmCellDiscardedInterval=acPMAtmCellDiscardedInterval, acPMAtm=acPMAtm, acPMAtmCellDiscardedEntry=acPMAtmCellDiscardedEntry, acPMAtmCellTxInterface=acPMAtmCellTxInterface, acPMAtmCellDiscardedInterface=acPMAtmCellDiscardedInterface, acPMAtmCellRxEntry=acPMAtmCellRxEntry, audioCodes=audioCodes)
