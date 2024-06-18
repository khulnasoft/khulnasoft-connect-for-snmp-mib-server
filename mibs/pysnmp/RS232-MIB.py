#
# PySNMP MIB module RS232-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RS232-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:50:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ObjectIdentity, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, experimental, iso, Bits, Integer32, NotificationType, Counter32, TimeTicks, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "experimental", "iso", "Bits", "Integer32", "NotificationType", "Counter32", "TimeTicks", "IpAddress", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rs232 = MibIdentifier((1, 3, 6, 1, 3, 20))
rs232Number = MibScalar((1, 3, 6, 1, 3, 20, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232Number.setStatus('mandatory')
rs232PortTable = MibTable((1, 3, 6, 1, 3, 20, 2), )
if mibBuilder.loadTexts: rs232PortTable.setStatus('mandatory')
rs232PortEntry = MibTableRow((1, 3, 6, 1, 3, 20, 2, 1), ).setIndexNames((0, "RS232-MIB", "rs232PortIndex"))
if mibBuilder.loadTexts: rs232PortEntry.setStatus('mandatory')
rs232PortIndex = MibTableColumn((1, 3, 6, 1, 3, 20, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232PortIndex.setStatus('mandatory')
rs232PortType = MibTableColumn((1, 3, 6, 1, 3, 20, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("rs232", 2), ("rs422", 3), ("rs423", 4), ("v35", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232PortType.setStatus('mandatory')
rs232PortInSigNumber = MibTableColumn((1, 3, 6, 1, 3, 20, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232PortInSigNumber.setStatus('mandatory')
rs232PortOutSigNumber = MibTableColumn((1, 3, 6, 1, 3, 20, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232PortOutSigNumber.setStatus('mandatory')
rs232PortInSpeed = MibTableColumn((1, 3, 6, 1, 3, 20, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232PortInSpeed.setStatus('mandatory')
rs232PortOutSpeed = MibTableColumn((1, 3, 6, 1, 3, 20, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232PortOutSpeed.setStatus('mandatory')
rs232AsyncPortTable = MibTable((1, 3, 6, 1, 3, 20, 3), )
if mibBuilder.loadTexts: rs232AsyncPortTable.setStatus('mandatory')
rs232AsyncPortEntry = MibTableRow((1, 3, 6, 1, 3, 20, 3, 1), ).setIndexNames((0, "RS232-MIB", "rs232AsyncPortIndex"))
if mibBuilder.loadTexts: rs232AsyncPortEntry.setStatus('mandatory')
rs232AsyncPortIndex = MibTableColumn((1, 3, 6, 1, 3, 20, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232AsyncPortIndex.setStatus('mandatory')
rs232AsyncPortBits = MibTableColumn((1, 3, 6, 1, 3, 20, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232AsyncPortBits.setStatus('mandatory')
rs232AsyncPortStopBits = MibTableColumn((1, 3, 6, 1, 3, 20, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("one-and-half", 3), ("dynamic", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232AsyncPortStopBits.setStatus('mandatory')
rs232AsyncPortParity = MibTableColumn((1, 3, 6, 1, 3, 20, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("odd", 2), ("even", 3), ("mark", 4), ("space", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232AsyncPortParity.setStatus('mandatory')
rs232AsyncPortAutobaud = MibTableColumn((1, 3, 6, 1, 3, 20, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232AsyncPortAutobaud.setStatus('mandatory')
rs232AsyncPortParityErrs = MibTableColumn((1, 3, 6, 1, 3, 20, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232AsyncPortParityErrs.setStatus('mandatory')
rs232AsyncPortFramingErrs = MibTableColumn((1, 3, 6, 1, 3, 20, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232AsyncPortFramingErrs.setStatus('mandatory')
rs232AsyncPortOverrunErrs = MibTableColumn((1, 3, 6, 1, 3, 20, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232AsyncPortOverrunErrs.setStatus('mandatory')
rs232SyncPortTable = MibTable((1, 3, 6, 1, 3, 20, 4), )
if mibBuilder.loadTexts: rs232SyncPortTable.setStatus('mandatory')
rs232SyncPortEntry = MibTableRow((1, 3, 6, 1, 3, 20, 4, 1), ).setIndexNames((0, "RS232-MIB", "rs232SyncPortIndex"))
if mibBuilder.loadTexts: rs232SyncPortEntry.setStatus('mandatory')
rs232SyncPortIndex = MibTableColumn((1, 3, 6, 1, 3, 20, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortIndex.setStatus('mandatory')
rs232SyncPortClockSource = MibTableColumn((1, 3, 6, 1, 3, 20, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("internal", 1), ("external", 2), ("split", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232SyncPortClockSource.setStatus('mandatory')
rs232SyncPortFrameCheckErrs = MibTableColumn((1, 3, 6, 1, 3, 20, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortFrameCheckErrs.setStatus('mandatory')
rs232SyncPortTransmitUnderrunErrs = MibTableColumn((1, 3, 6, 1, 3, 20, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortTransmitUnderrunErrs.setStatus('mandatory')
rs232SyncPortReceiveOverrunErrs = MibTableColumn((1, 3, 6, 1, 3, 20, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortReceiveOverrunErrs.setStatus('mandatory')
rs232SyncPortInterruptedFrames = MibTableColumn((1, 3, 6, 1, 3, 20, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortInterruptedFrames.setStatus('mandatory')
rs232SyncPortAbortedFrames = MibTableColumn((1, 3, 6, 1, 3, 20, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortAbortedFrames.setStatus('mandatory')
rs232InSigTable = MibTable((1, 3, 6, 1, 3, 20, 5), )
if mibBuilder.loadTexts: rs232InSigTable.setStatus('mandatory')
rs232InSigEntry = MibTableRow((1, 3, 6, 1, 3, 20, 5, 1), ).setIndexNames((0, "RS232-MIB", "rs232InSigPortIndex"), (0, "RS232-MIB", "rs232InSigName"))
if mibBuilder.loadTexts: rs232InSigEntry.setStatus('mandatory')
rs232InSigPortIndex = MibTableColumn((1, 3, 6, 1, 3, 20, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232InSigPortIndex.setStatus('mandatory')
rs232InSigName = MibTableColumn((1, 3, 6, 1, 3, 20, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("rts", 1), ("cts", 2), ("dsr", 3), ("dtr", 4), ("ri", 5), ("dcd", 6), ("sq", 7), ("srs", 8), ("srts", 9), ("scts", 10), ("sdcd", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232InSigName.setStatus('mandatory')
rs232InSigState = MibTableColumn((1, 3, 6, 1, 3, 20, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("on", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232InSigState.setStatus('mandatory')
rs232InSigChanges = MibTableColumn((1, 3, 6, 1, 3, 20, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232InSigChanges.setStatus('mandatory')
rs232OutSigTable = MibTable((1, 3, 6, 1, 3, 20, 6), )
if mibBuilder.loadTexts: rs232OutSigTable.setStatus('mandatory')
rs232OutSigEntry = MibTableRow((1, 3, 6, 1, 3, 20, 6, 1), ).setIndexNames((0, "RS232-MIB", "rs232OutSigPortIndex"), (0, "RS232-MIB", "rs232OutSigName"))
if mibBuilder.loadTexts: rs232OutSigEntry.setStatus('mandatory')
rs232OutSigPortIndex = MibTableColumn((1, 3, 6, 1, 3, 20, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232OutSigPortIndex.setStatus('mandatory')
rs232OutSigName = MibTableColumn((1, 3, 6, 1, 3, 20, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("rts", 1), ("cts", 2), ("dsr", 3), ("dtr", 4), ("ri", 5), ("dcd", 6), ("sq", 7), ("srs", 8), ("srts", 9), ("scts", 10), ("sdcd", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232OutSigName.setStatus('mandatory')
rs232OutSigState = MibTableColumn((1, 3, 6, 1, 3, 20, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("on", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232OutSigState.setStatus('mandatory')
rs232OutSigChanges = MibTableColumn((1, 3, 6, 1, 3, 20, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232OutSigChanges.setStatus('mandatory')
mibBuilder.exportSymbols("RS232-MIB", rs232OutSigName=rs232OutSigName, rs232AsyncPortBits=rs232AsyncPortBits, rs232AsyncPortParityErrs=rs232AsyncPortParityErrs, rs232Number=rs232Number, rs232InSigPortIndex=rs232InSigPortIndex, rs232InSigEntry=rs232InSigEntry, rs232PortType=rs232PortType, rs232SyncPortClockSource=rs232SyncPortClockSource, rs232InSigChanges=rs232InSigChanges, rs232AsyncPortEntry=rs232AsyncPortEntry, rs232SyncPortEntry=rs232SyncPortEntry, rs232SyncPortTable=rs232SyncPortTable, rs232PortInSpeed=rs232PortInSpeed, rs232AsyncPortTable=rs232AsyncPortTable, rs232AsyncPortStopBits=rs232AsyncPortStopBits, rs232OutSigPortIndex=rs232OutSigPortIndex, rs232SyncPortInterruptedFrames=rs232SyncPortInterruptedFrames, rs232SyncPortTransmitUnderrunErrs=rs232SyncPortTransmitUnderrunErrs, rs232PortTable=rs232PortTable, rs232SyncPortAbortedFrames=rs232SyncPortAbortedFrames, rs232AsyncPortFramingErrs=rs232AsyncPortFramingErrs, rs232InSigName=rs232InSigName, rs232AsyncPortOverrunErrs=rs232AsyncPortOverrunErrs, rs232OutSigChanges=rs232OutSigChanges, rs232AsyncPortParity=rs232AsyncPortParity, rs232PortIndex=rs232PortIndex, rs232OutSigEntry=rs232OutSigEntry, rs232InSigState=rs232InSigState, rs232OutSigTable=rs232OutSigTable, rs232=rs232, rs232PortOutSpeed=rs232PortOutSpeed, rs232SyncPortIndex=rs232SyncPortIndex, rs232PortEntry=rs232PortEntry, rs232AsyncPortIndex=rs232AsyncPortIndex, rs232InSigTable=rs232InSigTable, rs232SyncPortFrameCheckErrs=rs232SyncPortFrameCheckErrs, rs232PortOutSigNumber=rs232PortOutSigNumber, rs232AsyncPortAutobaud=rs232AsyncPortAutobaud, rs232OutSigState=rs232OutSigState, rs232SyncPortReceiveOverrunErrs=rs232SyncPortReceiveOverrunErrs, rs232PortInSigNumber=rs232PortInSigNumber)
