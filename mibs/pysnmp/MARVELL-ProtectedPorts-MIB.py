#
# PySNMP MIB module MARVELL-ProtectedPorts-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-ProtectedPorts-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:59:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Unsigned32, TimeTicks, IpAddress, Integer32, NotificationType, ObjectIdentity, MibIdentifier, Counter64, iso, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Unsigned32", "TimeTicks", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter64", "iso", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
rlProtectedPorts = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 132))
rlProtectedPorts.setRevisions(('2008-05-03 12:34',))
if mibBuilder.loadTexts: rlProtectedPorts.setLastUpdated('200805031234Z')
if mibBuilder.loadTexts: rlProtectedPorts.setOrganization('MARVELL Semiconductor, Inc.')
rlProtectedPortsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 132, 1), )
if mibBuilder.loadTexts: rlProtectedPortsTable.setStatus('current')
rlProtectedPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 132, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlProtectedPortsEntry.setStatus('current')
rlProtectedPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 132, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-protected", 1), ("protected", 2))).clone('not-protected')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlProtectedPortType.setStatus('current')
rlProtectedPortCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 132, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlProtectedPortCommunity.setStatus('current')
rlProtectedPortsStatusTable = MibTable((1, 3, 6, 1, 4, 1, 89, 132, 2), )
if mibBuilder.loadTexts: rlProtectedPortsStatusTable.setStatus('current')
rlProtectedPortsStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 132, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlProtectedPortsStatusEntry.setStatus('current')
rlProtectedPortEgressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 132, 2, 1, 1), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlProtectedPortEgressPorts.setStatus('current')
rlProtectedPortsGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 132, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlProtectedPortsGlobalEnable.setStatus('current')
mibBuilder.exportSymbols("MARVELL-ProtectedPorts-MIB", rlProtectedPortType=rlProtectedPortType, rlProtectedPorts=rlProtectedPorts, PYSNMP_MODULE_ID=rlProtectedPorts, rlProtectedPortsStatusEntry=rlProtectedPortsStatusEntry, rlProtectedPortsGlobalEnable=rlProtectedPortsGlobalEnable, rlProtectedPortsTable=rlProtectedPortsTable, rlProtectedPortsEntry=rlProtectedPortsEntry, rlProtectedPortCommunity=rlProtectedPortCommunity, rlProtectedPortEgressPorts=rlProtectedPortEgressPorts, rlProtectedPortsStatusTable=rlProtectedPortsStatusTable)
