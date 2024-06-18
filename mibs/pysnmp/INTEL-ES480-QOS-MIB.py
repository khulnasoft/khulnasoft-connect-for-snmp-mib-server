#
# PySNMP MIB module INTEL-ES480-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-ES480-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:42:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
es480tAgent, = mibBuilder.importSymbols("INTEL-ES480-MIB", "es480tAgent")
es480tVlanIfIndex, = mibBuilder.importSymbols("INTEL-ES480-VLAN-MIB", "es480tVlanIfIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, Bits, iso, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, MibIdentifier, Gauge32, Counter32, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Bits", "iso", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "MibIdentifier", "Gauge32", "Counter32", "IpAddress", "Counter64")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
es480tQos = ModuleIdentity((1, 3, 6, 1, 4, 1, 343, 6, 60, 3))
if mibBuilder.loadTexts: es480tQos.setLastUpdated('9803020000Z')
if mibBuilder.loadTexts: es480tQos.setOrganization('Intel Corp.')
es480tQosCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1))
es480tQosMode = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ingress", 1), ("egress", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: es480tQosMode.setStatus('mandatory')
es480tQosUnconfigure = MibScalar((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: es480tQosUnconfigure.setStatus('mandatory')
es480tQosProfileTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6), )
if mibBuilder.loadTexts: es480tQosProfileTable.setStatus('mandatory')
es480tQosProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1), ).setIndexNames((0, "INTEL-ES480-QOS-MIB", "es480tQosProfileIndex"))
if mibBuilder.loadTexts: es480tQosProfileEntry.setStatus('mandatory')
es480tQosProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: es480tQosProfileIndex.setStatus('mandatory')
es480tQosProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: es480tQosProfileName.setStatus('mandatory')
es480tQosProfileMinBw = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: es480tQosProfileMinBw.setStatus('mandatory')
es480tQosProfileMaxBw = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: es480tQosProfileMaxBw.setStatus('mandatory')
es480tQosProfilePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("low", 1), ("lowNormal", 2), ("normal", 3), ("normalMedium", 4), ("medium", 5), ("mediumHi", 6), ("high", 7), ("highHi", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: es480tQosProfilePriority.setStatus('mandatory')
es480tQosProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 6, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: es480tQosProfileRowStatus.setStatus('mandatory')
es480tQosByVlanMappingTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 7), )
if mibBuilder.loadTexts: es480tQosByVlanMappingTable.setStatus('mandatory')
es480tQosByVlanMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 7, 1), ).setIndexNames((0, "INTEL-ES480-VLAN-MIB", "es480tVlanIfIndex"))
if mibBuilder.loadTexts: es480tQosByVlanMappingEntry.setStatus('mandatory')
es480tQosByVlanMappingQosProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 60, 3, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: es480tQosByVlanMappingQosProfileIndex.setStatus('mandatory')
mibBuilder.exportSymbols("INTEL-ES480-QOS-MIB", es480tQos=es480tQos, es480tQosCommon=es480tQosCommon, es480tQosProfileTable=es480tQosProfileTable, es480tQosByVlanMappingTable=es480tQosByVlanMappingTable, es480tQosUnconfigure=es480tQosUnconfigure, es480tQosProfileMinBw=es480tQosProfileMinBw, es480tQosProfileEntry=es480tQosProfileEntry, es480tQosByVlanMappingQosProfileIndex=es480tQosByVlanMappingQosProfileIndex, es480tQosProfileRowStatus=es480tQosProfileRowStatus, es480tQosProfilePriority=es480tQosProfilePriority, es480tQosProfileMaxBw=es480tQosProfileMaxBw, es480tQosProfileName=es480tQosProfileName, es480tQosProfileIndex=es480tQosProfileIndex, es480tQosByVlanMappingEntry=es480tQosByVlanMappingEntry, es480tQosMode=es480tQosMode, PYSNMP_MODULE_ID=es480tQos)
