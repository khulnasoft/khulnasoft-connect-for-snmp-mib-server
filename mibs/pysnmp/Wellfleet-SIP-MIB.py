#
# PySNMP MIB module Wellfleet-SIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-SIP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:35:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Opaque, Gauge32, Bits, Counter64, ModuleIdentity, Counter32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, mgmt, NotificationType, MibIdentifier, Integer32, enterprises, TimeTicks, IpAddress, Unsigned32, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Opaque", "Gauge32", "Bits", "Counter64", "ModuleIdentity", "Counter32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "mgmt", "NotificationType", "MibIdentifier", "Integer32", "enterprises", "TimeTicks", "IpAddress", "Unsigned32", "mib-2")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfSipGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfSipGroup")
wfSipPlcpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2))
wfSipL2 = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1), )
if mibBuilder.loadTexts: wfSipL2.setStatus('mandatory')
wfSipL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1), ).setIndexNames((0, "Wellfleet-SIP-MIB", "wfSipL2Index"))
if mibBuilder.loadTexts: wfSipL2Entry.setStatus('mandatory')
wfSipL2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2Index.setStatus('mandatory')
wfSipL2ReceivedCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2ReceivedCounts.setStatus('mandatory')
wfSipL2SentCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2SentCounts.setStatus('mandatory')
wfSipHcsOrCRCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipHcsOrCRCErrors.setStatus('mandatory')
wfSipL2PayloadLengthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2PayloadLengthErrors.setStatus('mandatory')
wfSipL2SequenceNumberErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2SequenceNumberErrors.setStatus('mandatory')
wfSipL2MidCurrentlyActiveErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2MidCurrentlyActiveErrors.setStatus('mandatory')
wfSipL2BomOrSSMsMIDErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2BomOrSSMsMIDErrors.setStatus('mandatory')
wfSipL2EomsMIDErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipL2EomsMIDErrors.setStatus('mandatory')
wfSipDs1Plcp = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1), )
if mibBuilder.loadTexts: wfSipDs1Plcp.setStatus('mandatory')
wfSipDs1PlcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1), ).setIndexNames((0, "Wellfleet-SIP-MIB", "wfSipDs1PlcpIndex"))
if mibBuilder.loadTexts: wfSipDs1PlcpEntry.setStatus('mandatory')
wfSipDs1PlcpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs1PlcpIndex.setStatus('mandatory')
wfSipDs1PlcpSEFs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs1PlcpSEFs.setStatus('mandatory')
wfSipDs1PlcpAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noalarm", 1), ("receivedfarendalarm", 2), ("incominglof", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs1PlcpAlarmState.setStatus('mandatory')
wfSipDs1PlcpUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs1PlcpUASs.setStatus('mandatory')
wfSipDs3Plcp = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2), )
if mibBuilder.loadTexts: wfSipDs3Plcp.setStatus('mandatory')
wfSipDs3PlcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1), ).setIndexNames((0, "Wellfleet-SIP-MIB", "wfSipDs3PlcpIndex"))
if mibBuilder.loadTexts: wfSipDs3PlcpEntry.setStatus('mandatory')
wfSipDs3PlcpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs3PlcpIndex.setStatus('mandatory')
wfSipDs3PlcpSEFs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs3PlcpSEFs.setStatus('mandatory')
wfSipDs3PlcpAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noalarm", 1), ("receivedfarendalarm", 2), ("incominglof", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs3PlcpAlarmState.setStatus('mandatory')
wfSipDs3PlcpUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 14, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSipDs3PlcpUASs.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-SIP-MIB", wfSipL2SentCounts=wfSipL2SentCounts, wfSipDs3PlcpSEFs=wfSipDs3PlcpSEFs, wfSipL2BomOrSSMsMIDErrors=wfSipL2BomOrSSMsMIDErrors, wfSipL2=wfSipL2, wfSipL2PayloadLengthErrors=wfSipL2PayloadLengthErrors, wfSipDs1PlcpEntry=wfSipDs1PlcpEntry, wfSipL2ReceivedCounts=wfSipL2ReceivedCounts, wfSipHcsOrCRCErrors=wfSipHcsOrCRCErrors, wfSipL2EomsMIDErrors=wfSipL2EomsMIDErrors, wfSipL2Index=wfSipL2Index, wfSipDs1Plcp=wfSipDs1Plcp, wfSipDs3PlcpUASs=wfSipDs3PlcpUASs, wfSipDs3PlcpEntry=wfSipDs3PlcpEntry, wfSipDs1PlcpAlarmState=wfSipDs1PlcpAlarmState, wfSipDs3PlcpIndex=wfSipDs3PlcpIndex, wfSipDs1PlcpUASs=wfSipDs1PlcpUASs, wfSipL2SequenceNumberErrors=wfSipL2SequenceNumberErrors, wfSipDs3Plcp=wfSipDs3Plcp, wfSipL2MidCurrentlyActiveErrors=wfSipL2MidCurrentlyActiveErrors, wfSipDs1PlcpIndex=wfSipDs1PlcpIndex, wfSipDs3PlcpAlarmState=wfSipDs3PlcpAlarmState, wfSipDs1PlcpSEFs=wfSipDs1PlcpSEFs, wfSipL2Entry=wfSipL2Entry, wfSipPlcpGroup=wfSipPlcpGroup)
