#
# PySNMP MIB module ALTEON-ISD-PLATFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTEON-ISD-PLATFORM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:05:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
platform, = mibBuilder.importSymbols("ALTEON-ROOT-MIB", "platform")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Bits, Gauge32, Counter64, Counter32, Integer32, Unsigned32, MibIdentifier, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Bits", "Gauge32", "Counter64", "Counter32", "Integer32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "IpAddress")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
alteonPlatformISDModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 1))
alteonPlatformISDModule.setRevisions(('1902-05-13 00:00', '1901-02-09 17:00',))
if mibBuilder.loadTexts: alteonPlatformISDModule.setLastUpdated('0205130000Z')
if mibBuilder.loadTexts: alteonPlatformISDModule.setOrganization('Alteon Web Systems Inc.')
alteonISDPlatformMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2))
if mibBuilder.loadTexts: alteonISDPlatformMIB.setStatus('current')
isdObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1))
if mibBuilder.loadTexts: isdObjects.setStatus('current')
isdCluster = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1))
if mibBuilder.loadTexts: isdCluster.setStatus('current')
currentAlarm = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3))
if mibBuilder.loadTexts: currentAlarm.setStatus('current')
isdMonitor = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5))
if mibBuilder.loadTexts: isdMonitor.setStatus('current')
class AlarmSeverity(TextualConvention, Integer32):
    reference = 'X.733, ITU Alarm Reporting Function'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5))
    namedValues = NamedValues(("indeterminate", 0), ("critical", 1), ("major", 2), ("warning", 4), ("clear", 5))

isdClusterTable = MibTable((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1), )
if mibBuilder.loadTexts: isdClusterTable.setStatus('current')
isdClusterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1), ).setIndexNames((0, "ALTEON-ISD-PLATFORM-MIB", "isdIndex"))
if mibBuilder.loadTexts: isdClusterEntry.setStatus('current')
isdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: isdIndex.setStatus('current')
isdIP = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdIP.setStatus('current')
isdType = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("master", 1), ("slave", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdType.setStatus('current')
isdOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdOperStatus.setStatus('current')
isdMIPOwner = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdMIPOwner.setStatus('current')
isdCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdCurrentTime.setStatus('current')
isdVersion = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdVersion.setStatus('current')
isdImageTable = MibTable((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5), )
if mibBuilder.loadTexts: isdImageTable.setStatus('current')
isdImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1), ).setIndexNames((0, "ALTEON-ISD-PLATFORM-MIB", "isdImageIndex"))
if mibBuilder.loadTexts: isdImageEntry.setStatus('current')
isdImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: isdImageIndex.setStatus('current')
isdImageVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdImageVersion.setStatus('current')
isdImageName = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdImageName.setStatus('current')
isdImageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("permanent", 1), ("current", 2), ("old", 3), ("unpacked", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdImageStatus.setStatus('current')
isdClusterMIP = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdClusterMIP.setStatus('current')
isdClusterMask = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdClusterMask.setStatus('current')
isdResourceTable = MibTable((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1), )
if mibBuilder.loadTexts: isdResourceTable.setStatus('current')
isdResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1), ).setIndexNames((0, "ALTEON-ISD-PLATFORM-MIB", "isdIndex"))
if mibBuilder.loadTexts: isdResourceEntry.setStatus('current')
isdResourceUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdResourceUptime.setStatus('current')
isdResourceCpu = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdResourceCpu.setStatus('current')
isdResourceMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdResourceMemory.setStatus('current')
isdResourceDisk = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdResourceDisk.setStatus('current')
isdNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3))
if mibBuilder.loadTexts: isdNotifications.setStatus('current')
isdNotificationObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4))
if mibBuilder.loadTexts: isdNotificationObjects.setStatus('current')
numberOfCurrentAlarms = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfCurrentAlarms.setStatus('current')
currentAlarmLastTimeChanged = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmLastTimeChanged.setStatus('current')
currentAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3), )
if mibBuilder.loadTexts: currentAlarmTable.setStatus('current')
currentAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1), ).setIndexNames((0, "ALTEON-ISD-PLATFORM-MIB", "currentAlarmIndex"))
if mibBuilder.loadTexts: currentAlarmEntry.setStatus('current')
currentAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: currentAlarmIndex.setStatus('current')
currentAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 2), AlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currentAlarmSeverity.setStatus('current')
currentAlarmOid = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmOid.setStatus('current')
currentAlarmObject = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmObject.setStatus('current')
currentAlarmCause = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmCause.setStatus('current')
currentAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlarmTime.setStatus('current')
isdEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1))
if mibBuilder.loadTexts: isdEvents.setStatus('current')
isdAlarms = ObjectIdentity((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2))
if mibBuilder.loadTexts: isdAlarms.setStatus('current')
isdAlarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1, 1)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "isdEventTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmOid"))
if mibBuilder.loadTexts: isdAlarmCleared.setStatus('current')
isdTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1, 2)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "isdEventTime"), ("ALTEON-ISD-PLATFORM-MIB", "isdEventDescription"))
if mibBuilder.loadTexts: isdTopologyChange.setStatus('current')
isdAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1, 4)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "isdEventTime"))
if mibBuilder.loadTexts: isdAuthenticationFailure.setStatus('current')
isdMipMigration = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1, 5)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "isdEventTime"), ("ALTEON-ISD-PLATFORM-MIB", "isdIP"))
if mibBuilder.loadTexts: isdMipMigration.setStatus('current')
isdDown = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 1)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"), ("ALTEON-ISD-PLATFORM-MIB", "isdIP"))
if mibBuilder.loadTexts: isdDown.setStatus('current')
isdUp = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 2)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"), ("ALTEON-ISD-PLATFORM-MIB", "isdIP"))
if mibBuilder.loadTexts: isdUp.setStatus('current')
isdSingleMaster = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 3)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"))
if mibBuilder.loadTexts: isdSingleMaster.setStatus('current')
isdMemoryStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 4)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"), ("ALTEON-ISD-PLATFORM-MIB", "isdIP"), ("ALTEON-ISD-PLATFORM-MIB", "isdUtilization"))
if mibBuilder.loadTexts: isdMemoryStateChange.setStatus('current')
isdCpuStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 5)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"), ("ALTEON-ISD-PLATFORM-MIB", "isdIP"), ("ALTEON-ISD-PLATFORM-MIB", "isdLoad"))
if mibBuilder.loadTexts: isdCpuStateChange.setStatus('current')
isdDiskStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 6)).setObjects(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"), ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"), ("ALTEON-ISD-PLATFORM-MIB", "isdIP"), ("ALTEON-ISD-PLATFORM-MIB", "isdUtilization"))
if mibBuilder.loadTexts: isdDiskStateChange.setStatus('current')
isdEventTime = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4, 1), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isdEventTime.setStatus('current')
isdEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isdEventDescription.setStatus('current')
isdUtilization = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isdUtilization.setStatus('current')
isdLoad = MibScalar((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4, 4), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: isdLoad.setStatus('current')
mibBuilder.exportSymbols("ALTEON-ISD-PLATFORM-MIB", isdUp=isdUp, PYSNMP_MODULE_ID=alteonPlatformISDModule, currentAlarmEntry=currentAlarmEntry, isdAlarms=isdAlarms, isdMIPOwner=isdMIPOwner, isdResourceEntry=isdResourceEntry, isdMemoryStateChange=isdMemoryStateChange, isdImageName=isdImageName, currentAlarmTime=currentAlarmTime, isdImageVersion=isdImageVersion, isdUtilization=isdUtilization, isdCurrentTime=isdCurrentTime, isdEvents=isdEvents, isdCpuStateChange=isdCpuStateChange, isdAuthenticationFailure=isdAuthenticationFailure, isdEventTime=isdEventTime, alteonISDPlatformMIB=alteonISDPlatformMIB, currentAlarmTable=currentAlarmTable, currentAlarmSeverity=currentAlarmSeverity, isdImageEntry=isdImageEntry, isdResourceCpu=isdResourceCpu, isdImageStatus=isdImageStatus, isdIP=isdIP, isdImageTable=isdImageTable, isdNotifications=isdNotifications, isdDiskStateChange=isdDiskStateChange, isdResourceDisk=isdResourceDisk, isdResourceTable=isdResourceTable, currentAlarmLastTimeChanged=currentAlarmLastTimeChanged, isdOperStatus=isdOperStatus, AlarmSeverity=AlarmSeverity, currentAlarm=currentAlarm, isdSingleMaster=isdSingleMaster, isdClusterEntry=isdClusterEntry, currentAlarmCause=currentAlarmCause, isdDown=isdDown, isdLoad=isdLoad, currentAlarmOid=currentAlarmOid, isdMonitor=isdMonitor, isdClusterTable=isdClusterTable, currentAlarmObject=currentAlarmObject, isdTopologyChange=isdTopologyChange, isdEventDescription=isdEventDescription, isdCluster=isdCluster, isdNotificationObjects=isdNotificationObjects, numberOfCurrentAlarms=numberOfCurrentAlarms, currentAlarmIndex=currentAlarmIndex, isdType=isdType, isdImageIndex=isdImageIndex, isdClusterMask=isdClusterMask, isdClusterMIP=isdClusterMIP, isdAlarmCleared=isdAlarmCleared, isdResourceMemory=isdResourceMemory, alteonPlatformISDModule=alteonPlatformISDModule, isdObjects=isdObjects, isdVersion=isdVersion, isdResourceUptime=isdResourceUptime, isdIndex=isdIndex, isdMipMigration=isdMipMigration)
