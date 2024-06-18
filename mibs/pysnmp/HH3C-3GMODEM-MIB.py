#
# PySNMP MIB module HH3C-3GMODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-3GMODEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:12:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, Integer32, Counter32, ModuleIdentity, Gauge32, IpAddress, iso, TimeTicks, MibIdentifier, Bits, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Integer32", "Counter32", "ModuleIdentity", "Gauge32", "IpAddress", "iso", "TimeTicks", "MibIdentifier", "Bits", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3c3GModem = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 98))
hh3c3GModem.setRevisions(('2009-04-30 12:00',))
if mibBuilder.loadTexts: hh3c3GModem.setLastUpdated('200904301200Z')
if mibBuilder.loadTexts: hh3c3GModem.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class Hh3cUIMStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("absent", 1), ("initial", 2), ("fault", 3), ("unprotected", 4), ("protected", 5), ("pinLocked", 6), ("pukLocked", 7), ("selfDestruct", 8))

hh3c3GModemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1))
hh3cWirelessCard = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1))
hh3cUIM = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2))
hh3cWirelessCardTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1), )
if mibBuilder.loadTexts: hh3cWirelessCardTable.setStatus('current')
hh3cWirelessCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1), ).setIndexNames((0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"))
if mibBuilder.loadTexts: hh3cWirelessCardEntry.setStatus('current')
hh3cWirelessCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cWirelessCardIndex.setStatus('current')
hh3cWirelessCardModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cWirelessCardModelName.setStatus('current')
hh3cWirelessCardMfgName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cWirelessCardMfgName.setStatus('current')
hh3cWirelessCardDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cWirelessCardDescription.setStatus('current')
hh3cWirelessCardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cWirelessCardSerialNumber.setStatus('current')
hh3cWirelessCardCMIIID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cWirelessCardCMIIID.setStatus('current')
hh3cWirelessCardHardwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cWirelessCardHardwareVersion.setStatus('current')
hh3cWirelessCardFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cWirelessCardFirmwareVersion.setStatus('current')
hh3cWirelessCardPRLVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cWirelessCardPRLVersion.setStatus('current')
hh3cUIMInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1), )
if mibBuilder.loadTexts: hh3cUIMInfoTable.setStatus('current')
hh3cUIMInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1), ).setIndexNames((0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"), (0, "HH3C-3GMODEM-MIB", "hh3cUIMIndex"))
if mibBuilder.loadTexts: hh3cUIMInfoEntry.setStatus('current')
hh3cUIMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hh3cUIMIndex.setStatus('current')
hh3cUIMStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 2), Hh3cUIMStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUIMStatus.setStatus('current')
hh3cUIMImsi = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUIMImsi.setStatus('current')
hh3cUIMPin = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUIMPin.setStatus('current')
hh3cUIMVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('milli-volt').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUIMVoltage.setStatus('current')
hh3cUIMProvider = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUIMProvider.setStatus('current')
hh3cUIMSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 31), ValueRangeConstraint(99, 99), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUIMSignal.setStatus('current')
hh3cUIMTryPinPukTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cUIMTryPinPukTimes.setStatus('current')
hh3cUIMOldPin = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 9))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cUIMOldPin.setStatus('current')
hh3c3GModemTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 98, 2))
hh3c3GModemTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 98, 3))
hh3c3GModemTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0))
hh3cDevSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDevSerialNumber.setStatus('current')
hh3cDeviceOUI = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDeviceOUI.setStatus('current')
hh3cAccessMedia = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("air", 2), ("cable", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cAccessMedia.setStatus('current')
hh3cWirelessCardInserted = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 1)).setObjects(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"), ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"), ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"), ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"))
if mibBuilder.loadTexts: hh3cWirelessCardInserted.setStatus('current')
hh3cWirelessCardPulledOut = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 2)).setObjects(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"), ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"), ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"), ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"))
if mibBuilder.loadTexts: hh3cWirelessCardPulledOut.setStatus('current')
hh3cUIMPinInvalid = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 3)).setObjects(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"), ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"), ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"), ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"))
if mibBuilder.loadTexts: hh3cUIMPinInvalid.setStatus('current')
hh3cUIMPinChanged = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 4)).setObjects(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"), ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"), ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"), ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"), ("HH3C-3GMODEM-MIB", "hh3cUIMOldPin"), ("HH3C-3GMODEM-MIB", "hh3cUIMPin"))
if mibBuilder.loadTexts: hh3cUIMPinChanged.setStatus('current')
hh3cAccessMediaChanged = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 5)).setObjects(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"), ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"), ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"), ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"), ("HH3C-3GMODEM-MIB", "hh3cAccessMedia"))
if mibBuilder.loadTexts: hh3cAccessMediaChanged.setStatus('current')
mibBuilder.exportSymbols("HH3C-3GMODEM-MIB", hh3cUIMInfoEntry=hh3cUIMInfoEntry, hh3cUIMStatus=hh3cUIMStatus, hh3cUIMOldPin=hh3cUIMOldPin, hh3c3GModemTrap=hh3c3GModemTrap, PYSNMP_MODULE_ID=hh3c3GModem, hh3cWirelessCard=hh3cWirelessCard, Hh3cUIMStatusType=Hh3cUIMStatusType, hh3cWirelessCardPRLVersion=hh3cWirelessCardPRLVersion, hh3c3GModemTraps=hh3c3GModemTraps, hh3cWirelessCardTable=hh3cWirelessCardTable, hh3cDevSerialNumber=hh3cDevSerialNumber, hh3cUIMImsi=hh3cUIMImsi, hh3cDeviceOUI=hh3cDeviceOUI, hh3cAccessMedia=hh3cAccessMedia, hh3cWirelessCardCMIIID=hh3cWirelessCardCMIIID, hh3cWirelessCardMfgName=hh3cWirelessCardMfgName, hh3cUIMTryPinPukTimes=hh3cUIMTryPinPukTimes, hh3cUIMProvider=hh3cUIMProvider, hh3cWirelessCardModelName=hh3cWirelessCardModelName, hh3c3GModem=hh3c3GModem, hh3cWirelessCardPulledOut=hh3cWirelessCardPulledOut, hh3cUIM=hh3cUIM, hh3cWirelessCardHardwareVersion=hh3cWirelessCardHardwareVersion, hh3cUIMPin=hh3cUIMPin, hh3cWirelessCardEntry=hh3cWirelessCardEntry, hh3cWirelessCardFirmwareVersion=hh3cWirelessCardFirmwareVersion, hh3cUIMInfoTable=hh3cUIMInfoTable, hh3c3GModemObjects=hh3c3GModemObjects, hh3cWirelessCardInserted=hh3cWirelessCardInserted, hh3cWirelessCardIndex=hh3cWirelessCardIndex, hh3cWirelessCardSerialNumber=hh3cWirelessCardSerialNumber, hh3cWirelessCardDescription=hh3cWirelessCardDescription, hh3cUIMPinInvalid=hh3cUIMPinInvalid, hh3cUIMVoltage=hh3cUIMVoltage, hh3c3GModemTrapPrefix=hh3c3GModemTrapPrefix, hh3cUIMIndex=hh3cUIMIndex, hh3cAccessMediaChanged=hh3cAccessMediaChanged, hh3cUIMSignal=hh3cUIMSignal, hh3cUIMPinChanged=hh3cUIMPinChanged)
