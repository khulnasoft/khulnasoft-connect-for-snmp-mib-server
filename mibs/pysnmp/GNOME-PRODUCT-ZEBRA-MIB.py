#
# PySNMP MIB module GNOME-PRODUCT-ZEBRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GNOME-PRODUCT-ZEBRA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
gnomeProducts, = mibBuilder.importSymbols("GNOME-SMI", "gnomeProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, TimeTicks, Counter32, Counter64, MibIdentifier, Bits, iso, IpAddress, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "TimeTicks", "Counter32", "Counter64", "MibIdentifier", "Bits", "iso", "IpAddress", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zebra = ModuleIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2))
if mibBuilder.loadTexts: zebra.setLastUpdated('200004250000Z')
if mibBuilder.loadTexts: zebra.setOrganization('GNOME project')
zserv = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2, 1))
if mibBuilder.loadTexts: zserv.setStatus('current')
bgpd = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2, 2))
if mibBuilder.loadTexts: bgpd.setStatus('current')
ripd = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2, 3))
if mibBuilder.loadTexts: ripd.setStatus('current')
ripngd = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2, 4))
if mibBuilder.loadTexts: ripngd.setStatus('current')
ospfd = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2, 5))
if mibBuilder.loadTexts: ospfd.setStatus('current')
ospf6d = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1, 2, 6))
if mibBuilder.loadTexts: ospf6d.setStatus('current')
mibBuilder.exportSymbols("GNOME-PRODUCT-ZEBRA-MIB", ospf6d=ospf6d, PYSNMP_MODULE_ID=zebra, ripngd=ripngd, bgpd=bgpd, zserv=zserv, ripd=ripd, zebra=zebra, ospfd=ospfd)
