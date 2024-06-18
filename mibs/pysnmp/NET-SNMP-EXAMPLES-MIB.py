#
# PySNMP MIB module NET-SNMP-EXAMPLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NET-SNMP-EXAMPLES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
netSnmp, = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmp")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, MibIdentifier, iso, Bits, Counter64, NotificationType, Counter32, Integer32, TimeTicks, Unsigned32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "MibIdentifier", "iso", "Bits", "Counter64", "NotificationType", "Counter32", "Integer32", "TimeTicks", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "StorageType")
netSnmpExamples = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 2))
netSnmpExamples.setRevisions(('2004-06-15 00:00', '2002-02-06 00:00',))
if mibBuilder.loadTexts: netSnmpExamples.setLastUpdated('200406150000Z')
if mibBuilder.loadTexts: netSnmpExamples.setOrganization('www.net-snmp.org')
netSnmpExampleScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 2, 1))
netSnmpExampleTables = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 2, 2))
netSnmpExampleNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 2, 3))
netSnmpExampleNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 2, 3, 0))
netSnmpExampleNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 2, 3, 2))
netSnmpExampleInteger = MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 1, 1), Integer32().clone(42)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netSnmpExampleInteger.setStatus('current')
netSnmpExampleSleeper = MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 1, 2), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netSnmpExampleSleeper.setStatus('current')
netSnmpExampleString = MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 1, 3), SnmpAdminString().clone('So long, and thanks for all the fish!')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netSnmpExampleString.setStatus('current')
netSnmpIETFWGTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 2, 2, 1), )
if mibBuilder.loadTexts: netSnmpIETFWGTable.setStatus('current')
netSnmpIETFWGEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 2, 2, 1, 1), ).setIndexNames((0, "NET-SNMP-EXAMPLES-MIB", "nsIETFWGName"))
if mibBuilder.loadTexts: netSnmpIETFWGEntry.setStatus('current')
nsIETFWGName = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: nsIETFWGName.setStatus('current')
nsIETFWGChair1 = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 1, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsIETFWGChair1.setStatus('current')
nsIETFWGChair2 = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 1, 1, 3), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsIETFWGChair2.setStatus('current')
netSnmpHostsTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2), )
if mibBuilder.loadTexts: netSnmpHostsTable.setStatus('current')
netSnmpHostsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1), ).setIndexNames((0, "NET-SNMP-EXAMPLES-MIB", "netSnmpHostName"))
if mibBuilder.loadTexts: netSnmpHostsEntry.setStatus('current')
netSnmpHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: netSnmpHostName.setStatus('current')
netSnmpHostAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: netSnmpHostAddressType.setStatus('current')
netSnmpHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: netSnmpHostAddress.setStatus('current')
netSnmpHostStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: netSnmpHostStorage.setStatus('current')
netSnmpHostRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: netSnmpHostRowStatus.setStatus('current')
netSnmpExampleHeartbeatRate = MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 3, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: netSnmpExampleHeartbeatRate.setStatus('current')
netSnmpExampleHeartbeatName = MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 3, 2, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: netSnmpExampleHeartbeatName.setStatus('current')
netSnmpExampleHeartbeatNotification = NotificationType((1, 3, 6, 1, 4, 1, 8072, 2, 3, 0, 1)).setObjects(("NET-SNMP-EXAMPLES-MIB", "netSnmpExampleHeartbeatRate"))
if mibBuilder.loadTexts: netSnmpExampleHeartbeatNotification.setStatus('current')
netSnmpExampleNotification = MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 3, 1), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: netSnmpExampleNotification.setStatus('obsolete')
mibBuilder.exportSymbols("NET-SNMP-EXAMPLES-MIB", nsIETFWGName=nsIETFWGName, netSnmpExampleNotifications=netSnmpExampleNotifications, netSnmpHostAddressType=netSnmpHostAddressType, netSnmpHostRowStatus=netSnmpHostRowStatus, netSnmpExampleInteger=netSnmpExampleInteger, netSnmpExampleNotificationPrefix=netSnmpExampleNotificationPrefix, netSnmpExampleScalars=netSnmpExampleScalars, netSnmpHostAddress=netSnmpHostAddress, netSnmpExampleHeartbeatName=netSnmpExampleHeartbeatName, netSnmpExampleHeartbeatNotification=netSnmpExampleHeartbeatNotification, netSnmpExampleNotification=netSnmpExampleNotification, netSnmpHostsEntry=netSnmpHostsEntry, netSnmpExampleTables=netSnmpExampleTables, PYSNMP_MODULE_ID=netSnmpExamples, nsIETFWGChair1=nsIETFWGChair1, netSnmpHostsTable=netSnmpHostsTable, netSnmpExampleSleeper=netSnmpExampleSleeper, nsIETFWGChair2=nsIETFWGChair2, netSnmpExamples=netSnmpExamples, netSnmpExampleNotificationObjects=netSnmpExampleNotificationObjects, netSnmpExampleHeartbeatRate=netSnmpExampleHeartbeatRate, netSnmpHostStorage=netSnmpHostStorage, netSnmpIETFWGTable=netSnmpIETFWGTable, netSnmpHostName=netSnmpHostName, netSnmpExampleString=netSnmpExampleString, netSnmpIETFWGEntry=netSnmpIETFWGEntry)
