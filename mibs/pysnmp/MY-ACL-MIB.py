#
# PySNMP MIB module MY-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-ACL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
ConfigStatus, IfIndex = mibBuilder.importSymbols("MY-TC", "ConfigStatus", "IfIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, MibIdentifier, Bits, iso, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Bits", "iso", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Gauge32", "Unsigned32")
RowStatus, MacAddress, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "TruthValue", "TextualConvention", "DisplayString")
myAclMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17))
myAclMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: myAclMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: myAclMIB.setOrganization('D-Link Crop.')
myAclMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1))
myAclTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 1), )
if mibBuilder.loadTexts: myAclTable.setStatus('current')
myAclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 1, 1), ).setIndexNames((0, "MY-ACL-MIB", "myAclName"))
if mibBuilder.loadTexts: myAclEntry.setStatus('current')
myAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myAclName.setStatus('current')
myAclMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("acl-ip-standard", 1), ("acl-ip-extended", 2), ("acl-mac-extended", 3), ("acl-expert", 4), ("acl-ipv6-extended", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: myAclMode.setStatus('current')
myAclEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 1, 1, 3), ConfigStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: myAclEntryStatus.setStatus('current')
myAclIfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3), )
if mibBuilder.loadTexts: myAclIfTable.setStatus('current')
myAclIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3, 1), ).setIndexNames((0, "MY-ACL-MIB", "myAclIfIndex"))
if mibBuilder.loadTexts: myAclIfEntry.setStatus('current')
myAclIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3, 1, 1), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myAclIfIndex.setStatus('current')
myAclIfMaxEntryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myAclIfMaxEntryNum.setStatus('current')
myAclIfCurruntEntryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myAclIfCurruntEntryNum.setStatus('current')
myIfInAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfInAclName.setStatus('current')
myIfOutAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfOutAclName.setStatus('current')
myAceExtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4), )
if mibBuilder.loadTexts: myAceExtTable.setStatus('current')
myAceExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1), ).setIndexNames((0, "MY-ACL-MIB", "myAceExtAclName"), (0, "MY-ACL-MIB", "myAceExtIndex"))
if mibBuilder.loadTexts: myAceExtEntry.setStatus('current')
myAceExtAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myAceExtAclName.setStatus('current')
myAceExtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myAceExtIndex.setStatus('current')
myAceExtIfAnyVID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyVID.setStatus('current')
myAceExtVID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtVID.setStatus('current')
myAceExtIfAnySourceIp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnySourceIp.setStatus('current')
myAceExtSourceIp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtSourceIp.setStatus('current')
myAceExtIfAnySourceWildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 7), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnySourceWildCard.setStatus('current')
myAceExtSourceWildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtSourceWildCard.setStatus('current')
myAceExtIfAnySourceMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 9), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnySourceMacAddr.setStatus('current')
myAceExtSourceMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 10), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtSourceMacAddr.setStatus('current')
myAceExtIfAnyDestIp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 11), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyDestIp.setStatus('current')
myAceExtDestIp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtDestIp.setStatus('current')
myAceExtIfAnyDestWildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 13), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyDestWildCard.setStatus('current')
myAceExtDestIpWildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 14), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtDestIpWildCard.setStatus('current')
myAceExtIfAnyDestMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 15), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyDestMacAddr.setStatus('current')
myAceExtDestMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 16), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtDestMacAddr.setStatus('current')
myAceExtIfAnyEtherLikeType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 17), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyEtherLikeType.setStatus('current')
myAceExtEtherLikeType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtEtherLikeType.setStatus('current')
myAceExtIfAnyIpProtocolField = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 19), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyIpProtocolField.setStatus('current')
myAceExtIpProtocolField = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIpProtocolField.setStatus('current')
myAceExtSourceProtocolPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtSourceProtocolPort.setStatus('current')
myAceExtDestProtocolPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtDestProtocolPort.setStatus('current')
myAceExtIfAnyProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 23), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyProtocolType.setStatus('current')
myAceExtProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtProtocolType.setStatus('current')
myAceExtFlowAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtFlowAction.setStatus('current')
myAceExtEntryStauts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 26), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: myAceExtEntryStauts.setStatus('current')
myAceExtTimeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtTimeRangeName.setStatus('current')
myAceExtSourcePortOp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noOperator", 1), ("lt", 2), ("gt", 3), ("eq", 4), ("neq", 5), ("range", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtSourcePortOp.setStatus('current')
myAceExtSourceProtocolPortRange = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 29), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtSourceProtocolPortRange.setStatus('current')
myAceExtDestPortOp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noOperator", 1), ("lt", 2), ("gt", 3), ("eq", 4), ("neq", 5), ("range", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtDestPortOp.setStatus('current')
myAceExtDestProtocolPortRange = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 31), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtDestProtocolPortRange.setStatus('current')
myAceExtIfAnyCos = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 32), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyCos.setStatus('current')
myAceExtCos = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 33), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtCos.setStatus('current')
myAceExtIfAnyIpPrec = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 34), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyIpPrec.setStatus('current')
myAceExtIpPrec = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 35), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIpPrec.setStatus('current')
myAceExtIfAnyDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 36), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyDscp.setStatus('current')
myAceExtDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 37), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtDscp.setStatus('current')
myAceExtIfAnyTcpFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 38), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyTcpFlag.setStatus('current')
myAceExtTcpFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 39), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtTcpFlag.setStatus('current')
myAceExtIfAnySourceMacAddrWildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 40), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnySourceMacAddrWildCard.setStatus('current')
myAceExtSourceMacAddrWildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 41), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtSourceMacAddrWildCard.setStatus('current')
myAceExtIfAnyDestMacAddrWildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 42), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyDestMacAddrWildCard.setStatus('current')
myAceExtDestMacAddrWildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 43), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtDestMacAddrWildCard.setStatus('current')
myAceExtIfAnySourceIp6 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 44), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnySourceIp6.setStatus('current')
myAceExtSourceIp6 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 45), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtSourceIp6.setStatus('current')
myAceExtIfAnySourceIp6WildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 46), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnySourceIp6WildCard.setStatus('current')
myAceExtSourceIp6WildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 47), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtSourceIp6WildCard.setStatus('current')
myAceExtIfAnyDestIp6 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 48), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyDestIp6.setStatus('current')
myAceExtDestIp6 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 49), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtDestIp6.setStatus('current')
myAceExtIfAnyDestIp6WildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 50), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtIfAnyDestIp6WildCard.setStatus('current')
myAceExtDestIp6WildCard = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 1, 4, 1, 51), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myAceExtDestIp6WildCard.setStatus('current')
myAclMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 2))
myAclMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 2, 1))
myAclMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 2, 2))
myAclMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 2, 1, 1)).setObjects(("MY-ACL-MIB", "myAclMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myAclMIBCompliance = myAclMIBCompliance.setStatus('current')
myAclMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 17, 2, 2, 1)).setObjects(("MY-ACL-MIB", "myAclName"), ("MY-ACL-MIB", "myAclMode"), ("MY-ACL-MIB", "myAclEntryStatus"), ("MY-ACL-MIB", "myAceExtAclName"), ("MY-ACL-MIB", "myAceExtIndex"), ("MY-ACL-MIB", "myAceExtIfAnyVID"), ("MY-ACL-MIB", "myAceExtVID"), ("MY-ACL-MIB", "myAceExtIfAnySourceIp"), ("MY-ACL-MIB", "myAceExtSourceIp"), ("MY-ACL-MIB", "myAceExtIfAnySourceWildCard"), ("MY-ACL-MIB", "myAceExtSourceWildCard"), ("MY-ACL-MIB", "myAceExtIfAnySourceMacAddr"), ("MY-ACL-MIB", "myAceExtSourceMacAddr"), ("MY-ACL-MIB", "myAceExtIfAnyDestIp"), ("MY-ACL-MIB", "myAceExtDestIp"), ("MY-ACL-MIB", "myAceExtIfAnyDestWildCard"), ("MY-ACL-MIB", "myAceExtDestIpWildCard"), ("MY-ACL-MIB", "myAceExtIfAnyDestMacAddr"), ("MY-ACL-MIB", "myAceExtDestMacAddr"), ("MY-ACL-MIB", "myAceExtIfAnyEtherLikeType"), ("MY-ACL-MIB", "myAceExtEtherLikeType"), ("MY-ACL-MIB", "myAceExtIfAnyIpProtocolField"), ("MY-ACL-MIB", "myAceExtIpProtocolField"), ("MY-ACL-MIB", "myAceExtSourceProtocolPort"), ("MY-ACL-MIB", "myAceExtDestProtocolPort"), ("MY-ACL-MIB", "myAceExtProtocolType"), ("MY-ACL-MIB", "myAceExtProtocolType"), ("MY-ACL-MIB", "myAceExtFlowAction"), ("MY-ACL-MIB", "myAceExtEntryStauts"), ("MY-ACL-MIB", "myAceExtTimeRangeName"), ("MY-ACL-MIB", "myAceExtSourcePortOp"), ("MY-ACL-MIB", "myAceExtSourceProtocolPortRange"), ("MY-ACL-MIB", "myAceExtDestPortOp"), ("MY-ACL-MIB", "myAceExtDestProtocolPortRange"), ("MY-ACL-MIB", "myAceExtIfAnyCos"), ("MY-ACL-MIB", "myAceExtCos"), ("MY-ACL-MIB", "myAceExtIfAnyIpPrec"), ("MY-ACL-MIB", "myAceExtIpPrec"), ("MY-ACL-MIB", "myAceExtIfAnyDscp"), ("MY-ACL-MIB", "myAceExtDscp"), ("MY-ACL-MIB", "myAceExtIfAnyTcpFlag"), ("MY-ACL-MIB", "myAceExtTcpFlag"), ("MY-ACL-MIB", "myAceExtIfAnySourceMacAddrWildCard"), ("MY-ACL-MIB", "myAceExtSourceMacAddrWildCard"), ("MY-ACL-MIB", "myAceExtIfAnyDestMacAddrWildCard"), ("MY-ACL-MIB", "myAceExtDestMacAddrWildCard"), ("MY-ACL-MIB", "myAceExtIfAnySourceIp6"), ("MY-ACL-MIB", "myAceExtSourceIp6"), ("MY-ACL-MIB", "myAceExtIfAnySourceIp6WildCard"), ("MY-ACL-MIB", "myAceExtSourceIp6WildCard"), ("MY-ACL-MIB", "myAceExtIfAnyDestIp6"), ("MY-ACL-MIB", "myAceExtDestIp6"), ("MY-ACL-MIB", "myAceExtIfAnyDestIp6WildCard"), ("MY-ACL-MIB", "myAceExtDestIp6WildCard"), ("MY-ACL-MIB", "myAclIfIndex"), ("MY-ACL-MIB", "myAclIfMaxEntryNum"), ("MY-ACL-MIB", "myAclIfCurruntEntryNum"), ("MY-ACL-MIB", "myIfInAclName"), ("MY-ACL-MIB", "myIfOutAclName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myAclMIBGroup = myAclMIBGroup.setStatus('current')
mibBuilder.exportSymbols("MY-ACL-MIB", myAceExtEntryStauts=myAceExtEntryStauts, myAceExtIpProtocolField=myAceExtIpProtocolField, myAceExtIfAnyDestIp=myAceExtIfAnyDestIp, myAclName=myAclName, myAceExtIfAnySourceMacAddrWildCard=myAceExtIfAnySourceMacAddrWildCard, myAceExtDestMacAddrWildCard=myAceExtDestMacAddrWildCard, myAceExtVID=myAceExtVID, myAceExtSourceProtocolPortRange=myAceExtSourceProtocolPortRange, myAceExtDestIpWildCard=myAceExtDestIpWildCard, myAceExtTcpFlag=myAceExtTcpFlag, myAclIfTable=myAclIfTable, myAceExtDestIp=myAceExtDestIp, myAceExtIfAnyDestIp6=myAceExtIfAnyDestIp6, myAceExtSourceMacAddrWildCard=myAceExtSourceMacAddrWildCard, myAclEntry=myAclEntry, myAclIfEntry=myAclIfEntry, myIfOutAclName=myIfOutAclName, myAceExtIfAnyCos=myAceExtIfAnyCos, myAceExtSourceIp6WildCard=myAceExtSourceIp6WildCard, myAceExtIfAnyDscp=myAceExtIfAnyDscp, myAceExtIfAnyTcpFlag=myAceExtIfAnyTcpFlag, myAclIfMaxEntryNum=myAclIfMaxEntryNum, myAceExtIfAnySourceWildCard=myAceExtIfAnySourceWildCard, myAceExtTable=myAceExtTable, myAceExtTimeRangeName=myAceExtTimeRangeName, myAceExtDestProtocolPort=myAceExtDestProtocolPort, myAceExtSourceProtocolPort=myAceExtSourceProtocolPort, myAclMIBObjects=myAclMIBObjects, myAceExtDscp=myAceExtDscp, myAceExtDestPortOp=myAceExtDestPortOp, myAceExtCos=myAceExtCos, PYSNMP_MODULE_ID=myAclMIB, myAceExtIfAnyIpPrec=myAceExtIfAnyIpPrec, myAceExtIfAnySourceIp6=myAceExtIfAnySourceIp6, myAclMIB=myAclMIB, myAclIfCurruntEntryNum=myAclIfCurruntEntryNum, myAceExtIfAnyEtherLikeType=myAceExtIfAnyEtherLikeType, myAceExtIfAnyProtocolType=myAceExtIfAnyProtocolType, myAceExtSourceIp6=myAceExtSourceIp6, myAceExtDestIp6=myAceExtDestIp6, myAclMIBGroup=myAclMIBGroup, myAceExtIfAnyDestMacAddr=myAceExtIfAnyDestMacAddr, myAceExtIpPrec=myAceExtIpPrec, myAclMIBGroups=myAclMIBGroups, myAceExtProtocolType=myAceExtProtocolType, myAceExtIfAnyIpProtocolField=myAceExtIfAnyIpProtocolField, myAceExtIfAnyVID=myAceExtIfAnyVID, myAceExtDestMacAddr=myAceExtDestMacAddr, myAclMIBConformance=myAclMIBConformance, myAclMIBCompliances=myAclMIBCompliances, myAclMIBCompliance=myAclMIBCompliance, myAceExtSourcePortOp=myAceExtSourcePortOp, myAceExtDestProtocolPortRange=myAceExtDestProtocolPortRange, myAceExtSourceMacAddr=myAceExtSourceMacAddr, myAceExtIfAnyDestMacAddrWildCard=myAceExtIfAnyDestMacAddrWildCard, myAceExtDestIp6WildCard=myAceExtDestIp6WildCard, myAceExtIfAnyDestIp6WildCard=myAceExtIfAnyDestIp6WildCard, myAceExtIndex=myAceExtIndex, myAceExtIfAnySourceMacAddr=myAceExtIfAnySourceMacAddr, myAceExtSourceIp=myAceExtSourceIp, myAclIfIndex=myAclIfIndex, myAceExtIfAnyDestWildCard=myAceExtIfAnyDestWildCard, myAceExtEtherLikeType=myAceExtEtherLikeType, myAceExtFlowAction=myAceExtFlowAction, myAceExtEntry=myAceExtEntry, myIfInAclName=myIfInAclName, myAceExtIfAnySourceIp6WildCard=myAceExtIfAnySourceIp6WildCard, myAclEntryStatus=myAclEntryStatus, myAclTable=myAclTable, myAceExtAclName=myAceExtAclName, myAclMode=myAclMode, myAceExtSourceWildCard=myAceExtSourceWildCard, myAceExtIfAnySourceIp=myAceExtIfAnySourceIp)
