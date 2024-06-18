#
# PySNMP MIB module HUAWEI-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-LLDP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:34:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
lldpPortConfigPortNum, lldpLocSysCapSupported, lldpLocSysCapEnabled = mibBuilder.importSymbols("LLDP-MIB", "lldpPortConfigPortNum", "lldpLocSysCapSupported", "lldpLocSysCapEnabled")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, iso, Bits, MibIdentifier, Unsigned32, Counter64, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "iso", "Bits", "MibIdentifier", "Unsigned32", "Counter64", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "NotificationType", "IpAddress")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
hwLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134))
if mibBuilder.loadTexts: hwLldpMIB.setLastUpdated('200611240000Z')
if mibBuilder.loadTexts: hwLldpMIB.setOrganization('Huawei Technologies co.,Ltd.')
class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hwLldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1))
hwLldpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2))
hwLldpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3))
hwLldpConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1))
hwLldpRemoteSystemData = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 2))
hwLldpEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 1), EnabledStatus().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLldpEnable.setStatus('current')
hwLldpLocManIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLldpLocManIPAddr.setStatus('current')
hwLldpCounterReset = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLldpCounterReset.setStatus('current')
hwLldpNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 4), EnabledStatus().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLldpNotificationEnable.setStatus('current')
hwLldpPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 5), )
if mibBuilder.loadTexts: hwLldpPortConfigTable.setStatus('current')
hwLldpPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 5, 1), ).setIndexNames((0, "LLDP-MIB", "lldpPortConfigPortNum"))
if mibBuilder.loadTexts: hwLldpPortConfigEntry.setStatus('current')
hwLldpPortConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 5, 1, 11), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLldpPortConfigIfIndex.setStatus('current')
hwLldpPortConfigCounterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 5, 1, 12), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLldpPortConfigCounterReset.setStatus('current')
hwLldpRemProtoTypeTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 2, 1), )
if mibBuilder.loadTexts: hwLldpRemProtoTypeTable.setStatus('current')
hwLldpRemProtoTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 2, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpPortConfigPortNum"))
if mibBuilder.loadTexts: hwLldpRemProtoTypeEntry.setStatus('current')
hwLldpRemProtoType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("lldp", 1), ("cdp", 2), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLldpRemProtoType.setStatus('current')
hwLldpEnabled = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 1))
if mibBuilder.loadTexts: hwLldpEnabled.setStatus('current')
hwLldpDisabled = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 2))
if mibBuilder.loadTexts: hwLldpDisabled.setStatus('current')
hwLldpLocSysCapSupportedChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 3)).setObjects(("LLDP-MIB", "lldpLocSysCapSupported"))
if mibBuilder.loadTexts: hwLldpLocSysCapSupportedChange.setStatus('current')
hwLldpLocSysCapEnabledChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 4)).setObjects(("LLDP-MIB", "lldpLocSysCapEnabled"))
if mibBuilder.loadTexts: hwLldpLocSysCapEnabledChange.setStatus('current')
hwLldpLocManIPAddrChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 5)).setObjects(("HUAWEI-LLDP-MIB", "hwLldpLocManIPAddr"))
if mibBuilder.loadTexts: hwLldpLocManIPAddrChange.setStatus('current')
hwLldpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 1))
hwLldpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2))
lldpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 1, 1)).setObjects(("HUAWEI-LLDP-MIB", "hwLldpConfigGroup"), ("HUAWEI-LLDP-MIB", "hwLldpStatsGroup"), ("HUAWEI-LLDP-MIB", "hwLldpPortGroup"), ("HUAWEI-LLDP-MIB", "hwLldpTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpCompliance = lldpCompliance.setStatus('current')
hwLldpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2, 1)).setObjects(("HUAWEI-LLDP-MIB", "hwLldpEnable"), ("HUAWEI-LLDP-MIB", "hwLldpLocManIPAddr"), ("HUAWEI-LLDP-MIB", "hwLldpNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLldpConfigGroup = hwLldpConfigGroup.setStatus('current')
hwLldpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2, 2)).setObjects(("HUAWEI-LLDP-MIB", "hwLldpCounterReset"), ("HUAWEI-LLDP-MIB", "hwLldpPortConfigCounterReset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLldpStatsGroup = hwLldpStatsGroup.setStatus('current')
hwLldpPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2, 3)).setObjects(("HUAWEI-LLDP-MIB", "hwLldpPortConfigIfIndex"), ("HUAWEI-LLDP-MIB", "hwLldpRemProtoType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLldpPortGroup = hwLldpPortGroup.setStatus('current')
hwLldpTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2, 4)).setObjects(("HUAWEI-LLDP-MIB", "hwLldpEnabled"), ("HUAWEI-LLDP-MIB", "hwLldpDisabled"), ("HUAWEI-LLDP-MIB", "hwLldpLocSysCapSupportedChange"), ("HUAWEI-LLDP-MIB", "hwLldpLocSysCapEnabledChange"), ("HUAWEI-LLDP-MIB", "hwLldpLocManIPAddrChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwLldpTrapGroup = hwLldpTrapGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-LLDP-MIB", hwLldpRemoteSystemData=hwLldpRemoteSystemData, hwLldpPortConfigTable=hwLldpPortConfigTable, hwLldpEnable=hwLldpEnable, hwLldpTraps=hwLldpTraps, hwLldpLocManIPAddrChange=hwLldpLocManIPAddrChange, hwLldpLocSysCapSupportedChange=hwLldpLocSysCapSupportedChange, hwLldpPortGroup=hwLldpPortGroup, hwLldpGroups=hwLldpGroups, hwLldpStatsGroup=hwLldpStatsGroup, PYSNMP_MODULE_ID=hwLldpMIB, hwLldpPortConfigEntry=hwLldpPortConfigEntry, hwLldpObjects=hwLldpObjects, hwLldpCompliances=hwLldpCompliances, hwLldpMIB=hwLldpMIB, hwLldpConfiguration=hwLldpConfiguration, hwLldpPortConfigCounterReset=hwLldpPortConfigCounterReset, hwLldpRemProtoTypeTable=hwLldpRemProtoTypeTable, hwLldpNotificationEnable=hwLldpNotificationEnable, hwLldpCounterReset=hwLldpCounterReset, hwLldpRemProtoType=hwLldpRemProtoType, hwLldpLocManIPAddr=hwLldpLocManIPAddr, lldpCompliance=lldpCompliance, hwLldpTrapGroup=hwLldpTrapGroup, hwLldpRemProtoTypeEntry=hwLldpRemProtoTypeEntry, hwLldpLocSysCapEnabledChange=hwLldpLocSysCapEnabledChange, EnabledStatus=EnabledStatus, hwLldpPortConfigIfIndex=hwLldpPortConfigIfIndex, hwLldpConfigGroup=hwLldpConfigGroup, hwLldpEnabled=hwLldpEnabled, hwLldpDisabled=hwLldpDisabled, hwLldpConformance=hwLldpConformance)
