#
# PySNMP MIB module AISLCSYSCFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AISLCSYSCFG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:00:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Integer32, ObjectIdentity, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, NotificationType, Counter64, MibIdentifier, Gauge32, iso, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Integer32", "ObjectIdentity", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "NotificationType", "Counter64", "MibIdentifier", "Gauge32", "iso", "ModuleIdentity", "IpAddress")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiSLCSysCfg = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 21))
if mibBuilder.loadTexts: aiSLCSysCfg.setLastUpdated('0006200500Z')
if mibBuilder.loadTexts: aiSLCSysCfg.setOrganization('Applied Innovation Inc.')
aislcscSystemPrompt = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscSystemPrompt.setStatus('current')
aislcscShellMinLogLevel = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscShellMinLogLevel.setStatus('current')
aislcscFtpPort = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscFtpPort.setStatus('current')
aislcscTelnetPort = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscTelnetPort.setStatus('current')
aiSLCSysCfgManagerTable = MibTable((1, 3, 6, 1, 4, 1, 539, 21, 5), )
if mibBuilder.loadTexts: aiSLCSysCfgManagerTable.setStatus('current')
aiSLCSysCfgManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 21, 5, 1), ).setIndexNames((0, "AISLCSYSCFG-MIB", "aislcscManagerIndex"))
if mibBuilder.loadTexts: aiSLCSysCfgManagerEntry.setStatus('current')
aislcscManagerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 21, 5, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcscManagerIndex.setStatus('current')
aislcscManagerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 21, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscManagerAddress.setStatus('current')
aislcscManagerTrapPort = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 21, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscManagerTrapPort.setStatus('current')
aislcscReadCommunity = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscReadCommunity.setStatus('current')
aislcscWriteCommunity = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscWriteCommunity.setStatus('current')
aislcsctl1SourceID = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcsctl1SourceID.setStatus('current')
aislcsctl1LogonRequired = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcsctl1LogonRequired.setStatus('current')
aislcsctl1NumBadLogons = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 10), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcsctl1NumBadLogons.setStatus('current')
aislcscExtProbeStatus = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcscExtProbeStatus.setStatus('current')
aislcscExtLowThreshCelsius = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-54, 124))).setUnits('degrees Celsius').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscExtLowThreshCelsius.setStatus('current')
aislcscExtHighThreshCelsius = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-54, 124))).setUnits('degrees Celsius').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscExtHighThreshCelsius.setStatus('current')
aislcscExtTempCelsius = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-55, 125))).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcscExtTempCelsius.setStatus('current')
aislcscIntProbeStatus = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcscIntProbeStatus.setStatus('current')
aislcscIntLowThreshCelsius = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-54, 124))).setUnits('degrees Celsius').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscIntLowThreshCelsius.setStatus('current')
aislcscIntHighThreshCelsius = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-54, 124))).setUnits('degrees Celsius').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscIntHighThreshCelsius.setStatus('current')
aislcscIntTempCelsius = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-55, 125))).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcscIntTempCelsius.setStatus('current')
aislcscExceededThresholdValue = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-55, 125))).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcscExceededThresholdValue.setStatus('current')
aiSLCSysCfgKeepAliveTable = MibTable((1, 3, 6, 1, 4, 1, 539, 21, 20), )
if mibBuilder.loadTexts: aiSLCSysCfgKeepAliveTable.setStatus('current')
aiSLCSysCfgKeepAliveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 21, 20, 1), ).setIndexNames((0, "AISLCSYSCFG-MIB", "aislcscKeepAliveIndex"))
if mibBuilder.loadTexts: aiSLCSysCfgKeepAliveEntry.setStatus('current')
aislcscKeepAliveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 21, 20, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcscKeepAliveIndex.setStatus('current')
aislcscKeepAliveAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 21, 20, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscKeepAliveAddress.setStatus('current')
aislcscKeepAliveInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 21, 20, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscKeepAliveInterval.setStatus('current')
aislcscKeepAliveWarningText = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 21, 20, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscKeepAliveWarningText.setStatus('current')
aislcscKeepAliveOKText = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 21, 20, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscKeepAliveOKText.setStatus('current')
aislcscKeepAliveCommStat = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 21, 20, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("ok", 2), ("lost", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcscKeepAliveCommStat.setStatus('current')
aislcscActiveConfigName = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscActiveConfigName.setStatus('current')
aislcscActiveConfigCRC = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcscActiveConfigCRC.setStatus('current')
aislcscSoftwareUpdateName = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscSoftwareUpdateName.setStatus('current')
aislcscSoftwareUpdateStatus = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ready", 1), ("inProgress", 2), ("ok", 3), ("error", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscSoftwareUpdateStatus.setStatus('current')
aislcscResetSystem = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("coldStart", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscResetSystem.setStatus('current')
aislcscDiscPowerSupplyStatus = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("okay", 1), ("trouble", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcscDiscPowerSupplyStatus.setStatus('current')
aislcsc48VSupplyAStatus = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("okay", 1), ("underVoltage", 2), ("overVoltage", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcsc48VSupplyAStatus.setStatus('current')
aislcsc48VSupplyBStatus = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("okay", 1), ("underVoltage", 2), ("overVoltage", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcsc48VSupplyBStatus.setStatus('current')
aislcscFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("okay", 1), ("fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcscFanStatus.setStatus('current')
aislcscMib2ReadCommunity = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscMib2ReadCommunity.setStatus('current')
aislcscOverallAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscOverallAlarmSeverity.setStatus('current')
aislcSysCfgTime = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 21, 32))
aislcscTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 32, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscTimeZone.setStatus('current')
aislcscDayLightSaving = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 32, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscDayLightSaving.setStatus('current')
aislcscSntpPoll = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 32, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscSntpPoll.setStatus('current')
aislcscNtpServerAddr1 = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 32, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscNtpServerAddr1.setStatus('current')
aislcscNtpServerAddr2 = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 32, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscNtpServerAddr2.setStatus('current')
aislcscSntpPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 32, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscSntpPollInterval.setStatus('current')
aislcscStandaloneStatus = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standalone", 1), ("nonStandalone", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcscStandaloneStatus.setStatus('current')
aislcscShellPromptTimeout = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 34), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscShellPromptTimeout.setStatus('current')
aislcscDestMenuBreakSeq = MibScalar((1, 3, 6, 1, 4, 1, 539, 21, 35), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcscDestMenuBreakSeq.setStatus('current')
mibBuilder.exportSymbols("AISLCSYSCFG-MIB", aislcscManagerIndex=aislcscManagerIndex, aislcscWriteCommunity=aislcscWriteCommunity, aislcsctl1SourceID=aislcsctl1SourceID, aislcscFtpPort=aislcscFtpPort, aislcscDiscPowerSupplyStatus=aislcscDiscPowerSupplyStatus, aislcscIntTempCelsius=aislcscIntTempCelsius, aislcscActiveConfigCRC=aislcscActiveConfigCRC, aislcsc48VSupplyAStatus=aislcsc48VSupplyAStatus, aislcscSntpPollInterval=aislcscSntpPollInterval, aislcscResetSystem=aislcscResetSystem, aiSLCSysCfgManagerTable=aiSLCSysCfgManagerTable, aislcscKeepAliveAddress=aislcscKeepAliveAddress, aislcscKeepAliveOKText=aislcscKeepAliveOKText, aislcscFanStatus=aislcscFanStatus, aislcscMib2ReadCommunity=aislcscMib2ReadCommunity, aislcscShellPromptTimeout=aislcscShellPromptTimeout, aislcSysCfgTime=aislcSysCfgTime, aislcscDestMenuBreakSeq=aislcscDestMenuBreakSeq, aislcscReadCommunity=aislcscReadCommunity, aislcscSoftwareUpdateStatus=aislcscSoftwareUpdateStatus, PYSNMP_MODULE_ID=aiSLCSysCfg, aiSLCSysCfgKeepAliveEntry=aiSLCSysCfgKeepAliveEntry, aislcsc48VSupplyBStatus=aislcsc48VSupplyBStatus, aislcscIntHighThreshCelsius=aislcscIntHighThreshCelsius, PositiveInteger=PositiveInteger, aislcscActiveConfigName=aislcscActiveConfigName, aislcscSystemPrompt=aislcscSystemPrompt, aislcscIntProbeStatus=aislcscIntProbeStatus, aislcscNtpServerAddr2=aislcscNtpServerAddr2, aislcscKeepAliveWarningText=aislcscKeepAliveWarningText, aislcscKeepAliveCommStat=aislcscKeepAliveCommStat, aislcscIntLowThreshCelsius=aislcscIntLowThreshCelsius, aislcscDayLightSaving=aislcscDayLightSaving, aislcscNtpServerAddr1=aislcscNtpServerAddr1, aislcscStandaloneStatus=aislcscStandaloneStatus, aislcscExtTempCelsius=aislcscExtTempCelsius, aislcscKeepAliveIndex=aislcscKeepAliveIndex, aislcscExtProbeStatus=aislcscExtProbeStatus, aislcscTimeZone=aislcscTimeZone, aiSLCSysCfgManagerEntry=aiSLCSysCfgManagerEntry, aislcsctl1LogonRequired=aislcsctl1LogonRequired, aislcscSoftwareUpdateName=aislcscSoftwareUpdateName, aislcscOverallAlarmSeverity=aislcscOverallAlarmSeverity, aislcscExtLowThreshCelsius=aislcscExtLowThreshCelsius, aislcscManagerAddress=aislcscManagerAddress, aislcscSntpPoll=aislcscSntpPoll, aislcscShellMinLogLevel=aislcscShellMinLogLevel, aislcscExtHighThreshCelsius=aislcscExtHighThreshCelsius, aislcscExceededThresholdValue=aislcscExceededThresholdValue, aiSLCSysCfg=aiSLCSysCfg, aislcscManagerTrapPort=aislcscManagerTrapPort, aislcsctl1NumBadLogons=aislcsctl1NumBadLogons, aiSLCSysCfgKeepAliveTable=aiSLCSysCfgKeepAliveTable, aislcscTelnetPort=aislcscTelnetPort, aislcscKeepAliveInterval=aislcscKeepAliveInterval, aii=aii)
