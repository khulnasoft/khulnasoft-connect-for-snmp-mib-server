#
# PySNMP MIB module ALTIGA-PPTP-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-PPTP-STATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:05:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alPptpMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alPptpMibModule")
alPptpGroup, alStatsPptp = mibBuilder.importSymbols("ALTIGA-MIB", "alPptpGroup", "alStatsPptp")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Counter32, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, ModuleIdentity, Integer32, MibIdentifier, Unsigned32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Counter32", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "ModuleIdentity", "Integer32", "MibIdentifier", "Unsigned32", "iso", "NotificationType")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
altigaPptpStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 10, 2))
altigaPptpStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaPptpStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaPptpStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsPptpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1))
alPptpStatsLocalProtVers = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsLocalProtVers.setStatus('current')
alPptpStatsLocalFraming = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsLocalFraming.setStatus('current')
alPptpStatsLocalBearer = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsLocalBearer.setStatus('current')
alPptpStatsLocalFirmwareRev = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsLocalFirmwareRev.setStatus('current')
alPptpStatsTotalTunnels = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTotalTunnels.setStatus('current')
alPptpStatsActiveTunnels = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsActiveTunnels.setStatus('current')
alPptpStatsMaxTunnels = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsMaxTunnels.setStatus('current')
alPptpStatsTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTotalSessions.setStatus('current')
alPptpStatsActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsActiveSessions.setStatus('current')
alPptpStatsMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsMaxSessions.setStatus('current')
alPptpStatsControlRecvOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsControlRecvOctets.setStatus('current')
alPptpStatsControlRecvPackets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsControlRecvPackets.setStatus('current')
alPptpStatsControlRecvDiscards = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsControlRecvDiscards.setStatus('current')
alPptpStatsControlSendOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsControlSendOctets.setStatus('current')
alPptpStatsControlSendPackets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsControlSendPackets.setStatus('current')
alPptpStatsPayloadRecvOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsPayloadRecvOctets.setStatus('current')
alPptpStatsPayloadRecvPackets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsPayloadRecvPackets.setStatus('current')
alPptpStatsPayloadRecvDiscards = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsPayloadRecvDiscards.setStatus('current')
alPptpStatsPayloadSendOctets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsPayloadSendOctets.setStatus('current')
alPptpStatsPayloadSendPackets = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsPayloadSendPackets.setStatus('current')
alPptpStatsTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2), )
if mibBuilder.loadTexts: alPptpStatsTunnelTable.setStatus('current')
alPptpStatsTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1), ).setIndexNames((0, "ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerIpAddr"))
if mibBuilder.loadTexts: alPptpStatsTunnelEntry.setStatus('current')
alPptpStatsTunnelRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alPptpStatsTunnelRowStatus.setStatus('current')
alPptpStatsTunnelPeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTunnelPeerIpAddr.setStatus('current')
alPptpStatsTunnelDatastreamId = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTunnelDatastreamId.setStatus('current')
alPptpStatsTunnelLocalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTunnelLocalIpAddr.setStatus('current')
alPptpStatsTunnelPeerHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTunnelPeerHostName.setStatus('current')
alPptpStatsTunnelPeerVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTunnelPeerVendorName.setStatus('current')
alPptpStatsTunnelPeerFirmwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTunnelPeerFirmwareRev.setStatus('current')
alPptpStatsTunnelPeerProtVers = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTunnelPeerProtVers.setStatus('current')
alPptpStatsTunnelPeerFramingCap = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTunnelPeerFramingCap.setStatus('current')
alPptpStatsTunnelPeerBearerCap = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTunnelPeerBearerCap.setStatus('current')
alPptpStatsTunnelPeerMaxChan = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTunnelPeerMaxChan.setStatus('current')
alPptpStatsTunnelActiveSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsTunnelActiveSessions.setStatus('current')
alPptpStatsSessionTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3), )
if mibBuilder.loadTexts: alPptpStatsSessionTable.setStatus('current')
alPptpStatsSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1), ).setIndexNames((0, "ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionDatastreamId"))
if mibBuilder.loadTexts: alPptpStatsSessionEntry.setStatus('current')
alPptpStatsSessionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alPptpStatsSessionRowStatus.setStatus('current')
alPptpStatsSessionDatastreamId = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionDatastreamId.setStatus('current')
alPptpStatsSessionLocalCallId = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionLocalCallId.setStatus('current')
alPptpStatsSessionPeerCallId = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionPeerCallId.setStatus('current')
alPptpStatsSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionUserName.setStatus('current')
alPptpStatsSessionSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionSerial.setStatus('current')
alPptpStatsSessionMinimumSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionMinimumSpeed.setStatus('current')
alPptpStatsSessionMaximumSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionMaximumSpeed.setStatus('current')
alPptpStatsSessionConnectSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionConnectSpeed.setStatus('current')
alPptpStatsSessionBearerType = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("analog", 1), ("digital", 2), ("any", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionBearerType.setStatus('current')
alPptpStatsSessionFramingType = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("asynchronous", 1), ("synchronous", 2), ("either", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionFramingType.setStatus('current')
alPptpStatsSessionPhysicalChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionPhysicalChannel.setStatus('current')
alPptpStatsSessionLocalWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionLocalWindowSize.setStatus('current')
alPptpStatsSessionPeerWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionPeerWindowSize.setStatus('current')
alPptpStatsSessionLocalPpd = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionLocalPpd.setStatus('current')
alPptpStatsSessionPeerPpd = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionPeerPpd.setStatus('current')
alPptpStatsSessionRecvOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionRecvOctets.setStatus('current')
alPptpStatsSessionRecvPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionRecvPackets.setStatus('current')
alPptpStatsSessionRecvDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionRecvDiscards.setStatus('current')
alPptpStatsSessionRecvZLB = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionRecvZLB.setStatus('current')
alPptpStatsSessionSendOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionSendOctets.setStatus('current')
alPptpStatsSessionSendPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionSendPackets.setStatus('current')
alPptpStatsSessionSendZLB = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionSendZLB.setStatus('current')
alPptpStatsSessionAckTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionAckTimeouts.setStatus('current')
alPptpStatsSessionLocalFlowOff = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 25), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionLocalFlowOff.setStatus('current')
alPptpStatsSessionPeerFlowOff = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 26), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionPeerFlowOff.setStatus('current')
alPptpStatsSessionOutOfWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionOutOfWindow.setStatus('current')
alPptpStatsSessionOutOfSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionOutOfSequence.setStatus('current')
alPptpStatsSessionTunnelPeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 3, 3, 1, 29), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPptpStatsSessionTunnelPeerIpAddr.setStatus('current')
altigaPptpStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 10, 2, 1))
altigaPptpStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 10, 2, 1, 1))
altigaPptpStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 10, 2, 1, 1, 1)).setObjects(("ALTIGA-PPTP-STATS-MIB", "altigaPptpStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaPptpStatsMibCompliance = altigaPptpStatsMibCompliance.setStatus('current')
altigaPptpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 3, 2)).setObjects(("ALTIGA-PPTP-STATS-MIB", "alPptpStatsLocalProtVers"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsLocalFraming"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsLocalBearer"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsLocalFirmwareRev"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTotalTunnels"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsActiveTunnels"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsMaxTunnels"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTotalSessions"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsActiveSessions"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsMaxSessions"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsControlRecvOctets"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsControlRecvPackets"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsControlRecvDiscards"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsControlSendOctets"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsControlSendPackets"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsPayloadRecvOctets"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsPayloadRecvPackets"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsPayloadRecvDiscards"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsPayloadSendOctets"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsPayloadSendPackets"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelRowStatus"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelDatastreamId"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelLocalIpAddr"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerIpAddr"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerHostName"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerVendorName"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerFirmwareRev"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerProtVers"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerFramingCap"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerBearerCap"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelPeerMaxChan"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsTunnelActiveSessions"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionRowStatus"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionDatastreamId"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionLocalCallId"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionPeerCallId"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionUserName"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionSerial"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionMinimumSpeed"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionMaximumSpeed"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionConnectSpeed"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionBearerType"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionFramingType"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionPhysicalChannel"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionLocalWindowSize"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionPeerWindowSize"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionLocalPpd"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionPeerPpd"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionRecvOctets"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionRecvPackets"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionRecvDiscards"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionRecvZLB"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionSendOctets"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionSendPackets"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionSendZLB"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionAckTimeouts"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionLocalFlowOff"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionPeerFlowOff"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionOutOfWindow"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionOutOfSequence"), ("ALTIGA-PPTP-STATS-MIB", "alPptpStatsSessionTunnelPeerIpAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaPptpStatsGroup = altigaPptpStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-PPTP-STATS-MIB", alPptpStatsSessionLocalWindowSize=alPptpStatsSessionLocalWindowSize, alPptpStatsSessionTable=alPptpStatsSessionTable, alPptpStatsSessionOutOfSequence=alPptpStatsSessionOutOfSequence, alStatsPptpGlobal=alStatsPptpGlobal, alPptpStatsTotalSessions=alPptpStatsTotalSessions, alPptpStatsPayloadSendOctets=alPptpStatsPayloadSendOctets, alPptpStatsSessionPhysicalChannel=alPptpStatsSessionPhysicalChannel, alPptpStatsTunnelDatastreamId=alPptpStatsTunnelDatastreamId, alPptpStatsSessionLocalFlowOff=alPptpStatsSessionLocalFlowOff, altigaPptpStatsMibConformance=altigaPptpStatsMibConformance, alPptpStatsControlSendOctets=alPptpStatsControlSendOctets, PYSNMP_MODULE_ID=altigaPptpStatsMibModule, alPptpStatsSessionFramingType=alPptpStatsSessionFramingType, alPptpStatsSessionPeerWindowSize=alPptpStatsSessionPeerWindowSize, alPptpStatsTunnelActiveSessions=alPptpStatsTunnelActiveSessions, alPptpStatsSessionPeerPpd=alPptpStatsSessionPeerPpd, alPptpStatsSessionRecvZLB=alPptpStatsSessionRecvZLB, alPptpStatsSessionAckTimeouts=alPptpStatsSessionAckTimeouts, alPptpStatsSessionPeerFlowOff=alPptpStatsSessionPeerFlowOff, altigaPptpStatsMibCompliance=altigaPptpStatsMibCompliance, alPptpStatsControlRecvDiscards=alPptpStatsControlRecvDiscards, alPptpStatsTunnelPeerHostName=alPptpStatsTunnelPeerHostName, alPptpStatsSessionSendOctets=alPptpStatsSessionSendOctets, alPptpStatsTunnelEntry=alPptpStatsTunnelEntry, alPptpStatsSessionRowStatus=alPptpStatsSessionRowStatus, alPptpStatsSessionDatastreamId=alPptpStatsSessionDatastreamId, alPptpStatsControlRecvOctets=alPptpStatsControlRecvOctets, alPptpStatsActiveTunnels=alPptpStatsActiveTunnels, alPptpStatsSessionRecvPackets=alPptpStatsSessionRecvPackets, alPptpStatsSessionSerial=alPptpStatsSessionSerial, alPptpStatsSessionConnectSpeed=alPptpStatsSessionConnectSpeed, alPptpStatsLocalBearer=alPptpStatsLocalBearer, alPptpStatsSessionRecvOctets=alPptpStatsSessionRecvOctets, alPptpStatsTunnelLocalIpAddr=alPptpStatsTunnelLocalIpAddr, alPptpStatsMaxSessions=alPptpStatsMaxSessions, alPptpStatsTunnelRowStatus=alPptpStatsTunnelRowStatus, alPptpStatsSessionTunnelPeerIpAddr=alPptpStatsSessionTunnelPeerIpAddr, altigaPptpStatsGroup=altigaPptpStatsGroup, alPptpStatsSessionLocalPpd=alPptpStatsSessionLocalPpd, alPptpStatsSessionLocalCallId=alPptpStatsSessionLocalCallId, alPptpStatsTunnelPeerVendorName=alPptpStatsTunnelPeerVendorName, alPptpStatsPayloadRecvPackets=alPptpStatsPayloadRecvPackets, alPptpStatsSessionUserName=alPptpStatsSessionUserName, alPptpStatsSessionSendPackets=alPptpStatsSessionSendPackets, alPptpStatsTotalTunnels=alPptpStatsTotalTunnels, alPptpStatsActiveSessions=alPptpStatsActiveSessions, alPptpStatsSessionMinimumSpeed=alPptpStatsSessionMinimumSpeed, alPptpStatsSessionRecvDiscards=alPptpStatsSessionRecvDiscards, alPptpStatsSessionSendZLB=alPptpStatsSessionSendZLB, alPptpStatsControlRecvPackets=alPptpStatsControlRecvPackets, alPptpStatsLocalFraming=alPptpStatsLocalFraming, alPptpStatsSessionOutOfWindow=alPptpStatsSessionOutOfWindow, alPptpStatsPayloadRecvOctets=alPptpStatsPayloadRecvOctets, alPptpStatsTunnelPeerFramingCap=alPptpStatsTunnelPeerFramingCap, alPptpStatsTunnelPeerBearerCap=alPptpStatsTunnelPeerBearerCap, altigaPptpStatsMibCompliances=altigaPptpStatsMibCompliances, alPptpStatsSessionBearerType=alPptpStatsSessionBearerType, altigaPptpStatsMibModule=altigaPptpStatsMibModule, alPptpStatsMaxTunnels=alPptpStatsMaxTunnels, alPptpStatsLocalFirmwareRev=alPptpStatsLocalFirmwareRev, alPptpStatsPayloadSendPackets=alPptpStatsPayloadSendPackets, alPptpStatsSessionEntry=alPptpStatsSessionEntry, alPptpStatsTunnelPeerIpAddr=alPptpStatsTunnelPeerIpAddr, alPptpStatsPayloadRecvDiscards=alPptpStatsPayloadRecvDiscards, alPptpStatsControlSendPackets=alPptpStatsControlSendPackets, alPptpStatsTunnelPeerProtVers=alPptpStatsTunnelPeerProtVers, alPptpStatsTunnelTable=alPptpStatsTunnelTable, alPptpStatsTunnelPeerMaxChan=alPptpStatsTunnelPeerMaxChan, alPptpStatsSessionPeerCallId=alPptpStatsSessionPeerCallId, alPptpStatsLocalProtVers=alPptpStatsLocalProtVers, alPptpStatsSessionMaximumSpeed=alPptpStatsSessionMaximumSpeed, alPptpStatsTunnelPeerFirmwareRev=alPptpStatsTunnelPeerFirmwareRev)
