#
# PySNMP MIB module ELTEX-IPSLA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-IPSLA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, Counter64, Unsigned32, NotificationType, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, ObjectIdentity, IpAddress, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Counter64", "Unsigned32", "NotificationType", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "ObjectIdentity", "IpAddress", "TimeTicks", "ModuleIdentity")
TimeStamp, RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
eltexIpSlaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 32))
if mibBuilder.loadTexts: eltexIpSlaMIB.setLastUpdated('201505250000Z')
if mibBuilder.loadTexts: eltexIpSlaMIB.setOrganization('Eltex Ltd.')
eltexIpSlaObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 32, 1))
eltexIpSlaAppl = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 32, 1, 1))
eltexIpSlaAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2))
eltexIpSlaStats = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3))
eltexIpSlaSchedule = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 32, 1, 4))
class EltexIpSlaOperationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("icmp-echo", 1), ("udp-jitter", 2))

class EltexIpSlaOperationStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

eltexIpSlaApplResponder = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 32, 1, 1, 13))
eltexIpSlaApplResponderUdpJitterPort = MibScalar((1, 3, 6, 1, 4, 1, 35265, 32, 1, 1, 13, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaApplResponderUdpJitterPort.setStatus('current')
eltexIpSlaAdminCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminCtrlTable.setStatus('current')
eltexIpSlaAdminCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1), ).setMaxAccess("readwrite").setIndexNames((0, "ELTEX-IPSLA-MIB", "eltexIpSlaAdminCtrlIndex"))
if mibBuilder.loadTexts: eltexIpSlaAdminCtrlEntry.setStatus('current')
eltexIpSlaAdminCtrlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminCtrlIndex.setStatus('current')
eltexIpSlaAdminCtrlType = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 2), EltexIpSlaOperationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminCtrlType.setStatus('current')
eltexIpSlaAdminCtrlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 3), EltexIpSlaOperationStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaAdminCtrlStatus.setStatus('current')
eltexIpSlaAdminCtrlFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 604800)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminCtrlFrequency.setStatus('current')
eltexIpSlaAdminCtrlTag = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminCtrlTag.setStatus('current')
eltexIpSlaAdminCtrlOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminCtrlOwner.setStatus('current')
eltexIpSlaAdminCtrlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminCtrlRowStatus.setStatus('current')
eltexIpSlaAdminIcmpEchoTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminIcmpEchoTable.setStatus('current')
eltexIpSlaAdminIcmpEchoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1), ).setMaxAccess("readwrite").setIndexNames((0, "ELTEX-IPSLA-MIB", "eltexIpSlaAdminIcmpEchoIndex"))
if mibBuilder.loadTexts: eltexIpSlaAdminIcmpEchoEntry.setStatus('current')
eltexIpSlaAdminIcmpEchoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminIcmpEchoIndex.setStatus('current')
eltexIpSlaAdminIcmpEchoTargetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminIcmpEchoTargetAddress.setStatus('current')
eltexIpSlaAdminIcmpEchoSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminIcmpEchoSourceAddress.setStatus('current')
eltexIpSlaAdminIcmpEchoSourceInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminIcmpEchoSourceInterface.setStatus('current')
eltexIpSlaAdminIcmpEchoTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminIcmpEchoTimeOut.setStatus('current')
eltexIpSlaAdminIcmpEchoReqDataSize = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1432)).clone(56)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminIcmpEchoReqDataSize.setStatus('current')
eltexIpSlaAdminIcmpEchoTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminIcmpEchoTOS.setStatus('current')
eltexIpSlaAdminIcmpEchoRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminIcmpEchoRowStatus.setStatus('current')
class EltexIpSlaStatsOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("failed", 2))

eltexIpSlaAdminUdpJitterTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterTable.setStatus('current')
eltexIpSlaAdminUdpJitterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1), ).setMaxAccess("readwrite").setIndexNames((0, "ELTEX-IPSLA-MIB", "eltexIpSlaAdminUdpJitterIndex"))
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterEntry.setStatus('current')
eltexIpSlaAdminUdpJitterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterIndex.setStatus('current')
eltexIpSlaAdminUdpJitterTargetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterTargetAddress.setStatus('current')
eltexIpSlaAdminUdpJitterTargetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterTargetPort.setStatus('current')
eltexIpSlaAdminUdpJitterSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterSourceAddress.setStatus('current')
eltexIpSlaAdminUdpJitterSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterSourcePort.setStatus('current')
eltexIpSlaAdminUdpJitterSourceInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 6), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterSourceInterface.setStatus('current')
eltexIpSlaAdminUdpJitterInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60000)).clone(20)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterInterval.setStatus('current')
eltexIpSlaAdminUdpJitterNumPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterNumPackets.setStatus('current')
eltexIpSlaAdminUdpJitterTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterTimeOut.setStatus('current')
eltexIpSlaAdminUdpJitterReqDataSize = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1432)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterReqDataSize.setStatus('current')
eltexIpSlaAdminUdpJitterTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterTOS.setStatus('current')
eltexIpSlaAdminUdpJitterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 12), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaAdminUdpJitterRowStatus.setStatus('current')
eltexIpSlaStatsIcmpEchoTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoTable.setStatus('current')
eltexIpSlaStatsIcmpEchoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1), ).setMaxAccess("readwrite").setIndexNames((0, "ELTEX-IPSLA-MIB", "eltexIpSlaStatsIcmpEchoIndex"))
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoEntry.setStatus('current')
eltexIpSlaStatsIcmpEchoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoIndex.setStatus('current')
eltexIpSlaStatsIcmpEchoLastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 2), EltexIpSlaStatsOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoLastStatus.setStatus('current')
eltexIpSlaStatsIcmpEchoLastLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 3), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoLastLatency.setStatus('current')
eltexIpSlaStatsIcmpEchoMinLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 4), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoMinLatency.setStatus('current')
eltexIpSlaStatsIcmpEchoAvgLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 5), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoAvgLatency.setStatus('current')
eltexIpSlaStatsIcmpEchoMaxLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 6), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoMaxLatency.setStatus('current')
eltexIpSlaStatsIcmpEchoOperationsCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoOperationsCtr.setStatus('current')
eltexIpSlaStatsIcmpEchoSuccessesCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoSuccessesCtr.setStatus('current')
eltexIpSlaStatsIcmpEchoFailuresCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoFailuresCtr.setStatus('current')
eltexIpSlaStatsIcmpEchoTimeoutCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoTimeoutCtr.setStatus('current')
eltexIpSlaStatsIcmpEchoUnreachNetCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoUnreachNetCtr.setStatus('current')
eltexIpSlaStatsIcmpEchoUnreachHostCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoUnreachHostCtr.setStatus('current')
eltexIpSlaStatsIcmpEchoUnreachProtCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoUnreachProtCtr.setStatus('current')
eltexIpSlaStatsIcmpEchoExTimeTransCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoExTimeTransCtr.setStatus('current')
eltexIpSlaStatsIcmpEchoExTimeReassCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoExTimeReassCtr.setStatus('current')
eltexIpSlaStatsIcmpEchoUnableSendCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoUnableSendCtr.setStatus('current')
eltexIpSlaStatsIcmpEchoBadReplyCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsIcmpEchoBadReplyCtr.setStatus('current')
eltexIpSlaStatsUdpJitterTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterTable.setStatus('current')
eltexIpSlaStatsUdpJitterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1), ).setMaxAccess("readwrite").setIndexNames((0, "ELTEX-IPSLA-MIB", "eltexIpSlaStatsUdpJitterIndex"))
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterEntry.setStatus('current')
eltexIpSlaStatsUdpJitterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterIndex.setStatus('current')
eltexIpSlaStatsUdpJitterLastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 2), EltexIpSlaStatsOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterLastStatus.setStatus('current')
eltexIpSlaStatsUdpJitterLastLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 3), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterLastLatency.setStatus('current')
eltexIpSlaStatsUdpJitterNumLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 4), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterNumLatency.setStatus('current')
eltexIpSlaStatsUdpJitterSumLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 5), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterSumLatency.setStatus('current')
eltexIpSlaStatsUdpJitterMinLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 6), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMinLatency.setStatus('current')
eltexIpSlaStatsUdpJitterAvgLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 7), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterAvgLatency.setStatus('current')
eltexIpSlaStatsUdpJitterMaxLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 8), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMaxLatency.setStatus('current')
eltexIpSlaStatsUdpJitterNumSDLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterNumSDLatency.setStatus('current')
eltexIpSlaStatsUdpJitterSumSDLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 10), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterSumSDLatency.setStatus('current')
eltexIpSlaStatsUdpJitterMinSDLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 11), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMinSDLatency.setStatus('current')
eltexIpSlaStatsUdpJitterAvgSDLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 12), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterAvgSDLatency.setStatus('current')
eltexIpSlaStatsUdpJitterMaxSDLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 13), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMaxSDLatency.setStatus('current')
eltexIpSlaStatsUdpJitterNumDSLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterNumDSLatency.setStatus('current')
eltexIpSlaStatsUdpJitterSumDSLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 15), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterSumDSLatency.setStatus('current')
eltexIpSlaStatsUdpJitterMinDSLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 16), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMinDSLatency.setStatus('current')
eltexIpSlaStatsUdpJitterAvgDSLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 17), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterAvgDSLatency.setStatus('current')
eltexIpSlaStatsUdpJitterMaxDSLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 18), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMaxDSLatency.setStatus('current')
eltexIpSlaStatsUdpJitterNumSDPosJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterNumSDPosJitter.setStatus('current')
eltexIpSlaStatsUdpJitterSumSDPosJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterSumSDPosJitter.setStatus('current')
eltexIpSlaStatsUdpJitterMinSDPosJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 21), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMinSDPosJitter.setStatus('current')
eltexIpSlaStatsUdpJitterAvgSDPosJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 22), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterAvgSDPosJitter.setStatus('current')
eltexIpSlaStatsUdpJitterMaxSDPosJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 23), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMaxSDPosJitter.setStatus('current')
eltexIpSlaStatsUdpJitterNumDSPosJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterNumDSPosJitter.setStatus('current')
eltexIpSlaStatsUdpJitterSumDSPosJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 25), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterSumDSPosJitter.setStatus('current')
eltexIpSlaStatsUdpJitterMinDSPosJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 26), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMinDSPosJitter.setStatus('current')
eltexIpSlaStatsUdpJitterAvgDSPosJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 27), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterAvgDSPosJitter.setStatus('current')
eltexIpSlaStatsUdpJitterMaxDSPosJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 28), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMaxDSPosJitter.setStatus('current')
eltexIpSlaStatsUdpJitterNumSDNegJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterNumSDNegJitter.setStatus('current')
eltexIpSlaStatsUdpJitterSumSDNegJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterSumSDNegJitter.setStatus('current')
eltexIpSlaStatsUdpJitterMinSDNegJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 31), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMinSDNegJitter.setStatus('current')
eltexIpSlaStatsUdpJitterAvgSDNegJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 32), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterAvgSDNegJitter.setStatus('current')
eltexIpSlaStatsUdpJitterMaxSDNegJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 33), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMaxSDNegJitter.setStatus('current')
eltexIpSlaStatsUdpJitterNumDSNegJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterNumDSNegJitter.setStatus('current')
eltexIpSlaStatsUdpJitterSumDSNegJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 35), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterSumDSNegJitter.setStatus('current')
eltexIpSlaStatsUdpJitterMinDSNegJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 36), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMinDSNegJitter.setStatus('current')
eltexIpSlaStatsUdpJitterAvgDSNegJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 37), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterAvgDSNegJitter.setStatus('current')
eltexIpSlaStatsUdpJitterMaxDSNegJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 38), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterMaxDSNegJitter.setStatus('current')
eltexIpSlaStatsUdpJitterOperationsCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterOperationsCtr.setStatus('current')
eltexIpSlaStatsUdpJitterSuccessesCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterSuccessesCtr.setStatus('current')
eltexIpSlaStatsUdpJitterFailuresCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterFailuresCtr.setStatus('current')
eltexIpSlaStatsUdpJitterTimeoutCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterTimeoutCtr.setStatus('current')
eltexIpSlaStatsUdpJitterUnreachNetCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterUnreachNetCtr.setStatus('current')
eltexIpSlaStatsUdpJitterUnreachHostCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterUnreachHostCtr.setStatus('current')
eltexIpSlaStatsUdpJitterUnreachPortCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterUnreachPortCtr.setStatus('current')
eltexIpSlaStatsUdpJitterUnreachProtCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterUnreachProtCtr.setStatus('current')
eltexIpSlaStatsUdpJitterExTimeTransCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 47), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterExTimeTransCtr.setStatus('current')
eltexIpSlaStatsUdpJitterExTimeReassCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterExTimeReassCtr.setStatus('current')
eltexIpSlaStatsUdpJitterUnableSendCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 49), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterUnableSendCtr.setStatus('current')
eltexIpSlaStatsUdpJitterBadReplyCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 50), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterBadReplyCtr.setStatus('current')
eltexIpSlaStatsUdpJitterPacketsOOSCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 51), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexIpSlaStatsUdpJitterPacketsOOSCtr.setStatus('current')
eltexIpSlaScheduleStartTrigger = MibScalar((1, 3, 6, 1, 4, 1, 35265, 32, 1, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaScheduleStartTrigger.setStatus('current')
eltexIpSlaScheduleStopTrigger = MibScalar((1, 3, 6, 1, 4, 1, 35265, 32, 1, 4, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexIpSlaScheduleStopTrigger.setStatus('current')
mibBuilder.exportSymbols("ELTEX-IPSLA-MIB", eltexIpSlaStatsUdpJitterNumDSPosJitter=eltexIpSlaStatsUdpJitterNumDSPosJitter, eltexIpSlaStatsUdpJitterSuccessesCtr=eltexIpSlaStatsUdpJitterSuccessesCtr, eltexIpSlaStatsUdpJitterAvgSDPosJitter=eltexIpSlaStatsUdpJitterAvgSDPosJitter, eltexIpSlaAdminUdpJitterTable=eltexIpSlaAdminUdpJitterTable, eltexIpSlaStatsUdpJitterMaxDSLatency=eltexIpSlaStatsUdpJitterMaxDSLatency, eltexIpSlaStatsUdpJitterMinDSNegJitter=eltexIpSlaStatsUdpJitterMinDSNegJitter, eltexIpSlaAdminCtrlIndex=eltexIpSlaAdminCtrlIndex, eltexIpSlaStatsIcmpEchoLastStatus=eltexIpSlaStatsIcmpEchoLastStatus, PYSNMP_MODULE_ID=eltexIpSlaMIB, eltexIpSlaStatsIcmpEchoMinLatency=eltexIpSlaStatsIcmpEchoMinLatency, eltexIpSlaStatsUdpJitterNumSDNegJitter=eltexIpSlaStatsUdpJitterNumSDNegJitter, eltexIpSlaAdminIcmpEchoTOS=eltexIpSlaAdminIcmpEchoTOS, eltexIpSlaStatsUdpJitterEntry=eltexIpSlaStatsUdpJitterEntry, eltexIpSlaAdminUdpJitterIndex=eltexIpSlaAdminUdpJitterIndex, eltexIpSlaStatsUdpJitterMaxLatency=eltexIpSlaStatsUdpJitterMaxLatency, eltexIpSlaScheduleStartTrigger=eltexIpSlaScheduleStartTrigger, eltexIpSlaStatsIcmpEchoUnreachHostCtr=eltexIpSlaStatsIcmpEchoUnreachHostCtr, eltexIpSlaStatsIcmpEchoSuccessesCtr=eltexIpSlaStatsIcmpEchoSuccessesCtr, eltexIpSlaStatsUdpJitterLastStatus=eltexIpSlaStatsUdpJitterLastStatus, eltexIpSlaStatsUdpJitterPacketsOOSCtr=eltexIpSlaStatsUdpJitterPacketsOOSCtr, eltexIpSlaStatsUdpJitterAvgDSNegJitter=eltexIpSlaStatsUdpJitterAvgDSNegJitter, eltexIpSlaAdminUdpJitterEntry=eltexIpSlaAdminUdpJitterEntry, eltexIpSlaStatsUdpJitterMinLatency=eltexIpSlaStatsUdpJitterMinLatency, eltexIpSlaAdminUdpJitterTimeOut=eltexIpSlaAdminUdpJitterTimeOut, eltexIpSlaStatsUdpJitterAvgDSLatency=eltexIpSlaStatsUdpJitterAvgDSLatency, eltexIpSlaStatsUdpJitterNumSDPosJitter=eltexIpSlaStatsUdpJitterNumSDPosJitter, eltexIpSlaObjects=eltexIpSlaObjects, eltexIpSlaStatsIcmpEchoExTimeReassCtr=eltexIpSlaStatsIcmpEchoExTimeReassCtr, eltexIpSlaStatsUdpJitterUnreachProtCtr=eltexIpSlaStatsUdpJitterUnreachProtCtr, eltexIpSlaStatsUdpJitterAvgLatency=eltexIpSlaStatsUdpJitterAvgLatency, eltexIpSlaStatsUdpJitterTimeoutCtr=eltexIpSlaStatsUdpJitterTimeoutCtr, eltexIpSlaStatsUdpJitterNumDSNegJitter=eltexIpSlaStatsUdpJitterNumDSNegJitter, eltexIpSlaAdminCtrlEntry=eltexIpSlaAdminCtrlEntry, eltexIpSlaStatsUdpJitterTable=eltexIpSlaStatsUdpJitterTable, eltexIpSlaAppl=eltexIpSlaAppl, eltexIpSlaAdminIcmpEchoReqDataSize=eltexIpSlaAdminIcmpEchoReqDataSize, eltexIpSlaStatsIcmpEchoExTimeTransCtr=eltexIpSlaStatsIcmpEchoExTimeTransCtr, eltexIpSlaAdminIcmpEchoTimeOut=eltexIpSlaAdminIcmpEchoTimeOut, eltexIpSlaAdminUdpJitterRowStatus=eltexIpSlaAdminUdpJitterRowStatus, eltexIpSlaApplResponder=eltexIpSlaApplResponder, eltexIpSlaStatsUdpJitterAvgSDNegJitter=eltexIpSlaStatsUdpJitterAvgSDNegJitter, eltexIpSlaAdminUdpJitterInterval=eltexIpSlaAdminUdpJitterInterval, eltexIpSlaStatsUdpJitterMinSDPosJitter=eltexIpSlaStatsUdpJitterMinSDPosJitter, eltexIpSlaStatsIcmpEchoEntry=eltexIpSlaStatsIcmpEchoEntry, eltexIpSlaStatsUdpJitterSumDSPosJitter=eltexIpSlaStatsUdpJitterSumDSPosJitter, eltexIpSlaSchedule=eltexIpSlaSchedule, eltexIpSlaStatsIcmpEchoAvgLatency=eltexIpSlaStatsIcmpEchoAvgLatency, eltexIpSlaAdminUdpJitterReqDataSize=eltexIpSlaAdminUdpJitterReqDataSize, eltexIpSlaStats=eltexIpSlaStats, eltexIpSlaStatsUdpJitterSumSDNegJitter=eltexIpSlaStatsUdpJitterSumSDNegJitter, eltexIpSlaStatsUdpJitterUnreachPortCtr=eltexIpSlaStatsUdpJitterUnreachPortCtr, eltexIpSlaStatsUdpJitterUnreachHostCtr=eltexIpSlaStatsUdpJitterUnreachHostCtr, eltexIpSlaAdminCtrlRowStatus=eltexIpSlaAdminCtrlRowStatus, eltexIpSlaAdmin=eltexIpSlaAdmin, eltexIpSlaStatsUdpJitterNumSDLatency=eltexIpSlaStatsUdpJitterNumSDLatency, eltexIpSlaStatsUdpJitterSumLatency=eltexIpSlaStatsUdpJitterSumLatency, eltexIpSlaAdminUdpJitterTargetAddress=eltexIpSlaAdminUdpJitterTargetAddress, eltexIpSlaStatsUdpJitterMaxSDLatency=eltexIpSlaStatsUdpJitterMaxSDLatency, eltexIpSlaStatsUdpJitterLastLatency=eltexIpSlaStatsUdpJitterLastLatency, eltexIpSlaStatsIcmpEchoMaxLatency=eltexIpSlaStatsIcmpEchoMaxLatency, eltexIpSlaStatsUdpJitterMinDSLatency=eltexIpSlaStatsUdpJitterMinDSLatency, eltexIpSlaAdminIcmpEchoTargetAddress=eltexIpSlaAdminIcmpEchoTargetAddress, eltexIpSlaAdminIcmpEchoRowStatus=eltexIpSlaAdminIcmpEchoRowStatus, eltexIpSlaAdminCtrlFrequency=eltexIpSlaAdminCtrlFrequency, eltexIpSlaStatsUdpJitterFailuresCtr=eltexIpSlaStatsUdpJitterFailuresCtr, eltexIpSlaAdminUdpJitterNumPackets=eltexIpSlaAdminUdpJitterNumPackets, eltexIpSlaStatsUdpJitterNumDSLatency=eltexIpSlaStatsUdpJitterNumDSLatency, eltexIpSlaStatsUdpJitterUnableSendCtr=eltexIpSlaStatsUdpJitterUnableSendCtr, eltexIpSlaStatsUdpJitterMinSDNegJitter=eltexIpSlaStatsUdpJitterMinSDNegJitter, eltexIpSlaAdminCtrlType=eltexIpSlaAdminCtrlType, eltexIpSlaAdminUdpJitterSourcePort=eltexIpSlaAdminUdpJitterSourcePort, eltexIpSlaStatsUdpJitterSumDSNegJitter=eltexIpSlaStatsUdpJitterSumDSNegJitter, eltexIpSlaStatsIcmpEchoUnreachProtCtr=eltexIpSlaStatsIcmpEchoUnreachProtCtr, eltexIpSlaAdminUdpJitterSourceAddress=eltexIpSlaAdminUdpJitterSourceAddress, eltexIpSlaAdminCtrlTag=eltexIpSlaAdminCtrlTag, eltexIpSlaAdminIcmpEchoSourceAddress=eltexIpSlaAdminIcmpEchoSourceAddress, eltexIpSlaAdminIcmpEchoTable=eltexIpSlaAdminIcmpEchoTable, eltexIpSlaStatsUdpJitterIndex=eltexIpSlaStatsUdpJitterIndex, eltexIpSlaApplResponderUdpJitterPort=eltexIpSlaApplResponderUdpJitterPort, eltexIpSlaAdminCtrlOwner=eltexIpSlaAdminCtrlOwner, eltexIpSlaStatsIcmpEchoUnableSendCtr=eltexIpSlaStatsIcmpEchoUnableSendCtr, eltexIpSlaStatsUdpJitterSumDSLatency=eltexIpSlaStatsUdpJitterSumDSLatency, eltexIpSlaStatsUdpJitterMaxDSPosJitter=eltexIpSlaStatsUdpJitterMaxDSPosJitter, eltexIpSlaStatsUdpJitterMaxSDNegJitter=eltexIpSlaStatsUdpJitterMaxSDNegJitter, eltexIpSlaAdminUdpJitterTOS=eltexIpSlaAdminUdpJitterTOS, eltexIpSlaStatsIcmpEchoTable=eltexIpSlaStatsIcmpEchoTable, eltexIpSlaStatsUdpJitterAvgSDLatency=eltexIpSlaStatsUdpJitterAvgSDLatency, eltexIpSlaAdminIcmpEchoSourceInterface=eltexIpSlaAdminIcmpEchoSourceInterface, eltexIpSlaStatsUdpJitterMinDSPosJitter=eltexIpSlaStatsUdpJitterMinDSPosJitter, eltexIpSlaAdminUdpJitterTargetPort=eltexIpSlaAdminUdpJitterTargetPort, eltexIpSlaStatsIcmpEchoIndex=eltexIpSlaStatsIcmpEchoIndex, eltexIpSlaAdminIcmpEchoEntry=eltexIpSlaAdminIcmpEchoEntry, eltexIpSlaStatsUdpJitterAvgDSPosJitter=eltexIpSlaStatsUdpJitterAvgDSPosJitter, eltexIpSlaAdminCtrlStatus=eltexIpSlaAdminCtrlStatus, eltexIpSlaScheduleStopTrigger=eltexIpSlaScheduleStopTrigger, eltexIpSlaStatsUdpJitterMaxDSNegJitter=eltexIpSlaStatsUdpJitterMaxDSNegJitter, eltexIpSlaStatsUdpJitterMinSDLatency=eltexIpSlaStatsUdpJitterMinSDLatency, eltexIpSlaStatsUdpJitterExTimeTransCtr=eltexIpSlaStatsUdpJitterExTimeTransCtr, eltexIpSlaStatsUdpJitterBadReplyCtr=eltexIpSlaStatsUdpJitterBadReplyCtr, eltexIpSlaStatsUdpJitterMaxSDPosJitter=eltexIpSlaStatsUdpJitterMaxSDPosJitter, EltexIpSlaOperationStatus=EltexIpSlaOperationStatus, eltexIpSlaStatsIcmpEchoBadReplyCtr=eltexIpSlaStatsIcmpEchoBadReplyCtr, eltexIpSlaStatsUdpJitterSumSDPosJitter=eltexIpSlaStatsUdpJitterSumSDPosJitter, eltexIpSlaStatsUdpJitterExTimeReassCtr=eltexIpSlaStatsUdpJitterExTimeReassCtr, eltexIpSlaStatsIcmpEchoTimeoutCtr=eltexIpSlaStatsIcmpEchoTimeoutCtr, eltexIpSlaStatsUdpJitterSumSDLatency=eltexIpSlaStatsUdpJitterSumSDLatency, eltexIpSlaStatsIcmpEchoLastLatency=eltexIpSlaStatsIcmpEchoLastLatency, eltexIpSlaStatsIcmpEchoOperationsCtr=eltexIpSlaStatsIcmpEchoOperationsCtr, eltexIpSlaAdminCtrlTable=eltexIpSlaAdminCtrlTable, eltexIpSlaStatsUdpJitterUnreachNetCtr=eltexIpSlaStatsUdpJitterUnreachNetCtr, eltexIpSlaAdminUdpJitterSourceInterface=eltexIpSlaAdminUdpJitterSourceInterface, eltexIpSlaStatsIcmpEchoFailuresCtr=eltexIpSlaStatsIcmpEchoFailuresCtr, EltexIpSlaOperationType=EltexIpSlaOperationType, eltexIpSlaMIB=eltexIpSlaMIB, eltexIpSlaStatsIcmpEchoUnreachNetCtr=eltexIpSlaStatsIcmpEchoUnreachNetCtr, eltexIpSlaStatsUdpJitterOperationsCtr=eltexIpSlaStatsUdpJitterOperationsCtr, eltexIpSlaAdminIcmpEchoIndex=eltexIpSlaAdminIcmpEchoIndex, eltexIpSlaStatsUdpJitterNumLatency=eltexIpSlaStatsUdpJitterNumLatency, EltexIpSlaStatsOperStatus=EltexIpSlaStatsOperStatus)
