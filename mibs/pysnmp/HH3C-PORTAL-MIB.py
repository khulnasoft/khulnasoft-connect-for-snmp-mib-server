#
# PySNMP MIB module HH3C-PORTAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-PORTAL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
InetAddressType, InetAddressPrefixLength, InetAddress, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddressPrefixLength", "InetAddress", "InetAddressIPv4")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, iso, NotificationType, Counter32, Gauge32, Bits, Integer32, ObjectIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "NotificationType", "Counter32", "Gauge32", "Bits", "Integer32", "ObjectIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "IpAddress")
TextualConvention, DisplayString, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress", "RowStatus")
hh3cPortal = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 99))
if mibBuilder.loadTexts: hh3cPortal.setLastUpdated('201111080000Z')
if mibBuilder.loadTexts: hh3cPortal.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cPortalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 99, 1))
hh3cPortalMaxUserNumber = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPortalMaxUserNumber.setStatus('current')
hh3cPortalCurrentUserNumber = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalCurrentUserNumber.setStatus('current')
hh3cPortalStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatus.setStatus('current')
hh3cPortalUserNumberUpperLimit = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalUserNumberUpperLimit.setStatus('current')
hh3cPortalNasId = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPortalNasId.setStatus('current')
hh3cPortalTables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2))
hh3cPortalServerTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 1), )
if mibBuilder.loadTexts: hh3cPortalServerTable.setStatus('current')
hh3cPortalServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 1, 1), ).setIndexNames((0, "HH3C-PORTAL-MIB", "hh3cPortalServerName"))
if mibBuilder.loadTexts: hh3cPortalServerEntry.setStatus('current')
hh3cPortalServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cPortalServerName.setStatus('current')
hh3cPortalServerUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPortalServerUrl.setStatus('current')
hh3cPortalServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPortalServerPort.setStatus('current')
hh3cPortalIfInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 2), )
if mibBuilder.loadTexts: hh3cPortalIfInfoTable.setStatus('current')
hh3cPortalIfInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cPortalIfInfoEntry.setStatus('current')
hh3cPortalAuthReqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalAuthReqNumber.setStatus('current')
hh3cPortalAuthSuccNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalAuthSuccNumber.setStatus('current')
hh3cPortalAuthFailNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalAuthFailNumber.setStatus('current')
hh3cPortalIfServerTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 3), )
if mibBuilder.loadTexts: hh3cPortalIfServerTable.setStatus('current')
hh3cPortalIfServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 3, 1), ).setIndexNames((0, "HH3C-PORTAL-MIB", "hh3cPortalIfServerIndex"))
if mibBuilder.loadTexts: hh3cPortalIfServerEntry.setStatus('current')
hh3cPortalIfServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hh3cPortalIfServerIndex.setStatus('current')
hh3cPortalIfServerUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 3, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalIfServerUrl.setStatus('current')
hh3cPortalIfServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalIfServerRowStatus.setStatus('current')
hh3cPortalIfVlanNasIDTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 4), )
if mibBuilder.loadTexts: hh3cPortalIfVlanNasIDTable.setStatus('current')
hh3cPortalIfVlanNasIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 4, 1), ).setIndexNames((0, "HH3C-PORTAL-MIB", "hh3cPortalIfVlanNasIDIfIndex"), (0, "HH3C-PORTAL-MIB", "hh3cPortalIfVlanNasIDVlanID"))
if mibBuilder.loadTexts: hh3cPortalIfVlanNasIDEntry.setStatus('current')
hh3cPortalIfVlanNasIDIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hh3cPortalIfVlanNasIDIfIndex.setStatus('current')
hh3cPortalIfVlanNasIDVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cPortalIfVlanNasIDVlanID.setStatus('current')
hh3cPortalIfVlanNasIDNasID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalIfVlanNasIDNasID.setStatus('current')
hh3cPortalSSIDFreeRuleTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 5), )
if mibBuilder.loadTexts: hh3cPortalSSIDFreeRuleTable.setStatus('current')
hh3cPortalSSIDFreeRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 5, 1), ).setIndexNames((0, "HH3C-PORTAL-MIB", "hh3cPortalSSIDFreeRuleIndex"))
if mibBuilder.loadTexts: hh3cPortalSSIDFreeRuleEntry.setStatus('current')
hh3cPortalSSIDFreeRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hh3cPortalSSIDFreeRuleIndex.setStatus('current')
hh3cPortalSSIDFreeRuleSrcSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalSSIDFreeRuleSrcSSID.setStatus('current')
hh3cPortalSSIDFreeRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalSSIDFreeRuleRowStatus.setStatus('current')
hh3cPortalSSIDFreeRuleSrcSpot = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalSSIDFreeRuleSrcSpot.setStatus('current')
hh3cPortalMacTriggerSrvTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6), )
if mibBuilder.loadTexts: hh3cPortalMacTriggerSrvTable.setStatus('current')
hh3cPortalMacTriggerSrvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6, 1), ).setIndexNames((0, "HH3C-PORTAL-MIB", "hh3cPortalMacTriggerSrvIndex"))
if mibBuilder.loadTexts: hh3cPortalMacTriggerSrvEntry.setStatus('current')
hh3cPortalMacTriggerSrvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hh3cPortalMacTriggerSrvIndex.setStatus('current')
hh3cPortalMacTriggerSrvIPAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalMacTriggerSrvIPAddrType.setStatus('current')
hh3cPortalMacTriggerSrvIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalMacTriggerSrvIP.setStatus('current')
hh3cPortalMacTriggerSrvPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalMacTriggerSrvPort.setStatus('current')
hh3cPortalMacTriggerSrvRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalMacTriggerSrvRowStatus.setStatus('current')
hh3cPortalMacTriggerOnIfTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 7), )
if mibBuilder.loadTexts: hh3cPortalMacTriggerOnIfTable.setStatus('current')
hh3cPortalMacTriggerOnIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 7, 1), ).setIndexNames((0, "HH3C-PORTAL-MIB", "hh3cPortalMacTriggerOnIfIfIndex"))
if mibBuilder.loadTexts: hh3cPortalMacTriggerOnIfEntry.setStatus('current')
hh3cPortalMacTriggerOnIfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hh3cPortalMacTriggerOnIfIfIndex.setStatus('current')
hh3cPortalMacTriggerOnIfDetctFlowPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 7, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalMacTriggerOnIfDetctFlowPeriod.setStatus('current')
hh3cPortalMacTriggerOnIfThresholdFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 7, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalMacTriggerOnIfThresholdFlow.setStatus('current')
hh3cPortalMacTriggerOnIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalMacTriggerOnIfRowStatus.setStatus('current')
hh3cPortalFreeRuleTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8), )
if mibBuilder.loadTexts: hh3cPortalFreeRuleTable.setStatus('current')
hh3cPortalFreeRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1), ).setIndexNames((0, "HH3C-PORTAL-MIB", "hh3cPortalFreeRuleIndex"))
if mibBuilder.loadTexts: hh3cPortalFreeRuleEntry.setStatus('current')
hh3cPortalFreeRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hh3cPortalFreeRuleIndex.setStatus('current')
hh3cPortalFreeRuleSrcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalFreeRuleSrcIfIndex.setStatus('current')
hh3cPortalFreeRuleSrcVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalFreeRuleSrcVlanID.setStatus('current')
hh3cPortalFreeRuleSrcMac = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalFreeRuleSrcMac.setStatus('current')
hh3cPortalFreeRuleAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalFreeRuleAddrType.setStatus('current')
hh3cPortalFreeRuleSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalFreeRuleSrcAddr.setStatus('current')
hh3cPortalFreeRuleSrcPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 7), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalFreeRuleSrcPrefix.setStatus('current')
hh3cPortalFreeRuleDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 8), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalFreeRuleDstAddr.setStatus('current')
hh3cPortalFreeRuleDstPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 9), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalFreeRuleDstPrefix.setStatus('current')
hh3cPortalFreeRuleProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 6, 17))).clone(namedValues=NamedValues(("invalid", 0), ("tcp", 6), ("udp", 17)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalFreeRuleProtocol.setStatus('current')
hh3cPortalFreeRuleSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalFreeRuleSrcPort.setStatus('current')
hh3cPortalFreeRuleDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalFreeRuleDstPort.setStatus('current')
hh3cPortalFreeRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalFreeRuleRowStatus.setStatus('current')
hh3cPortalForbiddenRuleTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9), )
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleTable.setStatus('current')
hh3cPortalForbiddenRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1), ).setIndexNames((0, "HH3C-PORTAL-MIB", "hh3cPortalForbiddenRuleIndex"))
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleEntry.setStatus('current')
hh3cPortalForbiddenRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleIndex.setStatus('current')
hh3cPortalForbiddenRuleSrcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleSrcIfIndex.setStatus('current')
hh3cPortalForbiddenRuleSrcVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleSrcVlanID.setStatus('current')
hh3cPortalForbiddenRuleSrcMac = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleSrcMac.setStatus('current')
hh3cPortalForbiddenRuleAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 5), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleAddrType.setStatus('current')
hh3cPortalForbiddenRuleSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleSrcAddr.setStatus('current')
hh3cPortalForbiddenRuleSrcPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 7), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleSrcPrefix.setStatus('current')
hh3cPortalForbiddenRuleDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 8), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleDstAddr.setStatus('current')
hh3cPortalForbiddenRuleDstPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 9), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleDstPrefix.setStatus('current')
hh3cPortalForbiddenRuleProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 6, 17))).clone(namedValues=NamedValues(("invalid", 0), ("tcp", 6), ("udp", 17)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleProtocol.setStatus('current')
hh3cPortalForbiddenRuleSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleSrcPort.setStatus('current')
hh3cPortalForbiddenRuleDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleDstPort.setStatus('current')
hh3cPortalForbiddenRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPortalForbiddenRuleRowStatus.setStatus('current')
hh3cPortalTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 99, 3))
hh3cPortalTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 99, 3, 0))
hh3cPortalServerLost = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 99, 3, 0, 1)).setObjects(("HH3C-PORTAL-MIB", "hh3cPortalServerName"), ("HH3C-PORTAL-MIB", "hh3cPortalFirstTrapTime"), ("HH3C-PORTAL-MIB", "hh3cPortalServerIP"), ("HH3C-PORTAL-MIB", "hh3cPortalServerPort"))
if mibBuilder.loadTexts: hh3cPortalServerLost.setStatus('current')
hh3cPortalServerGet = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 99, 3, 0, 2)).setObjects(("HH3C-PORTAL-MIB", "hh3cPortalServerName"), ("HH3C-PORTAL-MIB", "hh3cPortalFirstTrapTime"), ("HH3C-PORTAL-MIB", "hh3cPortalServerIP"), ("HH3C-PORTAL-MIB", "hh3cPortalServerPort"))
if mibBuilder.loadTexts: hh3cPortalServerGet.setStatus('current')
hh3cPortalTrapVarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 99, 3, 1))
hh3cPortalFirstTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 3, 1, 1), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cPortalFirstTrapTime.setStatus('current')
hh3cPortalServerIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 3, 1, 2), InetAddressIPv4()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cPortalServerIP.setStatus('current')
hh3cPortalStatistic = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4))
hh3cPortalStatAuthReq = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatAuthReq.setStatus('current')
hh3cPortalStatAckLogout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatAckLogout.setStatus('current')
hh3cPortalStatNotifyLogout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatNotifyLogout.setStatus('current')
hh3cPortalStatChallengeTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatChallengeTimeout.setStatus('current')
hh3cPortalStatChallengeBusy = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatChallengeBusy.setStatus('current')
hh3cPortalStatChallengeFail = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatChallengeFail.setStatus('current')
hh3cPortalStatAuthTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatAuthTimeout.setStatus('current')
hh3cPortalStatAuthFail = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatAuthFail.setStatus('current')
hh3cPortalStatPwdError = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatPwdError.setStatus('current')
hh3cPortalStatAuthBusy = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatAuthBusy.setStatus('current')
hh3cPortalStatAuthDisordered = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatAuthDisordered.setStatus('current')
hh3cPortalStatAuthUnknownError = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatAuthUnknownError.setStatus('current')
hh3cPortalStatAuthResp = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatAuthResp.setStatus('current')
hh3cPortalStatChallengeReq = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatChallengeReq.setStatus('current')
hh3cPortalStatChallengeResp = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatChallengeResp.setStatus('current')
hh3cPortalStatHttpReq = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatHttpReq.setStatus('current')
hh3cPortalStatHttpResp = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalStatHttpResp.setStatus('current')
hh3cPortalPktStatistic = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5))
hh3cPortalPktStaReqAuthNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalPktStaReqAuthNum.setStatus('current')
hh3cPortalPktStaAckAuthSuccess = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalPktStaAckAuthSuccess.setStatus('current')
hh3cPortalPktStaAckAuthReject = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalPktStaAckAuthReject.setStatus('current')
hh3cPortalPktStaAckAuthEstablish = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalPktStaAckAuthEstablish.setStatus('current')
hh3cPortalPktStaAckAuthBusy = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalPktStaAckAuthBusy.setStatus('current')
hh3cPortalPktStaAckAuthAuthFail = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalPktStaAckAuthAuthFail.setStatus('current')
hh3cPortalPktStaReqChallengeNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalPktStaReqChallengeNum.setStatus('current')
hh3cPortalPktStaAckChallengeSuccess = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalPktStaAckChallengeSuccess.setStatus('current')
hh3cPortalPktStaAckChallengeReject = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalPktStaAckChallengeReject.setStatus('current')
hh3cPortalPktStaAckChallengeEstablish = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalPktStaAckChallengeEstablish.setStatus('current')
hh3cPortalPktStaAckChallengeBusy = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalPktStaAckChallengeBusy.setStatus('current')
hh3cPortalPktStaAckChallengeAuthFail = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPortalPktStaAckChallengeAuthFail.setStatus('current')
mibBuilder.exportSymbols("HH3C-PORTAL-MIB", hh3cPortalForbiddenRuleDstPort=hh3cPortalForbiddenRuleDstPort, hh3cPortalMacTriggerOnIfTable=hh3cPortalMacTriggerOnIfTable, hh3cPortalForbiddenRuleSrcMac=hh3cPortalForbiddenRuleSrcMac, hh3cPortalPktStaAckAuthAuthFail=hh3cPortalPktStaAckAuthAuthFail, hh3cPortalFreeRuleTable=hh3cPortalFreeRuleTable, hh3cPortalMacTriggerOnIfThresholdFlow=hh3cPortalMacTriggerOnIfThresholdFlow, hh3cPortalIfServerIndex=hh3cPortalIfServerIndex, hh3cPortalConfig=hh3cPortalConfig, hh3cPortalServerName=hh3cPortalServerName, hh3cPortalIfVlanNasIDVlanID=hh3cPortalIfVlanNasIDVlanID, hh3cPortalForbiddenRuleDstAddr=hh3cPortalForbiddenRuleDstAddr, hh3cPortalStatHttpResp=hh3cPortalStatHttpResp, hh3cPortalIfServerUrl=hh3cPortalIfServerUrl, hh3cPortalMacTriggerOnIfEntry=hh3cPortalMacTriggerOnIfEntry, hh3cPortalStatPwdError=hh3cPortalStatPwdError, hh3cPortalPktStaReqAuthNum=hh3cPortalPktStaReqAuthNum, hh3cPortalStatus=hh3cPortalStatus, hh3cPortalFreeRuleDstPort=hh3cPortalFreeRuleDstPort, hh3cPortalFreeRuleSrcIfIndex=hh3cPortalFreeRuleSrcIfIndex, hh3cPortalFreeRuleAddrType=hh3cPortalFreeRuleAddrType, hh3cPortalMacTriggerSrvRowStatus=hh3cPortalMacTriggerSrvRowStatus, hh3cPortalIfVlanNasIDNasID=hh3cPortalIfVlanNasIDNasID, hh3cPortalFreeRuleDstPrefix=hh3cPortalFreeRuleDstPrefix, hh3cPortalIfVlanNasIDEntry=hh3cPortalIfVlanNasIDEntry, hh3cPortalStatNotifyLogout=hh3cPortalStatNotifyLogout, hh3cPortalForbiddenRuleSrcAddr=hh3cPortalForbiddenRuleSrcAddr, hh3cPortalAuthFailNumber=hh3cPortalAuthFailNumber, hh3cPortalFreeRuleEntry=hh3cPortalFreeRuleEntry, hh3cPortalStatChallengeResp=hh3cPortalStatChallengeResp, hh3cPortalMaxUserNumber=hh3cPortalMaxUserNumber, hh3cPortalForbiddenRuleDstPrefix=hh3cPortalForbiddenRuleDstPrefix, hh3cPortalSSIDFreeRuleSrcSpot=hh3cPortalSSIDFreeRuleSrcSpot, hh3cPortalForbiddenRuleRowStatus=hh3cPortalForbiddenRuleRowStatus, hh3cPortalIfServerRowStatus=hh3cPortalIfServerRowStatus, hh3cPortalSSIDFreeRuleRowStatus=hh3cPortalSSIDFreeRuleRowStatus, hh3cPortalFreeRuleSrcPrefix=hh3cPortalFreeRuleSrcPrefix, hh3cPortalMacTriggerSrvEntry=hh3cPortalMacTriggerSrvEntry, hh3cPortalForbiddenRuleAddrType=hh3cPortalForbiddenRuleAddrType, hh3cPortalForbiddenRuleSrcPrefix=hh3cPortalForbiddenRuleSrcPrefix, hh3cPortalStatChallengeBusy=hh3cPortalStatChallengeBusy, hh3cPortalPktStaAckChallengeEstablish=hh3cPortalPktStaAckChallengeEstablish, hh3cPortalIfServerTable=hh3cPortalIfServerTable, hh3cPortalForbiddenRuleTable=hh3cPortalForbiddenRuleTable, hh3cPortalUserNumberUpperLimit=hh3cPortalUserNumberUpperLimit, hh3cPortalPktStaAckAuthReject=hh3cPortalPktStaAckAuthReject, hh3cPortalPktStaAckChallengeAuthFail=hh3cPortalPktStaAckChallengeAuthFail, hh3cPortalForbiddenRuleSrcIfIndex=hh3cPortalForbiddenRuleSrcIfIndex, hh3cPortalPktStaAckAuthEstablish=hh3cPortalPktStaAckAuthEstablish, hh3cPortalSSIDFreeRuleTable=hh3cPortalSSIDFreeRuleTable, hh3cPortalStatChallengeReq=hh3cPortalStatChallengeReq, hh3cPortalTables=hh3cPortalTables, hh3cPortalNasId=hh3cPortalNasId, hh3cPortalServerPort=hh3cPortalServerPort, hh3cPortalPktStaReqChallengeNum=hh3cPortalPktStaReqChallengeNum, hh3cPortalCurrentUserNumber=hh3cPortalCurrentUserNumber, hh3cPortalAuthReqNumber=hh3cPortalAuthReqNumber, PYSNMP_MODULE_ID=hh3cPortal, hh3cPortalTraps=hh3cPortalTraps, hh3cPortalServerEntry=hh3cPortalServerEntry, hh3cPortalFreeRuleIndex=hh3cPortalFreeRuleIndex, hh3cPortalStatAckLogout=hh3cPortalStatAckLogout, hh3cPortalServerLost=hh3cPortalServerLost, hh3cPortalPktStaAckChallengeBusy=hh3cPortalPktStaAckChallengeBusy, hh3cPortalFreeRuleSrcAddr=hh3cPortalFreeRuleSrcAddr, hh3cPortalMacTriggerSrvTable=hh3cPortalMacTriggerSrvTable, hh3cPortalStatAuthDisordered=hh3cPortalStatAuthDisordered, hh3cPortalFreeRuleDstAddr=hh3cPortalFreeRuleDstAddr, hh3cPortalPktStaAckAuthBusy=hh3cPortalPktStaAckAuthBusy, hh3cPortalStatHttpReq=hh3cPortalStatHttpReq, hh3cPortalForbiddenRuleIndex=hh3cPortalForbiddenRuleIndex, hh3cPortalStatistic=hh3cPortalStatistic, hh3cPortalStatChallengeFail=hh3cPortalStatChallengeFail, hh3cPortalServerTable=hh3cPortalServerTable, hh3cPortalStatAuthBusy=hh3cPortalStatAuthBusy, hh3cPortalMacTriggerSrvIPAddrType=hh3cPortalMacTriggerSrvIPAddrType, hh3cPortalStatAuthReq=hh3cPortalStatAuthReq, hh3cPortalStatAuthResp=hh3cPortalStatAuthResp, hh3cPortalFreeRuleProtocol=hh3cPortalFreeRuleProtocol, hh3cPortalIfVlanNasIDIfIndex=hh3cPortalIfVlanNasIDIfIndex, hh3cPortalStatAuthUnknownError=hh3cPortalStatAuthUnknownError, hh3cPortalPktStaAckAuthSuccess=hh3cPortalPktStaAckAuthSuccess, hh3cPortalSSIDFreeRuleSrcSSID=hh3cPortalSSIDFreeRuleSrcSSID, hh3cPortalIfServerEntry=hh3cPortalIfServerEntry, hh3cPortalFreeRuleSrcVlanID=hh3cPortalFreeRuleSrcVlanID, hh3cPortalFreeRuleSrcMac=hh3cPortalFreeRuleSrcMac, hh3cPortalStatAuthTimeout=hh3cPortalStatAuthTimeout, hh3cPortalServerUrl=hh3cPortalServerUrl, hh3cPortalForbiddenRuleSrcPort=hh3cPortalForbiddenRuleSrcPort, hh3cPortalFirstTrapTime=hh3cPortalFirstTrapTime, hh3cPortalStatAuthFail=hh3cPortalStatAuthFail, hh3cPortalServerIP=hh3cPortalServerIP, hh3cPortalFreeRuleSrcPort=hh3cPortalFreeRuleSrcPort, hh3cPortalAuthSuccNumber=hh3cPortalAuthSuccNumber, hh3cPortalMacTriggerOnIfDetctFlowPeriod=hh3cPortalMacTriggerOnIfDetctFlowPeriod, hh3cPortalForbiddenRuleSrcVlanID=hh3cPortalForbiddenRuleSrcVlanID, hh3cPortalForbiddenRuleProtocol=hh3cPortalForbiddenRuleProtocol, hh3cPortalSSIDFreeRuleEntry=hh3cPortalSSIDFreeRuleEntry, hh3cPortalPktStaAckChallengeReject=hh3cPortalPktStaAckChallengeReject, hh3cPortalTrapVarObjects=hh3cPortalTrapVarObjects, hh3cPortalMacTriggerSrvIP=hh3cPortalMacTriggerSrvIP, hh3cPortalMacTriggerOnIfIfIndex=hh3cPortalMacTriggerOnIfIfIndex, hh3cPortal=hh3cPortal, hh3cPortalTrapPrefix=hh3cPortalTrapPrefix, hh3cPortalStatChallengeTimeout=hh3cPortalStatChallengeTimeout, hh3cPortalMacTriggerOnIfRowStatus=hh3cPortalMacTriggerOnIfRowStatus, hh3cPortalServerGet=hh3cPortalServerGet, hh3cPortalFreeRuleRowStatus=hh3cPortalFreeRuleRowStatus, hh3cPortalPktStatistic=hh3cPortalPktStatistic, hh3cPortalMacTriggerSrvPort=hh3cPortalMacTriggerSrvPort, hh3cPortalForbiddenRuleEntry=hh3cPortalForbiddenRuleEntry, hh3cPortalIfInfoTable=hh3cPortalIfInfoTable, hh3cPortalMacTriggerSrvIndex=hh3cPortalMacTriggerSrvIndex, hh3cPortalIfVlanNasIDTable=hh3cPortalIfVlanNasIDTable, hh3cPortalSSIDFreeRuleIndex=hh3cPortalSSIDFreeRuleIndex, hh3cPortalIfInfoEntry=hh3cPortalIfInfoEntry, hh3cPortalPktStaAckChallengeSuccess=hh3cPortalPktStaAckChallengeSuccess)
