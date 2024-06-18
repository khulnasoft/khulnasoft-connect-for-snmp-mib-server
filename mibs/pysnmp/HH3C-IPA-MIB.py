#
# PySNMP MIB module HH3C-IPA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-IPA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, Counter64, Gauge32, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, ObjectIdentity, MibIdentifier, ModuleIdentity, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Counter64", "Gauge32", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Unsigned32", "TimeTicks")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
hh3cIpa = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 25))
if mibBuilder.loadTexts: hh3cIpa.setLastUpdated('200411010000Z')
if mibBuilder.loadTexts: hh3cIpa.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

hh3cIpaGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 25, 1))
hh3cIpaGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpaGlobalEnable.setStatus('current')
hh3cIpaTimeOutSeconds = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 2), Integer32().clone(43200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpaTimeOutSeconds.setStatus('current')
hh3cIpaIntListMaxItemNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 3), Integer32().clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpaIntListMaxItemNum.setStatus('current')
hh3cIpaExtListMaxItemNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpaExtListMaxItemNum.setStatus('current')
hh3cIpaFWListMaxItemNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaFWListMaxItemNum.setStatus('current')
hh3cIpaAccountListMaxItemNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaAccountListMaxItemNum.setStatus('current')
hh3cIpaAccountListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaAccountListNextIndex.setStatus('current')
hh3cIpaListCleaningFlag = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("idle", 1), ("cleaningAll", 2), ("cleaningIntList", 3), ("cleaningExtList", 4), ("cleaningFWList", 5))).clone('idle')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpaListCleaningFlag.setStatus('current')
hh3cIpaIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 25, 2), )
if mibBuilder.loadTexts: hh3cIpaIfConfigTable.setStatus('current')
hh3cIpaIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 25, 2, 1), ).setIndexNames((0, "HH3C-IPA-MIB", "hh3cIpaIfConfigIfIndex"))
if mibBuilder.loadTexts: hh3cIpaIfConfigEntry.setStatus('current')
hh3cIpaIfConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hh3cIpaIfConfigIfIndex.setStatus('current')
hh3cIpaIfConfigInEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpaIfConfigInEnable.setStatus('current')
hh3cIpaIfConfigOutEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpaIfConfigOutEnable.setStatus('current')
hh3cIpaIfConfigFWEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nodirection", 1), ("inbound", 2), ("outbound", 3), ("bidirection", 4))).clone('nodirection')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpaIfConfigFWEnable.setStatus('current')
hh3cIpaAccountListTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 25, 3), )
if mibBuilder.loadTexts: hh3cIpaAccountListTable.setStatus('current')
hh3cIpaAccountListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 25, 3, 1), ).setIndexNames((0, "HH3C-IPA-MIB", "hh3cIpaAccountListIndex"))
if mibBuilder.loadTexts: hh3cIpaAccountListEntry.setStatus('current')
hh3cIpaAccountListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cIpaAccountListIndex.setStatus('current')
hh3cIpaAccountListIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 3, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpaAccountListIpAddr.setStatus('current')
hh3cIpaAccountListIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 3, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpaAccountListIpMask.setStatus('current')
hh3cIpaAccountListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIpaAccountListRowStatus.setStatus('current')
hh3cIpaIntListTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 25, 4), )
if mibBuilder.loadTexts: hh3cIpaIntListTable.setStatus('current')
hh3cIpaIntListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1), ).setIndexNames((0, "HH3C-IPA-MIB", "hh3cIpaIntListIpSrc"), (0, "HH3C-IPA-MIB", "hh3cIpaIntListIpDst"), (0, "HH3C-IPA-MIB", "hh3cIpaIntListProtocol"))
if mibBuilder.loadTexts: hh3cIpaIntListEntry.setStatus('current')
hh3cIpaIntListIpSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: hh3cIpaIntListIpSrc.setStatus('current')
hh3cIpaIntListIpDst = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: hh3cIpaIntListIpDst.setStatus('current')
hh3cIpaIntListProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hh3cIpaIntListProtocol.setStatus('current')
hh3cIpaIntListInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaIntListInPackets.setStatus('current')
hh3cIpaIntListInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaIntListInBytes.setStatus('current')
hh3cIpaIntListOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaIntListOutPackets.setStatus('current')
hh3cIpaIntListOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaIntListOutBytes.setStatus('current')
hh3cIpaExtListTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 25, 5), )
if mibBuilder.loadTexts: hh3cIpaExtListTable.setStatus('current')
hh3cIpaExtListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1), ).setIndexNames((0, "HH3C-IPA-MIB", "hh3cIpaExtListIpSrc"), (0, "HH3C-IPA-MIB", "hh3cIpaExtListIpDst"), (0, "HH3C-IPA-MIB", "hh3cIpaExtListProtocol"))
if mibBuilder.loadTexts: hh3cIpaExtListEntry.setStatus('current')
hh3cIpaExtListIpSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: hh3cIpaExtListIpSrc.setStatus('current')
hh3cIpaExtListIpDst = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: hh3cIpaExtListIpDst.setStatus('current')
hh3cIpaExtListProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hh3cIpaExtListProtocol.setStatus('current')
hh3cIpaExtListInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaExtListInPackets.setStatus('current')
hh3cIpaExtListInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaExtListInBytes.setStatus('current')
hh3cIpaExtListOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaExtListOutPackets.setStatus('current')
hh3cIpaExtListOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaExtListOutBytes.setStatus('current')
hh3cIpaFWListTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 25, 6), )
if mibBuilder.loadTexts: hh3cIpaFWListTable.setStatus('current')
hh3cIpaFWListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1), ).setIndexNames((0, "HH3C-IPA-MIB", "hh3cIpaFWListIpSrc"), (0, "HH3C-IPA-MIB", "hh3cIpaFWListIpDst"))
if mibBuilder.loadTexts: hh3cIpaFWListEntry.setStatus('current')
hh3cIpaFWListIpSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: hh3cIpaFWListIpSrc.setStatus('current')
hh3cIpaFWListIpDst = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: hh3cIpaFWListIpDst.setStatus('current')
hh3cIpaFWListInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaFWListInPackets.setStatus('current')
hh3cIpaFWListInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaFWListInBytes.setStatus('current')
hh3cIpaFWListOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaFWListOutPackets.setStatus('current')
hh3cIpaFWListOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cIpaFWListOutBytes.setStatus('current')
mibBuilder.exportSymbols("HH3C-IPA-MIB", hh3cIpaFWListEntry=hh3cIpaFWListEntry, hh3cIpaAccountListEntry=hh3cIpaAccountListEntry, hh3cIpaExtListInPackets=hh3cIpaExtListInPackets, hh3cIpaIfConfigEntry=hh3cIpaIfConfigEntry, hh3cIpaIfConfigTable=hh3cIpaIfConfigTable, hh3cIpaIntListTable=hh3cIpaIntListTable, hh3cIpaExtListIpDst=hh3cIpaExtListIpDst, hh3cIpaIfConfigInEnable=hh3cIpaIfConfigInEnable, hh3cIpaFWListTable=hh3cIpaFWListTable, hh3cIpaFWListInBytes=hh3cIpaFWListInBytes, hh3cIpaAccountListIpAddr=hh3cIpaAccountListIpAddr, hh3cIpaFWListOutPackets=hh3cIpaFWListOutPackets, hh3cIpaExtListTable=hh3cIpaExtListTable, hh3cIpaIntListInBytes=hh3cIpaIntListInBytes, hh3cIpaIntListOutBytes=hh3cIpaIntListOutBytes, hh3cIpaIntListOutPackets=hh3cIpaIntListOutPackets, hh3cIpaAccountListNextIndex=hh3cIpaAccountListNextIndex, hh3cIpaIfConfigIfIndex=hh3cIpaIfConfigIfIndex, hh3cIpaIntListIpSrc=hh3cIpaIntListIpSrc, hh3cIpaGlobalEnable=hh3cIpaGlobalEnable, hh3cIpaExtListProtocol=hh3cIpaExtListProtocol, hh3cIpa=hh3cIpa, hh3cIpaAccountListRowStatus=hh3cIpaAccountListRowStatus, hh3cIpaExtListEntry=hh3cIpaExtListEntry, hh3cIpaFWListIpDst=hh3cIpaFWListIpDst, hh3cIpaFWListInPackets=hh3cIpaFWListInPackets, hh3cIpaIntListProtocol=hh3cIpaIntListProtocol, hh3cIpaExtListIpSrc=hh3cIpaExtListIpSrc, hh3cIpaIntListInPackets=hh3cIpaIntListInPackets, hh3cIpaExtListOutPackets=hh3cIpaExtListOutPackets, PYSNMP_MODULE_ID=hh3cIpa, hh3cIpaExtListMaxItemNum=hh3cIpaExtListMaxItemNum, hh3cIpaAccountListMaxItemNum=hh3cIpaAccountListMaxItemNum, hh3cIpaAccountListIndex=hh3cIpaAccountListIndex, hh3cIpaListCleaningFlag=hh3cIpaListCleaningFlag, hh3cIpaIfConfigOutEnable=hh3cIpaIfConfigOutEnable, hh3cIpaAccountListIpMask=hh3cIpaAccountListIpMask, hh3cIpaFWListMaxItemNum=hh3cIpaFWListMaxItemNum, hh3cIpaTimeOutSeconds=hh3cIpaTimeOutSeconds, hh3cIpaIntListIpDst=hh3cIpaIntListIpDst, hh3cIpaFWListIpSrc=hh3cIpaFWListIpSrc, hh3cIpaGlobalStats=hh3cIpaGlobalStats, hh3cIpaFWListOutBytes=hh3cIpaFWListOutBytes, InterfaceIndex=InterfaceIndex, hh3cIpaIntListMaxItemNum=hh3cIpaIntListMaxItemNum, hh3cIpaIfConfigFWEnable=hh3cIpaIfConfigFWEnable, hh3cIpaExtListOutBytes=hh3cIpaExtListOutBytes, hh3cIpaAccountListTable=hh3cIpaAccountListTable, hh3cIpaExtListInBytes=hh3cIpaExtListInBytes, hh3cIpaIntListEntry=hh3cIpaIntListEntry)
