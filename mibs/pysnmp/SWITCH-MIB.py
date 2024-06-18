#
# PySNMP MIB module SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWITCH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:05:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, enterprises, Unsigned32, MibIdentifier, Counter64, NotificationType, NotificationType, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, TimeTicks, Integer32, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "enterprises", "Unsigned32", "MibIdentifier", "Counter64", "NotificationType", "NotificationType", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "TimeTicks", "Integer32", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

vendor = MibIdentifier((1, 3, 6, 1, 4, 1, 295))
ethernetSwitchingDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3))
deviceHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 1))
deviceChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 1, 1))
devicePort = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 1, 2))
ethernetPort = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 1, 2, 1))
waveBusPort = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 1, 2, 2))
fddiPort = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 1, 2, 3))
deviceSoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 2))
deviceInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 295, 3, 2, 1))
chassisTable = MibTable((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1), )
if mibBuilder.loadTexts: chassisTable.setStatus('mandatory')
chassisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1), ).setIndexNames((0, "SWITCH-MIB", "chassisIndex"))
if mibBuilder.loadTexts: chassisEntry.setStatus('mandatory')
chassisProductCode = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisProductCode.setStatus('mandatory')
chassisSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSerialNumber.setStatus('mandatory')
chassisPlaceOfManufacture = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("ottawa", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPlaceOfManufacture.setStatus('mandatory')
chassisDateOfManufacture = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisDateOfManufacture.setStatus('mandatory')
chassisMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisMacAddress.setStatus('mandatory')
chassisCodeVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCodeVersion.setStatus('mandatory')
chassisBpeEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisBpeEnabled.setStatus('mandatory')
chassisEraseSnmpConfigInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisEraseSnmpConfigInfo.setStatus('mandatory')
chassisRestoreDot1dDefaults = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisRestoreDot1dDefaults.setStatus('mandatory')
chassisPerformReset = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisPerformReset.setStatus('mandatory')
chassisIdentPressed = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisIdentPressed.setStatus('mandatory')
chassisAgeFilterDatabase = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisAgeFilterDatabase.setStatus('mandatory')
chassisClearStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisClearStatistics.setStatus('mandatory')
chassisTcpKeepAlivesEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisTcpKeepAlivesEnabled.setStatus('mandatory')
chassisTcpKeepAlivePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisTcpKeepAlivePeriod.setStatus('mandatory')
chassisIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 1, 1, 100), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisIndex.setStatus('mandatory')
portTable = MibTable((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2), )
if mibBuilder.loadTexts: portTable.setStatus('mandatory')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1), ).setIndexNames((0, "SWITCH-MIB", "portIndex"))
if mibBuilder.loadTexts: portEntry.setStatus('mandatory')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIndex.setStatus('mandatory')
portProductCode = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portProductCode.setStatus('mandatory')
portSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portSerialNumber.setStatus('mandatory')
portPlaceOfManufacture = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("ottawa", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPlaceOfManufacture.setStatus('mandatory')
portDateOfManufacture = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portDateOfManufacture.setStatus('mandatory')
portState = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portState.setStatus('mandatory')
portHighSensitivity = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portHighSensitivity.setStatus('mandatory')
portRestoreFddiMibDefaults = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portRestoreFddiMibDefaults.setStatus('mandatory')
portTranslateAllEthertypes = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portTranslateAllEthertypes.setStatus('mandatory')
portTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portTxFrames.setStatus('mandatory')
portRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portRxFrames.setStatus('mandatory')
portFcsErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portFcsErrors.setStatus('mandatory')
portFilterDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portFilterDiscards.setStatus('mandatory')
portDelayExceededDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portDelayExceededDiscards.setStatus('mandatory')
portMtuExceededDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portMtuExceededDiscards.setStatus('mandatory')
portFddiTooLongNonIpFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portFddiTooLongNonIpFrames.setStatus('mandatory')
portConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConnected.setStatus('mandatory')
sttTable = MibTable((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3), )
if mibBuilder.loadTexts: sttTable.setStatus('mandatory')
sttEntry = MibTableRow((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1), ).setIndexNames((0, "SWITCH-MIB", "sttPortIndex"))
if mibBuilder.loadTexts: sttEntry.setStatus('mandatory')
sttPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sttPortIndex.setStatus('mandatory')
sttEthertype1 = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sttEthertype1.setStatus('mandatory')
sttEntryValid1 = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sttEntryValid1.setStatus('mandatory')
sttEthertype2 = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sttEthertype2.setStatus('mandatory')
sttEntryValid2 = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sttEntryValid2.setStatus('mandatory')
sttEthertype3 = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sttEthertype3.setStatus('mandatory')
sttEntryValid3 = MibTableColumn((1, 3, 6, 1, 4, 1, 295, 3, 2, 1, 3, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sttEntryValid3.setStatus('mandatory')
touched = NotificationType((1, 3, 6, 1, 4, 1, 295) + (0,9)).setObjects(("SWITCH-MIB", "chassisIdentPressed"))
mibBuilder.exportSymbols("SWITCH-MIB", portFddiTooLongNonIpFrames=portFddiTooLongNonIpFrames, portTranslateAllEthertypes=portTranslateAllEthertypes, chassisProductCode=chassisProductCode, chassisMacAddress=chassisMacAddress, sttEntry=sttEntry, deviceInfo=deviceInfo, ethernetSwitchingDevice=ethernetSwitchingDevice, portDelayExceededDiscards=portDelayExceededDiscards, portPlaceOfManufacture=portPlaceOfManufacture, sttEthertype2=sttEthertype2, MacAddress=MacAddress, touched=touched, portState=portState, sttEthertype1=sttEthertype1, portTxFrames=portTxFrames, fddiPort=fddiPort, portRestoreFddiMibDefaults=portRestoreFddiMibDefaults, portDateOfManufacture=portDateOfManufacture, chassisIndex=chassisIndex, vendor=vendor, chassisClearStatistics=chassisClearStatistics, chassisTcpKeepAlivePeriod=chassisTcpKeepAlivePeriod, portTable=portTable, chassisTable=chassisTable, deviceHardware=deviceHardware, waveBusPort=waveBusPort, chassisSerialNumber=chassisSerialNumber, chassisAgeFilterDatabase=chassisAgeFilterDatabase, portFilterDiscards=portFilterDiscards, portConnected=portConnected, deviceSoftware=deviceSoftware, sttEntryValid1=sttEntryValid1, sttEntryValid3=sttEntryValid3, deviceChassis=deviceChassis, portMtuExceededDiscards=portMtuExceededDiscards, chassisTcpKeepAlivesEnabled=chassisTcpKeepAlivesEnabled, portProductCode=portProductCode, chassisEraseSnmpConfigInfo=chassisEraseSnmpConfigInfo, portIndex=portIndex, portSerialNumber=portSerialNumber, portRxFrames=portRxFrames, portHighSensitivity=portHighSensitivity, portFcsErrors=portFcsErrors, devicePort=devicePort, chassisBpeEnabled=chassisBpeEnabled, sttEthertype3=sttEthertype3, chassisIdentPressed=chassisIdentPressed, chassisEntry=chassisEntry, sttEntryValid2=sttEntryValid2, chassisRestoreDot1dDefaults=chassisRestoreDot1dDefaults, chassisPerformReset=chassisPerformReset, chassisPlaceOfManufacture=chassisPlaceOfManufacture, chassisDateOfManufacture=chassisDateOfManufacture, chassisCodeVersion=chassisCodeVersion, sttTable=sttTable, sttPortIndex=sttPortIndex, portEntry=portEntry, ethernetPort=ethernetPort)
