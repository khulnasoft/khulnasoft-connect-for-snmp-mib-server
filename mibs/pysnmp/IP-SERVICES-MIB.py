#
# PySNMP MIB module IP-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IP-SERVICES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:44:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
cjnProtocol, = mibBuilder.importSymbols("Cajun-ROOT", "cjnProtocol")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Integer32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Gauge32, Counter32, TimeTicks, Counter64, Bits, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Gauge32", "Counter32", "TimeTicks", "Counter64", "Bits", "ModuleIdentity", "ObjectIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
cjnIpv4Serv = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5))
if mibBuilder.loadTexts: cjnIpv4Serv.setLastUpdated('9902110000Z')
if mibBuilder.loadTexts: cjnIpv4Serv.setOrganization("Avaya's Concord Technology Center (CTC)")
cjnIpIRDPGblGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1))
cjnIpIRDPIfTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1), )
if mibBuilder.loadTexts: cjnIpIRDPIfTable.setStatus('current')
cjnIpIRDPIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1), ).setIndexNames((0, "IP-SERVICES-MIB", "cjnIpIRDPIfIndex"))
if mibBuilder.loadTexts: cjnIpIRDPIfEntry.setStatus('current')
cjnIpIRDPIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpIRDPIfIndex.setStatus('current')
cjnIpIfIRDPEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfIRDPEnabled.setStatus('current')
cjnIpIfIRDPTxType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("multicast", 1), ("broadcast", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfIRDPTxType.setStatus('current')
cjnIpIfIRDPPref = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfIRDPPref.setStatus('current')
cjnIpIRDPTimerMax = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 5), Integer32().clone(600)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIRDPTimerMax.setStatus('current')
cjnIpIRDPTimerMin = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 6), Integer32().clone(450)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIRDPTimerMin.setStatus('current')
cjnIpIRDPLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 1, 1, 1, 7), Integer32().clone(900)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIRDPLifetime.setStatus('current')
cjnIpBootpRelayGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 2))
cjnBootpRelayEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnBootpRelayEnabled.setStatus('current')
cjnBootpRelayTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 2, 2), )
if mibBuilder.loadTexts: cjnBootpRelayTable.setStatus('current')
cjnBootpRelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 2, 2, 1), ).setIndexNames((0, "IP-SERVICES-MIB", "cjnBootpRelayServAddr"))
if mibBuilder.loadTexts: cjnBootpRelayEntry.setStatus('current')
cjnBootpRelayServAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 2, 2, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnBootpRelayServAddr.setStatus('current')
cjnBootpRelayRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnBootpRelayRowStatus.setStatus('current')
cjnIpBootpServStats = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3))
cjnBtprInReqs = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnBtprInReqs.setStatus('current')
cjnBtprInRsps = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnBtprInRsps.setStatus('current')
cjnBtprInDiscards = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnBtprInDiscards.setStatus('current')
cjnBtprInHopsExceededs = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnBtprInHopsExceededs.setStatus('current')
cjnBtprOutReqs = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnBtprOutReqs.setStatus('current')
cjnBtprOutRsps = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 3, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnBtprOutRsps.setStatus('current')
cjnIpHelperAddressGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4))
cjnIpHelperAddressTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1), )
if mibBuilder.loadTexts: cjnIpHelperAddressTable.setStatus('current')
cjnIpHelperAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1), ).setIndexNames((0, "IP-SERVICES-MIB", "cjnIpHelperAddressIfIndex"), (0, "IP-SERVICES-MIB", "cjnIpHelperAddressAddr"))
if mibBuilder.loadTexts: cjnIpHelperAddressEntry.setStatus('current')
cjnIpHelperAddressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpHelperAddressIfIndex.setStatus('current')
cjnIpHelperAddressAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpHelperAddressAddr.setStatus('current')
cjnIpHelperAddressTFTP = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpHelperAddressTFTP.setStatus('current')
cjnIpHelperAddressDNS = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpHelperAddressDNS.setStatus('current')
cjnIpHelperAddressTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpHelperAddressTime.setStatus('current')
cjnIpHelperAddressNetBiosName = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpHelperAddressNetBiosName.setStatus('current')
cjnIpHelperAddressNetBiosData = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpHelperAddressNetBiosData.setStatus('current')
cjnIpHelperAddressBootpServ = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpHelperAddressBootpServ.setStatus('current')
cjnIpHelperAddressBootpClient = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpHelperAddressBootpClient.setStatus('current')
cjnIpHelperAddressTacacs = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 4, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpHelperAddressTacacs.setStatus('current')
cjnIpDHCPOption82Group = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 5))
cjnDHCPOpt82Sub1Enabled = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnDHCPOpt82Sub1Enabled.setStatus('current')
cjnDHCPOpt82Sub2Enabled = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 5, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cjnDHCPOpt82Sub2Enabled.setStatus('current')
mibBuilder.exportSymbols("IP-SERVICES-MIB", cjnIpHelperAddressTFTP=cjnIpHelperAddressTFTP, cjnBtprInRsps=cjnBtprInRsps, PYSNMP_MODULE_ID=cjnIpv4Serv, cjnBootpRelayEnabled=cjnBootpRelayEnabled, cjnIpHelperAddressIfIndex=cjnIpHelperAddressIfIndex, cjnIpHelperAddressTacacs=cjnIpHelperAddressTacacs, cjnBootpRelayServAddr=cjnBootpRelayServAddr, cjnBtprOutReqs=cjnBtprOutReqs, cjnIpHelperAddressEntry=cjnIpHelperAddressEntry, cjnIpDHCPOption82Group=cjnIpDHCPOption82Group, cjnIpHelperAddressTime=cjnIpHelperAddressTime, cjnDHCPOpt82Sub1Enabled=cjnDHCPOpt82Sub1Enabled, cjnIpBootpServStats=cjnIpBootpServStats, cjnIpIRDPIfIndex=cjnIpIRDPIfIndex, cjnIpIRDPIfEntry=cjnIpIRDPIfEntry, cjnIpIfIRDPEnabled=cjnIpIfIRDPEnabled, cjnIpv4Serv=cjnIpv4Serv, cjnIpIRDPTimerMin=cjnIpIRDPTimerMin, cjnIpHelperAddressNetBiosName=cjnIpHelperAddressNetBiosName, cjnBootpRelayTable=cjnBootpRelayTable, cjnIpIRDPGblGroup=cjnIpIRDPGblGroup, cjnIpHelperAddressAddr=cjnIpHelperAddressAddr, cjnIpIRDPLifetime=cjnIpIRDPLifetime, cjnIpBootpRelayGroup=cjnIpBootpRelayGroup, cjnIpIRDPIfTable=cjnIpIRDPIfTable, cjnIpIfIRDPPref=cjnIpIfIRDPPref, cjnIpHelperAddressBootpServ=cjnIpHelperAddressBootpServ, cjnIpHelperAddressTable=cjnIpHelperAddressTable, cjnBootpRelayRowStatus=cjnBootpRelayRowStatus, cjnIpHelperAddressDNS=cjnIpHelperAddressDNS, cjnDHCPOpt82Sub2Enabled=cjnDHCPOpt82Sub2Enabled, cjnIpIfIRDPTxType=cjnIpIfIRDPTxType, cjnBootpRelayEntry=cjnBootpRelayEntry, cjnBtprInHopsExceededs=cjnBtprInHopsExceededs, cjnBtprInDiscards=cjnBtprInDiscards, cjnIpIRDPTimerMax=cjnIpIRDPTimerMax, cjnIpHelperAddressNetBiosData=cjnIpHelperAddressNetBiosData, cjnIpHelperAddressBootpClient=cjnIpHelperAddressBootpClient, cjnBtprInReqs=cjnBtprInReqs, cjnBtprOutRsps=cjnBtprOutRsps, cjnIpHelperAddressGroup=cjnIpHelperAddressGroup)
