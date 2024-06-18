#
# PySNMP MIB module CENTILLION-VIRTUALSEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-VIRTUALSEGMENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
BridgeGroupId, = mibBuilder.importSymbols("CENTILLION-BRIDGEGROUP-MIB", "BridgeGroupId")
StatusIndicator, Boolean, sysConfig = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "StatusIndicator", "Boolean", "sysConfig")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, TimeTicks, Counter64, Integer32, ModuleIdentity, NotificationType, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "TimeTicks", "Counter64", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class VirtualSegmentTypeId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("token-ring", 2), ("ethernet", 3))

virtualSegmentGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23))
virtualSegmentConfigNumber = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualSegmentConfigNumber.setStatus('mandatory')
virtualSegmentActiveNumber = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualSegmentActiveNumber.setStatus('mandatory')
virtualSegmentTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3), )
if mibBuilder.loadTexts: virtualSegmentTable.setStatus('mandatory')
virtualSegmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1), ).setIndexNames((0, "CENTILLION-VIRTUALSEGMENT-MIB", "virtualSegmentType"), (0, "CENTILLION-VIRTUALSEGMENT-MIB", "virtualSegmentId"))
if mibBuilder.loadTexts: virtualSegmentEntry.setStatus('mandatory')
virtualSegmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 1), VirtualSegmentTypeId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualSegmentType.setStatus('mandatory')
virtualSegmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualSegmentId.setStatus('mandatory')
virtualSegmentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 3), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualSegmentStatus.setStatus('mandatory')
virtualSegmentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualSegmentIfIndex.setStatus('mandatory')
virtualSegmentConfiguredPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualSegmentConfiguredPortNumber.setStatus('mandatory')
virtualSegmentActivePortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualSegmentActivePortNumber.setStatus('mandatory')
virtualSegmentSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualSegmentSpecific.setStatus('mandatory')
virtualSegmentAdminEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("iso88025-tokenRing", 2), ("ethernet-iso88023", 3), ("ethernet-csmacd", 4), ("iso88023-csmacd", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualSegmentAdminEncapsulation.setStatus('mandatory')
virtualSegmentBridgeGroupIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 9), BridgeGroupId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualSegmentBridgeGroupIdentifier.setStatus('mandatory')
virtualSegmentGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualSegmentGroupName.setStatus('mandatory')
virtualSegmentGroupServer = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 3, 1, 11), Boolean().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualSegmentGroupServer.setStatus('mandatory')
virtualSegmentPortTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4), )
if mibBuilder.loadTexts: virtualSegmentPortTable.setStatus('mandatory')
virtualSegmentPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1), ).setIndexNames((0, "CENTILLION-VIRTUALSEGMENT-MIB", "virtualSegmentPortType"), (0, "CENTILLION-VIRTUALSEGMENT-MIB", "virtualSegmentPortId"), (0, "CENTILLION-VIRTUALSEGMENT-MIB", "virtualSegmentPortCardNumber"), (0, "CENTILLION-VIRTUALSEGMENT-MIB", "virtualSegmentPortPortNumber"))
if mibBuilder.loadTexts: virtualSegmentPortEntry.setStatus('mandatory')
virtualSegmentPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1, 1), VirtualSegmentTypeId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualSegmentPortType.setStatus('mandatory')
virtualSegmentPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualSegmentPortId.setStatus('mandatory')
virtualSegmentPortCardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualSegmentPortCardNumber.setStatus('mandatory')
virtualSegmentPortPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualSegmentPortPortNumber.setStatus('mandatory')
virtualSegmentPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1, 5), StatusIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualSegmentPortStatus.setStatus('mandatory')
virtualSegmentPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 23, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualSegmentPortIfIndex.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-VIRTUALSEGMENT-MIB", virtualSegmentStatus=virtualSegmentStatus, virtualSegmentPortCardNumber=virtualSegmentPortCardNumber, virtualSegmentGroup=virtualSegmentGroup, VirtualSegmentTypeId=VirtualSegmentTypeId, virtualSegmentPortStatus=virtualSegmentPortStatus, virtualSegmentPortPortNumber=virtualSegmentPortPortNumber, virtualSegmentPortIfIndex=virtualSegmentPortIfIndex, virtualSegmentAdminEncapsulation=virtualSegmentAdminEncapsulation, virtualSegmentConfiguredPortNumber=virtualSegmentConfiguredPortNumber, virtualSegmentGroupName=virtualSegmentGroupName, virtualSegmentPortEntry=virtualSegmentPortEntry, virtualSegmentPortTable=virtualSegmentPortTable, virtualSegmentBridgeGroupIdentifier=virtualSegmentBridgeGroupIdentifier, virtualSegmentConfigNumber=virtualSegmentConfigNumber, virtualSegmentGroupServer=virtualSegmentGroupServer, virtualSegmentActivePortNumber=virtualSegmentActivePortNumber, virtualSegmentPortId=virtualSegmentPortId, virtualSegmentPortType=virtualSegmentPortType, virtualSegmentActiveNumber=virtualSegmentActiveNumber, virtualSegmentEntry=virtualSegmentEntry, virtualSegmentSpecific=virtualSegmentSpecific, virtualSegmentType=virtualSegmentType, virtualSegmentTable=virtualSegmentTable, virtualSegmentIfIndex=virtualSegmentIfIndex, virtualSegmentId=virtualSegmentId)
