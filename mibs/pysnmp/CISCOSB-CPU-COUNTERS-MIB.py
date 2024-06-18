#
# PySNMP MIB module CISCOSB-CPU-COUNTERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-CPU-COUNTERS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:06:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, Bits, MibIdentifier, Counter32, Counter64, ObjectIdentity, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Bits", "MibIdentifier", "Counter32", "Counter64", "ObjectIdentity", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "IpAddress", "Unsigned32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rlCpuCounters = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124))
rlCpuCounters.setRevisions(('2007-05-15 00:00',))
if mibBuilder.loadTexts: rlCpuCounters.setLastUpdated('2007010600Z')
if mibBuilder.loadTexts: rlCpuCounters.setOrganization('Cisco Systems, Inc.')
rlCpuCountersTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1), )
if mibBuilder.loadTexts: rlCpuCountersTable.setStatus('current')
rlCpuCountersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1), ).setIndexNames((0, "CISCOSB-CPU-COUNTERS-MIB", "rlCpuCountersTarget"))
if mibBuilder.loadTexts: rlCpuCountersEntry.setStatus('current')
rlCpuCountersTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("cpuCounters", 0))))
if mibBuilder.loadTexts: rlCpuCountersTarget.setStatus('current')
rlCpuCountersTxBC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersTxBC.setStatus('current')
rlCpuCountersTxMC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersTxMC.setStatus('current')
rlCpuCountersTxUC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersTxUC.setStatus('current')
rlCpuCountersTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersTxOctets.setStatus('current')
rlCpuCountersRxBC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersRxBC.setStatus('current')
rlCpuCountersRxMC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersRxMC.setStatus('current')
rlCpuCountersRxUC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersRxUC.setStatus('current')
rlCpuCountersRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersRxOctets.setStatus('current')
rlCpuCountersReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCpuCountersReset.setStatus('current')
rlCpuCountersEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCpuCountersEnabled.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-CPU-COUNTERS-MIB", rlCpuCountersEntry=rlCpuCountersEntry, rlCpuCountersTxUC=rlCpuCountersTxUC, rlCpuCountersRxOctets=rlCpuCountersRxOctets, PYSNMP_MODULE_ID=rlCpuCounters, rlCpuCountersTxMC=rlCpuCountersTxMC, rlCpuCountersTxOctets=rlCpuCountersTxOctets, rlCpuCountersTable=rlCpuCountersTable, rlCpuCountersRxUC=rlCpuCountersRxUC, rlCpuCountersReset=rlCpuCountersReset, rlCpuCountersTarget=rlCpuCountersTarget, rlCpuCounters=rlCpuCounters, rlCpuCountersEnabled=rlCpuCountersEnabled, rlCpuCountersRxBC=rlCpuCountersRxBC, rlCpuCountersRxMC=rlCpuCountersRxMC, rlCpuCountersTxBC=rlCpuCountersTxBC)
