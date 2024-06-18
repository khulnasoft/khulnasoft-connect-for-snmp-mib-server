#
# PySNMP MIB module SERVICE-LOCATION-PROTOCOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SERVICE-LOCATION-PROTOCOL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:53:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, Counter32, TimeTicks, Bits, ModuleIdentity, iso, ObjectIdentity, Counter64, Unsigned32, IpAddress, NotificationType, MibIdentifier, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "Counter32", "TimeTicks", "Bits", "ModuleIdentity", "iso", "ObjectIdentity", "Counter64", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
slpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 999))
if mibBuilder.loadTexts: slpMIB.setLastUpdated('200203010000Z')
if mibBuilder.loadTexts: slpMIB.setOrganization('SLP Project (at Source Forge)')
slpMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1))
slpMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 2))
slpMIBObjectGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 2, 2))
class SlpAgentTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("da", 1), ("sa", 2), ("ua", 3))

class SlpScopeSourceTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("static", 1), ("staticDA", 2), ("dhcp", 3), ("dhcpDA", 4), ("dynamicDA", 5), ("dynamicSA", 6), ("default", 7))

class SlpAttributeTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("attrBoolean", 1), ("attrInteger", 2), ("attrString", 3), ("attrOpaque", 4), ("attrKeyword", 5))

slpAgent = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1, 1))
slpAgentTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 1, 1), )
if mibBuilder.loadTexts: slpAgentTable.setStatus('current')
slpAgentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1), ).setIndexNames((0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIndex"))
if mibBuilder.loadTexts: slpAgentEntry.setStatus('current')
slpAgentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: slpAgentIndex.setStatus('current')
slpAgentSWInstalledIndexOrZero = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentSWInstalledIndexOrZero.setStatus('current')
slpAgentName = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentName.setStatus('current')
slpAgentType = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 4), SlpAgentTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentType.setStatus('current')
slpAgentIsBroadcastOnly = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentIsBroadcastOnly.setStatus('current')
slpAgentActiveDADiscovery = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentActiveDADiscovery.setStatus('current')
slpAgentPassiveDADiscovery = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 7), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentPassiveDADiscovery.setStatus('current')
slpAgentMessageTypesSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentMessageTypesSupported.setStatus('current')
slpAgentExtensionsSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAgentExtensionsSupported.setStatus('current')
slpScope = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1, 2))
slpScopeTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 2, 1), )
if mibBuilder.loadTexts: slpScopeTable.setStatus('current')
slpScopeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1), ).setIndexNames((0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIndex"), (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpScopeIndex"))
if mibBuilder.loadTexts: slpScopeEntry.setStatus('current')
slpScopeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: slpScopeIndex.setStatus('current')
slpScopeSource = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 2), SlpScopeSourceTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpScopeSource.setStatus('current')
slpScopeValue = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 2, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpScopeValue.setStatus('current')
slpAddress = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1, 3))
slpAddressTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 3, 1), )
if mibBuilder.loadTexts: slpAddressTable.setStatus('current')
slpAddressEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1), ).setIndexNames((0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIndex"), (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressIndex"))
if mibBuilder.loadTexts: slpAddressEntry.setStatus('current')
slpAddressIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: slpAddressIndex.setStatus('current')
slpAddressAgentType = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 2), SlpAgentTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAddressAgentType.setStatus('current')
slpAddressSource = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 3), SlpScopeSourceTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAddressSource.setStatus('current')
slpAddressOrName = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 3, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAddressOrName.setStatus('current')
slpAttribute = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1, 4))
slpAttributeTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 4, 1), )
if mibBuilder.loadTexts: slpAttributeTable.setStatus('current')
slpAttributeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1), ).setIndexNames((0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIndex"), (0, "SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeIndex"))
if mibBuilder.loadTexts: slpAttributeEntry.setStatus('current')
slpAttributeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: slpAttributeIndex.setStatus('current')
slpAttributeName = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAttributeName.setStatus('current')
slpAttributeType = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 3), SlpAttributeTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAttributeType.setStatus('current')
slpAttributeValue = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 4, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slpAttributeValue.setStatus('current')
slpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 999, 2, 1)).setObjects(("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentGroup"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpScopeGroup"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressGroup"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slpMIBCompliance = slpMIBCompliance.setStatus('current')
slpAgentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 2, 2, 1)).setObjects(("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentSWInstalledIndexOrZero"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentName"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentType"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentIsBroadcastOnly"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentActiveDADiscovery"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentPassiveDADiscovery"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentMessageTypesSupported"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAgentExtensionsSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slpAgentGroup = slpAgentGroup.setStatus('current')
slpScopeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 2, 2, 2)).setObjects(("SERVICE-LOCATION-PROTOCOL-MIB", "slpScopeSource"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpScopeValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slpScopeGroup = slpScopeGroup.setStatus('current')
slpAddressGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 2, 2, 3)).setObjects(("SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressAgentType"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressSource"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAddressOrName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slpAddressGroup = slpAddressGroup.setStatus('current')
slpAttributeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 2, 2, 4)).setObjects(("SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeName"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeType"), ("SERVICE-LOCATION-PROTOCOL-MIB", "slpAttributeValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    slpAttributeGroup = slpAttributeGroup.setStatus('current')
mibBuilder.exportSymbols("SERVICE-LOCATION-PROTOCOL-MIB", slpAddressSource=slpAddressSource, slpScopeIndex=slpScopeIndex, slpScopeEntry=slpScopeEntry, SlpScopeSourceTC=SlpScopeSourceTC, slpAgentType=slpAgentType, slpAttributeGroup=slpAttributeGroup, slpMIBObjectGroups=slpMIBObjectGroups, slpAgentGroup=slpAgentGroup, slpAttribute=slpAttribute, slpAgentIndex=slpAgentIndex, slpAddressTable=slpAddressTable, slpAddress=slpAddress, slpMIBObjects=slpMIBObjects, slpAgentTable=slpAgentTable, slpScope=slpScope, slpScopeGroup=slpScopeGroup, slpAttributeEntry=slpAttributeEntry, slpAgentActiveDADiscovery=slpAgentActiveDADiscovery, SlpAgentTypeTC=SlpAgentTypeTC, slpAgentMessageTypesSupported=slpAgentMessageTypesSupported, slpAgentEntry=slpAgentEntry, slpMIBCompliance=slpMIBCompliance, slpAgent=slpAgent, slpAddressGroup=slpAddressGroup, slpAgentIsBroadcastOnly=slpAgentIsBroadcastOnly, slpMIBConformance=slpMIBConformance, SlpAttributeTypeTC=SlpAttributeTypeTC, slpMIB=slpMIB, slpAddressEntry=slpAddressEntry, slpScopeTable=slpScopeTable, slpAttributeName=slpAttributeName, PYSNMP_MODULE_ID=slpMIB, slpAgentExtensionsSupported=slpAgentExtensionsSupported, slpAddressOrName=slpAddressOrName, slpAttributeValue=slpAttributeValue, slpAttributeTable=slpAttributeTable, slpAgentName=slpAgentName, slpScopeValue=slpScopeValue, slpAgentPassiveDADiscovery=slpAgentPassiveDADiscovery, slpAttributeType=slpAttributeType, slpAttributeIndex=slpAttributeIndex, slpScopeSource=slpScopeSource, slpAddressIndex=slpAddressIndex, slpAgentSWInstalledIndexOrZero=slpAgentSWInstalledIndexOrZero, slpAddressAgentType=slpAddressAgentType)
