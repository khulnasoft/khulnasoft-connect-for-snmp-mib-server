#
# PySNMP MIB module TE-LINK-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TE-LINK-STD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:58:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, transmission, NotificationType, IpAddress, ObjectIdentity, Bits, TimeTicks, Counter64, Gauge32, ModuleIdentity, Unsigned32, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "transmission", "NotificationType", "IpAddress", "ObjectIdentity", "Bits", "TimeTicks", "Counter64", "Gauge32", "ModuleIdentity", "Unsigned32", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString, StorageType, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "StorageType", "RowStatus")
teLinkStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 200))
teLinkStdMIB.setRevisions(('2005-10-11 00:00',))
if mibBuilder.loadTexts: teLinkStdMIB.setLastUpdated('200510110000Z')
if mibBuilder.loadTexts: teLinkStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
class TeLinkBandwidth(TextualConvention, OctetString):
    reference = 'IEEE Standard for Binary Floating-Point Arithmetic, Standard 754-1985'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TeLinkPriority(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class TeLinkProtection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

class TeLinkSwitchingCapability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 51, 100, 150, 200))
    namedValues = NamedValues(("packetSwitch1", 1), ("packetSwitch2", 2), ("packetSwitch3", 3), ("packetSwitch4", 4), ("layer2Switch", 51), ("tdm", 100), ("lambdaSwitch", 150), ("fiberSwitch", 200))

class TeLinkEncodingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5, 7, 8, 9, 11))
    namedValues = NamedValues(("packet", 1), ("ethernet", 2), ("ansiEtsiPdh", 3), ("sdhItuSonetAnsi", 5), ("digitalWrapper", 7), ("lambda", 8), ("fiber", 9), ("fiberChannel", 11))

class TeLinkSonetSdhIndication(TextualConvention, Integer32):
    reference = 'OSPF Extensions in Support of Generalized Multi-Protocol Label Switching (GMPLS), RFC 4203'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("standard", 0), ("arbitrary", 1))

teLinkNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 200, 0))
teLinkObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 200, 1))
teLinkConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 200, 2))
teLinkTable = MibTable((1, 3, 6, 1, 2, 1, 10, 200, 1, 1), )
if mibBuilder.loadTexts: teLinkTable.setStatus('current')
teLinkEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: teLinkEntry.setStatus('current')
teLinkAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 1), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkAddressType.setStatus('current')
teLinkLocalIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 2), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkLocalIpAddr.setStatus('current')
teLinkRemoteIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkRemoteIpAddr.setStatus('current')
teLinkMetric = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkMetric.setStatus('current')
teLinkMaximumReservableBandwidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 5), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: teLinkMaximumReservableBandwidth.setStatus('current')
teLinkProtectionType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("extraTraffic", 1), ("unprotected", 2), ("shared", 3), ("dedicated1For1", 4), ("dedicated1Plus1", 5), ("enhanced", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkProtectionType.setStatus('current')
teLinkWorkingPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 7), TeLinkPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkWorkingPriority.setStatus('current')
teLinkResourceClass = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkResourceClass.setStatus('current')
teLinkIncomingIfId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkIncomingIfId.setStatus('current')
teLinkOutgoingIfId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 10), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkOutgoingIfId.setStatus('current')
teLinkRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkRowStatus.setStatus('current')
teLinkStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 1, 1, 12), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkStorageType.setStatus('current')
teLinkDescriptorTable = MibTable((1, 3, 6, 1, 2, 1, 10, 200, 1, 2), )
if mibBuilder.loadTexts: teLinkDescriptorTable.setStatus('current')
teLinkDescriptorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TE-LINK-STD-MIB", "teLinkDescriptorId"))
if mibBuilder.loadTexts: teLinkDescriptorEntry.setStatus('current')
teLinkDescriptorId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: teLinkDescriptorId.setStatus('current')
teLinkDescrSwitchingCapability = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 2), TeLinkSwitchingCapability()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrSwitchingCapability.setStatus('current')
teLinkDescrEncodingType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 3), TeLinkEncodingType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrEncodingType.setStatus('current')
teLinkDescrMinLspBandwidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 4), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrMinLspBandwidth.setStatus('current')
teLinkDescrMaxLspBandwidthPrio0 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 5), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrMaxLspBandwidthPrio0.setStatus('current')
teLinkDescrMaxLspBandwidthPrio1 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 6), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrMaxLspBandwidthPrio1.setStatus('current')
teLinkDescrMaxLspBandwidthPrio2 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 7), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrMaxLspBandwidthPrio2.setStatus('current')
teLinkDescrMaxLspBandwidthPrio3 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 8), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrMaxLspBandwidthPrio3.setStatus('current')
teLinkDescrMaxLspBandwidthPrio4 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 9), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrMaxLspBandwidthPrio4.setStatus('current')
teLinkDescrMaxLspBandwidthPrio5 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 10), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrMaxLspBandwidthPrio5.setStatus('current')
teLinkDescrMaxLspBandwidthPrio6 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 11), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrMaxLspBandwidthPrio6.setStatus('current')
teLinkDescrMaxLspBandwidthPrio7 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 12), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrMaxLspBandwidthPrio7.setStatus('current')
teLinkDescrInterfaceMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrInterfaceMtu.setStatus('current')
teLinkDescrIndication = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 14), TeLinkSonetSdhIndication()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrIndication.setStatus('current')
teLinkDescrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrRowStatus.setStatus('current')
teLinkDescrStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 2, 1, 16), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkDescrStorageType.setStatus('current')
teLinkSrlgTable = MibTable((1, 3, 6, 1, 2, 1, 10, 200, 1, 3), )
if mibBuilder.loadTexts: teLinkSrlgTable.setStatus('current')
teLinkSrlgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 200, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TE-LINK-STD-MIB", "teLinkSrlg"))
if mibBuilder.loadTexts: teLinkSrlgEntry.setStatus('current')
teLinkSrlg = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: teLinkSrlg.setStatus('current')
teLinkSrlgRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkSrlgRowStatus.setStatus('current')
teLinkSrlgStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 3, 1, 3), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkSrlgStorageType.setStatus('current')
teLinkBandwidthTable = MibTable((1, 3, 6, 1, 2, 1, 10, 200, 1, 4), )
if mibBuilder.loadTexts: teLinkBandwidthTable.setStatus('current')
teLinkBandwidthEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 200, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TE-LINK-STD-MIB", "teLinkBandwidthPriority"))
if mibBuilder.loadTexts: teLinkBandwidthEntry.setStatus('current')
teLinkBandwidthPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 4, 1, 1), TeLinkPriority())
if mibBuilder.loadTexts: teLinkBandwidthPriority.setStatus('current')
teLinkBandwidthUnreserved = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 4, 1, 2), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: teLinkBandwidthUnreserved.setStatus('current')
teLinkBandwidthRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkBandwidthRowStatus.setStatus('current')
teLinkBandwidthStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 4, 1, 4), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: teLinkBandwidthStorageType.setStatus('current')
componentLinkTable = MibTable((1, 3, 6, 1, 2, 1, 10, 200, 1, 5), )
if mibBuilder.loadTexts: componentLinkTable.setStatus('current')
componentLinkEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 200, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: componentLinkEntry.setStatus('current')
componentLinkMaxResBandwidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 5, 1, 1), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkMaxResBandwidth.setStatus('current')
componentLinkPreferredProtection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 5, 1, 2), TeLinkProtection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkPreferredProtection.setStatus('current')
componentLinkCurrentProtection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 5, 1, 3), TeLinkProtection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: componentLinkCurrentProtection.setStatus('current')
componentLinkRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkRowStatus.setStatus('current')
componentLinkStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 5, 1, 5), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkStorageType.setStatus('current')
componentLinkDescriptorTable = MibTable((1, 3, 6, 1, 2, 1, 10, 200, 1, 6), )
if mibBuilder.loadTexts: componentLinkDescriptorTable.setStatus('current')
componentLinkDescriptorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TE-LINK-STD-MIB", "componentLinkDescrId"))
if mibBuilder.loadTexts: componentLinkDescriptorEntry.setStatus('current')
componentLinkDescrId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: componentLinkDescrId.setStatus('current')
componentLinkDescrSwitchingCapability = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 2), TeLinkSwitchingCapability()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrSwitchingCapability.setStatus('current')
componentLinkDescrEncodingType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 3), TeLinkEncodingType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrEncodingType.setStatus('current')
componentLinkDescrMinLspBandwidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 4), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrMinLspBandwidth.setStatus('current')
componentLinkDescrMaxLspBandwidthPrio0 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 5), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrMaxLspBandwidthPrio0.setStatus('current')
componentLinkDescrMaxLspBandwidthPrio1 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 6), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrMaxLspBandwidthPrio1.setStatus('current')
componentLinkDescrMaxLspBandwidthPrio2 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 7), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrMaxLspBandwidthPrio2.setStatus('current')
componentLinkDescrMaxLspBandwidthPrio3 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 8), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrMaxLspBandwidthPrio3.setStatus('current')
componentLinkDescrMaxLspBandwidthPrio4 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 9), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrMaxLspBandwidthPrio4.setStatus('current')
componentLinkDescrMaxLspBandwidthPrio5 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 10), TeLinkBandwidth()).setUnits('thousand bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrMaxLspBandwidthPrio5.setStatus('current')
componentLinkDescrMaxLspBandwidthPrio6 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 11), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrMaxLspBandwidthPrio6.setStatus('current')
componentLinkDescrMaxLspBandwidthPrio7 = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 12), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrMaxLspBandwidthPrio7.setStatus('current')
componentLinkDescrInterfaceMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrInterfaceMtu.setStatus('current')
componentLinkDescrIndication = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 14), TeLinkSonetSdhIndication()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrIndication.setStatus('current')
componentLinkDescrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrRowStatus.setStatus('current')
componentLinkDescrStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 6, 1, 16), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkDescrStorageType.setStatus('current')
componentLinkBandwidthTable = MibTable((1, 3, 6, 1, 2, 1, 10, 200, 1, 7), )
if mibBuilder.loadTexts: componentLinkBandwidthTable.setStatus('current')
componentLinkBandwidthEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 200, 1, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TE-LINK-STD-MIB", "componentLinkBandwidthPriority"))
if mibBuilder.loadTexts: componentLinkBandwidthEntry.setStatus('current')
componentLinkBandwidthPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 7, 1, 1), TeLinkPriority())
if mibBuilder.loadTexts: componentLinkBandwidthPriority.setStatus('current')
componentLinkBandwidthUnreserved = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 7, 1, 2), TeLinkBandwidth()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: componentLinkBandwidthUnreserved.setStatus('current')
componentLinkBandwidthRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 7, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkBandwidthRowStatus.setStatus('current')
componentLinkBandwidthStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 200, 1, 7, 1, 4), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: componentLinkBandwidthStorageType.setStatus('current')
teLinkCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 200, 2, 1))
teLinkGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 200, 2, 2))
teLinkModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 200, 2, 1, 1)).setObjects(("TE-LINK-STD-MIB", "teLinkGroup"), ("TE-LINK-STD-MIB", "teLinkBandwidthGroup"), ("TE-LINK-STD-MIB", "componentLinkBandwidthGroup"), ("TE-LINK-STD-MIB", "teLinkSrlgGroup"), ("TE-LINK-STD-MIB", "teLinkPscGroup"), ("TE-LINK-STD-MIB", "teLinkTdmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    teLinkModuleFullCompliance = teLinkModuleFullCompliance.setStatus('current')
teLinkModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 200, 2, 1, 2)).setObjects(("TE-LINK-STD-MIB", "teLinkGroup"), ("TE-LINK-STD-MIB", "teLinkBandwidthGroup"), ("TE-LINK-STD-MIB", "componentLinkBandwidthGroup"), ("TE-LINK-STD-MIB", "teLinkSrlgGroup"), ("TE-LINK-STD-MIB", "teLinkPscGroup"), ("TE-LINK-STD-MIB", "teLinkTdmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    teLinkModuleReadOnlyCompliance = teLinkModuleReadOnlyCompliance.setStatus('current')
teLinkGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 200, 2, 2, 1)).setObjects(("TE-LINK-STD-MIB", "teLinkAddressType"), ("TE-LINK-STD-MIB", "teLinkLocalIpAddr"), ("TE-LINK-STD-MIB", "teLinkRemoteIpAddr"), ("TE-LINK-STD-MIB", "teLinkMetric"), ("TE-LINK-STD-MIB", "teLinkProtectionType"), ("TE-LINK-STD-MIB", "teLinkWorkingPriority"), ("TE-LINK-STD-MIB", "teLinkResourceClass"), ("TE-LINK-STD-MIB", "teLinkIncomingIfId"), ("TE-LINK-STD-MIB", "teLinkOutgoingIfId"), ("TE-LINK-STD-MIB", "teLinkRowStatus"), ("TE-LINK-STD-MIB", "teLinkStorageType"), ("TE-LINK-STD-MIB", "teLinkDescrSwitchingCapability"), ("TE-LINK-STD-MIB", "teLinkDescrEncodingType"), ("TE-LINK-STD-MIB", "teLinkDescrRowStatus"), ("TE-LINK-STD-MIB", "teLinkDescrStorageType"), ("TE-LINK-STD-MIB", "componentLinkPreferredProtection"), ("TE-LINK-STD-MIB", "componentLinkCurrentProtection"), ("TE-LINK-STD-MIB", "componentLinkRowStatus"), ("TE-LINK-STD-MIB", "componentLinkStorageType"), ("TE-LINK-STD-MIB", "componentLinkDescrSwitchingCapability"), ("TE-LINK-STD-MIB", "componentLinkDescrEncodingType"), ("TE-LINK-STD-MIB", "componentLinkDescrRowStatus"), ("TE-LINK-STD-MIB", "componentLinkDescrStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    teLinkGroup = teLinkGroup.setStatus('current')
teLinkSrlgGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 200, 2, 2, 2)).setObjects(("TE-LINK-STD-MIB", "teLinkSrlgRowStatus"), ("TE-LINK-STD-MIB", "teLinkSrlgStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    teLinkSrlgGroup = teLinkSrlgGroup.setStatus('current')
teLinkBandwidthGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 200, 2, 2, 3)).setObjects(("TE-LINK-STD-MIB", "teLinkMaximumReservableBandwidth"), ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio0"), ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio1"), ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio2"), ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio3"), ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio4"), ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio5"), ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio6"), ("TE-LINK-STD-MIB", "teLinkDescrMaxLspBandwidthPrio7"), ("TE-LINK-STD-MIB", "teLinkBandwidthUnreserved"), ("TE-LINK-STD-MIB", "teLinkBandwidthRowStatus"), ("TE-LINK-STD-MIB", "teLinkBandwidthStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    teLinkBandwidthGroup = teLinkBandwidthGroup.setStatus('current')
componentLinkBandwidthGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 200, 2, 2, 4)).setObjects(("TE-LINK-STD-MIB", "componentLinkMaxResBandwidth"), ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio0"), ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio1"), ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio2"), ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio3"), ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio4"), ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio5"), ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio6"), ("TE-LINK-STD-MIB", "componentLinkDescrMaxLspBandwidthPrio7"), ("TE-LINK-STD-MIB", "componentLinkBandwidthUnreserved"), ("TE-LINK-STD-MIB", "componentLinkBandwidthRowStatus"), ("TE-LINK-STD-MIB", "componentLinkBandwidthStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    componentLinkBandwidthGroup = componentLinkBandwidthGroup.setStatus('current')
teLinkPscGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 200, 2, 2, 5)).setObjects(("TE-LINK-STD-MIB", "teLinkDescrMinLspBandwidth"), ("TE-LINK-STD-MIB", "teLinkDescrInterfaceMtu"), ("TE-LINK-STD-MIB", "componentLinkDescrMinLspBandwidth"), ("TE-LINK-STD-MIB", "componentLinkDescrInterfaceMtu"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    teLinkPscGroup = teLinkPscGroup.setStatus('current')
teLinkTdmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 200, 2, 2, 6)).setObjects(("TE-LINK-STD-MIB", "teLinkDescrMinLspBandwidth"), ("TE-LINK-STD-MIB", "teLinkDescrIndication"), ("TE-LINK-STD-MIB", "componentLinkDescrMinLspBandwidth"), ("TE-LINK-STD-MIB", "componentLinkDescrIndication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    teLinkTdmGroup = teLinkTdmGroup.setStatus('current')
mibBuilder.exportSymbols("TE-LINK-STD-MIB", componentLinkDescrStorageType=componentLinkDescrStorageType, teLinkDescrMaxLspBandwidthPrio7=teLinkDescrMaxLspBandwidthPrio7, componentLinkBandwidthTable=componentLinkBandwidthTable, teLinkProtectionType=teLinkProtectionType, teLinkDescrRowStatus=teLinkDescrRowStatus, componentLinkStorageType=componentLinkStorageType, teLinkSrlg=teLinkSrlg, teLinkBandwidthPriority=teLinkBandwidthPriority, teLinkDescrIndication=teLinkDescrIndication, TeLinkSonetSdhIndication=TeLinkSonetSdhIndication, componentLinkMaxResBandwidth=componentLinkMaxResBandwidth, teLinkDescrStorageType=teLinkDescrStorageType, componentLinkRowStatus=componentLinkRowStatus, teLinkWorkingPriority=teLinkWorkingPriority, teLinkStorageType=teLinkStorageType, teLinkDescrMaxLspBandwidthPrio2=teLinkDescrMaxLspBandwidthPrio2, teLinkConformance=teLinkConformance, componentLinkDescrRowStatus=componentLinkDescrRowStatus, teLinkBandwidthRowStatus=teLinkBandwidthRowStatus, componentLinkBandwidthRowStatus=componentLinkBandwidthRowStatus, teLinkNotifications=teLinkNotifications, teLinkMaximumReservableBandwidth=teLinkMaximumReservableBandwidth, teLinkDescriptorEntry=teLinkDescriptorEntry, componentLinkBandwidthGroup=componentLinkBandwidthGroup, teLinkPscGroup=teLinkPscGroup, teLinkStdMIB=teLinkStdMIB, teLinkDescrMinLspBandwidth=teLinkDescrMinLspBandwidth, teLinkSrlgStorageType=teLinkSrlgStorageType, teLinkRowStatus=teLinkRowStatus, componentLinkDescrEncodingType=componentLinkDescrEncodingType, componentLinkBandwidthUnreserved=componentLinkBandwidthUnreserved, componentLinkDescrId=componentLinkDescrId, TeLinkEncodingType=TeLinkEncodingType, teLinkSrlgEntry=teLinkSrlgEntry, teLinkDescriptorId=teLinkDescriptorId, teLinkDescrMaxLspBandwidthPrio3=teLinkDescrMaxLspBandwidthPrio3, teLinkDescriptorTable=teLinkDescriptorTable, componentLinkDescrMaxLspBandwidthPrio7=componentLinkDescrMaxLspBandwidthPrio7, teLinkDescrMaxLspBandwidthPrio4=teLinkDescrMaxLspBandwidthPrio4, teLinkBandwidthGroup=teLinkBandwidthGroup, componentLinkDescrMaxLspBandwidthPrio6=componentLinkDescrMaxLspBandwidthPrio6, componentLinkDescrMaxLspBandwidthPrio1=componentLinkDescrMaxLspBandwidthPrio1, teLinkBandwidthEntry=teLinkBandwidthEntry, teLinkGroup=teLinkGroup, teLinkDescrEncodingType=teLinkDescrEncodingType, teLinkModuleFullCompliance=teLinkModuleFullCompliance, teLinkGroups=teLinkGroups, componentLinkEntry=componentLinkEntry, teLinkIncomingIfId=teLinkIncomingIfId, teLinkDescrMaxLspBandwidthPrio6=teLinkDescrMaxLspBandwidthPrio6, componentLinkPreferredProtection=componentLinkPreferredProtection, teLinkEntry=teLinkEntry, TeLinkBandwidth=TeLinkBandwidth, teLinkBandwidthUnreserved=teLinkBandwidthUnreserved, TeLinkProtection=TeLinkProtection, componentLinkDescrInterfaceMtu=componentLinkDescrInterfaceMtu, teLinkBandwidthTable=teLinkBandwidthTable, componentLinkCurrentProtection=componentLinkCurrentProtection, teLinkLocalIpAddr=teLinkLocalIpAddr, teLinkDescrMaxLspBandwidthPrio1=teLinkDescrMaxLspBandwidthPrio1, teLinkDescrSwitchingCapability=teLinkDescrSwitchingCapability, teLinkTable=teLinkTable, componentLinkDescriptorEntry=componentLinkDescriptorEntry, TeLinkSwitchingCapability=TeLinkSwitchingCapability, componentLinkDescrMaxLspBandwidthPrio2=componentLinkDescrMaxLspBandwidthPrio2, TeLinkPriority=TeLinkPriority, componentLinkDescrMaxLspBandwidthPrio0=componentLinkDescrMaxLspBandwidthPrio0, componentLinkDescrMaxLspBandwidthPrio5=componentLinkDescrMaxLspBandwidthPrio5, teLinkTdmGroup=teLinkTdmGroup, componentLinkTable=componentLinkTable, teLinkMetric=teLinkMetric, teLinkObjects=teLinkObjects, teLinkModuleReadOnlyCompliance=teLinkModuleReadOnlyCompliance, teLinkResourceClass=teLinkResourceClass, teLinkSrlgRowStatus=teLinkSrlgRowStatus, componentLinkBandwidthEntry=componentLinkBandwidthEntry, teLinkOutgoingIfId=teLinkOutgoingIfId, componentLinkBandwidthStorageType=componentLinkBandwidthStorageType, teLinkSrlgTable=teLinkSrlgTable, componentLinkDescrMaxLspBandwidthPrio4=componentLinkDescrMaxLspBandwidthPrio4, componentLinkDescrMaxLspBandwidthPrio3=componentLinkDescrMaxLspBandwidthPrio3, teLinkRemoteIpAddr=teLinkRemoteIpAddr, teLinkCompliances=teLinkCompliances, teLinkDescrInterfaceMtu=teLinkDescrInterfaceMtu, PYSNMP_MODULE_ID=teLinkStdMIB, teLinkDescrMaxLspBandwidthPrio5=teLinkDescrMaxLspBandwidthPrio5, teLinkDescrMaxLspBandwidthPrio0=teLinkDescrMaxLspBandwidthPrio0, componentLinkDescriptorTable=componentLinkDescriptorTable, componentLinkDescrIndication=componentLinkDescrIndication, teLinkSrlgGroup=teLinkSrlgGroup, componentLinkBandwidthPriority=componentLinkBandwidthPriority, componentLinkDescrMinLspBandwidth=componentLinkDescrMinLspBandwidth, teLinkBandwidthStorageType=teLinkBandwidthStorageType, teLinkAddressType=teLinkAddressType, componentLinkDescrSwitchingCapability=componentLinkDescrSwitchingCapability)
