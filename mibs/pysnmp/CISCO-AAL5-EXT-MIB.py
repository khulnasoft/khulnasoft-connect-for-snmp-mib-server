#
# PySNMP MIB module CISCO-AAL5-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-AAL5-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
aal5VccEntry, = mibBuilder.importSymbols("ATM-MIB", "aal5VccEntry")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, ModuleIdentity, Integer32, iso, NotificationType, ObjectIdentity, TimeTicks, Gauge32, MibIdentifier, Counter64, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "ModuleIdentity", "Integer32", "iso", "NotificationType", "ObjectIdentity", "TimeTicks", "Gauge32", "MibIdentifier", "Counter64", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAal5ExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9999))
ciscoAal5ExtMIB.setRevisions(('2001-11-05 00:00',))
if mibBuilder.loadTexts: ciscoAal5ExtMIB.setLastUpdated('200111050000Z')
if mibBuilder.loadTexts: ciscoAal5ExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoAal5ExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1))
cAal5ExtConnections = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1))
cAal5ExtVccTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1), )
if mibBuilder.loadTexts: cAal5ExtVccTable.setStatus('current')
cAal5ExtVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1), )
aal5VccEntry.registerAugmentions(("CISCO-AAL5-EXT-MIB", "cAal5ExtVccEntry"))
cAal5ExtVccEntry.setIndexNames(*aal5VccEntry.getIndexNames())
if mibBuilder.loadTexts: cAal5ExtVccEntry.setStatus('current')
cAal5VccInDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInDroppedPkts.setStatus('current')
cAal5VccOutDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutDroppedPkts.setStatus('current')
cAal5VccInDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 3), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInDroppedOctets.setStatus('current')
cAal5VccOutDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 4), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutDroppedOctets.setStatus('current')
cAal5VccInCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 5), Counter32()).setUnits('cells').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInCells.setStatus('current')
cAal5VccOutCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 6), Counter32()).setUnits('cells').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutCells.setStatus('current')
cAal5VccInDroppedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 7), Counter32()).setUnits('cells').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInDroppedCells.setStatus('current')
cAal5VccOutDroppedCells = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 8), Counter32()).setUnits('cells').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutDroppedCells.setStatus('current')
ciscoAAL5ExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2))
ciscoAAL5ExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1))
ciscoAAL5ExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2))
ciscoAAL5ExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)).setObjects(("CISCO-AAL5-EXT-MIB", "ciscoAal5ExtMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAL5ExtMIBCompliance = ciscoAAL5ExtMIBCompliance.setStatus('current')
ciscoAal5ExtMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)).setObjects(("CISCO-AAL5-EXT-MIB", "cAal5VccInDroppedPkts"), ("CISCO-AAL5-EXT-MIB", "cAal5VccOutDroppedPkts"), ("CISCO-AAL5-EXT-MIB", "cAal5VccInDroppedOctets"), ("CISCO-AAL5-EXT-MIB", "cAal5VccOutDroppedOctets"), ("CISCO-AAL5-EXT-MIB", "cAal5VccInCells"), ("CISCO-AAL5-EXT-MIB", "cAal5VccOutCells"), ("CISCO-AAL5-EXT-MIB", "cAal5VccInDroppedCells"), ("CISCO-AAL5-EXT-MIB", "cAal5VccOutDroppedCells"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5ExtMIBGroup = ciscoAal5ExtMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAL5-EXT-MIB", ciscoAAL5ExtMIBCompliance=ciscoAAL5ExtMIBCompliance, cAal5VccOutDroppedPkts=cAal5VccOutDroppedPkts, ciscoAal5ExtMIB=ciscoAal5ExtMIB, ciscoAal5ExtMIBGroup=ciscoAal5ExtMIBGroup, cAal5VccInDroppedPkts=cAal5VccInDroppedPkts, cAal5ExtConnections=cAal5ExtConnections, ciscoAAL5ExtMIBCompliances=ciscoAAL5ExtMIBCompliances, cAal5VccOutDroppedOctets=cAal5VccOutDroppedOctets, cAal5VccInDroppedCells=cAal5VccInDroppedCells, cAal5VccInDroppedOctets=cAal5VccInDroppedOctets, ciscoAAL5ExtMIBGroups=ciscoAAL5ExtMIBGroups, cAal5VccInCells=cAal5VccInCells, ciscoAAL5ExtMIBConformance=ciscoAAL5ExtMIBConformance, cAal5ExtVccEntry=cAal5ExtVccEntry, ciscoAal5ExtMIBObjects=ciscoAal5ExtMIBObjects, PYSNMP_MODULE_ID=ciscoAal5ExtMIB, cAal5VccOutCells=cAal5VccOutCells, cAal5ExtVccTable=cAal5ExtVccTable, cAal5VccOutDroppedCells=cAal5VccOutDroppedCells)
