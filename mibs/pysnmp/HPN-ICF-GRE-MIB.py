#
# PySNMP MIB module HPN-ICF-GRE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-GRE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:26:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, ObjectIdentity, Gauge32, IpAddress, ModuleIdentity, Bits, Counter64, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "ObjectIdentity", "Gauge32", "IpAddress", "ModuleIdentity", "Bits", "Counter64", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfGre = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54))
hpnicfGre.setRevisions(('2005-06-04 00:00',))
if mibBuilder.loadTexts: hpnicfGre.setLastUpdated('200506040000Z')
if mibBuilder.loadTexts: hpnicfGre.setOrganization('')
hpnicfGreObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54, 1))
hpnicfGreTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54, 1, 1), )
if mibBuilder.loadTexts: hpnicfGreTable.setStatus('current')
hpnicfGreEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfGreEntry.setStatus('current')
hpnicfGreKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfGreKeyValue.setStatus('current')
hpnicfGreKey = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfGreKey.setStatus('current')
hpnicfGreChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfGreChecksum.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-GRE-MIB", hpnicfGreTable=hpnicfGreTable, hpnicfGreObjects=hpnicfGreObjects, hpnicfGreEntry=hpnicfGreEntry, hpnicfGreKeyValue=hpnicfGreKeyValue, PYSNMP_MODULE_ID=hpnicfGre, hpnicfGre=hpnicfGre, hpnicfGreChecksum=hpnicfGreChecksum, hpnicfGreKey=hpnicfGreKey)
