#
# PySNMP MIB module ALU-POWER-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALU-POWER-ETHERNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1InLinePower, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1InLinePower")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, NotificationType, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Bits, Integer32, TimeTicks, IpAddress, iso, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Bits", "Integer32", "TimeTicks", "IpAddress", "iso", "Counter64", "Unsigned32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
powerEthernetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999))
powerEthernetMIB.setRevisions(('2002-12-02 00:00',))
if mibBuilder.loadTexts: powerEthernetMIB.setLastUpdated('200212020000Z')
if mibBuilder.loadTexts: powerEthernetMIB.setOrganization('IETF Ethernet Interfaces and Hub MIB Working Group')
pethNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 0))
pethObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1))
pethConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2))
pethPsePortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1), )
if mibBuilder.loadTexts: pethPsePortTable.setStatus('current')
pethPsePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1), ).setIndexNames((0, "ALU-POWER-ETHERNET-MIB", "pethPsePortGroupIndex"), (0, "ALU-POWER-ETHERNET-MIB", "pethPsePortIndex"))
if mibBuilder.loadTexts: pethPsePortEntry.setStatus('current')
pethPsePortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethPsePortGroupIndex.setStatus('current')
pethPsePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethPsePortIndex.setStatus('current')
pethPsePortAdminEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortAdminEnable.setStatus('current')
pethPsePortPowerPairsControlAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerPairsControlAbility.setStatus('current')
pethPsePortPowerPairs = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("signal", 1), ("spare", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerPairs.setStatus('current')
pethPsePortPowerDetectionControl = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("test", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerDetectionControl.setStatus('current')
pethPsePortDetectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 7, 8))).clone(namedValues=NamedValues(("disabled", 1), ("searching", 2), ("deliveringPower", 4), ("fault", 5), ("test", 7), ("denyLowPriority", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortDetectionStatus.setStatus('current')
pethPsePortPowerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerPriority.setStatus('current')
pethPsePortPowerMaintenanceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("underCurrent", 2), ("mPSAbsent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerMaintenanceStatus.setStatus('current')
pethPsePortMPSAbsentCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortMPSAbsentCounter.setStatus('current')
pethPsePortOverCurrentCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortOverCurrentCounter.setStatus('current')
pethPsePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("telephone", 2), ("webcam", 3), ("wireless", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortType.setStatus('current')
pethPsePortPowerClassifications = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("class0", 1), ("class1", 2), ("class2", 3), ("class3", 4), ("class4", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerClassifications.setStatus('current')
pethPdPortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 2), )
if mibBuilder.loadTexts: pethPdPortTable.setStatus('current')
pethPdPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 2, 1), ).setIndexNames((0, "ALU-POWER-ETHERNET-MIB", "pethPdPortIndex"))
if mibBuilder.loadTexts: pethPdPortEntry.setStatus('current')
pethPdPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: pethPdPortIndex.setStatus('current')
pethPdPortAdminEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPdPortAdminEnable.setStatus('current')
pethMainPseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3))
pethMainPseTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1), )
if mibBuilder.loadTexts: pethMainPseTable.setStatus('current')
pethMainPseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1, 1), ).setIndexNames((0, "ALU-POWER-ETHERNET-MIB", "pethMainPseGroupIndex"))
if mibBuilder.loadTexts: pethMainPseEntry.setStatus('current')
pethMainPseGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethMainPseGroupIndex.setStatus('current')
pethMainPsePower = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPsePower.setStatus('current')
pethMainPseOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("faulty", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseOperStatus.setStatus('current')
pethMainPseConsumptionPower = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1, 1, 4), Gauge32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseConsumptionPower.setStatus('current')
pethMainPseUsageThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethMainPseUsageThreshold.setStatus('current')
pethNotificationControl = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 4))
pethNotificationControlTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 4, 1), )
if mibBuilder.loadTexts: pethNotificationControlTable.setStatus('current')
pethNotificationControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 4, 1, 1), ).setIndexNames((0, "ALU-POWER-ETHERNET-MIB", "pethNotificationControlGroupIndex"))
if mibBuilder.loadTexts: pethNotificationControlEntry.setStatus('current')
pethNotificationControlGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethNotificationControlGroupIndex.setStatus('current')
pethNotificationControlEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethNotificationControlEnable.setStatus('current')
pethPsePortOnOffNotification = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 0, 1)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"))
if mibBuilder.loadTexts: pethPsePortOnOffNotification.setStatus('current')
pethPsePortPowerMaintenanceStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 0, 2)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerMaintenanceStatus"))
if mibBuilder.loadTexts: pethPsePortPowerMaintenanceStatusNotification.setStatus('current')
pethMainPowerUsageOnNotification = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 0, 4)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"))
if mibBuilder.loadTexts: pethMainPowerUsageOnNotification.setStatus('current')
pethMainPowerUsageOffNotification = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 0, 5)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"))
if mibBuilder.loadTexts: pethMainPowerUsageOffNotification.setStatus('current')
pethCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 1))
pethGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 2))
pethCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 1, 1)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethPsePortGroup"), ("ALU-POWER-ETHERNET-MIB", "pethPdPortGroup"), ("ALU-POWER-ETHERNET-MIB", "pethMainPseGroup"), ("ALU-POWER-ETHERNET-MIB", "pethNotificationControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethCompliance = pethCompliance.setStatus('current')
pethPseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 1, 2)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethPsePortGroup"), ("ALU-POWER-ETHERNET-MIB", "pethMainPseGroup"), ("ALU-POWER-ETHERNET-MIB", "pethNotificationControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethPseCompliance = pethPseCompliance.setStatus('current')
pethPdCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 1, 3)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethPdPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethPdCompliance = pethPdCompliance.setStatus('current')
pethPsePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 2, 1)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethPsePortAdminEnable"), ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerPairsControlAbility"), ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerDetectionControl"), ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerPairs"), ("ALU-POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"), ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerPriority"), ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerMaintenanceStatus"), ("ALU-POWER-ETHERNET-MIB", "pethPsePortMPSAbsentCounter"), ("ALU-POWER-ETHERNET-MIB", "pethPsePortOverCurrentCounter"), ("ALU-POWER-ETHERNET-MIB", "pethPsePortType"), ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerClassifications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethPsePortGroup = pethPsePortGroup.setStatus('current')
pethPdPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 2, 2)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethPdPortAdminEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethPdPortGroup = pethPdPortGroup.setStatus('current')
pethMainPseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 2, 3)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethMainPsePower"), ("ALU-POWER-ETHERNET-MIB", "pethMainPseOperStatus"), ("ALU-POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"), ("ALU-POWER-ETHERNET-MIB", "pethMainPseUsageThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethMainPseGroup = pethMainPseGroup.setStatus('current')
pethNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 2, 4)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethNotificationControlEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethNotificationControlGroup = pethNotificationControlGroup.setStatus('current')
pethPsePortNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 1, 4)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethPsePortOnOffNotification"), ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerMaintenanceStatusNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethPsePortNotificationGroup = pethPsePortNotificationGroup.setStatus('current')
pethMainPowerNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 1, 5)).setObjects(("ALU-POWER-ETHERNET-MIB", "pethMainPowerUsageOnNotification"), ("ALU-POWER-ETHERNET-MIB", "pethMainPowerUsageOffNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethMainPowerNotificationGroup = pethMainPowerNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ALU-POWER-ETHERNET-MIB", pethConformance=pethConformance, pethPsePortPowerClassifications=pethPsePortPowerClassifications, pethPsePortOnOffNotification=pethPsePortOnOffNotification, pethPdCompliance=pethPdCompliance, pethPsePortTable=pethPsePortTable, pethMainPseConsumptionPower=pethMainPseConsumptionPower, pethPsePortPowerDetectionControl=pethPsePortPowerDetectionControl, pethPsePortGroup=pethPsePortGroup, pethNotificationControlGroup=pethNotificationControlGroup, pethMainPseGroup=pethMainPseGroup, pethPdPortAdminEnable=pethPdPortAdminEnable, pethPsePortEntry=pethPsePortEntry, pethCompliances=pethCompliances, pethGroups=pethGroups, pethNotificationControlEnable=pethNotificationControlEnable, pethMainPseTable=pethMainPseTable, pethPsePortGroupIndex=pethPsePortGroupIndex, pethCompliance=pethCompliance, pethPsePortOverCurrentCounter=pethPsePortOverCurrentCounter, pethPsePortMPSAbsentCounter=pethPsePortMPSAbsentCounter, pethPsePortType=pethPsePortType, pethNotificationControlEntry=pethNotificationControlEntry, pethPsePortDetectionStatus=pethPsePortDetectionStatus, pethPsePortAdminEnable=pethPsePortAdminEnable, pethMainPseOperStatus=pethMainPseOperStatus, pethMainPseEntry=pethMainPseEntry, PYSNMP_MODULE_ID=powerEthernetMIB, pethPsePortPowerPriority=pethPsePortPowerPriority, pethPdPortGroup=pethPdPortGroup, pethPsePortPowerMaintenanceStatusNotification=pethPsePortPowerMaintenanceStatusNotification, pethObjects=pethObjects, pethNotificationControl=pethNotificationControl, pethPseCompliance=pethPseCompliance, pethNotifications=pethNotifications, powerEthernetMIB=powerEthernetMIB, pethPsePortIndex=pethPsePortIndex, pethPdPortEntry=pethPdPortEntry, pethMainPseUsageThreshold=pethMainPseUsageThreshold, pethMainPseGroupIndex=pethMainPseGroupIndex, pethPdPortTable=pethPdPortTable, pethPsePortPowerPairsControlAbility=pethPsePortPowerPairsControlAbility, pethMainPowerUsageOffNotification=pethMainPowerUsageOffNotification, pethNotificationControlTable=pethNotificationControlTable, pethMainPowerNotificationGroup=pethMainPowerNotificationGroup, pethNotificationControlGroupIndex=pethNotificationControlGroupIndex, pethMainPsePower=pethMainPsePower, pethMainPowerUsageOnNotification=pethMainPowerUsageOnNotification, pethPsePortPowerMaintenanceStatus=pethPsePortPowerMaintenanceStatus, pethPdPortIndex=pethPdPortIndex, pethMainPseObjects=pethMainPseObjects, pethPsePortPowerPairs=pethPsePortPowerPairs, pethPsePortNotificationGroup=pethPsePortNotificationGroup)
