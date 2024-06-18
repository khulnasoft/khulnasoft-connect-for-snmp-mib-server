#
# PySNMP MIB module Fore-Lane-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Lane-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
systems, NsapAddr, AtmAddress, EntryStatus = mibBuilder.importSymbols("Fore-Common-MIB", "systems", "NsapAddr", "AtmAddress", "EntryStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, ModuleIdentity, Gauge32, MibIdentifier, Bits, Counter32, ObjectIdentity, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32", "MibIdentifier", "Bits", "Counter32", "ObjectIdentity", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Integer32")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
foreLaneModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 4))
if mibBuilder.loadTexts: foreLaneModule.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: foreLaneModule.setOrganization('FORE')
class LecConfigType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("wellknown", 1), ("manual", 2))

class LaneDataFrameFormat(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unspecified", 1), ("aflane8023", 2), ("aflane8025", 3))

class LaneDataFrameSize(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unspecified", 1), ("max1516", 2), ("max4544", 3), ("max9234", 4), ("max18190", 5), ("max1580", 6))

laneLecGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 1))
lecConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1))
lecStatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 2))
lecArpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3))
laneLesGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 2))
lesConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1))
lesStatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 2))
laneBusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 3))
busConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1))
busStatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 2))
laneLecsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 4))
lecsConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1))
lecsStatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 2))
laneMibExtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 5))
lecDefaultLecsConfigType = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 1), LecConfigType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecDefaultLecsConfigType.setStatus('current')
lecDefaultLecsAtmAddress = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 2), AtmAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecDefaultLecsAtmAddress.setStatus('current')
lecConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10), )
if mibBuilder.loadTexts: lecConfTable.setStatus('current')
lecConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1), ).setIndexNames((0, "Fore-Lane-MIB", "lecConfIndex"))
if mibBuilder.loadTexts: lecConfEntry.setStatus('current')
lecConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConfIndex.setStatus('current')
lecConfAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 2), AtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecConfAtmAddress.setStatus('current')
lecConfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecConfAdminStatus.setStatus('current')
lecConfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("joining", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConfOperStatus.setStatus('current')
lecConfElanName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecConfElanName.setStatus('current')
lecConfMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConfMacAddress.setStatus('current')
lecConfLecsConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 7), LecConfigType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecConfLecsConfigType.setStatus('current')
lecConfLecsAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 8), AtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecConfLecsAtmAddress.setStatus('current')
lecConfLesAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 9), AtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecConfLesAtmAddress.setStatus('current')
lecConfEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 10), EntryStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecConfEntryStatus.setStatus('current')
lecConfIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 1, 10, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecConfIfName.setStatus('current')
elarpFlush = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elarpFlush.setStatus('current')
lecArpTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10), )
if mibBuilder.loadTexts: lecArpTable.setStatus('current')
lecArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1), ).setIndexNames((0, "Fore-Lane-MIB", "lecArpMacAddress"))
if mibBuilder.loadTexts: lecArpEntry.setStatus('current')
lecArpMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecArpMacAddress.setStatus('current')
lecArpAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 2), AtmAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecArpAtmAddress.setStatus('current')
lecArpFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("incomplete", 1), ("loopback", 2), ("pending", 3), ("valid", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecArpFlags.setStatus('current')
lecArpConnVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecArpConnVPI.setStatus('current')
lecArpConnVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecArpConnVCI.setStatus('current')
lecArpFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lecArpFlush.setStatus('current')
lecArpElanName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 1, 3, 10, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecArpElanName.setStatus('current')
lesConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1), )
if mibBuilder.loadTexts: lesConfTable.setStatus('current')
lesConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1), ).setIndexNames((0, "Fore-Lane-MIB", "lesConfIndex"))
if mibBuilder.loadTexts: lesConfEntry.setStatus('current')
lesConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lesConfIndex.setStatus('current')
lesConfAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 2), AtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfAtmAddress.setStatus('current')
lesConfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfAdminStatus.setStatus('current')
lesConfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lesConfOperStatus.setStatus('current')
lesConfElanName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfElanName.setStatus('current')
lesConfBusAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 6), AtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfBusAtmAddress.setStatus('current')
lesConfBusMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfBusMaster.setStatus('deprecated')
lesConfEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 8), EntryStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfEntryStatus.setStatus('current')
lesConfLanType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 9), LaneDataFrameFormat()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfLanType.setStatus('current')
lesConfMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 10), LaneDataFrameSize()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfMaxFrameSize.setStatus('current')
lesConfSecureServer = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfSecureServer.setStatus('current')
lesConfLECSAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 12), AtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfLECSAtmAddress.setStatus('current')
lesConfAnycastAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 13), AtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfAnycastAtmAddress.setStatus('current')
lesConfRegisterTLVs = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfRegisterTLVs.setStatus('current')
lesConfElanId = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfElanId.setStatus('current')
lesConfTokenRingNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfTokenRingNumber.setStatus('current')
lesConfForwardArp = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lesConfForwardArp.setStatus('current')
lesLnniConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 2), )
if mibBuilder.loadTexts: lesLnniConfTable.setStatus('current')
lesLnniConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 2, 1), ).setIndexNames((0, "Fore-Lane-MIB", "lesConfIndex"), (0, "Fore-Lane-MIB", "lesLnniConfAtmAddress"))
if mibBuilder.loadTexts: lesLnniConfEntry.setStatus('current')
lesLnniConfAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 2, 1, 1), NsapAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lesLnniConfAtmAddress.setStatus('current')
lesLnniConfEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 2, 1, 2), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesLnniConfEntryStatus.setStatus('current')
lesLeqGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3))
lesLeqConfLesId = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesLeqConfLesId.setStatus('current')
lesLeqTableReload = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("idle", 1), ("go", 2), ("inProgress", 3), ("succeeded", 4), ("failed", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lesLeqTableReload.setStatus('current')
lesLeqStatLesId = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lesLeqStatLesId.setStatus('current')
lesLeqLastTime = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lesLeqLastTime.setStatus('current')
lesLeqTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 5), )
if mibBuilder.loadTexts: lesLeqTable.setStatus('current')
lesLeqEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 5, 1), ).setIndexNames((0, "Fore-Lane-MIB", "lesLeqIndex"))
if mibBuilder.loadTexts: lesLeqEntry.setStatus('current')
lesLeqIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lesLeqIndex.setStatus('current')
lesLeqNsap = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 5, 1, 2), NsapAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lesLeqNsap.setStatus('current')
lesLeqName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 2, 1, 3, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lesLeqName.setStatus('current')
busConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1), )
if mibBuilder.loadTexts: busConfTable.setStatus('deprecated')
busConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1), ).setIndexNames((0, "Fore-Lane-MIB", "busConfIndex"))
if mibBuilder.loadTexts: busConfEntry.setStatus('deprecated')
busConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: busConfIndex.setStatus('deprecated')
busConfAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 2), AtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: busConfAtmAddress.setStatus('deprecated')
busConfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: busConfAdminStatus.setStatus('deprecated')
busConfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: busConfOperStatus.setStatus('deprecated')
busConfName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: busConfName.setStatus('deprecated')
busConfEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 6), EntryStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: busConfEntryStatus.setStatus('deprecated')
busConfLanType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 7), LaneDataFrameFormat()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: busConfLanType.setStatus('deprecated')
busConfMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 3, 1, 1, 1, 8), LaneDataFrameSize()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: busConfMaxFrameSize.setStatus('deprecated')
lecsConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1), )
if mibBuilder.loadTexts: lecsConfTable.setStatus('current')
lecsConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1), ).setIndexNames((0, "Fore-Lane-MIB", "lecsConfIndex"))
if mibBuilder.loadTexts: lecsConfEntry.setStatus('current')
lecsConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsConfIndex.setStatus('current')
lecsConfAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 2), AtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecsConfAtmAddress.setStatus('current')
lecsConfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecsConfAdminStatus.setStatus('current')
lecsConfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lecsConfOperStatus.setStatus('current')
lecsConfDatabase = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecsConfDatabase.setStatus('current')
lecsConfEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 6), EntryStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecsConfEntryStatus.setStatus('current')
lecsConfDefaultLesFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecsConfDefaultLesFlag.setStatus('current')
lecsConfDefaultLesAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 8), AtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecsConfDefaultLesAtmAddress.setStatus('current')
lecsConfWellKnownAddressFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("atm-forum", 2), ("other", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecsConfWellKnownAddressFlag.setStatus('current')
lecsConfWellKnownAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 4, 4, 1, 1, 1, 10), AtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lecsConfWellKnownAddress.setStatus('current')
mibBuilder.exportSymbols("Fore-Lane-MIB", lecsConfWellKnownAddressFlag=lecsConfWellKnownAddressFlag, lecConfLecsAtmAddress=lecConfLecsAtmAddress, laneLecsGroup=laneLecsGroup, lecConfTable=lecConfTable, lecConfAdminStatus=lecConfAdminStatus, lecConfEntryStatus=lecConfEntryStatus, lecsConfDatabase=lecsConfDatabase, lesConfEntry=lesConfEntry, lesLeqIndex=lesLeqIndex, elarpFlush=elarpFlush, busConfIndex=busConfIndex, lecArpConnVPI=lecArpConnVPI, lesConfLanType=lesConfLanType, lesLeqTable=lesLeqTable, lecsConfIndex=lecsConfIndex, LecConfigType=LecConfigType, busConfAdminStatus=busConfAdminStatus, busConfTable=busConfTable, LaneDataFrameFormat=LaneDataFrameFormat, LaneDataFrameSize=LaneDataFrameSize, lecArpGroup=lecArpGroup, lecArpFlush=lecArpFlush, lesLnniConfEntry=lesLnniConfEntry, lecArpEntry=lecArpEntry, lesLeqStatLesId=lesLeqStatLesId, lecConfAtmAddress=lecConfAtmAddress, lesConfElanName=lesConfElanName, busConfGroup=busConfGroup, lecConfOperStatus=lecConfOperStatus, lecDefaultLecsConfigType=lecDefaultLecsConfigType, lesConfBusAtmAddress=lesConfBusAtmAddress, PYSNMP_MODULE_ID=foreLaneModule, lecDefaultLecsAtmAddress=lecDefaultLecsAtmAddress, lesConfAtmAddress=lesConfAtmAddress, busConfEntryStatus=busConfEntryStatus, lecArpTable=lecArpTable, lecsConfEntryStatus=lecsConfEntryStatus, busConfAtmAddress=busConfAtmAddress, lecsConfDefaultLesFlag=lecsConfDefaultLesFlag, lecConfIndex=lecConfIndex, lecArpConnVCI=lecArpConnVCI, lesConfLECSAtmAddress=lesConfLECSAtmAddress, laneBusGroup=laneBusGroup, lesLeqLastTime=lesLeqLastTime, busConfMaxFrameSize=busConfMaxFrameSize, lecConfLecsConfigType=lecConfLecsConfigType, lecsConfOperStatus=lecsConfOperStatus, lesStatGroup=lesStatGroup, lecsConfDefaultLesAtmAddress=lecsConfDefaultLesAtmAddress, lesLeqConfLesId=lesLeqConfLesId, lesLnniConfTable=lesLnniConfTable, laneMibExtGroup=laneMibExtGroup, lecConfElanName=lecConfElanName, lesLeqName=lesLeqName, busConfEntry=busConfEntry, lecsConfEntry=lecsConfEntry, lesConfOperStatus=lesConfOperStatus, busConfName=busConfName, lecsConfTable=lecsConfTable, lecConfMacAddress=lecConfMacAddress, laneLesGroup=laneLesGroup, lecsConfWellKnownAddress=lecsConfWellKnownAddress, laneLecGroup=laneLecGroup, lecConfLesAtmAddress=lecConfLesAtmAddress, lesConfAnycastAtmAddress=lesConfAnycastAtmAddress, lecArpElanName=lecArpElanName, lecArpFlags=lecArpFlags, lesConfForwardArp=lesConfForwardArp, lecConfGroup=lecConfGroup, lecConfIfName=lecConfIfName, foreLaneModule=foreLaneModule, lesConfGroup=lesConfGroup, lesConfElanId=lesConfElanId, lesConfMaxFrameSize=lesConfMaxFrameSize, lesConfAdminStatus=lesConfAdminStatus, lecArpAtmAddress=lecArpAtmAddress, lesConfEntryStatus=lesConfEntryStatus, lesLnniConfEntryStatus=lesLnniConfEntryStatus, lesLeqEntry=lesLeqEntry, lecStatGroup=lecStatGroup, lesLnniConfAtmAddress=lesLnniConfAtmAddress, lesLeqTableReload=lesLeqTableReload, lesConfTable=lesConfTable, lecConfEntry=lecConfEntry, lesConfSecureServer=lesConfSecureServer, lesLeqNsap=lesLeqNsap, lecsConfAdminStatus=lecsConfAdminStatus, lesConfRegisterTLVs=lesConfRegisterTLVs, lecsConfAtmAddress=lecsConfAtmAddress, lesConfBusMaster=lesConfBusMaster, busStatGroup=busStatGroup, lesConfTokenRingNumber=lesConfTokenRingNumber, lecArpMacAddress=lecArpMacAddress, busConfOperStatus=busConfOperStatus, lesLeqGroup=lesLeqGroup, lecsConfGroup=lecsConfGroup, lecsStatGroup=lecsStatGroup, lesConfIndex=lesConfIndex, busConfLanType=busConfLanType)
