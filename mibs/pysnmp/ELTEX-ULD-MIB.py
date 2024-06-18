#
# PySNMP MIB module ELTEX-ULD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-ULD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:48:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Integer32, Counter64, TimeTicks, MibIdentifier, Bits, iso, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Integer32", "Counter64", "TimeTicks", "MibIdentifier", "Bits", "iso", "Counter32", "Gauge32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
eltexULDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 34))
if mibBuilder.loadTexts: eltexULDMIB.setLastUpdated('201301280000Z')
if mibBuilder.loadTexts: eltexULDMIB.setOrganization('Eltex Ltd.')
eltexULDNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 34, 0))
eltexULDMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 34, 1))
eltexULDTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 34, 1, 1), )
if mibBuilder.loadTexts: eltexULDTable.setStatus('current')
eltexULDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eltexULDEntry.setStatus('current')
eltexULDAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexULDAdminState.setStatus('current')
eltexULDOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexULDOperStatus.setStatus('current')
eltexULDMode = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("log", 1), ("err-disable", 2))).clone('log')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexULDMode.setStatus('current')
eltexULDDiscoveryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 300)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexULDDiscoveryTime.setStatus('current')
eltexULDIsAggressive = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexULDIsAggressive.setStatus('current')
eltexULDLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 34, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("unidirectional", 2), ("bidirectional", 3), ("tx-rx-loop", 4), ("neighbor-mismatch", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltexULDLinkStatus.setStatus('current')
eltexULDLinkStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 35265, 34, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("ELTEX-ULD-MIB", "eltexULDLinkStatus"))
if mibBuilder.loadTexts: eltexULDLinkStatusChanged.setStatus('current')
mibBuilder.exportSymbols("ELTEX-ULD-MIB", eltexULDNotifications=eltexULDNotifications, eltexULDLinkStatus=eltexULDLinkStatus, eltexULDOperStatus=eltexULDOperStatus, eltexULDAdminState=eltexULDAdminState, eltexULDMgmt=eltexULDMgmt, eltexULDIsAggressive=eltexULDIsAggressive, PYSNMP_MODULE_ID=eltexULDMIB, eltexULDDiscoveryTime=eltexULDDiscoveryTime, eltexULDMIB=eltexULDMIB, eltexULDEntry=eltexULDEntry, eltexULDMode=eltexULDMode, eltexULDLinkStatusChanged=eltexULDLinkStatusChanged, eltexULDTable=eltexULDTable)
