#
# PySNMP MIB module HPN-ICF-DSP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-DSP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:25:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, TimeTicks, ObjectIdentity, Integer32, MibIdentifier, iso, Gauge32, Unsigned32, IpAddress, ModuleIdentity, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "TimeTicks", "ObjectIdentity", "Integer32", "MibIdentifier", "iso", "Gauge32", "Unsigned32", "IpAddress", "ModuleIdentity", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfDSP = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89))
hpnicfDSP.setRevisions(('2008-01-16 13:00',))
if mibBuilder.loadTexts: hpnicfDSP.setLastUpdated('200801161300Z')
if mibBuilder.loadTexts: hpnicfDSP.setOrganization('')
hpnicfVPMStatusTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1), )
if mibBuilder.loadTexts: hpnicfVPMStatusTable.setStatus('current')
hpnicfVPMStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1), ).setIndexNames((0, "HPN-ICF-DSP-MIB", "hpnicfVPMIndex"))
if mibBuilder.loadTexts: hpnicfVPMStatusEntry.setStatus('current')
hpnicfVPMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfVPMIndex.setStatus('current')
hpnicfVPMEnPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1, 2), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVPMEnPhysicalIndex.setStatus('current')
hpnicfVPMState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("fatal", 3), ("offLine", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVPMState.setStatus('current')
hpnicfVPMResourceUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVPMResourceUtilization.setStatus('current')
hpnicfVPMHiWaterUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVPMHiWaterUtilization.setStatus('current')
hpnicfVPMMaxChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVPMMaxChannel.setStatus('current')
hpnicfDSPStatusTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2), )
if mibBuilder.loadTexts: hpnicfDSPStatusTable.setStatus('current')
hpnicfDSPStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1), ).setIndexNames((0, "HPN-ICF-DSP-MIB", "hpnicfDSPIndex"))
if mibBuilder.loadTexts: hpnicfDSPStatusEntry.setStatus('current')
hpnicfDSPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDSPIndex.setStatus('current')
hpnicfDSPVPMIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDSPVPMIndex.setStatus('current')
hpnicfDSPEnPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDSPEnPhysicalIndex.setStatus('current')
hpnicfDSPResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDSPResetTime.setStatus('current')
hpnicfDSPMaxChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDSPMaxChannel.setStatus('current')
hpnicfDSPState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("fatal", 3), ("offLine", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDSPState.setStatus('current')
hpnicfDSPInUseChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDSPInUseChannel.setStatus('current')
hpnicfDSPTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 3))
hpnicfDSPTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 3, 0))
hpnicfVPMStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 3, 0, 1)).setObjects(("HPN-ICF-DSP-MIB", "hpnicfVPMIndex"), ("HPN-ICF-DSP-MIB", "hpnicfVPMEnPhysicalIndex"), ("HPN-ICF-DSP-MIB", "hpnicfVPMState"))
if mibBuilder.loadTexts: hpnicfVPMStateChange.setStatus('current')
hpnicfDSPStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89, 3, 0, 2)).setObjects(("HPN-ICF-DSP-MIB", "hpnicfDSPIndex"), ("HPN-ICF-DSP-MIB", "hpnicfDSPVPMIndex"), ("HPN-ICF-DSP-MIB", "hpnicfDSPEnPhysicalIndex"), ("HPN-ICF-DSP-MIB", "hpnicfDSPState"))
if mibBuilder.loadTexts: hpnicfDSPStateChange.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-DSP-MIB", hpnicfDSPInUseChannel=hpnicfDSPInUseChannel, hpnicfVPMState=hpnicfVPMState, hpnicfVPMStatusTable=hpnicfVPMStatusTable, hpnicfDSPVPMIndex=hpnicfDSPVPMIndex, hpnicfVPMIndex=hpnicfVPMIndex, PYSNMP_MODULE_ID=hpnicfDSP, hpnicfVPMEnPhysicalIndex=hpnicfVPMEnPhysicalIndex, hpnicfDSPResetTime=hpnicfDSPResetTime, hpnicfDSPEnPhysicalIndex=hpnicfDSPEnPhysicalIndex, hpnicfDSPTrapPrex=hpnicfDSPTrapPrex, hpnicfDSPState=hpnicfDSPState, hpnicfDSPStatusEntry=hpnicfDSPStatusEntry, hpnicfDSP=hpnicfDSP, hpnicfDSPMaxChannel=hpnicfDSPMaxChannel, hpnicfVPMStatusEntry=hpnicfVPMStatusEntry, hpnicfDSPTrap=hpnicfDSPTrap, hpnicfDSPStatusTable=hpnicfDSPStatusTable, hpnicfVPMStateChange=hpnicfVPMStateChange, hpnicfVPMResourceUtilization=hpnicfVPMResourceUtilization, hpnicfDSPIndex=hpnicfDSPIndex, hpnicfVPMMaxChannel=hpnicfVPMMaxChannel, hpnicfVPMHiWaterUtilization=hpnicfVPMHiWaterUtilization, hpnicfDSPStateChange=hpnicfDSPStateChange)
