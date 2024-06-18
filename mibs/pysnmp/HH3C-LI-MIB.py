#
# PySNMP MIB module HH3C-LI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetPortNumber, InetAddressPrefixLength, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddressPrefixLength", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, ModuleIdentity, Unsigned32, MibIdentifier, Integer32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, IpAddress, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Integer32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "IpAddress", "TimeTicks", "Bits")
DateAndTime, RowStatus, TextualConvention, DisplayString, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "TextualConvention", "DisplayString", "TruthValue", "MacAddress")
hh3cLI = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 111))
hh3cLI.setRevisions(('2009-08-25 10:00',))
if mibBuilder.loadTexts: hh3cLI.setLastUpdated('200908251000Z')
if mibBuilder.loadTexts: hh3cLI.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cLICommon = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1))
hh3cLITrapBindObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 1))
hh3cLIBoardInformation = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cLIBoardInformation.setStatus('current')
hh3cLINotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 2))
hh3cLINotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 2, 0))
hh3cLIActive = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 2, 0, 1)).setObjects(("HH3C-LI-MIB", "hh3cLIStreamtype"))
if mibBuilder.loadTexts: hh3cLIActive.setStatus('current')
hh3cLITimeOut = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 2, 0, 2)).setObjects(("HH3C-LI-MIB", "hh3cLIMediationRowStatus"))
if mibBuilder.loadTexts: hh3cLITimeOut.setStatus('current')
hh3cLIFailureInformation = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 2, 0, 3)).setObjects(("HH3C-LI-MIB", "hh3cLIStreamtype"), ("HH3C-LI-MIB", "hh3cLIBoardInformation"))
if mibBuilder.loadTexts: hh3cLIFailureInformation.setStatus('current')
hh3cLIObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3))
hh3cLINewIndex = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLINewIndex.setStatus('current')
hh3cLIMediationTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2), )
if mibBuilder.loadTexts: hh3cLIMediationTable.setStatus('current')
hh3cLIMediationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1), ).setIndexNames((0, "HH3C-LI-MIB", "hh3cLIMediationIndex"))
if mibBuilder.loadTexts: hh3cLIMediationEntry.setStatus('current')
hh3cLIMediationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cLIMediationIndex.setStatus('current')
hh3cLIMediationDestAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 2), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMediationDestAddrType.setStatus('current')
hh3cLIMediationDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMediationDestAddr.setStatus('current')
hh3cLIMediationDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 4), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMediationDestPort.setStatus('current')
hh3cLIMediationSrcInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMediationSrcInterface.setStatus('current')
hh3cLIMediationDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 6), Integer32().clone(34)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMediationDscp.setStatus('current')
hh3cLIMediationTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 7), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMediationTimeOut.setStatus('current')
hh3cLIMediationTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("udp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMediationTransport.setStatus('current')
hh3cLIMediationNotificationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 9), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMediationNotificationEnable.setStatus('current')
hh3cLIMediationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 2, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cLIMediationRowStatus.setStatus('current')
hh3cLIStreamTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3), )
if mibBuilder.loadTexts: hh3cLIStreamTable.setStatus('current')
hh3cLIStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1), ).setIndexNames((0, "HH3C-LI-MIB", "hh3cLIMediationIndex"), (0, "HH3C-LI-MIB", "hh3cLIStreamIndex"))
if mibBuilder.loadTexts: hh3cLIStreamEntry.setStatus('current')
hh3cLIStreamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cLIStreamIndex.setStatus('current')
hh3cLIStreamtype = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ip", 1), ("mac", 2), ("userConnection", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIStreamtype.setStatus('current')
hh3cLIStreamEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIStreamEnable.setStatus('current')
hh3cLIStreamPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLIStreamPackets.setStatus('current')
hh3cLIStreamDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLIStreamDrops.setStatus('current')
hh3cLIStreamHPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLIStreamHPackets.setStatus('current')
hh3cLIStreamHDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLIStreamHDrops.setStatus('current')
hh3cLIStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 1, 3, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cLIStreamRowStatus.setStatus('current')
hh3cLIIPStream = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2))
hh3cLIIPStreamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1))
hh3cLIIPStreamTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1), )
if mibBuilder.loadTexts: hh3cLIIPStreamTable.setStatus('current')
hh3cLIIPStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1), ).setIndexNames((0, "HH3C-LI-MIB", "hh3cLIMediationIndex"), (0, "HH3C-LI-MIB", "hh3cLIStreamIndex"))
if mibBuilder.loadTexts: hh3cLIIPStreamEntry.setStatus('current')
hh3cLIIPStreamInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamInterface.setStatus('current')
hh3cLIIPStreamAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamAddrType.setStatus('current')
hh3cLIIPStreamDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 3), InetAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamDestAddr.setStatus('current')
hh3cLIIPStreamDestAddrLength = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 4), InetAddressPrefixLength()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamDestAddrLength.setStatus('current')
hh3cLIIPStreamSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 5), InetAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamSrcAddr.setStatus('current')
hh3cLIIPStreamSrcAddrLength = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 6), InetAddressPrefixLength()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamSrcAddrLength.setStatus('current')
hh3cLIIPStreamTosByte = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamTosByte.setStatus('current')
hh3cLIIPStreamTosByteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamTosByteMask.setStatus('current')
hh3cLIIPStreamFlowId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1048575), )).clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamFlowId.setStatus('current')
hh3cLIIPStreamProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )).clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamProtocol.setStatus('current')
hh3cLIIPStreamDestL4PortMin = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 11), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamDestL4PortMin.setStatus('current')
hh3cLIIPStreamDestL4PortMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 12), InetPortNumber().clone(65535)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamDestL4PortMax.setStatus('current')
hh3cLIIPStreamSrcL4PortMin = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 13), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamSrcL4PortMin.setStatus('current')
hh3cLIIPStreamSrcL4PortMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 14), InetPortNumber().clone(65535)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamSrcL4PortMax.setStatus('current')
hh3cLIIPStreamVRF = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 15), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIIPStreamVRF.setStatus('current')
hh3cLIIPStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 2, 1, 1, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cLIIPStreamRowStatus.setStatus('current')
hh3cLIMACStream = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 111, 3))
hh3cLIMACStreamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1))
hh3cLIMACStreamTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1), )
if mibBuilder.loadTexts: hh3cLIMACStreamTable.setStatus('current')
hh3cLIMACStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1), ).setIndexNames((0, "HH3C-LI-MIB", "hh3cLIMediationIndex"), (0, "HH3C-LI-MIB", "hh3cLIStreamIndex"))
if mibBuilder.loadTexts: hh3cLIMACStreamEntry.setStatus('current')
hh3cLIMACStreamFields = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("interface", 0), ("dstMacAddress", 1), ("srcMacAddress", 2), ("ethernetPid", 3), ("dSap", 4), ("sSap", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMACStreamFields.setStatus('current')
hh3cLIMACStreamInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMACStreamInterface.setStatus('current')
hh3cLIMACStreamDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMACStreamDestAddr.setStatus('current')
hh3cLIMACStreamSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 4), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMACStreamSrcAddr.setStatus('current')
hh3cLIMACStreamEthPid = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMACStreamEthPid.setStatus('current')
hh3cLIMACStreamDSap = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMACStreamDSap.setStatus('current')
hh3cLIMACStreamSSap = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIMACStreamSSap.setStatus('current')
hh3cLIMACStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 3, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cLIMACStreamRowStatus.setStatus('current')
hh3cLIUserStream = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 111, 4))
hh3cLIUserStreamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 111, 4, 1))
hh3cLIUserStreamTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 111, 4, 1, 1), )
if mibBuilder.loadTexts: hh3cLIUserStreamTable.setStatus('current')
hh3cLIUserStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 111, 4, 1, 1, 1), ).setIndexNames((0, "HH3C-LI-MIB", "hh3cLIMediationIndex"), (0, "HH3C-LI-MIB", "hh3cLIStreamIndex"))
if mibBuilder.loadTexts: hh3cLIUserStreamEntry.setStatus('current')
hh3cLIUserStreamAcctSessID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 4, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLIUserStreamAcctSessID.setStatus('current')
hh3cLIUserStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 111, 4, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cLIUserStreamRowStatus.setStatus('current')
mibBuilder.exportSymbols("HH3C-LI-MIB", hh3cLIUserStreamEntry=hh3cLIUserStreamEntry, hh3cLICommon=hh3cLICommon, hh3cLIIPStream=hh3cLIIPStream, hh3cLIActive=hh3cLIActive, hh3cLIIPStreamSrcAddr=hh3cLIIPStreamSrcAddr, hh3cLI=hh3cLI, hh3cLIIPStreamInterface=hh3cLIIPStreamInterface, hh3cLIMACStreamRowStatus=hh3cLIMACStreamRowStatus, hh3cLIMediationSrcInterface=hh3cLIMediationSrcInterface, hh3cLIStreamDrops=hh3cLIStreamDrops, hh3cLIMACStreamEthPid=hh3cLIMACStreamEthPid, hh3cLIMACStreamDSap=hh3cLIMACStreamDSap, hh3cLIMediationDestAddrType=hh3cLIMediationDestAddrType, hh3cLIMediationTable=hh3cLIMediationTable, hh3cLITrapBindObjects=hh3cLITrapBindObjects, hh3cLIIPStreamDestAddr=hh3cLIIPStreamDestAddr, hh3cLIUserStream=hh3cLIUserStream, hh3cLIStreamHPackets=hh3cLIStreamHPackets, hh3cLIMACStreamEntry=hh3cLIMACStreamEntry, hh3cLIUserStreamAcctSessID=hh3cLIUserStreamAcctSessID, hh3cLIMACStream=hh3cLIMACStream, hh3cLINotificationsPrefix=hh3cLINotificationsPrefix, hh3cLIObjects=hh3cLIObjects, hh3cLIUserStreamRowStatus=hh3cLIUserStreamRowStatus, hh3cLIMediationTransport=hh3cLIMediationTransport, hh3cLIIPStreamProtocol=hh3cLIIPStreamProtocol, hh3cLIMediationDscp=hh3cLIMediationDscp, hh3cLIStreamtype=hh3cLIStreamtype, hh3cLIFailureInformation=hh3cLIFailureInformation, hh3cLIIPStreamEntry=hh3cLIIPStreamEntry, hh3cLIIPStreamTosByteMask=hh3cLIIPStreamTosByteMask, hh3cLIUserStreamObjects=hh3cLIUserStreamObjects, hh3cLITimeOut=hh3cLITimeOut, hh3cLIIPStreamTosByte=hh3cLIIPStreamTosByte, hh3cLIUserStreamTable=hh3cLIUserStreamTable, hh3cLIIPStreamRowStatus=hh3cLIIPStreamRowStatus, hh3cLIIPStreamDestL4PortMin=hh3cLIIPStreamDestL4PortMin, hh3cLIMediationTimeOut=hh3cLIMediationTimeOut, hh3cLIMediationDestPort=hh3cLIMediationDestPort, hh3cLIIPStreamObjects=hh3cLIIPStreamObjects, hh3cLIStreamEntry=hh3cLIStreamEntry, hh3cLINewIndex=hh3cLINewIndex, hh3cLIBoardInformation=hh3cLIBoardInformation, hh3cLIIPStreamAddrType=hh3cLIIPStreamAddrType, hh3cLIIPStreamVRF=hh3cLIIPStreamVRF, hh3cLIMACStreamFields=hh3cLIMACStreamFields, hh3cLIMACStreamInterface=hh3cLIMACStreamInterface, hh3cLIIPStreamSrcAddrLength=hh3cLIIPStreamSrcAddrLength, hh3cLIMACStreamSSap=hh3cLIMACStreamSSap, hh3cLIStreamRowStatus=hh3cLIStreamRowStatus, hh3cLIMACStreamSrcAddr=hh3cLIMACStreamSrcAddr, hh3cLIIPStreamDestL4PortMax=hh3cLIIPStreamDestL4PortMax, hh3cLINotifications=hh3cLINotifications, hh3cLIMediationIndex=hh3cLIMediationIndex, hh3cLIMediationNotificationEnable=hh3cLIMediationNotificationEnable, hh3cLIIPStreamDestAddrLength=hh3cLIIPStreamDestAddrLength, hh3cLIStreamIndex=hh3cLIStreamIndex, hh3cLIMACStreamDestAddr=hh3cLIMACStreamDestAddr, hh3cLIStreamPackets=hh3cLIStreamPackets, hh3cLIMediationDestAddr=hh3cLIMediationDestAddr, hh3cLIIPStreamTable=hh3cLIIPStreamTable, hh3cLIMACStreamObjects=hh3cLIMACStreamObjects, hh3cLIIPStreamSrcL4PortMin=hh3cLIIPStreamSrcL4PortMin, hh3cLIMediationRowStatus=hh3cLIMediationRowStatus, hh3cLIStreamTable=hh3cLIStreamTable, hh3cLIIPStreamSrcL4PortMax=hh3cLIIPStreamSrcL4PortMax, hh3cLIStreamEnable=hh3cLIStreamEnable, hh3cLIMediationEntry=hh3cLIMediationEntry, hh3cLIIPStreamFlowId=hh3cLIIPStreamFlowId, hh3cLIMACStreamTable=hh3cLIMACStreamTable, PYSNMP_MODULE_ID=hh3cLI, hh3cLIStreamHDrops=hh3cLIStreamHDrops)
