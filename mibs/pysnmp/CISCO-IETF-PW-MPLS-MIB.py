#
# PySNMP MIB module CISCO-IETF-PW-MPLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PW-MPLS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
cpwVcIndex, = mibBuilder.importSymbols("CISCO-IETF-PW-MIB", "cpwVcIndex")
CpwVcIndexType, = mibBuilder.importSymbols("CISCO-IETF-PW-TC-MIB", "CpwVcIndexType")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
MplsTunnelInstanceIndex, MplsLdpIdentifier, MplsLsrIdentifier, MplsTunnelIndex = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsTunnelInstanceIndex", "MplsLdpIdentifier", "MplsLsrIdentifier", "MplsTunnelIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, ModuleIdentity, TimeTicks, Unsigned32, Counter64, NotificationType, Gauge32, IpAddress, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "TimeTicks", "Unsigned32", "Counter64", "NotificationType", "Gauge32", "IpAddress", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "ObjectIdentity")
RowStatus, DisplayString, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "StorageType", "TextualConvention")
cpwVcMplsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 107))
cpwVcMplsMIB.setRevisions(('2003-02-26 12:00', '2002-06-02 12:00', '2002-01-29 12:00', '2001-07-11 12:00', '2001-07-11 12:00',))
if mibBuilder.loadTexts: cpwVcMplsMIB.setLastUpdated('200302261200Z')
if mibBuilder.loadTexts: cpwVcMplsMIB.setOrganization('Cisco Systems, Inc.')
cpwVcMplsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 107, 0))
cpwVcMplsNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 107, 0, 0))
cpwVcMplsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 107, 1))
cpwVcMplsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 107, 2))
cpwVcMplsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1), )
if mibBuilder.loadTexts: cpwVcMplsTable.setStatus('current')
cpwVcMplsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1), ).setIndexNames((0, "CISCO-IETF-PW-MIB", "cpwVcIndex"))
if mibBuilder.loadTexts: cpwVcMplsEntry.setStatus('current')
cpwVcMplsMplsType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("mplsTe", 0), ("mplsNonTe", 1), ("vcOnly", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpwVcMplsMplsType.setStatus('current')
cpwVcMplsExpBitsMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("outerTunnel", 1), ("specifiedValue", 2), ("serviceDependant", 3))).clone('outerTunnel')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpwVcMplsExpBitsMode.setStatus('current')
cpwVcMplsExpBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpwVcMplsExpBits.setStatus('current')
cpwVcMplsTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpwVcMplsTtl.setStatus('current')
cpwVcMplsLocalLdpID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 5), MplsLdpIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpwVcMplsLocalLdpID.setStatus('current')
cpwVcMplsLocalLdpEntityID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpwVcMplsLocalLdpEntityID.setStatus('current')
cpwVcMplsPeerLdpID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 7), MplsLdpIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwVcMplsPeerLdpID.setStatus('current')
cpwVcMplsStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 1, 1, 8), StorageType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpwVcMplsStorageType.setStatus('current')
cpwVcMplsOutboundIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwVcMplsOutboundIndexNext.setStatus('current')
cpwVcMplsOutboundTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3), )
if mibBuilder.loadTexts: cpwVcMplsOutboundTable.setStatus('current')
cpwVcMplsOutboundEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1), ).setIndexNames((0, "CISCO-IETF-PW-MIB", "cpwVcIndex"), (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundIndex"))
if mibBuilder.loadTexts: cpwVcMplsOutboundEntry.setStatus('current')
cpwVcMplsOutboundIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: cpwVcMplsOutboundIndex.setStatus('current')
cpwVcMplsOutboundLsrXcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsOutboundLsrXcIndex.setStatus('current')
cpwVcMplsOutboundTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 3), MplsTunnelIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsOutboundTunnelIndex.setStatus('current')
cpwVcMplsOutboundTunnelInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 4), MplsTunnelInstanceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsOutboundTunnelInstance.setStatus('current')
cpwVcMplsOutboundTunnelLclLSR = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 5), MplsLsrIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsOutboundTunnelLclLSR.setStatus('current')
cpwVcMplsOutboundTunnelPeerLSR = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 6), MplsLsrIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsOutboundTunnelPeerLSR.setStatus('current')
cpwVcMplsOutboundIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsOutboundIfIndex.setStatus('current')
cpwVcMplsOutboundRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsOutboundRowStatus.setStatus('current')
cpwVcMplsOutboundStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 3, 1, 9), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsOutboundStorageType.setStatus('current')
cpwVcMplsInboundIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwVcMplsInboundIndexNext.setStatus('current')
cpwVcMplsInboundTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5), )
if mibBuilder.loadTexts: cpwVcMplsInboundTable.setStatus('current')
cpwVcMplsInboundEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1), ).setIndexNames((0, "CISCO-IETF-PW-MIB", "cpwVcIndex"), (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundIndex"))
if mibBuilder.loadTexts: cpwVcMplsInboundEntry.setStatus('current')
cpwVcMplsInboundIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: cpwVcMplsInboundIndex.setStatus('current')
cpwVcMplsInboundLsrXcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsInboundLsrXcIndex.setStatus('current')
cpwVcMplsInboundTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 3), MplsTunnelIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsInboundTunnelIndex.setStatus('current')
cpwVcMplsInboundTunnelInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 4), MplsTunnelInstanceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsInboundTunnelInstance.setStatus('current')
cpwVcMplsInboundTunnelLclLSR = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 5), MplsLsrIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsInboundTunnelLclLSR.setStatus('current')
cpwVcMplsInboundTunnelPeerLSR = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 6), MplsLsrIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsInboundTunnelPeerLSR.setStatus('current')
cpwVcMplsInboundIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsInboundIfIndex.setStatus('current')
cpwVcMplsInboundRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsInboundRowStatus.setStatus('current')
cpwVcMplsInboundStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 5, 1, 9), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcMplsInboundStorageType.setStatus('current')
cpwVcMplsNonTeMappingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 6), )
if mibBuilder.loadTexts: cpwVcMplsNonTeMappingTable.setStatus('current')
cpwVcMplsNonTeMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 6, 1), ).setIndexNames((0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsNonTeMappingTunnelDirection"), (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsNonTeMappingXcTunnelIndex"), (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsNonTeMappingIfIndex"), (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsNonTeMappingVcIndex"))
if mibBuilder.loadTexts: cpwVcMplsNonTeMappingEntry.setStatus('current')
cpwVcMplsNonTeMappingTunnelDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("outbound", 1), ("inbound", 2))))
if mibBuilder.loadTexts: cpwVcMplsNonTeMappingTunnelDirection.setStatus('current')
cpwVcMplsNonTeMappingXcTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 6, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: cpwVcMplsNonTeMappingXcTunnelIndex.setStatus('current')
cpwVcMplsNonTeMappingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 6, 1, 3), InterfaceIndexOrZero())
if mibBuilder.loadTexts: cpwVcMplsNonTeMappingIfIndex.setStatus('current')
cpwVcMplsNonTeMappingVcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 6, 1, 4), CpwVcIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwVcMplsNonTeMappingVcIndex.setStatus('current')
cpwVcMplsTeMappingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7), )
if mibBuilder.loadTexts: cpwVcMplsTeMappingTable.setStatus('current')
cpwVcMplsTeMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1), ).setIndexNames((0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingTunnelDirection"), (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingTunnelIndex"), (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingTunnelInstance"), (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingTunnelPeerLsrID"), (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingTunnelLocalLsrID"), (0, "CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingVcIndex"))
if mibBuilder.loadTexts: cpwVcMplsTeMappingEntry.setStatus('current')
cpwVcMplsTeMappingTunnelDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("outbound", 1), ("inbound", 2))))
if mibBuilder.loadTexts: cpwVcMplsTeMappingTunnelDirection.setStatus('current')
cpwVcMplsTeMappingTunnelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1, 2), MplsTunnelIndex())
if mibBuilder.loadTexts: cpwVcMplsTeMappingTunnelIndex.setStatus('current')
cpwVcMplsTeMappingTunnelInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1, 3), MplsTunnelInstanceIndex())
if mibBuilder.loadTexts: cpwVcMplsTeMappingTunnelInstance.setStatus('current')
cpwVcMplsTeMappingTunnelPeerLsrID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1, 4), MplsLsrIdentifier())
if mibBuilder.loadTexts: cpwVcMplsTeMappingTunnelPeerLsrID.setStatus('current')
cpwVcMplsTeMappingTunnelLocalLsrID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1, 5), MplsLsrIdentifier())
if mibBuilder.loadTexts: cpwVcMplsTeMappingTunnelLocalLsrID.setStatus('current')
cpwVcMplsTeMappingVcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 107, 1, 7, 1, 6), CpwVcIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwVcMplsTeMappingVcIndex.setStatus('current')
cpwVcMplsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 1))
cpwVcMplsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 2))
cpwMplsModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 2, 1)).setObjects(("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsGroup"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundGroup"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsMappingGroup"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwMplsModuleCompliance = cpwMplsModuleCompliance.setStatus('current')
cpwVcMplsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 1, 1)).setObjects(("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsMplsType"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsExpBitsMode"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsExpBits"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTtl"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsLocalLdpID"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsLocalLdpEntityID"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsPeerLdpID"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcMplsGroup = cpwVcMplsGroup.setStatus('current')
cpwVcMplsOutboundGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 1, 2)).setObjects(("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundIndexNext"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundLsrXcIndex"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundTunnelIndex"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundTunnelInstance"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundTunnelLclLSR"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundTunnelPeerLSR"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundIfIndex"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundRowStatus"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsOutboundStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcMplsOutboundGroup = cpwVcMplsOutboundGroup.setStatus('current')
cpwVcMplsInboundGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 1, 3)).setObjects(("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundIndexNext"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundLsrXcIndex"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundTunnelIndex"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundTunnelInstance"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundTunnelLclLSR"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundTunnelPeerLSR"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundIfIndex"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundRowStatus"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsInboundStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcMplsInboundGroup = cpwVcMplsInboundGroup.setStatus('current')
cpwVcMplsMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 107, 2, 1, 4)).setObjects(("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsNonTeMappingVcIndex"), ("CISCO-IETF-PW-MPLS-MIB", "cpwVcMplsTeMappingVcIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcMplsMappingGroup = cpwVcMplsMappingGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-PW-MPLS-MIB", cpwVcMplsInboundTunnelIndex=cpwVcMplsInboundTunnelIndex, cpwVcMplsOutboundIfIndex=cpwVcMplsOutboundIfIndex, cpwVcMplsOutboundIndexNext=cpwVcMplsOutboundIndexNext, cpwVcMplsOutboundGroup=cpwVcMplsOutboundGroup, cpwVcMplsTeMappingTunnelIndex=cpwVcMplsTeMappingTunnelIndex, cpwVcMplsStorageType=cpwVcMplsStorageType, cpwVcMplsNotifications=cpwVcMplsNotifications, cpwVcMplsTeMappingTunnelInstance=cpwVcMplsTeMappingTunnelInstance, cpwVcMplsOutboundLsrXcIndex=cpwVcMplsOutboundLsrXcIndex, cpwVcMplsGroups=cpwVcMplsGroups, cpwVcMplsInboundRowStatus=cpwVcMplsInboundRowStatus, cpwVcMplsOutboundIndex=cpwVcMplsOutboundIndex, cpwVcMplsInboundTunnelLclLSR=cpwVcMplsInboundTunnelLclLSR, cpwVcMplsTeMappingTunnelLocalLsrID=cpwVcMplsTeMappingTunnelLocalLsrID, cpwMplsModuleCompliance=cpwMplsModuleCompliance, cpwVcMplsTeMappingTunnelPeerLsrID=cpwVcMplsTeMappingTunnelPeerLsrID, cpwVcMplsEntry=cpwVcMplsEntry, cpwVcMplsOutboundTable=cpwVcMplsOutboundTable, cpwVcMplsOutboundTunnelIndex=cpwVcMplsOutboundTunnelIndex, cpwVcMplsNonTeMappingTable=cpwVcMplsNonTeMappingTable, cpwVcMplsExpBits=cpwVcMplsExpBits, PYSNMP_MODULE_ID=cpwVcMplsMIB, cpwVcMplsNonTeMappingTunnelDirection=cpwVcMplsNonTeMappingTunnelDirection, cpwVcMplsMplsType=cpwVcMplsMplsType, cpwVcMplsOutboundEntry=cpwVcMplsOutboundEntry, cpwVcMplsTeMappingTunnelDirection=cpwVcMplsTeMappingTunnelDirection, cpwVcMplsOutboundTunnelLclLSR=cpwVcMplsOutboundTunnelLclLSR, cpwVcMplsObjects=cpwVcMplsObjects, cpwVcMplsLocalLdpID=cpwVcMplsLocalLdpID, cpwVcMplsTable=cpwVcMplsTable, cpwVcMplsInboundTunnelInstance=cpwVcMplsInboundTunnelInstance, cpwVcMplsInboundIfIndex=cpwVcMplsInboundIfIndex, cpwVcMplsTeMappingTable=cpwVcMplsTeMappingTable, cpwVcMplsConformance=cpwVcMplsConformance, cpwVcMplsTtl=cpwVcMplsTtl, cpwVcMplsInboundIndexNext=cpwVcMplsInboundIndexNext, cpwVcMplsInboundTunnelPeerLSR=cpwVcMplsInboundTunnelPeerLSR, cpwVcMplsInboundGroup=cpwVcMplsInboundGroup, cpwVcMplsLocalLdpEntityID=cpwVcMplsLocalLdpEntityID, cpwVcMplsInboundTable=cpwVcMplsInboundTable, cpwVcMplsInboundStorageType=cpwVcMplsInboundStorageType, cpwVcMplsTeMappingEntry=cpwVcMplsTeMappingEntry, cpwVcMplsGroup=cpwVcMplsGroup, cpwVcMplsNotifyPrefix=cpwVcMplsNotifyPrefix, cpwVcMplsNonTeMappingEntry=cpwVcMplsNonTeMappingEntry, cpwVcMplsTeMappingVcIndex=cpwVcMplsTeMappingVcIndex, cpwVcMplsMappingGroup=cpwVcMplsMappingGroup, cpwVcMplsInboundLsrXcIndex=cpwVcMplsInboundLsrXcIndex, cpwVcMplsCompliances=cpwVcMplsCompliances, cpwVcMplsOutboundTunnelInstance=cpwVcMplsOutboundTunnelInstance, cpwVcMplsOutboundStorageType=cpwVcMplsOutboundStorageType, cpwVcMplsNonTeMappingIfIndex=cpwVcMplsNonTeMappingIfIndex, cpwVcMplsOutboundRowStatus=cpwVcMplsOutboundRowStatus, cpwVcMplsExpBitsMode=cpwVcMplsExpBitsMode, cpwVcMplsInboundEntry=cpwVcMplsInboundEntry, cpwVcMplsMIB=cpwVcMplsMIB, cpwVcMplsInboundIndex=cpwVcMplsInboundIndex, cpwVcMplsOutboundTunnelPeerLSR=cpwVcMplsOutboundTunnelPeerLSR, cpwVcMplsNonTeMappingXcTunnelIndex=cpwVcMplsNonTeMappingXcTunnelIndex, cpwVcMplsNonTeMappingVcIndex=cpwVcMplsNonTeMappingVcIndex, cpwVcMplsPeerLdpID=cpwVcMplsPeerLdpID)
