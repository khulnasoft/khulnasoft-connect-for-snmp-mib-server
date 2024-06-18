#
# PySNMP MIB module A3COM-HUAWEI-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-RADIUS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:52:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
radiusAccClientServerPortNumber, radiusAccServerIndex, radiusAccServerAddress = mibBuilder.importSymbols("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber", "radiusAccServerIndex", "radiusAccServerAddress")
radiusAuthClientServerPortNumber, radiusAuthServerIndex, radiusAuthServerAddress = mibBuilder.importSymbols("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber", "radiusAuthServerIndex", "radiusAuthServerAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, Integer32, Bits, ModuleIdentity, Counter64, iso, TimeTicks, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "Integer32", "Bits", "ModuleIdentity", "Counter64", "iso", "TimeTicks", "ObjectIdentity", "Counter32")
TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
h3cRadius = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13))
if mibBuilder.loadTexts: h3cRadius.setLastUpdated('201008260000Z')
if mibBuilder.loadTexts: h3cRadius.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class DisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

h3cRdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1))
h3cRdInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1), )
if mibBuilder.loadTexts: h3cRdInfoTable.setStatus('current')
h3cRdInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdGroupName"))
if mibBuilder.loadTexts: h3cRdInfoEntry.setStatus('current')
h3cRdGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: h3cRdGroupName.setStatus('current')
h3cRdPrimAuthIp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdPrimAuthIp.setStatus('deprecated')
h3cRdPrimUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdPrimUdpPort.setStatus('current')
h3cRdPrimState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("block", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdPrimState.setStatus('current')
h3cRdSecAuthIp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecAuthIp.setStatus('deprecated')
h3cRdSecUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecUdpPort.setStatus('current')
h3cRdSecState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("block", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecState.setStatus('current')
h3cRdKey = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdKey.setStatus('current')
h3cRdRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdRetry.setStatus('current')
h3cRdTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdTimeout.setStatus('current')
h3cRdPrimAuthIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 11), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdPrimAuthIpAddrType.setStatus('current')
h3cRdPrimAuthIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 12), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdPrimAuthIpAddr.setStatus('current')
h3cRdSecAuthIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 13), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecAuthIpAddrType.setStatus('current')
h3cRdSecAuthIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 14), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecAuthIpAddr.setStatus('current')
h3cRdServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("standard", 1), ("iphotel", 2), ("portal", 3), ("extended", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdServerType.setStatus('current')
h3cRdQuietTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdQuietTime.setStatus('current')
h3cRdUserNameFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("withoutdomain", 1), ("withdomain", 2), ("keeporignal", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdUserNameFormat.setStatus('current')
h3cRdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdRowStatus.setStatus('current')
h3cRdSecKey = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecKey.setStatus('current')
h3cRdPrimVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdPrimVpnName.setStatus('current')
h3cRdSecVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecVpnName.setStatus('current')
h3cRdAuthNasIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 22), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAuthNasIpAddrType.setStatus('current')
h3cRdAuthNasIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 1, 1, 23), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAuthNasIpAddr.setStatus('current')
h3cRdAccInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2), )
if mibBuilder.loadTexts: h3cRdAccInfoTable.setStatus('current')
h3cRdAccInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdAccGroupName"))
if mibBuilder.loadTexts: h3cRdAccInfoEntry.setStatus('current')
h3cRdAccGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: h3cRdAccGroupName.setStatus('current')
h3cRdPrimAccIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdPrimAccIpAddrType.setStatus('current')
h3cRdPrimAccIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdPrimAccIpAddr.setStatus('current')
h3cRdPrimAccUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdPrimAccUdpPort.setStatus('current')
h3cRdPrimAccState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("block", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdPrimAccState.setStatus('current')
h3cRdSecAccIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 6), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecAccIpAddrType.setStatus('current')
h3cRdSecAccIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecAccIpAddr.setStatus('current')
h3cRdSecAccUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecAccUdpPort.setStatus('current')
h3cRdSecAccState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("block", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecAccState.setStatus('current')
h3cRdAccKey = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccKey.setStatus('current')
h3cRdAccRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccRetry.setStatus('current')
h3cRdAccTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccTimeout.setStatus('current')
h3cRdAccServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("standard", 1), ("iphotel", 2), ("portal", 3), ("extended", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccServerType.setStatus('current')
h3cRdAccQuietTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccQuietTime.setStatus('current')
h3cRdAccFailureAction = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ignore", 1), ("reject", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccFailureAction.setStatus('current')
h3cRdAccRealTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccRealTime.setStatus('current')
h3cRdAccRealTimeRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccRealTimeRetry.setStatus('current')
h3cRdAccSaveStopPktEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 18), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccSaveStopPktEnable.setStatus('current')
h3cRdAccStopRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccStopRetry.setStatus('current')
h3cRdAccDataFlowUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("byte", 1), ("kiloByte", 2), ("megaByte", 3), ("gigaByte", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccDataFlowUnit.setStatus('current')
h3cRdAccPacketUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("onePacket", 1), ("kiloPacket", 2), ("megaPacket", 3), ("gigaPacket", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccPacketUnit.setStatus('current')
h3cRdAccRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 22), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccRowStatus.setStatus('current')
h3cRdAcctOnEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 23), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAcctOnEnable.setStatus('current')
h3cRdAcctOnSendTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 24), Integer32().clone(15)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAcctOnSendTimes.setStatus('current')
h3cRdAcctOnSendInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 25), Integer32().clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAcctOnSendInterval.setStatus('current')
h3cRdSecAccKey = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecAccKey.setStatus('current')
h3cRdPrimAccVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdPrimAccVpnName.setStatus('current')
h3cRdSecAccVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecAccVpnName.setStatus('current')
h3cRdAccNasIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 29), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccNasIpAddrType.setStatus('current')
h3cRdAccNasIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 2, 1, 30), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdAccNasIpAddr.setStatus('current')
h3cRadiusGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 3))
h3cRadiusAuthErrThreshold = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 3, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(30)).setUnits('percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cRadiusAuthErrThreshold.setStatus('current')
h3cRdSecondaryAuthServerTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4), )
if mibBuilder.loadTexts: h3cRdSecondaryAuthServerTable.setStatus('current')
h3cRdSecondaryAuthServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdGroupName"), (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAuthIpAddrType"), (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAuthIpAddr"), (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAuthVpnName"), (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAuthUdpPort"))
if mibBuilder.loadTexts: h3cRdSecondaryAuthServerEntry.setStatus('current')
h3cRdSecondaryAuthIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 1), InetAddressType())
if mibBuilder.loadTexts: h3cRdSecondaryAuthIpAddrType.setStatus('current')
h3cRdSecondaryAuthIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 2), InetAddress())
if mibBuilder.loadTexts: h3cRdSecondaryAuthIpAddr.setStatus('current')
h3cRdSecondaryAuthVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: h3cRdSecondaryAuthVpnName.setStatus('current')
h3cRdSecondaryAuthUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cRdSecondaryAuthUdpPort.setStatus('current')
h3cRdSecondaryAuthState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("block", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecondaryAuthState.setStatus('current')
h3cRdSecondaryAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecondaryAuthKey.setStatus('current')
h3cRdSecondaryAuthRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 4, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecondaryAuthRowStatus.setStatus('current')
h3cRdSecondaryAccServerTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5), )
if mibBuilder.loadTexts: h3cRdSecondaryAccServerTable.setStatus('current')
h3cRdSecondaryAccServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1), ).setIndexNames((0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdAccGroupName"), (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAccIpAddrType"), (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAccIpAddr"), (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAccVpnName"), (0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRdSecondaryAccUdpPort"))
if mibBuilder.loadTexts: h3cRdSecondaryAccServerEntry.setStatus('current')
h3cRdSecondaryAccIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 1), InetAddressType())
if mibBuilder.loadTexts: h3cRdSecondaryAccIpAddrType.setStatus('current')
h3cRdSecondaryAccIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 2), InetAddress())
if mibBuilder.loadTexts: h3cRdSecondaryAccIpAddr.setStatus('current')
h3cRdSecondaryAccVpnName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: h3cRdSecondaryAccVpnName.setStatus('current')
h3cRdSecondaryAccUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cRdSecondaryAccUdpPort.setStatus('current')
h3cRdSecondaryAccState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("block", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecondaryAccState.setStatus('current')
h3cRdSecondaryAccKey = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecondaryAccKey.setStatus('current')
h3cRdSecondaryAccRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 1, 5, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRdSecondaryAccRowStatus.setStatus('current')
h3cRadiusAccounting = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2))
h3cRadiusAccClient = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1))
h3cRadiusAccServerTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1), )
if mibBuilder.loadTexts: h3cRadiusAccServerTable.setStatus('current')
h3cRadiusAccServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1), ).setIndexNames((0, "RADIUS-ACC-CLIENT-MIB", "radiusAccServerIndex"))
if mibBuilder.loadTexts: h3cRadiusAccServerEntry.setStatus('current')
h3cRadiusAccClientStartRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusAccClientStartRequests.setStatus('current')
h3cRadiusAccClientStartResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusAccClientStartResponses.setStatus('current')
h3cRadiusAccClientInterimRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusAccClientInterimRequests.setStatus('current')
h3cRadiusAccClientInterimResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusAccClientInterimResponses.setStatus('current')
h3cRadiusAccClientStopRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusAccClientStopRequests.setStatus('current')
h3cRadiusAccClientStopResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusAccClientStopResponses.setStatus('current')
h3cRadiusServerTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3))
h3cRadiusAuthServerDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3, 1)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"), ("A3COM-HUAWEI-RADIUS-MIB", "h3cRadiusServerFirstTrapTime"))
if mibBuilder.loadTexts: h3cRadiusAuthServerDownTrap.setStatus('current')
h3cRadiusAccServerDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3, 2)).setObjects(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"), ("A3COM-HUAWEI-RADIUS-MIB", "h3cRadiusServerFirstTrapTime"))
if mibBuilder.loadTexts: h3cRadiusAccServerDownTrap.setStatus('current')
h3cRadiusServerTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3, 0))
h3cRadiusAuthServerUpTrap = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3, 0, 1)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"), ("A3COM-HUAWEI-RADIUS-MIB", "h3cRadiusServerFirstTrapTime"))
if mibBuilder.loadTexts: h3cRadiusAuthServerUpTrap.setStatus('current')
h3cRadiusAccServerUpTrap = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3, 0, 2)).setObjects(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"), ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"), ("A3COM-HUAWEI-RADIUS-MIB", "h3cRadiusServerFirstTrapTime"))
if mibBuilder.loadTexts: h3cRadiusAccServerUpTrap.setStatus('current')
h3cRadiusAuthErrTrap = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 3, 0, 3)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"))
if mibBuilder.loadTexts: h3cRadiusAuthErrTrap.setStatus('current')
h3cRadiusAuthenticating = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4))
h3cRadiusAuthClient = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4, 1))
h3cRadiusAuthServerTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4, 1, 1), )
if mibBuilder.loadTexts: h3cRadiusAuthServerTable.setStatus('current')
h3cRadiusAuthServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4, 1, 1, 1), ).setIndexNames((0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerIndex"))
if mibBuilder.loadTexts: h3cRadiusAuthServerEntry.setStatus('current')
h3cRadiusAuthFailureTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusAuthFailureTimes.setStatus('current')
h3cRadiusAuthTimeoutTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusAuthTimeoutTimes.setStatus('current')
h3cRadiusAuthRejectTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 4, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusAuthRejectTimes.setStatus('current')
h3cRadiusExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5))
h3cRadiusExtendObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 1))
h3cRadiusExtendTables = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2))
h3cRadiusExtendTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 3))
h3cRadiusSchAuthTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1), )
if mibBuilder.loadTexts: h3cRadiusSchAuthTable.setStatus('current')
h3cRadiusSchAuthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRadiusSchAuthGroupName"))
if mibBuilder.loadTexts: h3cRadiusSchAuthEntry.setStatus('current')
h3cRadiusSchAuthGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: h3cRadiusSchAuthGroupName.setStatus('current')
h3cRadiusSchAuthPrimIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAuthPrimIpAddr.setStatus('current')
h3cRadiusSchAuthPrimUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 3), Integer32().clone(1812)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAuthPrimUdpPort.setStatus('current')
h3cRadiusSchAuthPrimKey = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAuthPrimKey.setStatus('current')
h3cRadiusSchAuthSecIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAuthSecIpAddr.setStatus('current')
h3cRadiusSchAuthSecUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 6), Integer32().clone(1812)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAuthSecUdpPort.setStatus('current')
h3cRadiusSchAuthSecKey = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAuthSecKey.setStatus('current')
h3cRadiusSchAuthRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAuthRowStatus.setStatus('current')
h3cRadiusSchAccTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2), )
if mibBuilder.loadTexts: h3cRadiusSchAccTable.setStatus('current')
h3cRadiusSchAccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-RADIUS-MIB", "h3cRadiusSchAccGroupName"))
if mibBuilder.loadTexts: h3cRadiusSchAccEntry.setStatus('current')
h3cRadiusSchAccGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 1), DisplayString())
if mibBuilder.loadTexts: h3cRadiusSchAccGroupName.setStatus('current')
h3cRadiusSchAccPrimIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAccPrimIpAddr.setStatus('current')
h3cRadiusSchAccPrimUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 3), Integer32().clone(1812)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAccPrimUdpPort.setStatus('current')
h3cRadiusSchAccPrimKey = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAccPrimKey.setStatus('current')
h3cRadiusSchAccSecIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAccSecIpAddr.setStatus('current')
h3cRadiusSchAccSecUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 6), Integer32().clone(1812)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAccSecUdpPort.setStatus('current')
h3cRadiusSchAccSecKey = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAccSecKey.setStatus('current')
h3cRadiusSchAccRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 5, 2, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRadiusSchAccRowStatus.setStatus('current')
h3cRadiusStatistic = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 6))
h3cRadiusStatAccReq = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 6, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusStatAccReq.setStatus('current')
h3cRadiusStatAccAck = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 6, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusStatAccAck.setStatus('current')
h3cRadiusStatLogoutReq = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 6, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusStatLogoutReq.setStatus('current')
h3cRadiusStatLogoutAck = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 6, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRadiusStatLogoutAck.setStatus('current')
h3cRadiusServerTrapVarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 7))
h3cRadiusServerFirstTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 13, 7, 1), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cRadiusServerFirstTrapTime.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-RADIUS-MIB", h3cRdAccRowStatus=h3cRdAccRowStatus, h3cRadiusSchAuthRowStatus=h3cRadiusSchAuthRowStatus, h3cRadiusStatLogoutAck=h3cRadiusStatLogoutAck, h3cRdObjects=h3cRdObjects, h3cRdSecAuthIpAddrType=h3cRdSecAuthIpAddrType, h3cRdSecAccVpnName=h3cRdSecAccVpnName, h3cRadiusAccServerDownTrap=h3cRadiusAccServerDownTrap, h3cRdSecondaryAccIpAddr=h3cRdSecondaryAccIpAddr, h3cRadiusAuthErrTrap=h3cRadiusAuthErrTrap, h3cRadiusAuthClient=h3cRadiusAuthClient, h3cRadiusAccClientInterimRequests=h3cRadiusAccClientInterimRequests, h3cRdRetry=h3cRdRetry, h3cRdSecondaryAuthServerEntry=h3cRdSecondaryAuthServerEntry, h3cRadiusSchAuthPrimUdpPort=h3cRadiusSchAuthPrimUdpPort, h3cRadiusAccClientStopResponses=h3cRadiusAccClientStopResponses, h3cRdSecondaryAuthIpAddrType=h3cRdSecondaryAuthIpAddrType, h3cRdAccRetry=h3cRdAccRetry, h3cRdAccKey=h3cRdAccKey, h3cRdPrimAuthIpAddrType=h3cRdPrimAuthIpAddrType, h3cRdSecAccUdpPort=h3cRdSecAccUdpPort, h3cRdSecondaryAuthServerTable=h3cRdSecondaryAuthServerTable, h3cRadiusAccClientStartRequests=h3cRadiusAccClientStartRequests, h3cRadiusSchAccEntry=h3cRadiusSchAccEntry, h3cRdPrimAccState=h3cRdPrimAccState, h3cRdAccServerType=h3cRdAccServerType, h3cRdSecAccIpAddrType=h3cRdSecAccIpAddrType, h3cRdPrimUdpPort=h3cRdPrimUdpPort, h3cRdPrimState=h3cRdPrimState, h3cRdSecondaryAccUdpPort=h3cRdSecondaryAccUdpPort, h3cRadiusAccServerEntry=h3cRadiusAccServerEntry, h3cRdAuthNasIpAddr=h3cRdAuthNasIpAddr, h3cRadiusSchAccSecUdpPort=h3cRadiusSchAccSecUdpPort, DisplayString=DisplayString, h3cRdPrimAccVpnName=h3cRdPrimAccVpnName, h3cRdSecondaryAuthVpnName=h3cRdSecondaryAuthVpnName, h3cRadiusSchAuthSecIpAddr=h3cRadiusSchAuthSecIpAddr, h3cRdAcctOnEnable=h3cRdAcctOnEnable, h3cRdSecondaryAccState=h3cRdSecondaryAccState, h3cRdGroupName=h3cRdGroupName, h3cRdAccNasIpAddr=h3cRdAccNasIpAddr, h3cRadiusServerTrapPrefix=h3cRadiusServerTrapPrefix, h3cRdPrimVpnName=h3cRdPrimVpnName, h3cRdSecondaryAuthState=h3cRdSecondaryAuthState, h3cRadiusServerTrap=h3cRadiusServerTrap, h3cRadiusSchAccTable=h3cRadiusSchAccTable, h3cRadiusAuthServerTable=h3cRadiusAuthServerTable, h3cRadiusAuthServerDownTrap=h3cRadiusAuthServerDownTrap, h3cRdSecondaryAccKey=h3cRdSecondaryAccKey, h3cRdAccStopRetry=h3cRdAccStopRetry, h3cRdPrimAccIpAddrType=h3cRdPrimAccIpAddrType, h3cRadiusSchAccPrimUdpPort=h3cRadiusSchAccPrimUdpPort, h3cRdSecondaryAuthKey=h3cRdSecondaryAuthKey, h3cRadiusExtendTables=h3cRadiusExtendTables, h3cRadiusExtendObjects=h3cRadiusExtendObjects, h3cRdAccSaveStopPktEnable=h3cRdAccSaveStopPktEnable, h3cRadiusAccounting=h3cRadiusAccounting, h3cRadiusServerTrapVarObjects=h3cRadiusServerTrapVarObjects, h3cRdSecAccState=h3cRdSecAccState, h3cRadiusAccClientInterimResponses=h3cRadiusAccClientInterimResponses, h3cRdSecVpnName=h3cRdSecVpnName, h3cRadiusAuthServerEntry=h3cRadiusAuthServerEntry, h3cRdSecAccKey=h3cRdSecAccKey, h3cRadiusSchAccSecKey=h3cRadiusSchAccSecKey, h3cRadiusGlobalConfig=h3cRadiusGlobalConfig, h3cRadiusSchAuthSecKey=h3cRadiusSchAuthSecKey, h3cRdPrimAccIpAddr=h3cRdPrimAccIpAddr, PYSNMP_MODULE_ID=h3cRadius, h3cRdRowStatus=h3cRdRowStatus, h3cRdPrimAccUdpPort=h3cRdPrimAccUdpPort, h3cRadiusSchAuthSecUdpPort=h3cRadiusSchAuthSecUdpPort, h3cRdSecondaryAccVpnName=h3cRdSecondaryAccVpnName, h3cRdSecondaryAuthRowStatus=h3cRdSecondaryAuthRowStatus, h3cRdSecondaryAccRowStatus=h3cRdSecondaryAccRowStatus, h3cRadiusSchAccPrimIpAddr=h3cRadiusSchAccPrimIpAddr, h3cRdAcctOnSendInterval=h3cRdAcctOnSendInterval, h3cRdQuietTime=h3cRdQuietTime, h3cRdSecondaryAccServerTable=h3cRdSecondaryAccServerTable, h3cRadiusAccServerTable=h3cRadiusAccServerTable, h3cRdAccInfoEntry=h3cRdAccInfoEntry, h3cRdSecondaryAuthIpAddr=h3cRdSecondaryAuthIpAddr, h3cRdSecondaryAccServerEntry=h3cRdSecondaryAccServerEntry, h3cRadiusSchAccSecIpAddr=h3cRadiusSchAccSecIpAddr, h3cRadiusSchAuthTable=h3cRadiusSchAuthTable, h3cRdInfoTable=h3cRdInfoTable, h3cRadiusStatAccAck=h3cRadiusStatAccAck, h3cRadiusAccClientStartResponses=h3cRadiusAccClientStartResponses, h3cRdSecState=h3cRdSecState, h3cRadiusExtend=h3cRadiusExtend, h3cRadiusSchAuthEntry=h3cRadiusSchAuthEntry, h3cRdPrimAuthIp=h3cRdPrimAuthIp, h3cRdTimeout=h3cRdTimeout, h3cRadiusAccClient=h3cRadiusAccClient, h3cRdSecUdpPort=h3cRdSecUdpPort, h3cRdAccTimeout=h3cRdAccTimeout, h3cRadiusStatLogoutReq=h3cRadiusStatLogoutReq, h3cRdServerType=h3cRdServerType, h3cRdKey=h3cRdKey, h3cRdAccFailureAction=h3cRdAccFailureAction, h3cRadiusAuthErrThreshold=h3cRadiusAuthErrThreshold, h3cRadiusServerFirstTrapTime=h3cRadiusServerFirstTrapTime, h3cRdPrimAuthIpAddr=h3cRdPrimAuthIpAddr, h3cRdAuthNasIpAddrType=h3cRdAuthNasIpAddrType, h3cRadiusAccServerUpTrap=h3cRadiusAccServerUpTrap, h3cRadiusSchAuthGroupName=h3cRadiusSchAuthGroupName, h3cRdSecondaryAuthUdpPort=h3cRdSecondaryAuthUdpPort, h3cRadiusSchAccRowStatus=h3cRadiusSchAccRowStatus, h3cRadiusSchAccPrimKey=h3cRadiusSchAccPrimKey, h3cRadius=h3cRadius, h3cRdAccRealTime=h3cRdAccRealTime, h3cRadiusSchAccGroupName=h3cRadiusSchAccGroupName, h3cRadiusAuthServerUpTrap=h3cRadiusAuthServerUpTrap, h3cRdAccRealTimeRetry=h3cRdAccRealTimeRetry, h3cRadiusSchAuthPrimIpAddr=h3cRadiusSchAuthPrimIpAddr, h3cRdAccDataFlowUnit=h3cRdAccDataFlowUnit, h3cRdSecAuthIpAddr=h3cRdSecAuthIpAddr, h3cRdAccGroupName=h3cRdAccGroupName, h3cRdSecondaryAccIpAddrType=h3cRdSecondaryAccIpAddrType, h3cRadiusStatistic=h3cRadiusStatistic, h3cRdAccQuietTime=h3cRdAccQuietTime, h3cRadiusSchAuthPrimKey=h3cRadiusSchAuthPrimKey, h3cRdSecAuthIp=h3cRdSecAuthIp, h3cRadiusAuthenticating=h3cRadiusAuthenticating, h3cRdAccInfoTable=h3cRdAccInfoTable, h3cRadiusAuthTimeoutTimes=h3cRadiusAuthTimeoutTimes, h3cRdSecKey=h3cRdSecKey, h3cRdAccNasIpAddrType=h3cRdAccNasIpAddrType, h3cRadiusExtendTraps=h3cRadiusExtendTraps, h3cRdSecAccIpAddr=h3cRdSecAccIpAddr, h3cRadiusAccClientStopRequests=h3cRadiusAccClientStopRequests, h3cRdAcctOnSendTimes=h3cRdAcctOnSendTimes, h3cRdAccPacketUnit=h3cRdAccPacketUnit, h3cRdInfoEntry=h3cRdInfoEntry, h3cRdUserNameFormat=h3cRdUserNameFormat, h3cRadiusAuthRejectTimes=h3cRadiusAuthRejectTimes, h3cRadiusStatAccReq=h3cRadiusStatAccReq, h3cRadiusAuthFailureTimes=h3cRadiusAuthFailureTimes)
