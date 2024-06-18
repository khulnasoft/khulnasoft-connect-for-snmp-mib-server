#
# PySNMP MIB module JUNIPER-OTN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-OTN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:49:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
jnxOtnMibRoot, jnxOtnNotifications = mibBuilder.importSymbols("JUNIPER-SMI", "jnxOtnMibRoot", "jnxOtnNotifications")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, NotificationType, ObjectIdentity, MibIdentifier, Bits, Gauge32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "NotificationType", "ObjectIdentity", "MibIdentifier", "Bits", "Gauge32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Unsigned32", "TimeTicks")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
jnxOtnMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1))
jnxOtnMib.setRevisions(('2015-06-17 00:00', '2008-07-10 00:00', '2008-07-10 00:00',))
if mibBuilder.loadTexts: jnxOtnMib.setLastUpdated('201506171138Z')
if mibBuilder.loadTexts: jnxOtnMib.setOrganization('Juniper Networks, Inc.')
class JnxOtnAlarmId(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("otnLosAlarm", 0), ("otnLofAlarm", 1), ("otnLomAlarm", 2), ("otnWavelengthlockAlarm", 3), ("otnOtuAisAlarm", 4), ("otnOtuBdiAlarm", 5), ("otnOtuTtimAlarm", 6), ("otnOtuIaeAlarm", 7), ("otnOtuSdAlarm", 8), ("otnOtuSfAlarm", 9), ("otnOtuFecExcessiveErrsAlarm", 10), ("otnOtuFecDegradedErrsAlarm", 11), ("otnOtuBbeThreholdAlarm", 12), ("otnOtuEsThreholdAlarm", 13), ("otnOtuSesThreholdAlarm", 14), ("otnOtuUasThreholdAlarm", 15), ("otnOduAisAlarm", 16), ("otnOduOciAlarm", 17), ("otnOduLckAlarm", 18), ("otnOduBdiAlarm", 19), ("otnOduTtimAlarm", 20), ("otnOduSdAlarm", 21), ("otnOduSfAlarm", 22), ("otnOduRxApsChange", 23), ("otnOduBbeThreholdAlarm", 24), ("otnOduEsThreholdAlarm", 25), ("otnOduSesThreholdAlarm", 26), ("otnOduUasThreholdAlarm", 27), ("otnOpuPMTAlarm", 28))

jnxOtnAlarms = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1))
jnxOtnAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1), )
if mibBuilder.loadTexts: jnxOtnAlarmTable.setStatus('current')
jnxOtnAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxOtnAlarmEntry.setStatus('current')
jnxOtnCurrentAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1, 1, 1), JnxOtnAlarmId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentAlarms.setStatus('current')
jnxOtnLastAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1, 1, 2), JnxOtnAlarmId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnLastAlarmId.setStatus('current')
jnxOtnLastAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnLastAlarmTime.setStatus('current')
jnxOtnLastAlarmDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnLastAlarmDate.setStatus('current')
jnxOtnLastAlarmEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("set", 2), ("cleared", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnLastAlarmEvent.setStatus('current')
jnxOtnPerformanceMonitoring = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2))
jnxOtnCurrentOdu15minTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1), )
if mibBuilder.loadTexts: jnxOtnCurrentOdu15minTable.setStatus('current')
jnxOtnCurrentOdu15minEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxOtnCurrentOdu15minEntry.setStatus('current')
jnxOtnCurrentOdu15minBIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOdu15minBIP.setStatus('current')
jnxOtnCurrentOdu15minBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOdu15minBBE.setStatus('current')
jnxOtnCurrentOdu15minES = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOdu15minES.setStatus('current')
jnxOtnCurrentOdu15minSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOdu15minSES.setStatus('current')
jnxOtnCurrentOdu15minUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOdu15minUAS.setStatus('current')
jnxOtnCurrentOdu15minElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOdu15minElapsedTime.setStatus('current')
jnxOtnIntervalOdu15minTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2), )
if mibBuilder.loadTexts: jnxOtnIntervalOdu15minTable.setStatus('current')
jnxOtnIntervalOdu15minEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "JUNIPER-OTN-MIB", "jnxOtnIntervalOdu15minIntervalNumber"))
if mibBuilder.loadTexts: jnxOtnIntervalOdu15minEntry.setStatus('current')
jnxOtnIntervalOdu15minIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: jnxOtnIntervalOdu15minIntervalNumber.setStatus('current')
jnxOtnIntervalOdu15minBIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOdu15minBIP.setStatus('current')
jnxOtnIntervalOdu15minBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOdu15minBBE.setStatus('current')
jnxOtnIntervalOdu15minES = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOdu15minES.setStatus('current')
jnxOtnIntervalOdu15minSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOdu15minSES.setStatus('current')
jnxOtnIntervalOdu15minUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOdu15minUAS.setStatus('current')
jnxOtnIntervalOdu15minInvalidData = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOdu15minInvalidData.setStatus('current')
jnxOtnIntervalODdu15minTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 2, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalODdu15minTimeStamp.setStatus('current')
jnxOtnTotalOduTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3), )
if mibBuilder.loadTexts: jnxOtnTotalOduTable.setStatus('current')
jnxOtnTotalOduEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxOtnTotalOduEntry.setStatus('current')
jnxOtnTotalOduDayNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOduDayNumber.setStatus('current')
jnxOtnTotalOduBIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOduBIP.setStatus('current')
jnxOtnTotalOduBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOduBBE.setStatus('current')
jnxOtnTotalOduES = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOduES.setStatus('current')
jnxOtnTotalOduSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOduSES.setStatus('current')
jnxOtnTotalOduUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOduUAS.setStatus('current')
jnxOtnCurrentOtu15minTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4), )
if mibBuilder.loadTexts: jnxOtnCurrentOtu15minTable.setStatus('current')
jnxOtnCurrentOtu15minEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxOtnCurrentOtu15minEntry.setStatus('current')
jnxOtnCurrentOtu15minBIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOtu15minBIP.setStatus('current')
jnxOtnCurrentOtu15minBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOtu15minBBE.setStatus('current')
jnxOtnCurrentOtu15minES = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOtu15minES.setStatus('current')
jnxOtnCurrentOtu15minSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOtu15minSES.setStatus('current')
jnxOtnCurrentOtu15minUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOtu15minUAS.setStatus('current')
jnxOtnCurrentOtu15minElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOtu15minElapsedTime.setStatus('current')
jnxOtnIntervalOtu15minTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5), )
if mibBuilder.loadTexts: jnxOtnIntervalOtu15minTable.setStatus('current')
jnxOtnIntervalOtu15minEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "JUNIPER-OTN-MIB", "jnxOtnIntervalOtu15minIntervalNumber"))
if mibBuilder.loadTexts: jnxOtnIntervalOtu15minEntry.setStatus('current')
jnxOtnIntervalOtu15minIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: jnxOtnIntervalOtu15minIntervalNumber.setStatus('current')
jnxOtnIntervalOtu15minBIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOtu15minBIP.setStatus('current')
jnxOtnIntervalOtu15minBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOtu15minBBE.setStatus('current')
jnxOtnIntervalOtu15minES = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOtu15minES.setStatus('current')
jnxOtnIntervalOtu15minSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOtu15minSES.setStatus('current')
jnxOtnIntervalOtu15minUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOtu15minUAS.setStatus('current')
jnxOtnIntervalOtu15minInvalidData = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOtu15minInvalidData.setStatus('current')
jnxOtnIntervalOtu15minTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 5, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOtu15minTimeStamp.setStatus('current')
jnxOtnTotalOtuTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6), )
if mibBuilder.loadTexts: jnxOtnTotalOtuTable.setStatus('current')
jnxOtnTotalOtuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxOtnTotalOtuEntry.setStatus('current')
jnxOtnTotalOtuDayNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOtuDayNumber.setStatus('current')
jnxOtnTotalOtuBIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOtuBIP.setStatus('current')
jnxOtnTotalOtuBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOtuBBE.setStatus('current')
jnxOtnTotalOtuES = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOtuES.setStatus('current')
jnxOtnTotalOtuSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOtuSES.setStatus('current')
jnxOtnTotalOtuUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 6, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOtuUAS.setStatus('current')
jnxOtnCurrentOtuFec15minTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7), )
if mibBuilder.loadTexts: jnxOtnCurrentOtuFec15minTable.setStatus('current')
jnxOtnCurrentOtuFec15minEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxOtnCurrentOtuFec15minEntry.setStatus('current')
jnxOtnCurrentOtuFec15minCorrectedErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOtuFec15minCorrectedErrors.setStatus('current')
jnxOtnCurrentOtuFec15minCorrectedErrorRatioX = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOtuFec15minCorrectedErrorRatioX.setStatus('current')
jnxOtnCurrentOtuFec15minCorrectedErrorRatioY = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOtuFec15minCorrectedErrorRatioY.setStatus('current')
jnxOtnCurrentOtuFec15minUncorrectedWords = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOtuFec15minUncorrectedWords.setStatus('current')
jnxOtnCurrentOtuFec15minElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 7, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnCurrentOtuFec15minElapsedTime.setStatus('current')
jnxOtnIntervalOtuFec15minTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8), )
if mibBuilder.loadTexts: jnxOtnIntervalOtuFec15minTable.setStatus('current')
jnxOtnIntervalOtuFec15minEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "JUNIPER-OTN-MIB", "jnxOtnIntervalOtuFec15minIntervalNumber"))
if mibBuilder.loadTexts: jnxOtnIntervalOtuFec15minEntry.setStatus('current')
jnxOtnIntervalOtuFec15minIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: jnxOtnIntervalOtuFec15minIntervalNumber.setStatus('current')
jnxOtnIntervalOtuFec15minCorrectedErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOtuFec15minCorrectedErrors.setStatus('current')
jnxOtnIntervalOtuFec15minCorrectedErrorRatioX = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOtuFec15minCorrectedErrorRatioX.setStatus('current')
jnxOtnIntervalOtuFec15minCorrectedErrorRatioY = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOtuFec15minCorrectedErrorRatioY.setStatus('current')
jnxOtnIntervalOtuFec15minUncorrectedWords = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOtuFec15minUncorrectedWords.setStatus('current')
jnxOtnIntervalOtuFec15minTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 8, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnIntervalOtuFec15minTimeStamp.setStatus('current')
jnxOtnTotalOtuFecTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 9), )
if mibBuilder.loadTexts: jnxOtnTotalOtuFecTable.setStatus('current')
jnxOtnTotalOtuFecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 9, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxOtnTotalOtuFecEntry.setStatus('current')
jnxOtnTotalOtuFecDayNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOtuFecDayNumber.setStatus('current')
jnxOtnTotalOtuFecCorrectedErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 9, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOtuFecCorrectedErrors.setStatus('current')
jnxOtnTotalOtuFecUncorrectedWords = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 56, 1, 2, 9, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxOtnTotalOtuFecUncorrectedWords.setStatus('current')
jnxOtnNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 15, 0))
jnxOtnAlarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 15, 0, 1)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-OTN-MIB", "jnxOtnLastAlarmId"), ("JUNIPER-OTN-MIB", "jnxOtnCurrentAlarms"), ("JUNIPER-OTN-MIB", "jnxOtnLastAlarmDate"))
if mibBuilder.loadTexts: jnxOtnAlarmSet.setStatus('current')
jnxOtnAlarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 15, 0, 2)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-OTN-MIB", "jnxOtnLastAlarmId"), ("JUNIPER-OTN-MIB", "jnxOtnCurrentAlarms"), ("JUNIPER-OTN-MIB", "jnxOtnLastAlarmDate"))
if mibBuilder.loadTexts: jnxOtnAlarmCleared.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-OTN-MIB", jnxOtnCurrentOtuFec15minEntry=jnxOtnCurrentOtuFec15minEntry, jnxOtnTotalOtuBIP=jnxOtnTotalOtuBIP, jnxOtnAlarmEntry=jnxOtnAlarmEntry, jnxOtnCurrentOdu15minElapsedTime=jnxOtnCurrentOdu15minElapsedTime, jnxOtnTotalOduSES=jnxOtnTotalOduSES, jnxOtnTotalOduUAS=jnxOtnTotalOduUAS, jnxOtnTotalOtuUAS=jnxOtnTotalOtuUAS, jnxOtnIntervalOdu15minBBE=jnxOtnIntervalOdu15minBBE, jnxOtnIntervalOtu15minTable=jnxOtnIntervalOtu15minTable, jnxOtnTotalOduDayNumber=jnxOtnTotalOduDayNumber, jnxOtnIntervalOtuFec15minEntry=jnxOtnIntervalOtuFec15minEntry, jnxOtnCurrentOtuFec15minCorrectedErrorRatioY=jnxOtnCurrentOtuFec15minCorrectedErrorRatioY, jnxOtnTotalOtuDayNumber=jnxOtnTotalOtuDayNumber, jnxOtnIntervalOtu15minUAS=jnxOtnIntervalOtu15minUAS, jnxOtnIntervalODdu15minTimeStamp=jnxOtnIntervalODdu15minTimeStamp, jnxOtnNotificationPrefix=jnxOtnNotificationPrefix, jnxOtnCurrentAlarms=jnxOtnCurrentAlarms, jnxOtnAlarmTable=jnxOtnAlarmTable, jnxOtnIntervalOdu15minSES=jnxOtnIntervalOdu15minSES, jnxOtnCurrentOtuFec15minUncorrectedWords=jnxOtnCurrentOtuFec15minUncorrectedWords, jnxOtnTotalOtuFecTable=jnxOtnTotalOtuFecTable, jnxOtnTotalOduBBE=jnxOtnTotalOduBBE, jnxOtnCurrentOtuFec15minCorrectedErrorRatioX=jnxOtnCurrentOtuFec15minCorrectedErrorRatioX, jnxOtnAlarmCleared=jnxOtnAlarmCleared, jnxOtnTotalOtuFecEntry=jnxOtnTotalOtuFecEntry, jnxOtnCurrentOtuFec15minCorrectedErrors=jnxOtnCurrentOtuFec15minCorrectedErrors, jnxOtnCurrentOtu15minEntry=jnxOtnCurrentOtu15minEntry, jnxOtnIntervalOtuFec15minTable=jnxOtnIntervalOtuFec15minTable, jnxOtnTotalOtuSES=jnxOtnTotalOtuSES, jnxOtnCurrentOdu15minSES=jnxOtnCurrentOdu15minSES, jnxOtnIntervalOtuFec15minUncorrectedWords=jnxOtnIntervalOtuFec15minUncorrectedWords, jnxOtnCurrentOdu15minBIP=jnxOtnCurrentOdu15minBIP, jnxOtnTotalOtuFecDayNumber=jnxOtnTotalOtuFecDayNumber, jnxOtnCurrentOtuFec15minTable=jnxOtnCurrentOtuFec15minTable, jnxOtnIntervalOdu15minIntervalNumber=jnxOtnIntervalOdu15minIntervalNumber, jnxOtnPerformanceMonitoring=jnxOtnPerformanceMonitoring, jnxOtnTotalOtuBBE=jnxOtnTotalOtuBBE, jnxOtnCurrentOtu15minTable=jnxOtnCurrentOtu15minTable, jnxOtnTotalOtuFecUncorrectedWords=jnxOtnTotalOtuFecUncorrectedWords, PYSNMP_MODULE_ID=jnxOtnMib, jnxOtnIntervalOdu15minUAS=jnxOtnIntervalOdu15minUAS, jnxOtnCurrentOtu15minUAS=jnxOtnCurrentOtu15minUAS, jnxOtnCurrentOtuFec15minElapsedTime=jnxOtnCurrentOtuFec15minElapsedTime, jnxOtnMib=jnxOtnMib, jnxOtnIntervalOtu15minBIP=jnxOtnIntervalOtu15minBIP, jnxOtnIntervalOdu15minInvalidData=jnxOtnIntervalOdu15minInvalidData, jnxOtnIntervalOtu15minTimeStamp=jnxOtnIntervalOtu15minTimeStamp, jnxOtnTotalOtuEntry=jnxOtnTotalOtuEntry, jnxOtnCurrentOtu15minElapsedTime=jnxOtnCurrentOtu15minElapsedTime, jnxOtnIntervalOtu15minSES=jnxOtnIntervalOtu15minSES, jnxOtnCurrentOtu15minSES=jnxOtnCurrentOtu15minSES, jnxOtnIntervalOdu15minBIP=jnxOtnIntervalOdu15minBIP, jnxOtnIntervalOtu15minEntry=jnxOtnIntervalOtu15minEntry, jnxOtnLastAlarmTime=jnxOtnLastAlarmTime, jnxOtnLastAlarmDate=jnxOtnLastAlarmDate, jnxOtnAlarmSet=jnxOtnAlarmSet, jnxOtnTotalOtuTable=jnxOtnTotalOtuTable, jnxOtnLastAlarmEvent=jnxOtnLastAlarmEvent, jnxOtnAlarms=jnxOtnAlarms, jnxOtnIntervalOtu15minBBE=jnxOtnIntervalOtu15minBBE, jnxOtnTotalOtuFecCorrectedErrors=jnxOtnTotalOtuFecCorrectedErrors, jnxOtnIntervalOdu15minES=jnxOtnIntervalOdu15minES, jnxOtnIntervalOtu15minIntervalNumber=jnxOtnIntervalOtu15minIntervalNumber, jnxOtnCurrentOdu15minUAS=jnxOtnCurrentOdu15minUAS, jnxOtnIntervalOtuFec15minTimeStamp=jnxOtnIntervalOtuFec15minTimeStamp, jnxOtnCurrentOdu15minTable=jnxOtnCurrentOdu15minTable, jnxOtnTotalOduES=jnxOtnTotalOduES, jnxOtnIntervalOtuFec15minCorrectedErrorRatioX=jnxOtnIntervalOtuFec15minCorrectedErrorRatioX, jnxOtnTotalOtuES=jnxOtnTotalOtuES, jnxOtnIntervalOtuFec15minCorrectedErrorRatioY=jnxOtnIntervalOtuFec15minCorrectedErrorRatioY, jnxOtnCurrentOdu15minEntry=jnxOtnCurrentOdu15minEntry, jnxOtnIntervalOtuFec15minIntervalNumber=jnxOtnIntervalOtuFec15minIntervalNumber, jnxOtnTotalOduTable=jnxOtnTotalOduTable, jnxOtnLastAlarmId=jnxOtnLastAlarmId, jnxOtnCurrentOdu15minES=jnxOtnCurrentOdu15minES, jnxOtnCurrentOtu15minES=jnxOtnCurrentOtu15minES, JnxOtnAlarmId=JnxOtnAlarmId, jnxOtnCurrentOtu15minBBE=jnxOtnCurrentOtu15minBBE, jnxOtnIntervalOdu15minTable=jnxOtnIntervalOdu15minTable, jnxOtnIntervalOtuFec15minCorrectedErrors=jnxOtnIntervalOtuFec15minCorrectedErrors, jnxOtnIntervalOtu15minES=jnxOtnIntervalOtu15minES, jnxOtnIntervalOtu15minInvalidData=jnxOtnIntervalOtu15minInvalidData, jnxOtnCurrentOdu15minBBE=jnxOtnCurrentOdu15minBBE, jnxOtnCurrentOtu15minBIP=jnxOtnCurrentOtu15minBIP, jnxOtnIntervalOdu15minEntry=jnxOtnIntervalOdu15minEntry, jnxOtnTotalOduEntry=jnxOtnTotalOduEntry, jnxOtnTotalOduBIP=jnxOtnTotalOduBIP)
