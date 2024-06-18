#
# PySNMP MIB module AISYSCFGPOWER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AISYSCFGPOWER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:00:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, IpAddress, Gauge32, ObjectIdentity, NotificationType, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Unsigned32, Counter32, ModuleIdentity, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "IpAddress", "Gauge32", "ObjectIdentity", "NotificationType", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Unsigned32", "Counter32", "ModuleIdentity", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiSysCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 32))
aiSysCfgPower = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 32, 3))
aiSysCfgPower.setRevisions(('2001-04-30 17:00',))
if mibBuilder.loadTexts: aiSysCfgPower.setLastUpdated('200104301700Z')
if mibBuilder.loadTexts: aiSysCfgPower.setOrganization('Applied Innovation Inc.')
aiSCPowerTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 32, 3, 0))
aiSCPowerTrapFeedFail = NotificationType((1, 3, 6, 1, 4, 1, 539, 32, 3, 0, 1)).setObjects(("AISYSCFGPOWER-MIB", "aiSCPowerFeedIndex"), ("AISYSCFGPOWER-MIB", "aiSCPowerFeedStatus"))
if mibBuilder.loadTexts: aiSCPowerTrapFeedFail.setStatus('current')
aiSCPowerTrapFeedOk = NotificationType((1, 3, 6, 1, 4, 1, 539, 32, 3, 0, 2)).setObjects(("AISYSCFGPOWER-MIB", "aiSCPowerFeedIndex"), ("AISYSCFGPOWER-MIB", "aiSCPowerFeedStatus"))
if mibBuilder.loadTexts: aiSCPowerTrapFeedOk.setStatus('current')
aiSCPowerTrapConverterFail = NotificationType((1, 3, 6, 1, 4, 1, 539, 32, 3, 0, 3)).setObjects(("AISYSCFGPOWER-MIB", "aiSCPowerConverterIndex"), ("AISYSCFGPOWER-MIB", "aiSCPowerConverterStatus"))
if mibBuilder.loadTexts: aiSCPowerTrapConverterFail.setStatus('current')
aiSCPowerTrapConverterOk = NotificationType((1, 3, 6, 1, 4, 1, 539, 32, 3, 0, 4)).setObjects(("AISYSCFGPOWER-MIB", "aiSCPowerConverterIndex"), ("AISYSCFGPOWER-MIB", "aiSCPowerConverterStatus"))
if mibBuilder.loadTexts: aiSCPowerTrapConverterOk.setStatus('current')
aiSCPowerAgregateStatus = MibScalar((1, 3, 6, 1, 4, 1, 539, 32, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("okay", 1), ("trouble", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCPowerAgregateStatus.setStatus('current')
aiSCPowerFeedTable = MibTable((1, 3, 6, 1, 4, 1, 539, 32, 3, 2), )
if mibBuilder.loadTexts: aiSCPowerFeedTable.setStatus('current')
aiSCPowerFeedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 32, 3, 2, 1), ).setIndexNames((0, "AISYSCFGPOWER-MIB", "aiSCPowerFeedIndex"))
if mibBuilder.loadTexts: aiSCPowerFeedEntry.setStatus('current')
aiSCPowerFeedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCPowerFeedIndex.setStatus('current')
aiSCPowerFeedDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCPowerFeedDescription.setStatus('current')
aiSCPowerFeedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("okay", 1), ("fail", 2), ("underVoltage", 3), ("overVoltage", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCPowerFeedStatus.setStatus('current')
aiSCPowerConverterTable = MibTable((1, 3, 6, 1, 4, 1, 539, 32, 3, 3), )
if mibBuilder.loadTexts: aiSCPowerConverterTable.setStatus('current')
aiSCPowerConverterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 32, 3, 3, 1), ).setIndexNames((0, "AISYSCFGPOWER-MIB", "aiSCPowerConverterIndex"))
if mibBuilder.loadTexts: aiSCPowerConverterEntry.setStatus('current')
aiSCPowerConverterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCPowerConverterIndex.setStatus('current')
aiSCPowerConverterDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 3, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCPowerConverterDescription.setStatus('current')
aiSCPowerConverterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 32, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("okay", 1), ("fail", 2), ("underVoltage", 3), ("overVoltage", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiSCPowerConverterStatus.setStatus('current')
mibBuilder.exportSymbols("AISYSCFGPOWER-MIB", PYSNMP_MODULE_ID=aiSysCfgPower, aiSCPowerTrapFeedFail=aiSCPowerTrapFeedFail, aiSCPowerFeedIndex=aiSCPowerFeedIndex, aiSCPowerConverterTable=aiSCPowerConverterTable, aiSCPowerTrapFeedOk=aiSCPowerTrapFeedOk, aiSCPowerAgregateStatus=aiSCPowerAgregateStatus, aiSysCfgPower=aiSysCfgPower, aiSCPowerTrapInfo=aiSCPowerTrapInfo, aiSCPowerTrapConverterOk=aiSCPowerTrapConverterOk, aiSCPowerFeedTable=aiSCPowerFeedTable, aiSCPowerFeedDescription=aiSCPowerFeedDescription, aii=aii, aiSCPowerConverterIndex=aiSCPowerConverterIndex, aiSCPowerFeedStatus=aiSCPowerFeedStatus, aiSCPowerConverterDescription=aiSCPowerConverterDescription, aiSCPowerFeedEntry=aiSCPowerFeedEntry, aiSCPowerConverterStatus=aiSCPowerConverterStatus, aiSCPowerConverterEntry=aiSCPowerConverterEntry, aiSCPowerTrapConverterFail=aiSCPowerTrapConverterFail, aiSysCfg=aiSysCfg)
