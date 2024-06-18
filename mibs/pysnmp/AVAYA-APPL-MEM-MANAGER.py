#
# PySNMP MIB module AVAYA-APPL-MEM-MANAGER (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVAYA-APPL-MEM-MANAGER
# Produced by pysmi-0.3.4 at Mon Apr 29 17:16:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
avGatewayMibs, = mibBuilder.importSymbols("AVAYAGEN-MIB", "avGatewayMibs")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
enterprises, Counter32, MibIdentifier, ModuleIdentity, iso, Bits, ObjectIdentity, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, TimeTicks, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "MibIdentifier", "ModuleIdentity", "iso", "Bits", "ObjectIdentity", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "TimeTicks", "Gauge32", "Integer32")
TruthValue, DisplayString, RowStatus, TimeInterval, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TimeInterval", "TextualConvention", "DateAndTime")
avApplMemManager = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 2, 6, 3))
if mibBuilder.loadTexts: avApplMemManager.setLastUpdated('200410201534Z')
if mibBuilder.loadTexts: avApplMemManager.setOrganization('Avaya')
avApplMemManagerGenConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 1))
avApplMemManagerTotalRamSize = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avApplMemManagerTotalRamSize.setStatus('current')
avApplMemManagerTotalNvRamSize = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avApplMemManagerTotalNvRamSize.setStatus('current')
avApplMemManagerTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2), )
if mibBuilder.loadTexts: avApplMemManagerTable.setStatus('current')
avApplMemManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1), ).setIndexNames((0, "AVAYA-APPL-MEM-MANAGER", "avApplMemManagerId"), (0, "AVAYA-APPL-MEM-MANAGER", "avApplMemManagerType"))
if mibBuilder.loadTexts: avApplMemManagerEntry.setStatus('current')
avApplMemManagerId = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avApplMemManagerId.setStatus('current')
avApplMemManagerType = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avApplMemManagerType.setStatus('current')
avApplMemManagerName = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avApplMemManagerName.setStatus('current')
avApplMemManagerSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avApplMemManagerSize.setStatus('current')
avApplMemManagerMinSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avApplMemManagerMinSize.setStatus('current')
avApplMemManagerMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avApplMemManagerMaxSize.setStatus('current')
mibBuilder.exportSymbols("AVAYA-APPL-MEM-MANAGER", PYSNMP_MODULE_ID=avApplMemManager, avApplMemManagerGenConfig=avApplMemManagerGenConfig, avApplMemManagerTotalNvRamSize=avApplMemManagerTotalNvRamSize, avApplMemManagerTable=avApplMemManagerTable, avApplMemManagerId=avApplMemManagerId, avApplMemManager=avApplMemManager, avApplMemManagerType=avApplMemManagerType, avApplMemManagerName=avApplMemManagerName, avApplMemManagerSize=avApplMemManagerSize, avApplMemManagerMinSize=avApplMemManagerMinSize, avApplMemManagerEntry=avApplMemManagerEntry, avApplMemManagerMaxSize=avApplMemManagerMaxSize, avApplMemManagerTotalRamSize=avApplMemManagerTotalRamSize)
