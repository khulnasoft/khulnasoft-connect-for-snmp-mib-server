#
# PySNMP MIB module UCD-DLMOD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UCD-DLMOD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:21:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, IpAddress, Unsigned32, Counter32, Integer32, iso, Bits, Gauge32, NotificationType, ModuleIdentity, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "IpAddress", "Unsigned32", "Counter32", "Integer32", "iso", "Bits", "Gauge32", "NotificationType", "ModuleIdentity", "ObjectIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ucdExperimental, = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdExperimental")
ucdDlmodMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 13, 14))
ucdDlmodMIB.setRevisions(('2000-01-26 00:00', '1999-12-10 00:00',))
if mibBuilder.loadTexts: ucdDlmodMIB.setLastUpdated('200001260000Z')
if mibBuilder.loadTexts: ucdDlmodMIB.setOrganization('University of California, Davis')
dlmodNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 2021, 13, 14, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmodNextIndex.setStatus('current')
dlmodTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2), )
if mibBuilder.loadTexts: dlmodTable.setStatus('current')
dlmodEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1), ).setIndexNames((0, "UCD-DLMOD-MIB", "dlmodIndex"))
if mibBuilder.loadTexts: dlmodEntry.setStatus('current')
dlmodIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: dlmodIndex.setStatus('current')
dlmodName = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlmodName.setStatus('current')
dlmodPath = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlmodPath.setStatus('current')
dlmodError = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmodError.setStatus('current')
dlmodStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 14, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("loaded", 1), ("unloaded", 2), ("error", 3), ("load", 4), ("unload", 5), ("create", 6), ("delete", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dlmodStatus.setStatus('current')
mibBuilder.exportSymbols("UCD-DLMOD-MIB", dlmodError=dlmodError, dlmodEntry=dlmodEntry, ucdDlmodMIB=ucdDlmodMIB, dlmodIndex=dlmodIndex, PYSNMP_MODULE_ID=ucdDlmodMIB, dlmodStatus=dlmodStatus, dlmodNextIndex=dlmodNextIndex, dlmodTable=dlmodTable, dlmodPath=dlmodPath, dlmodName=dlmodName)
