#
# PySNMP MIB module EVENTLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EVENTLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:52:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
eventlog, = mibBuilder.importSymbols("CORIOLIS-MIB", "eventlog")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter64, IpAddress, NotificationType, Gauge32, Counter32, TimeTicks, Integer32, MibIdentifier, ModuleIdentity, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter64", "IpAddress", "NotificationType", "Gauge32", "Counter32", "TimeTicks", "Integer32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eventlogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5812, 9, 1))
if mibBuilder.loadTexts: eventlogMIB.setLastUpdated('0010300000Z')
if mibBuilder.loadTexts: eventlogMIB.setOrganization('Coriolis Networks')
eventlogTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 9, 2), )
if mibBuilder.loadTexts: eventlogTable.setStatus('current')
eventlogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 9, 2, 1), ).setIndexNames((0, "EVENTLOG-MIB", "eventlogEventID"))
if mibBuilder.loadTexts: eventlogEntry.setStatus('current')
eventlogName = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventlogName.setStatus('current')
eventlogDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventlogDesc.setStatus('current')
eventlogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventlogSeverity.setStatus('current')
eventlogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventlogTime.setStatus('current')
eventlogSrcIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventlogSrcIpAddr.setStatus('current')
eventlogCorEventIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventlogCorEventIpAddr.setStatus('current')
eventlogEventID = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventlogEventID.setStatus('current')
eventlogCorEventID = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 9, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventlogCorEventID.setStatus('current')
mibBuilder.exportSymbols("EVENTLOG-MIB", eventlogMIB=eventlogMIB, eventlogTime=eventlogTime, eventlogEntry=eventlogEntry, eventlogCorEventIpAddr=eventlogCorEventIpAddr, eventlogSrcIpAddr=eventlogSrcIpAddr, eventlogTable=eventlogTable, PYSNMP_MODULE_ID=eventlogMIB, eventlogCorEventID=eventlogCorEventID, eventlogName=eventlogName, eventlogDesc=eventlogDesc, eventlogSeverity=eventlogSeverity, eventlogEventID=eventlogEventID)
