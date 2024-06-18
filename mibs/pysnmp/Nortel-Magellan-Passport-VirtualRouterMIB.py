#
# PySNMP MIB module Nortel-Magellan-Passport-VirtualRouterMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-VirtualRouterMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:17:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
Unsigned32, RowPointer, InterfaceIndex, DisplayString, RowStatus, Integer32, Counter32, Gauge32, StorageType = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "Unsigned32", "RowPointer", "InterfaceIndex", "DisplayString", "RowStatus", "Integer32", "Counter32", "Gauge32", "StorageType")
Link, NonReplicated, HexString, IntegerSequence, AsciiStringIndex, AsciiString = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "Link", "NonReplicated", "HexString", "IntegerSequence", "AsciiStringIndex", "AsciiString")
passportMIBs, components = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs", "components")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Unsigned32, ModuleIdentity, iso, MibIdentifier, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, ObjectIdentity, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Unsigned32", "ModuleIdentity", "iso", "MibIdentifier", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "ObjectIdentity", "TimeTicks", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
virtualRouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26))
vr = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100))
vrRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 1), )
if mibBuilder.loadTexts: vrRowStatusTable.setStatus('mandatory')
vrRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"))
if mibBuilder.loadTexts: vrRowStatusEntry.setStatus('mandatory')
vrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrRowStatus.setStatus('mandatory')
vrComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrComponentName.setStatus('mandatory')
vrStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrStorageType.setStatus('mandatory')
vrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 8)))
if mibBuilder.loadTexts: vrIndex.setStatus('mandatory')
vrAdminContorlTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 100), )
if mibBuilder.loadTexts: vrAdminContorlTable.setStatus('mandatory')
vrAdminContorlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 100, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"))
if mibBuilder.loadTexts: vrAdminContorlEntry.setStatus('mandatory')
vrSnmpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 100, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrSnmpAdminStatus.setStatus('mandatory')
vrManagementAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 100, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrManagementAccess.setStatus('mandatory')
vrVirtualPrivateIntranetIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 100, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrVirtualPrivateIntranetIdentifier.setStatus('mandatory')
vrCidDataTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 101), )
if mibBuilder.loadTexts: vrCidDataTable.setStatus('mandatory')
vrCidDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 101, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"))
if mibBuilder.loadTexts: vrCidDataEntry.setStatus('mandatory')
vrCustomerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 101, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrCustomerIdentifier.setStatus('mandatory')
vrOperStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 103), )
if mibBuilder.loadTexts: vrOperStatusTable.setStatus('mandatory')
vrOperStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 103, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"))
if mibBuilder.loadTexts: vrOperStatusEntry.setStatus('mandatory')
vrSnmpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 103, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrSnmpOperStatus.setStatus('mandatory')
vrStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 104), )
if mibBuilder.loadTexts: vrStateTable.setStatus('mandatory')
vrStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 104, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"))
if mibBuilder.loadTexts: vrStateEntry.setStatus('mandatory')
vrAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 104, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrAdminState.setStatus('mandatory')
vrOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 104, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrOperationalState.setStatus('mandatory')
vrUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 104, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrUsageState.setStatus('mandatory')
vrIfNumberOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 105), )
if mibBuilder.loadTexts: vrIfNumberOperTable.setStatus('mandatory')
vrIfNumberOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 105, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"))
if mibBuilder.loadTexts: vrIfNumberOperEntry.setStatus('mandatory')
vrIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 105, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfNumber.setStatus('mandatory')
vrMm = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2))
vrMmRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 1), )
if mibBuilder.loadTexts: vrMmRowStatusTable.setStatus('mandatory')
vrMmRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrMmIndex"))
if mibBuilder.loadTexts: vrMmRowStatusEntry.setStatus('mandatory')
vrMmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrMmRowStatus.setStatus('mandatory')
vrMmComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrMmComponentName.setStatus('mandatory')
vrMmStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrMmStorageType.setStatus('mandatory')
vrMmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: vrMmIndex.setStatus('mandatory')
vrMmProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10), )
if mibBuilder.loadTexts: vrMmProvTable.setStatus('mandatory')
vrMmProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrMmIndex"))
if mibBuilder.loadTexts: vrMmProvEntry.setStatus('mandatory')
vrMmVrMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrMmVrMaxHeapSpace.setStatus('mandatory')
vrMmIpMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrMmIpMaxHeapSpace.setStatus('mandatory')
vrMmIpxMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrMmIpxMaxHeapSpace.setStatus('mandatory')
vrMmBridgingMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrMmBridgingMaxHeapSpace.setStatus('mandatory')
vrMmNetSentryMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrMmNetSentryMaxHeapSpace.setStatus('mandatory')
vrMmSresMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrMmSresMaxHeapSpace.setStatus('mandatory')
vrMmSnaMaxHeapSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 10, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrMmSnaMaxHeapSpace.setStatus('mandatory')
vrMmOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11), )
if mibBuilder.loadTexts: vrMmOperTable.setStatus('mandatory')
vrMmOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrMmIndex"))
if mibBuilder.loadTexts: vrMmOperEntry.setStatus('mandatory')
vrMmVrHeapSpaceBytesAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrMmVrHeapSpaceBytesAllocated.setStatus('mandatory')
vrMmVrHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrMmVrHeapSpaceAllocated.setStatus('mandatory')
vrMmIpHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrMmIpHeapSpaceAllocated.setStatus('mandatory')
vrMmIpxHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrMmIpxHeapSpaceAllocated.setStatus('mandatory')
vrMmBridgingHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrMmBridgingHeapSpaceAllocated.setStatus('mandatory')
vrMmNetSentryHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrMmNetSentryHeapSpaceAllocated.setStatus('mandatory')
vrMmSresHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrMmSresHeapSpaceAllocated.setStatus('mandatory')
vrMmSnaHeapSpaceAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 2, 11, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrMmSnaHeapSpaceAllocated.setStatus('mandatory')
vrPp = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3))
vrPpRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 1), )
if mibBuilder.loadTexts: vrPpRowStatusTable.setStatus('mandatory')
vrPpRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"))
if mibBuilder.loadTexts: vrPpRowStatusEntry.setStatus('mandatory')
vrPpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrPpRowStatus.setStatus('mandatory')
vrPpComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrPpComponentName.setStatus('mandatory')
vrPpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrPpStorageType.setStatus('mandatory')
vrPpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 20)))
if mibBuilder.loadTexts: vrPpIndex.setStatus('mandatory')
vrPpAdminControlTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 100), )
if mibBuilder.loadTexts: vrPpAdminControlTable.setStatus('mandatory')
vrPpAdminControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 100, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"))
if mibBuilder.loadTexts: vrPpAdminControlEntry.setStatus('mandatory')
vrPpSnmpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 100, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrPpSnmpAdminStatus.setStatus('mandatory')
vrPpProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 101), )
if mibBuilder.loadTexts: vrPpProvTable.setStatus('mandatory')
vrPpProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 101, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"))
if mibBuilder.loadTexts: vrPpProvEntry.setStatus('mandatory')
vrPpLinkToMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 101, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrPpLinkToMedia.setStatus('mandatory')
vrPpOperStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 102), )
if mibBuilder.loadTexts: vrPpOperStatusTable.setStatus('mandatory')
vrPpOperStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 102, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"))
if mibBuilder.loadTexts: vrPpOperStatusEntry.setStatus('mandatory')
vrPpSnmpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 102, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrPpSnmpOperStatus.setStatus('mandatory')
vrPpStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 103), )
if mibBuilder.loadTexts: vrPpStateTable.setStatus('mandatory')
vrPpStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 103, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"))
if mibBuilder.loadTexts: vrPpStateEntry.setStatus('mandatory')
vrPpAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 103, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrPpAdminState.setStatus('mandatory')
vrPpOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 103, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrPpOperationalState.setStatus('mandatory')
vrPpUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 103, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrPpUsageState.setStatus('mandatory')
vrPpOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 104), )
if mibBuilder.loadTexts: vrPpOperTable.setStatus('mandatory')
vrPpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 104, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"))
if mibBuilder.loadTexts: vrPpOperEntry.setStatus('mandatory')
vrPpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 104, 1, 1), InterfaceIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrPpIfIndex.setStatus('mandatory')
vrPpNbmaAddressTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 105), )
if mibBuilder.loadTexts: vrPpNbmaAddressTable.setStatus('mandatory')
vrPpNbmaAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 105, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"))
if mibBuilder.loadTexts: vrPpNbmaAddressEntry.setStatus('mandatory')
vrPpAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 105, 1, 1), HexString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrPpAtmAddress.setStatus('mandatory')
vrIfTableEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10))
vrIfTableEntryRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 1), )
if mibBuilder.loadTexts: vrIfTableEntryRowStatusTable.setStatus('mandatory')
vrIfTableEntryRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIfTableEntryIndex"))
if mibBuilder.loadTexts: vrIfTableEntryRowStatusEntry.setStatus('mandatory')
vrIfTableEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryRowStatus.setStatus('mandatory')
vrIfTableEntryComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryComponentName.setStatus('mandatory')
vrIfTableEntryStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryStorageType.setStatus('mandatory')
vrIfTableEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: vrIfTableEntryIndex.setStatus('mandatory')
vrIfTableEntryIftTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10), )
if mibBuilder.loadTexts: vrIfTableEntryIftTable.setStatus('mandatory')
vrIfTableEntryIftEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIfTableEntryIndex"))
if mibBuilder.loadTexts: vrIfTableEntryIftEntry.setStatus('mandatory')
vrIfTableEntryIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfAdminStatus.setStatus('mandatory')
vrIfTableEntryIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfOperStatus.setStatus('mandatory')
vrIfTableEntryIfLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfLastChange.setStatus('mandatory')
vrIfTableEntryIfInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfInOctets.setStatus('mandatory')
vrIfTableEntryIfOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfOutOctets.setStatus('mandatory')
vrIfTableEntryIfInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfInDiscards.setStatus('mandatory')
vrIfTableEntryIfOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfOutDiscards.setStatus('mandatory')
vrIfTableEntryIfInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfInErrors.setStatus('mandatory')
vrIfTableEntryIfOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfOutErrors.setStatus('mandatory')
vrIfTableEntryIfInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfInUcastPkts.setStatus('mandatory')
vrIfTableEntryIfOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfOutUcastPkts.setStatus('mandatory')
vrIfTableEntryIfInNuCastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfInNuCastPkts.setStatus('mandatory')
vrIfTableEntryIfOutNuCastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfOutNuCastPkts.setStatus('mandatory')
vrIfTableEntryIfInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfInUnknownProtos.setStatus('mandatory')
vrIfTableEntryIfOutQlength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 16), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfOutQlength.setStatus('mandatory')
vrIfTableEntryIfDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 17), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfDescription.setStatus('mandatory')
vrIfTableEntryIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 30, 31, 32, 44, 45, 46, 59, 60, 64, 1039, 1040, 1041, 1042, 1043))).clone(namedValues=NamedValues(("other", 1), ("ddnX25", 4), ("rfc877x25", 5), ("ethernetCsmacd", 6), ("ethernet8023", 7), ("tokenBus8024", 8), ("tokenring8025", 9), ("man802", 10), ("starLan", 11), ("hyperChannel", 14), ("fddi", 15), ("lapb", 16), ("sdlc", 17), ("ds1", 18), ("e1", 19), ("basicIsdn", 20), ("primaryIsdn", 21), ("propPointToPointSerial", 22), ("ppp", 23), ("ds3", 30), ("smds", 31), ("frameRelay", 32), ("frameRelayService", 44), ("v35", 45), ("hssi", 46), ("aflane8023", 59), ("aflane8025", 60), ("v11", 64), ("atmMpeVcEncap", 1039), ("atmMpeLlcEncap", 1040), ("ilsForwarder", 1041), ("ipTunnel", 1042), ("virtualMedia", 1043)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfType.setStatus('mandatory')
vrIfTableEntryIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfMtu.setStatus('mandatory')
vrIfTableEntryIfSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfSpeed.setStatus('mandatory')
vrIfTableEntryIfPhysicalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 21), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfPhysicalAddress.setStatus('mandatory')
vrIfTableEntryIfSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 10, 1, 22), IntegerSequence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryIfSpecific.setStatus('mandatory')
vrIfTableEntryAdditionalInfoTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 11), )
if mibBuilder.loadTexts: vrIfTableEntryAdditionalInfoTable.setStatus('mandatory')
vrIfTableEntryAdditionalInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIfTableEntryIndex"))
if mibBuilder.loadTexts: vrIfTableEntryAdditionalInfoEntry.setStatus('mandatory')
vrIfTableEntryStdComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 10, 11, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrIfTableEntryStdComponentName.setStatus('mandatory')
vrQosP = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15))
vrQosPRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 1), )
if mibBuilder.loadTexts: vrQosPRowStatusTable.setStatus('mandatory')
vrQosPRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrQosPIndex"))
if mibBuilder.loadTexts: vrQosPRowStatusEntry.setStatus('mandatory')
vrQosPRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrQosPRowStatus.setStatus('mandatory')
vrQosPComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrQosPComponentName.setStatus('mandatory')
vrQosPStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrQosPStorageType.setStatus('mandatory')
vrQosPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3)))
if mibBuilder.loadTexts: vrQosPIndex.setStatus('mandatory')
vrQosPProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 10), )
if mibBuilder.loadTexts: vrQosPProvTable.setStatus('mandatory')
vrQosPProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"), (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrQosPIndex"))
if mibBuilder.loadTexts: vrQosPProvEntry.setStatus('mandatory')
vrQosPVnsDiscardPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrQosPVnsDiscardPriority.setStatus('mandatory')
vrQosPVnsEmissionPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrQosPVnsEmissionPriority.setStatus('mandatory')
vrQosPWanEmissionPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 15, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vrQosPWanEmissionPriority.setStatus('obsolete')
virtualRouterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 1))
virtualRouterGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 1, 5))
virtualRouterGroupBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 1, 5, 2))
virtualRouterGroupBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 1, 5, 2, 2))
virtualRouterCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 3))
virtualRouterCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 3, 5))
virtualRouterCapabilitiesBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 3, 5, 2))
virtualRouterCapabilitiesBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 26, 3, 5, 2, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-VirtualRouterMIB", virtualRouterGroupBE01=virtualRouterGroupBE01, vrVirtualPrivateIntranetIdentifier=vrVirtualPrivateIntranetIdentifier, virtualRouterCapabilitiesBE01=virtualRouterCapabilitiesBE01, vrIfTableEntryStdComponentName=vrIfTableEntryStdComponentName, vrMmOperEntry=vrMmOperEntry, vrPpOperStatusEntry=vrPpOperStatusEntry, vrIfTableEntryIftTable=vrIfTableEntryIftTable, vrIfTableEntryIfOperStatus=vrIfTableEntryIfOperStatus, vrPpSnmpOperStatus=vrPpSnmpOperStatus, vrIfTableEntry=vrIfTableEntry, vrRowStatusTable=vrRowStatusTable, vrMmSnaMaxHeapSpace=vrMmSnaMaxHeapSpace, vrIfTableEntryIfOutDiscards=vrIfTableEntryIfOutDiscards, vrIfTableEntryIfInOctets=vrIfTableEntryIfInOctets, vrUsageState=vrUsageState, vrPpOperStatusTable=vrPpOperStatusTable, virtualRouterGroupBE=virtualRouterGroupBE, vrQosPWanEmissionPriority=vrQosPWanEmissionPriority, vrPpProvTable=vrPpProvTable, vrPpRowStatusTable=vrPpRowStatusTable, vrIfTableEntryIfOutQlength=vrIfTableEntryIfOutQlength, vrMmStorageType=vrMmStorageType, vrQosP=vrQosP, vrMmIpHeapSpaceAllocated=vrMmIpHeapSpaceAllocated, vrPpStorageType=vrPpStorageType, vrMmOperTable=vrMmOperTable, vrPpNbmaAddressTable=vrPpNbmaAddressTable, vrMmRowStatus=vrMmRowStatus, vrSnmpAdminStatus=vrSnmpAdminStatus, vrPpUsageState=vrPpUsageState, vrQosPRowStatus=vrQosPRowStatus, virtualRouterCapabilitiesBE01A=virtualRouterCapabilitiesBE01A, vrMmSnaHeapSpaceAllocated=vrMmSnaHeapSpaceAllocated, vrQosPStorageType=vrQosPStorageType, vrPpProvEntry=vrPpProvEntry, vrPpIndex=vrPpIndex, vrIfTableEntryIfInUcastPkts=vrIfTableEntryIfInUcastPkts, virtualRouterGroup=virtualRouterGroup, vrCidDataEntry=vrCidDataEntry, vrMmSresMaxHeapSpace=vrMmSresMaxHeapSpace, vrPpOperEntry=vrPpOperEntry, vrIfTableEntryIfType=vrIfTableEntryIfType, vrStorageType=vrStorageType, vrMmVrHeapSpaceBytesAllocated=vrMmVrHeapSpaceBytesAllocated, vrMmIndex=vrMmIndex, vrQosPIndex=vrQosPIndex, vrQosPProvEntry=vrQosPProvEntry, vrOperationalState=vrOperationalState, vrIfTableEntryIfSpeed=vrIfTableEntryIfSpeed, vrMmVrHeapSpaceAllocated=vrMmVrHeapSpaceAllocated, vrMmIpMaxHeapSpace=vrMmIpMaxHeapSpace, vrIfTableEntryIfInDiscards=vrIfTableEntryIfInDiscards, vrPpAdminControlTable=vrPpAdminControlTable, vrIfTableEntryIfMtu=vrIfTableEntryIfMtu, vrIfNumberOperEntry=vrIfNumberOperEntry, vrPpRowStatusEntry=vrPpRowStatusEntry, vrIndex=vrIndex, vrAdminState=vrAdminState, virtualRouterGroupBE01A=virtualRouterGroupBE01A, vrPpNbmaAddressEntry=vrPpNbmaAddressEntry, vrIfTableEntryAdditionalInfoTable=vrIfTableEntryAdditionalInfoTable, vrMmComponentName=vrMmComponentName, vrMmRowStatusEntry=vrMmRowStatusEntry, vrMmNetSentryMaxHeapSpace=vrMmNetSentryMaxHeapSpace, vrIfTableEntryRowStatusTable=vrIfTableEntryRowStatusTable, vrIfTableEntryIfOutErrors=vrIfTableEntryIfOutErrors, vrIfTableEntryStorageType=vrIfTableEntryStorageType, vrStateTable=vrStateTable, vrIfTableEntryComponentName=vrIfTableEntryComponentName, vrIfTableEntryIfInNuCastPkts=vrIfTableEntryIfInNuCastPkts, vrPpLinkToMedia=vrPpLinkToMedia, vrManagementAccess=vrManagementAccess, vrAdminContorlEntry=vrAdminContorlEntry, vrPpStateEntry=vrPpStateEntry, vrCidDataTable=vrCidDataTable, vrPpComponentName=vrPpComponentName, vrIfTableEntryIfInErrors=vrIfTableEntryIfInErrors, vrIfNumber=vrIfNumber, vrQosPRowStatusTable=vrQosPRowStatusTable, vrIfTableEntryRowStatusEntry=vrIfTableEntryRowStatusEntry, vrMmIpxMaxHeapSpace=vrMmIpxMaxHeapSpace, vrOperStatusEntry=vrOperStatusEntry, vrMmProvTable=vrMmProvTable, vrPpOperationalState=vrPpOperationalState, virtualRouterCapabilities=virtualRouterCapabilities, vrIfTableEntryIfAdminStatus=vrIfTableEntryIfAdminStatus, vrPp=vrPp, vrRowStatus=vrRowStatus, vrRowStatusEntry=vrRowStatusEntry, vrIfNumberOperTable=vrIfNumberOperTable, vrSnmpOperStatus=vrSnmpOperStatus, vrQosPVnsDiscardPriority=vrQosPVnsDiscardPriority, vrPpStateTable=vrPpStateTable, vrPpIfIndex=vrPpIfIndex, vrOperStatusTable=vrOperStatusTable, vrIfTableEntryIfInUnknownProtos=vrIfTableEntryIfInUnknownProtos, vrMmVrMaxHeapSpace=vrMmVrMaxHeapSpace, vrIfTableEntryIfDescription=vrIfTableEntryIfDescription, vrIfTableEntryIfOutNuCastPkts=vrIfTableEntryIfOutNuCastPkts, vrCustomerIdentifier=vrCustomerIdentifier, vrMmProvEntry=vrMmProvEntry, vr=vr, vrQosPVnsEmissionPriority=vrQosPVnsEmissionPriority, vrMmIpxHeapSpaceAllocated=vrMmIpxHeapSpaceAllocated, vrIfTableEntryIfOutUcastPkts=vrIfTableEntryIfOutUcastPkts, vrQosPProvTable=vrQosPProvTable, vrIfTableEntryIfLastChange=vrIfTableEntryIfLastChange, vrMm=vrMm, vrIfTableEntryAdditionalInfoEntry=vrIfTableEntryAdditionalInfoEntry, virtualRouterMIB=virtualRouterMIB, vrIfTableEntryIfPhysicalAddress=vrIfTableEntryIfPhysicalAddress, vrMmBridgingHeapSpaceAllocated=vrMmBridgingHeapSpaceAllocated, vrPpAdminState=vrPpAdminState, vrMmRowStatusTable=vrMmRowStatusTable, vrMmSresHeapSpaceAllocated=vrMmSresHeapSpaceAllocated, vrStateEntry=vrStateEntry, vrQosPComponentName=vrQosPComponentName, vrIfTableEntryIfSpecific=vrIfTableEntryIfSpecific, vrIfTableEntryIfOutOctets=vrIfTableEntryIfOutOctets, vrPpAtmAddress=vrPpAtmAddress, vrIfTableEntryRowStatus=vrIfTableEntryRowStatus, virtualRouterCapabilitiesBE=virtualRouterCapabilitiesBE, vrIfTableEntryIndex=vrIfTableEntryIndex, vrIfTableEntryIftEntry=vrIfTableEntryIftEntry, vrQosPRowStatusEntry=vrQosPRowStatusEntry, vrMmNetSentryHeapSpaceAllocated=vrMmNetSentryHeapSpaceAllocated, vrAdminContorlTable=vrAdminContorlTable, vrMmBridgingMaxHeapSpace=vrMmBridgingMaxHeapSpace, vrPpOperTable=vrPpOperTable, vrPpRowStatus=vrPpRowStatus, vrPpAdminControlEntry=vrPpAdminControlEntry, vrPpSnmpAdminStatus=vrPpSnmpAdminStatus, vrComponentName=vrComponentName)
