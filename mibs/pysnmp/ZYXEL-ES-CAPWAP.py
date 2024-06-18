#
# PySNMP MIB module ZYXEL-ES-CAPWAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-ES-CAPWAP
# Produced by pysmi-0.3.4 at Mon Apr 29 21:43:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, IpAddress, Integer32, Gauge32, Bits, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, iso, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "IpAddress", "Integer32", "Gauge32", "Bits", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "iso", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
esCAPWAP = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3))
if mibBuilder.loadTexts: esCAPWAP.setLastUpdated('201010060000Z')
if mibBuilder.loadTexts: esCAPWAP.setOrganization('Enterprise Solution ZyXEL')
capwapInfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1))
if mibBuilder.loadTexts: capwapInfo.setStatus('current')
capwapTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2))
if mibBuilder.loadTexts: capwapTraps.setStatus('current')
capwapOnlineAP = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapOnlineAP.setStatus('current')
capwapOfflineAP = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapOfflineAP.setStatus('current')
capwapUnMgntAP = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapUnMgntAP.setStatus('current')
capwapTotalStation = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapTotalStation.setStatus('current')
capwapTrapsControl = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: capwapTrapsControl.setStatus('current')
capwapTrapsItems = ObjectIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 2))
if mibBuilder.loadTexts: capwapTrapsItems.setStatus('current')
capwapWTPOnline = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 2, 1))
if mibBuilder.loadTexts: capwapWTPOnline.setStatus('current')
capwapWTPOffline = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 2, 2))
if mibBuilder.loadTexts: capwapWTPOffline.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-ES-CAPWAP", capwapWTPOffline=capwapWTPOffline, capwapWTPOnline=capwapWTPOnline, capwapTrapsControl=capwapTrapsControl, capwapTotalStation=capwapTotalStation, esCAPWAP=esCAPWAP, PYSNMP_MODULE_ID=esCAPWAP, capwapTraps=capwapTraps, capwapUnMgntAP=capwapUnMgntAP, capwapInfo=capwapInfo, capwapTrapsItems=capwapTrapsItems, capwapOnlineAP=capwapOnlineAP, capwapOfflineAP=capwapOfflineAP)
