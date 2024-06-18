#
# PySNMP MIB module CISCOSB-rlInterfaces (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-rlInterfaces
# Produced by pysmi-0.3.4 at Mon Apr 29 18:08:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
switch001, rlIfInterfaces = mibBuilder.importSymbols("CISCOSB-MIB", "switch001", "rlIfInterfaces")
ifIndex, InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, ModuleIdentity, Unsigned32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, NotificationType, Bits, MibIdentifier, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "ModuleIdentity", "Unsigned32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "NotificationType", "Bits", "MibIdentifier", "Gauge32", "Integer32")
TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
swInterfaces = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43))
swInterfaces.setRevisions(('2013-04-01 00:00',))
if mibBuilder.loadTexts: swInterfaces.setLastUpdated('201304010000Z')
if mibBuilder.loadTexts: swInterfaces.setOrganization('Cisco Small Business')
class AutoNegCapabilitiesBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("default", 0), ("unknown", 1), ("tenHalf", 2), ("tenFull", 3), ("fastHalf", 4), ("fastFull", 5), ("gigaHalf", 6), ("gigaFull", 7), ("tenGigaFull", 8))

swIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1), )
if mibBuilder.loadTexts: swIfTable.setStatus('current')
swIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1), ).setIndexNames((0, "CISCOSB-rlInterfaces", "swIfIndex"))
if mibBuilder.loadTexts: swIfEntry.setStatus('current')
swIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfIndex.setStatus('current')
swIfPhysAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("reserve", 2))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfPhysAddressType.setStatus('obsolete')
swIfDuplexAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("half", 2), ("full", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfDuplexAdminMode.setStatus('current')
swIfDuplexOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("half", 1), ("full", 2), ("hybrid", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfDuplexOperMode.setStatus('current')
swIfBackPressureMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfBackPressureMode.setStatus('current')
swIfTaggedMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfTaggedMode.setStatus('current')
swIfTransceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("regular", 1), ("fiberOptics", 2), ("comboRegular", 3), ("comboFiberOptics", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfTransceiverType.setStatus('current')
swIfLockAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("locked", 1), ("unlocked", 2))).clone('unlocked')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfLockAdminStatus.setStatus('current')
swIfLockOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("locked", 1), ("unlocked", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfLockOperStatus.setStatus('current')
swIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("eth10M", 1), ("eth100M", 2), ("eth1000M", 3), ("eth10G", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfType.setStatus('current')
swIfDefaultTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfDefaultTag.setStatus('current')
swIfDefaultPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfDefaultPriority.setStatus('current')
swIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 13), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfStatus.setStatus('current')
swIfFlowControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("autoNegotiation", 3), ("enabledRx", 4), ("enabledTx", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfFlowControlMode.setStatus('current')
swIfSpeedAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfSpeedAdminMode.setStatus('current')
swIfSpeedDuplexAutoNegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfSpeedDuplexAutoNegotiation.setStatus('current')
swIfOperFlowControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("enabledRx", 3), ("enabledTx", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperFlowControlMode.setStatus('current')
swIfOperSpeedDuplexAutoNegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("hybrid", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperSpeedDuplexAutoNegotiation.setStatus('current')
swIfOperBackPressureMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("hybrid", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperBackPressureMode.setStatus('current')
swIfAdminLockAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("discard", 1), ("forwardNormal", 2), ("discardDisable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfAdminLockAction.setStatus('current')
swIfOperLockAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("discard", 1), ("forwardNormal", 2), ("discardDisable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperLockAction.setStatus('current')
swIfAdminLockTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 22), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfAdminLockTrapEnable.setStatus('current')
swIfOperLockTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 23), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperLockTrapEnable.setStatus('current')
swIfOperSuspendedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 24), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperSuspendedStatus.setStatus('current')
swIfLockOperTrapCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfLockOperTrapCount.setStatus('current')
swIfLockAdminTrapFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfLockAdminTrapFrequency.setStatus('current')
swIfReActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 27), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfReActivate.setStatus('current')
swIfAdminMdix = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cross", 1), ("normal", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfAdminMdix.setStatus('current')
swIfOperMdix = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cross", 1), ("normal", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperMdix.setStatus('current')
swIfHostMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("single", 1), ("multiple", 2), ("multiple-auth", 3))).clone('single')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfHostMode.setStatus('current')
swIfSingleHostViolationAdminAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("discard", 1), ("forwardNormal", 2), ("discardDisable", 3))).clone('discard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfSingleHostViolationAdminAction.setStatus('current')
swIfSingleHostViolationOperAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("discard", 1), ("forwardNormal", 2), ("discardDisable", 3))).clone('discard')).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfSingleHostViolationOperAction.setStatus('current')
swIfSingleHostViolationAdminTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 33), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfSingleHostViolationAdminTrapEnable.setStatus('current')
swIfSingleHostViolationOperTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 34), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfSingleHostViolationOperTrapEnable.setStatus('current')
swIfSingleHostViolationOperTrapCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 35), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfSingleHostViolationOperTrapCount.setStatus('current')
swIfSingleHostViolationAdminTrapFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 36), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfSingleHostViolationAdminTrapFrequency.setStatus('current')
swIfLockLimitationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("dynamic", 2), ("secure-permanent", 3), ("secure-delete-on-reset", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfLockLimitationMode.setStatus('current')
swIfLockMaxMacAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 38), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfLockMaxMacAddresses.setStatus('current')
swIfLockMacAddressesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 39), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfLockMacAddressesCount.setStatus('current')
swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 40), AutoNegCapabilitiesBits().clone(namedValues=NamedValues(("default", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities.setStatus('current')
swIfOperSpeedDuplexAutoNegotiationLocalCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 41), AutoNegCapabilitiesBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperSpeedDuplexAutoNegotiationLocalCapabilities.setStatus('current')
swIfSpeedDuplexNegotiationRemoteCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 42), AutoNegCapabilitiesBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfSpeedDuplexNegotiationRemoteCapabilities.setStatus('current')
swIfAdminComboMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 43), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("force-fiber", 1), ("force-copper", 2), ("prefer-fiber", 3), ("prefer-copper", 4))).clone('prefer-fiber')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfAdminComboMode.setStatus('current')
swIfOperComboMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 44), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fiber", 1), ("copper", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfOperComboMode.setStatus('current')
swIfAutoNegotiationMasterSlavePreference = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 1, 1, 45), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("preferMaster", 1), ("preferSlave", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfAutoNegotiationMasterSlavePreference.setStatus('current')
swIfMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfMibVersion.setStatus('current')
swIfPortLockSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfPortLockSupport.setStatus('current')
swIfPortLockActionSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfPortLockActionSupport.setStatus('current')
swIfPortLockTrapSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfPortLockTrapSupport.setStatus('current')
swIfPortLockIfRangeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 6), )
if mibBuilder.loadTexts: swIfPortLockIfRangeTable.setStatus('current')
swIfPortLockIfRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 6, 1), ).setIndexNames((0, "CISCOSB-rlInterfaces", "swIfPortLockIfRangeIndex"))
if mibBuilder.loadTexts: swIfPortLockIfRangeEntry.setStatus('current')
swIfPortLockIfRangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIfPortLockIfRangeIndex.setStatus('current')
swIfPortLockIfRange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 6, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfPortLockIfRange.setStatus('current')
swIfPortLockIfRangeLockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("locked", 1), ("unlocked", 2))).clone('unlocked')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfPortLockIfRangeLockStatus.setStatus('current')
swIfPortLockIfRangeAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("discard", 1), ("forwardNormal", 2), ("discardDisable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfPortLockIfRangeAction.setStatus('current')
swIfPortLockIfRangeTrapEn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 6, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfPortLockIfRangeTrapEn.setStatus('current')
swIfPortLockIfRangeTrapFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfPortLockIfRangeTrapFreq.setStatus('current')
swIfExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 7), )
if mibBuilder.loadTexts: swIfExtTable.setStatus('current')
swIfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: swIfExtEntry.setStatus('current')
swIfExtSFPSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("default", 1), ("eth100M", 2), ("eth1G", 3))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIfExtSFPSpeed.setStatus('current')
rlIfMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfMibVersion.setStatus('current')
rlIfNumOfPhPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfNumOfPhPorts.setStatus('current')
rlIfMapOfOnPhPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfMapOfOnPhPorts.setStatus('current')
rlIfClearPortMibCounters = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfClearPortMibCounters.setStatus('current')
rlIfNumOfUserDefinedPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfNumOfUserDefinedPorts.setStatus('current')
rlIfFirstOutOfBandIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfFirstOutOfBandIfIndex.setStatus('current')
rlIfNumOfLoopbackPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfNumOfLoopbackPorts.setStatus('current')
rlIfFirstLoopbackIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfFirstLoopbackIfIndex.setStatus('current')
rlIfExistingPortList = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 9), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfExistingPortList.setStatus('current')
rlIfBaseMACAddressPerIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfBaseMACAddressPerIfIndex.setStatus('current')
rlFlowControlCascadeMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFlowControlCascadeMode.setStatus('current')
rlFlowControlCascadeType = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internalonly", 1), ("internalexternal", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFlowControlCascadeType.setStatus('current')
rlFlowControlRxPerSystem = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFlowControlRxPerSystem.setStatus('current')
rlCascadePortProtectionAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 14), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCascadePortProtectionAction.setStatus('current')
rlManagementIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 15), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlManagementIfIndex.setStatus('current')
rlIfClearStackPortsCounters = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 16), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfClearStackPortsCounters.setStatus('current')
rlIfClearPortMacAddresses = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 17), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfClearPortMacAddresses.setStatus('current')
rlIfCutThroughPacketLength = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(257, 16383)).clone(1522)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfCutThroughPacketLength.setStatus('current')
rlIfCutPriorityZero = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 19), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfCutPriorityZero.setStatus('current')
rlIfCutPriorityOne = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 20), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfCutPriorityOne.setStatus('current')
rlIfCutPriorityTwo = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 21), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfCutPriorityTwo.setStatus('current')
rlIfCutPriorityThree = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 22), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfCutPriorityThree.setStatus('current')
rlIfCutPriorityFour = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 23), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfCutPriorityFour.setStatus('current')
rlIfCutPriorityFive = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 24), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfCutPriorityFive.setStatus('current')
rlIfCutPrioritySix = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 25), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfCutPrioritySix.setStatus('current')
rlIfCutPrioritySeven = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 26), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfCutPrioritySeven.setStatus('current')
rlIfCutThroughTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 27), )
if mibBuilder.loadTexts: rlIfCutThroughTable.setStatus('current')
rlIfCutThroughEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 27, 1), ).setIndexNames((0, "CISCOSB-rlInterfaces", "swIfIndex"))
if mibBuilder.loadTexts: rlIfCutThroughEntry.setStatus('current')
rlIfCutThroughPriorityEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 27, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfCutThroughPriorityEnable.setStatus('current')
rlIfCutThroughUntaggedEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 27, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIfCutThroughUntaggedEnable.setStatus('current')
rlIfCutThroughOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 27, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIfCutThroughOperMode.setStatus('current')
rlCutThroughPacketLength = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCutThroughPacketLength.setStatus('current')
rlCutThroughPacketLengthAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(257, 16383)).clone(1522)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCutThroughPacketLengthAfterReset.setStatus('current')
rlCutThroughEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 30), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCutThroughEnable.setStatus('current')
rlCutThroughEnableAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 31), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCutThroughEnableAfterReset.setStatus('current')
rlFlowControlMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("send-receive", 1), ("receive-only", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFlowControlMode.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-rlInterfaces", swIfReActivate=swIfReActivate, swIfAdminComboMode=swIfAdminComboMode, swIfAutoNegotiationMasterSlavePreference=swIfAutoNegotiationMasterSlavePreference, swIfOperMdix=swIfOperMdix, swIfLockLimitationMode=swIfLockLimitationMode, rlIfCutPrioritySix=rlIfCutPrioritySix, rlIfClearStackPortsCounters=rlIfClearStackPortsCounters, rlManagementIfIndex=rlManagementIfIndex, swIfPortLockTrapSupport=swIfPortLockTrapSupport, swIfLockAdminTrapFrequency=swIfLockAdminTrapFrequency, swIfSpeedAdminMode=swIfSpeedAdminMode, swIfAdminLockTrapEnable=swIfAdminLockTrapEnable, swIfBackPressureMode=swIfBackPressureMode, swIfSingleHostViolationAdminTrapEnable=swIfSingleHostViolationAdminTrapEnable, swIfTransceiverType=swIfTransceiverType, swIfLockMacAddressesCount=swIfLockMacAddressesCount, rlIfCutThroughPriorityEnable=rlIfCutThroughPriorityEnable, swIfPortLockIfRangeIndex=swIfPortLockIfRangeIndex, rlFlowControlCascadeMode=rlFlowControlCascadeMode, swIfSpeedDuplexNegotiationRemoteCapabilities=swIfSpeedDuplexNegotiationRemoteCapabilities, swIfAdminLockAction=swIfAdminLockAction, rlIfNumOfUserDefinedPorts=rlIfNumOfUserDefinedPorts, swIfMibVersion=swIfMibVersion, rlIfCutThroughUntaggedEnable=rlIfCutThroughUntaggedEnable, swIfTable=swIfTable, swIfExtSFPSpeed=swIfExtSFPSpeed, swIfPortLockIfRangeTable=swIfPortLockIfRangeTable, swIfExtTable=swIfExtTable, rlFlowControlMode=rlFlowControlMode, swIfPortLockIfRange=swIfPortLockIfRange, rlIfFirstLoopbackIfIndex=rlIfFirstLoopbackIfIndex, rlIfCutPriorityZero=rlIfCutPriorityZero, swIfSpeedDuplexAutoNegotiation=swIfSpeedDuplexAutoNegotiation, rlCascadePortProtectionAction=rlCascadePortProtectionAction, rlIfCutPriorityOne=rlIfCutPriorityOne, swIfPortLockIfRangeLockStatus=swIfPortLockIfRangeLockStatus, swIfDefaultTag=swIfDefaultTag, swIfOperFlowControlMode=swIfOperFlowControlMode, rlIfCutThroughTable=rlIfCutThroughTable, rlIfClearPortMibCounters=rlIfClearPortMibCounters, swIfDefaultPriority=swIfDefaultPriority, rlIfCutThroughOperMode=rlIfCutThroughOperMode, swIfAdminMdix=swIfAdminMdix, swIfLockOperStatus=swIfLockOperStatus, rlIfMibVersion=rlIfMibVersion, swIfLockAdminStatus=swIfLockAdminStatus, swIfPhysAddressType=swIfPhysAddressType, swIfOperSuspendedStatus=swIfOperSuspendedStatus, swIfPortLockActionSupport=swIfPortLockActionSupport, swIfSingleHostViolationOperTrapEnable=swIfSingleHostViolationOperTrapEnable, swIfSingleHostViolationAdminAction=swIfSingleHostViolationAdminAction, rlIfBaseMACAddressPerIfIndex=rlIfBaseMACAddressPerIfIndex, rlIfNumOfPhPorts=rlIfNumOfPhPorts, swIfPortLockIfRangeAction=swIfPortLockIfRangeAction, swIfDuplexOperMode=swIfDuplexOperMode, swIfOperSpeedDuplexAutoNegotiation=swIfOperSpeedDuplexAutoNegotiation, swIfLockOperTrapCount=swIfLockOperTrapCount, swIfOperSpeedDuplexAutoNegotiationLocalCapabilities=swIfOperSpeedDuplexAutoNegotiationLocalCapabilities, swIfStatus=swIfStatus, swIfSingleHostViolationOperTrapCount=swIfSingleHostViolationOperTrapCount, rlIfFirstOutOfBandIfIndex=rlIfFirstOutOfBandIfIndex, swIfEntry=swIfEntry, swIfHostMode=swIfHostMode, swIfType=swIfType, swIfDuplexAdminMode=swIfDuplexAdminMode, rlIfCutThroughEntry=rlIfCutThroughEntry, swIfLockMaxMacAddresses=swIfLockMaxMacAddresses, rlFlowControlCascadeType=rlFlowControlCascadeType, swIfPortLockIfRangeEntry=swIfPortLockIfRangeEntry, swIfIndex=swIfIndex, rlIfCutThroughPacketLength=rlIfCutThroughPacketLength, rlIfCutPriorityFour=rlIfCutPriorityFour, rlCutThroughPacketLength=rlCutThroughPacketLength, swIfPortLockSupport=swIfPortLockSupport, rlIfNumOfLoopbackPorts=rlIfNumOfLoopbackPorts, PYSNMP_MODULE_ID=swInterfaces, swIfOperBackPressureMode=swIfOperBackPressureMode, swInterfaces=swInterfaces, rlIfCutPrioritySeven=rlIfCutPrioritySeven, swIfOperComboMode=swIfOperComboMode, swIfOperLockTrapEnable=swIfOperLockTrapEnable, rlIfMapOfOnPhPorts=rlIfMapOfOnPhPorts, AutoNegCapabilitiesBits=AutoNegCapabilitiesBits, swIfExtEntry=swIfExtEntry, swIfPortLockIfRangeTrapEn=swIfPortLockIfRangeTrapEn, rlCutThroughEnable=rlCutThroughEnable, swIfTaggedMode=swIfTaggedMode, rlIfCutPriorityFive=rlIfCutPriorityFive, rlFlowControlRxPerSystem=rlFlowControlRxPerSystem, swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities=swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities, swIfFlowControlMode=swIfFlowControlMode, rlCutThroughPacketLengthAfterReset=rlCutThroughPacketLengthAfterReset, rlCutThroughEnableAfterReset=rlCutThroughEnableAfterReset, swIfSingleHostViolationOperAction=swIfSingleHostViolationOperAction, swIfOperLockAction=swIfOperLockAction, swIfPortLockIfRangeTrapFreq=swIfPortLockIfRangeTrapFreq, rlIfClearPortMacAddresses=rlIfClearPortMacAddresses, rlIfCutPriorityTwo=rlIfCutPriorityTwo, swIfSingleHostViolationAdminTrapFrequency=swIfSingleHostViolationAdminTrapFrequency, rlIfCutPriorityThree=rlIfCutPriorityThree, rlIfExistingPortList=rlIfExistingPortList)
