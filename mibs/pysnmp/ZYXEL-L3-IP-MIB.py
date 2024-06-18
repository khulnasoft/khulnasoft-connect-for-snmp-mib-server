#
# PySNMP MIB module ZYXEL-L3-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-L3-IP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:44:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Counter64, TimeTicks, Gauge32, Bits, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Integer32, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Counter64", "TimeTicks", "Gauge32", "Bits", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Integer32", "ObjectIdentity", "MibIdentifier")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelL3Ip = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40))
if mibBuilder.loadTexts: zyxelL3Ip.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelL3Ip.setOrganization('Enterprise Solution ZyXEL')
zyxelLayer3IpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1))
zyLayer3IpDnsIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer3IpDnsIpAddress.setStatus('current')
zyLayer3IpDefaultMgmt = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inBand", 0), ("outOfBand", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer3IpDefaultMgmt.setStatus('current')
zyLayer3IpDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer3IpDefaultGateway.setStatus('current')
zyLayer3IpInbandMaxNumberOfInterfaces = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyLayer3IpInbandMaxNumberOfInterfaces.setStatus('current')
zyxelLayer3IpInbandTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5), )
if mibBuilder.loadTexts: zyxelLayer3IpInbandTable.setStatus('current')
zyxelLayer3IpInbandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1), ).setIndexNames((0, "ZYXEL-L3-IP-MIB", "zyLayer3IpInbandIpAddress"), (0, "ZYXEL-L3-IP-MIB", "zyLayer3IpInbandMask"))
if mibBuilder.loadTexts: zyxelLayer3IpInbandEntry.setStatus('current')
zyLayer3IpInbandIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: zyLayer3IpInbandIpAddress.setStatus('current')
zyLayer3IpInbandMask = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: zyLayer3IpInbandMask.setStatus('current')
zyLayer3IpInbandVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLayer3IpInbandVid.setStatus('current')
zyLayer3IpInbandRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyLayer3IpInbandRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-L3-IP-MIB", zyxelLayer3IpInbandEntry=zyxelLayer3IpInbandEntry, zyxelLayer3IpInbandTable=zyxelLayer3IpInbandTable, zyLayer3IpInbandIpAddress=zyLayer3IpInbandIpAddress, zyxelL3Ip=zyxelL3Ip, PYSNMP_MODULE_ID=zyxelL3Ip, zyLayer3IpInbandRowStatus=zyLayer3IpInbandRowStatus, zyLayer3IpInbandVid=zyLayer3IpInbandVid, zyLayer3IpInbandMaxNumberOfInterfaces=zyLayer3IpInbandMaxNumberOfInterfaces, zyLayer3IpInbandMask=zyLayer3IpInbandMask, zyLayer3IpDefaultGateway=zyLayer3IpDefaultGateway, zyLayer3IpDefaultMgmt=zyLayer3IpDefaultMgmt, zyxelLayer3IpSetup=zyxelLayer3IpSetup, zyLayer3IpDnsIpAddress=zyLayer3IpDnsIpAddress)
