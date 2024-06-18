#
# PySNMP MIB module ENTERASYS-DVMRP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-DVMRP-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:48:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
dvmrpInterfaceEntry, = mibBuilder.importSymbols("DVMRP-MIB", "dvmrpInterfaceEntry")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, ModuleIdentity, Counter64, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Unsigned32, Counter32, TimeTicks, Bits, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Counter64", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Unsigned32", "Counter32", "TimeTicks", "Bits", "iso", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
etsysDvmrpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69))
etsysDvmrpExtMIB.setRevisions(('2009-02-27 19:29',))
if mibBuilder.loadTexts: etsysDvmrpExtMIB.setLastUpdated('200902271929Z')
if mibBuilder.loadTexts: etsysDvmrpExtMIB.setOrganization('Enterasys Networks, Inc')
etsysDvmrpExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1))
etsysDvmrpExtGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 1))
etsysDvmrpExtTables = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2))
etsysDvmrpExtIfTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 1), )
if mibBuilder.loadTexts: etsysDvmrpExtIfTable.setStatus('current')
etsysDvmrpExtIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 1, 1), )
dvmrpInterfaceEntry.registerAugmentions(("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtIfEntry"))
etsysDvmrpExtIfEntry.setIndexNames(*dvmrpInterfaceEntry.getIndexNames())
if mibBuilder.loadTexts: etsysDvmrpExtIfEntry.setStatus('current')
etsysDvmrpExtIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adminStatusUp", 1), ("adminStatusDown", 2))).clone('adminStatusUp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysDvmrpExtIfAdminStatus.setStatus('current')
etsysDvmrpExtIfIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 8, 10, 11))).clone(namedValues=NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5), ("operStatusFailed", 8), ("operStatusFailedPerm", 10), ("operStatusFailing", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDvmrpExtIfIfOperStatus.setStatus('current')
etsysDvmrpExtIfStubInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysDvmrpExtIfStubInterface.setStatus('current')
etsysDvmrpExtIfP2PNoHellos = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysDvmrpExtIfP2PNoHellos.setStatus('current')
etsysDvmrpExtIfHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 18000)).clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysDvmrpExtIfHelloInterval.setStatus('current')
etsysDvmrpExtIfHelloHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(35)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysDvmrpExtIfHelloHoldtime.setStatus('current')
etsysDvmrpExtIfReportInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 18000)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysDvmrpExtIfReportInterval.setStatus('current')
etsysDvmrpExtTibMgrTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 2), )
if mibBuilder.loadTexts: etsysDvmrpExtTibMgrTable.setStatus('current')
etsysDvmrpExtTibMgrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 2, 1), ).setIndexNames((0, "ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtTibMgrIndex"))
if mibBuilder.loadTexts: etsysDvmrpExtTibMgrEntry.setStatus('current')
etsysDvmrpExtTibMgrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysDvmrpExtTibMgrIndex.setStatus('current')
etsysDvmrpExtTibMgrKeepalivePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 180)).clone(120)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDvmrpExtTibMgrKeepalivePeriod.setStatus('current')
etsysDvmrpExtTibMgrMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDvmrpExtTibMgrMetric.setStatus('current')
etsysDvmrpExtTibMgrSGStateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDvmrpExtTibMgrSGStateLimit.setStatus('current')
etsysDvmrpExtTibMgrSGStateWarnThold = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysDvmrpExtTibMgrSGStateWarnThold.setStatus('current')
etsysDvmrpExtTibMgrSGStateStored = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 1, 2, 2, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDvmrpExtTibMgrSGStateStored.setStatus('current')
etsysDvmrpExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 2))
etsysDvmrpExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 2, 1))
etsysDvmrpExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 2, 2))
etsysDvmrpExtIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 2, 1, 1)).setObjects(("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtIfAdminStatus"), ("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtIfIfOperStatus"), ("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtIfStubInterface"), ("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtIfP2PNoHellos"), ("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtIfHelloInterval"), ("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtIfHelloHoldtime"), ("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtIfReportInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDvmrpExtIfGroup = etsysDvmrpExtIfGroup.setStatus('current')
etsysDvmrpExtTibMgrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 2, 1, 2)).setObjects(("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtTibMgrIndex"), ("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtTibMgrKeepalivePeriod"), ("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtTibMgrMetric"), ("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtTibMgrSGStateLimit"), ("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtTibMgrSGStateWarnThold"), ("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtTibMgrSGStateStored"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDvmrpExtTibMgrGroup = etsysDvmrpExtTibMgrGroup.setStatus('current')
etsysDvmrpExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 69, 2, 2, 1)).setObjects(("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtIfGroup"), ("ENTERASYS-DVMRP-EXT-MIB", "etsysDvmrpExtTibMgrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDvmrpExtCompliance = etsysDvmrpExtCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-DVMRP-EXT-MIB", etsysDvmrpExtMIB=etsysDvmrpExtMIB, etsysDvmrpExtGlobals=etsysDvmrpExtGlobals, etsysDvmrpExtIfHelloInterval=etsysDvmrpExtIfHelloInterval, etsysDvmrpExtConformance=etsysDvmrpExtConformance, etsysDvmrpExtTibMgrSGStateLimit=etsysDvmrpExtTibMgrSGStateLimit, etsysDvmrpExtCompliances=etsysDvmrpExtCompliances, etsysDvmrpExtIfIfOperStatus=etsysDvmrpExtIfIfOperStatus, etsysDvmrpExtIfReportInterval=etsysDvmrpExtIfReportInterval, etsysDvmrpExtTibMgrGroup=etsysDvmrpExtTibMgrGroup, PYSNMP_MODULE_ID=etsysDvmrpExtMIB, etsysDvmrpExtIfHelloHoldtime=etsysDvmrpExtIfHelloHoldtime, etsysDvmrpExtIfStubInterface=etsysDvmrpExtIfStubInterface, etsysDvmrpExtIfGroup=etsysDvmrpExtIfGroup, etsysDvmrpExtObjects=etsysDvmrpExtObjects, etsysDvmrpExtIfEntry=etsysDvmrpExtIfEntry, etsysDvmrpExtIfAdminStatus=etsysDvmrpExtIfAdminStatus, etsysDvmrpExtIfP2PNoHellos=etsysDvmrpExtIfP2PNoHellos, etsysDvmrpExtTables=etsysDvmrpExtTables, etsysDvmrpExtGroups=etsysDvmrpExtGroups, etsysDvmrpExtTibMgrKeepalivePeriod=etsysDvmrpExtTibMgrKeepalivePeriod, etsysDvmrpExtTibMgrTable=etsysDvmrpExtTibMgrTable, etsysDvmrpExtTibMgrMetric=etsysDvmrpExtTibMgrMetric, etsysDvmrpExtTibMgrIndex=etsysDvmrpExtTibMgrIndex, etsysDvmrpExtTibMgrSGStateStored=etsysDvmrpExtTibMgrSGStateStored, etsysDvmrpExtTibMgrSGStateWarnThold=etsysDvmrpExtTibMgrSGStateWarnThold, etsysDvmrpExtTibMgrEntry=etsysDvmrpExtTibMgrEntry, etsysDvmrpExtCompliance=etsysDvmrpExtCompliance, etsysDvmrpExtIfTable=etsysDvmrpExtIfTable)
