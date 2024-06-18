#
# PySNMP MIB module CISCO-RPMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RPMS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, NotificationType, TimeTicks, Gauge32, iso, Unsigned32, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, ObjectIdentity, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "TimeTicks", "Gauge32", "iso", "Unsigned32", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "ObjectIdentity", "IpAddress", "MibIdentifier")
RowStatus, TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TimeStamp")
ciscoRpmsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 84))
ciscoRpmsMIB.setRevisions(('2002-04-17 00:00', '2001-11-01 00:00',))
if mibBuilder.loadTexts: ciscoRpmsMIB.setLastUpdated('200204170000Z')
if mibBuilder.loadTexts: ciscoRpmsMIB.setOrganization('Cisco Systems, Inc.')
ciscoRpmsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 1))
crpmsSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1))
crpmsCustomerProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2))
crpmsVpdn = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3))
crpmsNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 4))
crpmsSubsystemTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1), )
if mibBuilder.loadTexts: crpmsSubsystemTable.setStatus('current')
crpmsSubsystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-RPMS-MIB", "crpmsSubsystemIndex"))
if mibBuilder.loadTexts: crpmsSubsystemEntry.setStatus('current')
crpmsSubsystemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: crpmsSubsystemIndex.setStatus('current')
crpmsSubsystemName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsSubsystemName.setStatus('current')
crpmsSubsystemUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsSubsystemUptime.setStatus('current')
crpmsCpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1), )
if mibBuilder.loadTexts: crpmsCpTable.setStatus('current')
crpmsCpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1), ).setIndexNames((1, "CISCO-RPMS-MIB", "crpmsCpName"))
if mibBuilder.loadTexts: crpmsCpEntry.setStatus('current')
crpmsCpName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: crpmsCpName.setStatus('current')
crpmsCpLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpLimit.setStatus('current')
crpmsCpOverflowLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpOverflowLimit.setStatus('current')
crpmsCpActiveCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsCpActiveCalls.setStatus('current')
crpmsCpActiveOverflowCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsCpActiveOverflowCalls.setStatus('current')
crpmsCpAttemptedCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsCpAttemptedCalls.setStatus('current')
crpmsCpAttemptedOverflowCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsCpAttemptedOverflowCalls.setStatus('current')
crpmsCpRejections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsCpRejections.setStatus('current')
crpmsCpOverflowRejections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsCpOverflowRejections.setStatus('current')
crpmsCpLimitThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('percent').setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpLimitThreshold.setStatus('current')
crpmsCpOverflowLimitThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('percent').setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpOverflowLimitThreshold.setStatus('current')
crpmsCpCallRejectionThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('percent').setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpCallRejectionThreshold.setStatus('current')
crpmsCpOverflowRejectThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('percent').setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpOverflowRejectThreshold.setStatus('current')
crpmsCpEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpEntryStatus.setStatus('current')
crpmsVpdnGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1), )
if mibBuilder.loadTexts: crpmsVpdnGroupTable.setStatus('current')
crpmsVpdnGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1), ).setIndexNames((1, "CISCO-RPMS-MIB", "crpmsVpdnGroupName"))
if mibBuilder.loadTexts: crpmsVpdnGroupEntry.setStatus('current')
crpmsVpdnGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: crpmsVpdnGroupName.setStatus('current')
crpmsVpdnTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsVpdnTunnelId.setStatus('current')
crpmsVpdnTunnelProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("l2f", 1), ("l2tp", 2))).clone('l2f')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnTunnelProtocol.setStatus('current')
crpmsVpdnLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnLimit.setStatus('current')
crpmsVpdnOverflowLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnOverflowLimit.setStatus('current')
crpmsVpdnMlpBundleLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnMlpBundleLimit.setStatus('current')
crpmsVpdnLinksPerBundleLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnLinksPerBundleLimit.setStatus('current')
crpmsVpdnBundles = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsVpdnBundles.setStatus('current')
crpmsVpdnActiveCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsVpdnActiveCalls.setStatus('current')
crpmsVpdnActiveOverflowCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsVpdnActiveOverflowCalls.setStatus('current')
crpmsVpdnRejections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsVpdnRejections.setStatus('current')
crpmsVpdnSizeRejections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsVpdnSizeRejections.setStatus('current')
crpmsVpdnLimitThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('percent').setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnLimitThreshold.setStatus('current')
crpmsVpdnEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnEntryStatus.setStatus('current')
crpmsVpdnGroupCpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2), )
if mibBuilder.loadTexts: crpmsVpdnGroupCpTable.setStatus('current')
crpmsVpdnGroupCpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-RPMS-MIB", "crpmsVpdnGroupCpVpdnGroupName"), (1, "CISCO-RPMS-MIB", "crpmsVpdnGroupCpCpName"))
if mibBuilder.loadTexts: crpmsVpdnGroupCpEntry.setStatus('current')
crpmsVpdnGroupCpVpdnGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: crpmsVpdnGroupCpVpdnGroupName.setStatus('current')
crpmsVpdnGroupCpCpName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: crpmsVpdnGroupCpCpName.setStatus('current')
crpmsVpdnGroupCpEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnGroupCpEntryStatus.setStatus('current')
crpmsAlarmObject = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 4, 1), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crpmsAlarmObject.setStatus('current')
crpmsAlarmValue = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 4, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crpmsAlarmValue.setStatus('current')
crpmsAlarmThresholdObject = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 4, 3), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crpmsAlarmThresholdObject.setStatus('current')
ciscoRpmsMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 2))
ciscoRpmsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 2, 0))
crpmsRisingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 84, 2, 0, 1)).setObjects(("CISCO-RPMS-MIB", "crpmsAlarmObject"), ("CISCO-RPMS-MIB", "crpmsAlarmValue"), ("CISCO-RPMS-MIB", "crpmsAlarmThresholdObject"))
if mibBuilder.loadTexts: crpmsRisingAlarm.setStatus('current')
crpmsFallingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 84, 2, 0, 2)).setObjects(("CISCO-RPMS-MIB", "crpmsAlarmObject"), ("CISCO-RPMS-MIB", "crpmsAlarmValue"), ("CISCO-RPMS-MIB", "crpmsAlarmThresholdObject"))
if mibBuilder.loadTexts: crpmsFallingAlarm.setStatus('current')
ciscoRpmsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 3))
ciscoRpmsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 1))
ciscoRpmsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2))
ciscoRpmsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 1, 1)).setObjects(("CISCO-RPMS-MIB", "crpmsSystemGroup"), ("CISCO-RPMS-MIB", "crpmsCpGroup"), ("CISCO-RPMS-MIB", "crpmsVpdnGroup"), ("CISCO-RPMS-MIB", "crpmsNotifGroup"), ("CISCO-RPMS-MIB", "crpmsThresholdNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRpmsMIBCompliance = ciscoRpmsMIBCompliance.setStatus('current')
crpmsSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 1)).setObjects(("CISCO-RPMS-MIB", "crpmsSubsystemName"), ("CISCO-RPMS-MIB", "crpmsSubsystemUptime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crpmsSystemGroup = crpmsSystemGroup.setStatus('current')
crpmsCpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 2)).setObjects(("CISCO-RPMS-MIB", "crpmsCpLimit"), ("CISCO-RPMS-MIB", "crpmsCpOverflowLimit"), ("CISCO-RPMS-MIB", "crpmsCpActiveCalls"), ("CISCO-RPMS-MIB", "crpmsCpActiveOverflowCalls"), ("CISCO-RPMS-MIB", "crpmsCpAttemptedCalls"), ("CISCO-RPMS-MIB", "crpmsCpAttemptedOverflowCalls"), ("CISCO-RPMS-MIB", "crpmsCpRejections"), ("CISCO-RPMS-MIB", "crpmsCpOverflowRejections"), ("CISCO-RPMS-MIB", "crpmsCpLimitThreshold"), ("CISCO-RPMS-MIB", "crpmsCpOverflowLimitThreshold"), ("CISCO-RPMS-MIB", "crpmsCpCallRejectionThreshold"), ("CISCO-RPMS-MIB", "crpmsCpOverflowRejectThreshold"), ("CISCO-RPMS-MIB", "crpmsCpEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crpmsCpGroup = crpmsCpGroup.setStatus('current')
crpmsVpdnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 3)).setObjects(("CISCO-RPMS-MIB", "crpmsVpdnTunnelId"), ("CISCO-RPMS-MIB", "crpmsVpdnTunnelProtocol"), ("CISCO-RPMS-MIB", "crpmsVpdnLimit"), ("CISCO-RPMS-MIB", "crpmsVpdnOverflowLimit"), ("CISCO-RPMS-MIB", "crpmsVpdnMlpBundleLimit"), ("CISCO-RPMS-MIB", "crpmsVpdnLinksPerBundleLimit"), ("CISCO-RPMS-MIB", "crpmsVpdnBundles"), ("CISCO-RPMS-MIB", "crpmsVpdnActiveCalls"), ("CISCO-RPMS-MIB", "crpmsVpdnActiveOverflowCalls"), ("CISCO-RPMS-MIB", "crpmsVpdnRejections"), ("CISCO-RPMS-MIB", "crpmsVpdnSizeRejections"), ("CISCO-RPMS-MIB", "crpmsVpdnLimitThreshold"), ("CISCO-RPMS-MIB", "crpmsVpdnEntryStatus"), ("CISCO-RPMS-MIB", "crpmsVpdnGroupCpEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crpmsVpdnGroup = crpmsVpdnGroup.setStatus('current')
crpmsNotifGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 4)).setObjects(("CISCO-RPMS-MIB", "crpmsAlarmObject"), ("CISCO-RPMS-MIB", "crpmsAlarmValue"), ("CISCO-RPMS-MIB", "crpmsAlarmThresholdObject"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crpmsNotifGroup = crpmsNotifGroup.setStatus('current')
crpmsThresholdNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 5)).setObjects(("CISCO-RPMS-MIB", "crpmsRisingAlarm"), ("CISCO-RPMS-MIB", "crpmsFallingAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crpmsThresholdNotifGroup = crpmsThresholdNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-RPMS-MIB", crpmsCpEntryStatus=crpmsCpEntryStatus, crpmsVpdnOverflowLimit=crpmsVpdnOverflowLimit, crpmsVpdnTunnelId=crpmsVpdnTunnelId, ciscoRpmsMIBNotifications=ciscoRpmsMIBNotifications, crpmsCustomerProfile=crpmsCustomerProfile, crpmsVpdnActiveCalls=crpmsVpdnActiveCalls, ciscoRpmsMIBConformance=ciscoRpmsMIBConformance, crpmsVpdn=crpmsVpdn, crpmsVpdnGroupCpTable=crpmsVpdnGroupCpTable, crpmsCpTable=crpmsCpTable, crpmsVpdnGroupTable=crpmsVpdnGroupTable, ciscoRpmsMIBNotificationPrefix=ciscoRpmsMIBNotificationPrefix, crpmsAlarmThresholdObject=crpmsAlarmThresholdObject, crpmsVpdnGroupName=crpmsVpdnGroupName, crpmsVpdnEntryStatus=crpmsVpdnEntryStatus, crpmsSubsystemEntry=crpmsSubsystemEntry, crpmsCpOverflowLimitThreshold=crpmsCpOverflowLimitThreshold, crpmsVpdnGroupCpEntryStatus=crpmsVpdnGroupCpEntryStatus, ciscoRpmsMIB=ciscoRpmsMIB, crpmsVpdnTunnelProtocol=crpmsVpdnTunnelProtocol, crpmsVpdnGroupCpCpName=crpmsVpdnGroupCpCpName, crpmsVpdnRejections=crpmsVpdnRejections, ciscoRpmsMIBGroups=ciscoRpmsMIBGroups, crpmsVpdnMlpBundleLimit=crpmsVpdnMlpBundleLimit, crpmsAlarmObject=crpmsAlarmObject, crpmsVpdnActiveOverflowCalls=crpmsVpdnActiveOverflowCalls, crpmsCpLimitThreshold=crpmsCpLimitThreshold, crpmsSubsystemName=crpmsSubsystemName, crpmsVpdnGroupEntry=crpmsVpdnGroupEntry, crpmsSubsystemTable=crpmsSubsystemTable, crpmsNotif=crpmsNotif, crpmsCpActiveCalls=crpmsCpActiveCalls, crpmsCpOverflowRejectThreshold=crpmsCpOverflowRejectThreshold, crpmsVpdnLinksPerBundleLimit=crpmsVpdnLinksPerBundleLimit, crpmsSystemGroup=crpmsSystemGroup, ciscoRpmsMIBCompliance=ciscoRpmsMIBCompliance, crpmsVpdnGroup=crpmsVpdnGroup, crpmsCpName=crpmsCpName, crpmsVpdnGroupCpEntry=crpmsVpdnGroupCpEntry, crpmsVpdnBundles=crpmsVpdnBundles, crpmsCpAttemptedOverflowCalls=crpmsCpAttemptedOverflowCalls, crpmsCpOverflowRejections=crpmsCpOverflowRejections, crpmsCpOverflowLimit=crpmsCpOverflowLimit, crpmsVpdnGroupCpVpdnGroupName=crpmsVpdnGroupCpVpdnGroupName, crpmsFallingAlarm=crpmsFallingAlarm, crpmsCpRejections=crpmsCpRejections, crpmsCpCallRejectionThreshold=crpmsCpCallRejectionThreshold, crpmsVpdnSizeRejections=crpmsVpdnSizeRejections, ciscoRpmsMIBObjects=ciscoRpmsMIBObjects, crpmsAlarmValue=crpmsAlarmValue, crpmsSubsystemUptime=crpmsSubsystemUptime, crpmsRisingAlarm=crpmsRisingAlarm, crpmsCpAttemptedCalls=crpmsCpAttemptedCalls, crpmsSystem=crpmsSystem, crpmsNotifGroup=crpmsNotifGroup, ciscoRpmsMIBCompliances=ciscoRpmsMIBCompliances, PYSNMP_MODULE_ID=ciscoRpmsMIB, crpmsCpActiveOverflowCalls=crpmsCpActiveOverflowCalls, crpmsCpEntry=crpmsCpEntry, crpmsVpdnLimitThreshold=crpmsVpdnLimitThreshold, crpmsCpGroup=crpmsCpGroup, crpmsCpLimit=crpmsCpLimit, crpmsThresholdNotifGroup=crpmsThresholdNotifGroup, crpmsSubsystemIndex=crpmsSubsystemIndex, crpmsVpdnLimit=crpmsVpdnLimit)
