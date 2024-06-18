#
# PySNMP MIB module CISCO-DOT11-SSID-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-SSID-SECURITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
CDot11IfVlanIdOrZero, = mibBuilder.importSymbols("CISCO-DOT11-IF-MIB", "CDot11IfVlanIdOrZero")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
dot11AuthenticationAlgorithmsIndex, = mibBuilder.importSymbols("IEEE802dot11-MIB", "dot11AuthenticationAlgorithmsIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, NotificationType, Counter64, IpAddress, Integer32, ObjectIdentity, Unsigned32, iso, Gauge32, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "NotificationType", "Counter64", "IpAddress", "Integer32", "ObjectIdentity", "Unsigned32", "iso", "Gauge32", "Bits", "Counter32")
MacAddress, DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
ciscoDot11SsidSecMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 413))
ciscoDot11SsidSecMIB.setRevisions(('2007-04-12 00:00', '2006-05-16 00:00', '2004-09-14 00:00', '2004-05-15 00:00',))
if mibBuilder.loadTexts: ciscoDot11SsidSecMIB.setLastUpdated('200704120000Z')
if mibBuilder.loadTexts: ciscoDot11SsidSecMIB.setOrganization('Cisco System Inc.')
ciscoDot11SsidSecMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 413, 1))
cdot11SecSsidManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1))
cdot11SecAuthManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 2))
cdot11SecStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 3))
cdot11SecVlanManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 4))
class CDot11SecAuthKeyMgmtType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("cckm", 0), ("wpa", 1), ("wpa1", 2), ("wpa2", 3))

class CDot11WiFiPaPreSharedKey(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CDot11SsidString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class CDot11VlanName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class CDot11InformationElementType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ssidl", 0), ("advertisement", 1), ("wps", 2))

cdot11SecAuxSsidTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1), )
if mibBuilder.loadTexts: cdot11SecAuxSsidTable.setStatus('current')
cdot11SecAuxSsidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsid"))
if mibBuilder.loadTexts: cdot11SecAuxSsidEntry.setStatus('current')
cdot11SecAuxSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 1), CDot11SsidString())
if mibBuilder.loadTexts: cdot11SecAuxSsid.setStatus('current')
cdot11SecAuxSsidBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidBroadcast.setStatus('current')
cdot11SecAuxSsidInfraStruct = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("infraStructure", 1), ("nonInfraStructure", 2), ("optional", 3))).clone('nonInfraStructure')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidInfraStruct.setStatus('current')
cdot11SecAuxSsidProxyMobileIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidProxyMobileIp.setStatus('current')
cdot11SecAuxSsidMaxStations = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2007)).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidMaxStations.setStatus('current')
cdot11SecAuxSsidVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 6), CDot11IfVlanIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidVlan.setStatus('current')
cdot11SecAuxSsidWpaPsk = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 7), CDot11WiFiPaPreSharedKey().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidWpaPsk.setStatus('current')
cdot11SecAuxRadiusAccounting = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxRadiusAccounting.setStatus('current')
cdot11SecAuxSsidLoginUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidLoginUsername.setStatus('current')
cdot11SecAuxSsidLoginPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 10), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidLoginPassword.setStatus('current')
cdot11SecAuxSsidAuthKeyMgmt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 11), CDot11SecAuthKeyMgmtType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidAuthKeyMgmt.setStatus('current')
cdot11SecAuxSsidAuthKeyMgmtOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidAuthKeyMgmtOpt.setStatus('current')
cdot11SecAuxSsidRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidRowStatus.setStatus('current')
cdot11SecAuxSsidWirelessNetId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidWirelessNetId.setStatus('current')
cdot11SecSsidRedirectAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 15), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecSsidRedirectAddrType.setStatus('current')
cdot11SecSsidRedirectDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 16), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecSsidRedirectDestAddr.setStatus('current')
cdot11SecSsidRedirectFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 17), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecSsidRedirectFilter.setStatus('current')
cdot11SecSsidInformationElement = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 18), CDot11InformationElementType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecSsidInformationElement.setStatus('current')
cdot11SecAuxSsidVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 19), CDot11VlanName().clone(' ')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidVlanName.setStatus('current')
cdot11SecAuxSsidMbssidBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 20), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidMbssidBroadcast.setStatus('current')
cdot11SecAuxSsidMbssidDtimPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('beacons').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecAuxSsidMbssidDtimPeriod.setStatus('current')
cdot11SecAuxSsidAuthTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2), )
if mibBuilder.loadTexts: cdot11SecAuxSsidAuthTable.setStatus('current')
cdot11SecAuxSsidAuthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsid"), (0, "IEEE802dot11-MIB", "dot11AuthenticationAlgorithmsIndex"))
if mibBuilder.loadTexts: cdot11SecAuxSsidAuthEntry.setStatus('current')
cdot11SecAuxSsidAuthEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11SecAuxSsidAuthEnabled.setStatus('current')
cdot11SecAuxSsidAuthPlusEap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11SecAuxSsidAuthPlusEap.setStatus('current')
cdot11SecAuxSsidAuthPlusMac = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11SecAuxSsidAuthPlusMac.setStatus('current')
cdot11SecAuxSsidAuthEapMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1, 4), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11SecAuxSsidAuthEapMethod.setStatus('current')
cdot11SecAuxSsidAuthMacMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11SecAuxSsidAuthMacMethod.setStatus('current')
cdot11SecAuxSsidAuthMacAlternate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11SecAuxSsidAuthMacAlternate.setStatus('current')
cdot11SecInterfSsidTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 3), )
if mibBuilder.loadTexts: cdot11SecInterfSsidTable.setStatus('current')
cdot11SecInterfSsidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsid"))
if mibBuilder.loadTexts: cdot11SecInterfSsidEntry.setStatus('current')
cdot11SecInterfSsidRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 3, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecInterfSsidRowStatus.setStatus('current')
cdot11MbssidMacAddrSupportTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 4), )
if mibBuilder.loadTexts: cdot11MbssidMacAddrSupportTable.setStatus('current')
cdot11MbssidMacAddrSupportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11MbssidMacAddrIndex"))
if mibBuilder.loadTexts: cdot11MbssidMacAddrSupportEntry.setStatus('current')
cdot11MbssidMacAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11MbssidMacAddrIndex.setStatus('current')
cdot11MbssidMacAddrSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 4, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11MbssidMacAddrSupported.setStatus('current')
cdot11MbssidInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 5), )
if mibBuilder.loadTexts: cdot11MbssidInterfaceTable.setStatus('current')
cdot11MbssidInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (1, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsid"))
if mibBuilder.loadTexts: cdot11MbssidInterfaceEntry.setStatus('current')
cdot11MbssidIfMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 5, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11MbssidIfMacAddress.setStatus('current')
cdot11MbssidIfBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 5, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdot11MbssidIfBroadcast.setStatus('current')
cdot11SecSsidMaxBackupVlans = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11SecSsidMaxBackupVlans.setStatus('current')
cdot11SecSsidBackupVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 7), )
if mibBuilder.loadTexts: cdot11SecSsidBackupVlanTable.setStatus('current')
cdot11SecSsidBackupVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 7, 1), ).setIndexNames((0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsid"), (0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidBackupVlan"))
if mibBuilder.loadTexts: cdot11SecSsidBackupVlanEntry.setStatus('current')
cdot11SecSsidBackupVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 7, 1, 1), CDot11IfVlanIdOrZero().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: cdot11SecSsidBackupVlan.setStatus('current')
cdot11SecSsidBackupVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 1, 7, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecSsidBackupVlanRowStatus.setStatus('current')
cdot11SecLocalAuthServerEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdot11SecLocalAuthServerEnabled.setStatus('current')
cdot11SecVlanNameTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 4, 1), )
if mibBuilder.loadTexts: cdot11SecVlanNameTable.setStatus('current')
cdot11SecVlanNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecVlanName"))
if mibBuilder.loadTexts: cdot11SecVlanNameEntry.setStatus('current')
cdot11SecVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 4, 1, 1, 1), CDot11VlanName())
if mibBuilder.loadTexts: cdot11SecVlanName.setStatus('current')
cdot11SecVlanNameId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 4, 1, 1, 2), CDot11IfVlanIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecVlanNameId.setStatus('current')
cdot11SecVlanNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 413, 1, 4, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11SecVlanNameRowStatus.setStatus('current')
ciscoDot11SsidSecMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 413, 2))
ciscoDot11SsidSecMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 1))
ciscoDot11SsidSecMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2))
ciscoDot11SsidSecCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 1, 1)).setObjects(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidManagementGroup"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SsidAuthenticationGroup"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11ModuleAuthenticationGroup"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecVlanManagementGroup"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11MbssidSupportGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11SsidSecCompliance = ciscoDot11SsidSecCompliance.setStatus('deprecated')
ciscoDot11SsidSecComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 1, 2)).setObjects(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidManagementGroup"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SsidAuthenticationGroup"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11ModuleAuthenticationGroup"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidBackupVlanManagementGroup"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecVlanManagementGroup"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11MbssidSupportGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11SsidSecComplianceRev1 = ciscoDot11SsidSecComplianceRev1.setStatus('current')
cdot11SecSsidManagementGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2, 1)).setObjects(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidBroadcast"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidInfraStruct"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidProxyMobileIp"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidMaxStations"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidVlan"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidWpaPsk"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxRadiusAccounting"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidLoginUsername"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidLoginPassword"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthKeyMgmt"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthKeyMgmtOpt"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidRowStatus"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidWirelessNetId"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidRedirectAddrType"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidRedirectDestAddr"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidRedirectFilter"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidInformationElement"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidVlanName"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecInterfSsidRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdot11SecSsidManagementGroup = cdot11SecSsidManagementGroup.setStatus('current')
cdot11SsidAuthenticationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2, 2)).setObjects(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthEnabled"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthPlusEap"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthPlusMac"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthEapMethod"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthMacMethod"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidAuthMacAlternate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdot11SsidAuthenticationGroup = cdot11SsidAuthenticationGroup.setStatus('current')
cdot11ModuleAuthenticationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2, 3)).setObjects(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecLocalAuthServerEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdot11ModuleAuthenticationGroup = cdot11ModuleAuthenticationGroup.setStatus('current')
cdot11SecVlanManagementGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2, 4)).setObjects(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecVlanNameId"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecVlanNameRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdot11SecVlanManagementGroup = cdot11SecVlanManagementGroup.setStatus('current')
cdot11MbssidSupportGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2, 5)).setObjects(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidMbssidBroadcast"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecAuxSsidMbssidDtimPeriod"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11MbssidMacAddrIndex"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11MbssidMacAddrSupported"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11MbssidIfMacAddress"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11MbssidIfBroadcast"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdot11MbssidSupportGroup = cdot11MbssidSupportGroup.setStatus('current')
cdot11SecSsidBackupVlanManagementGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 413, 2, 2, 6)).setObjects(("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidBackupVlanRowStatus"), ("CISCO-DOT11-SSID-SECURITY-MIB", "cdot11SecSsidMaxBackupVlans"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdot11SecSsidBackupVlanManagementGroup = cdot11SecSsidBackupVlanManagementGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-SSID-SECURITY-MIB", cdot11SecAuxSsidMbssidDtimPeriod=cdot11SecAuxSsidMbssidDtimPeriod, cdot11SecSsidBackupVlan=cdot11SecSsidBackupVlan, CDot11VlanName=CDot11VlanName, cdot11MbssidInterfaceTable=cdot11MbssidInterfaceTable, cdot11SecAuxSsidWpaPsk=cdot11SecAuxSsidWpaPsk, cdot11SecVlanNameEntry=cdot11SecVlanNameEntry, cdot11SecAuxSsidInfraStruct=cdot11SecAuxSsidInfraStruct, ciscoDot11SsidSecComplianceRev1=ciscoDot11SsidSecComplianceRev1, cdot11SecSsidRedirectDestAddr=cdot11SecSsidRedirectDestAddr, cdot11SecAuxSsidAuthPlusMac=cdot11SecAuxSsidAuthPlusMac, cdot11SecLocalAuthServerEnabled=cdot11SecLocalAuthServerEnabled, cdot11SecSsidManagement=cdot11SecSsidManagement, cdot11SecAuxRadiusAccounting=cdot11SecAuxRadiusAccounting, cdot11MbssidMacAddrIndex=cdot11MbssidMacAddrIndex, cdot11MbssidMacAddrSupportTable=cdot11MbssidMacAddrSupportTable, CDot11InformationElementType=CDot11InformationElementType, cdot11SecAuxSsidAuthPlusEap=cdot11SecAuxSsidAuthPlusEap, cdot11SecInterfSsidEntry=cdot11SecInterfSsidEntry, cdot11SecSsidManagementGroup=cdot11SecSsidManagementGroup, cdot11SecSsidRedirectAddrType=cdot11SecSsidRedirectAddrType, CDot11SsidString=CDot11SsidString, cdot11SecAuxSsidVlanName=cdot11SecAuxSsidVlanName, cdot11SecInterfSsidRowStatus=cdot11SecInterfSsidRowStatus, cdot11SecAuxSsid=cdot11SecAuxSsid, cdot11SecAuxSsidAuthEnabled=cdot11SecAuxSsidAuthEnabled, cdot11SecVlanNameId=cdot11SecVlanNameId, cdot11SecInterfSsidTable=cdot11SecInterfSsidTable, cdot11MbssidMacAddrSupportEntry=cdot11MbssidMacAddrSupportEntry, cdot11SecVlanManagementGroup=cdot11SecVlanManagementGroup, cdot11SecAuxSsidEntry=cdot11SecAuxSsidEntry, cdot11MbssidSupportGroup=cdot11MbssidSupportGroup, cdot11SecSsidBackupVlanEntry=cdot11SecSsidBackupVlanEntry, CDot11WiFiPaPreSharedKey=CDot11WiFiPaPreSharedKey, cdot11SecStatistics=cdot11SecStatistics, cdot11SecVlanNameTable=cdot11SecVlanNameTable, cdot11SecAuxSsidMbssidBroadcast=cdot11SecAuxSsidMbssidBroadcast, cdot11SecAuxSsidLoginPassword=cdot11SecAuxSsidLoginPassword, cdot11SecSsidBackupVlanRowStatus=cdot11SecSsidBackupVlanRowStatus, ciscoDot11SsidSecMIB=ciscoDot11SsidSecMIB, cdot11SecAuxSsidAuthEntry=cdot11SecAuxSsidAuthEntry, cdot11SecAuxSsidLoginUsername=cdot11SecAuxSsidLoginUsername, cdot11SecAuxSsidVlan=cdot11SecAuxSsidVlan, cdot11SecVlanNameRowStatus=cdot11SecVlanNameRowStatus, ciscoDot11SsidSecCompliance=ciscoDot11SsidSecCompliance, cdot11SecVlanName=cdot11SecVlanName, PYSNMP_MODULE_ID=ciscoDot11SsidSecMIB, cdot11SecAuxSsidAuthTable=cdot11SecAuxSsidAuthTable, cdot11SecAuxSsidTable=cdot11SecAuxSsidTable, cdot11SecAuxSsidAuthMacMethod=cdot11SecAuxSsidAuthMacMethod, ciscoDot11SsidSecMIBObjects=ciscoDot11SsidSecMIBObjects, cdot11SecAuxSsidAuthEapMethod=cdot11SecAuxSsidAuthEapMethod, cdot11SecSsidRedirectFilter=cdot11SecSsidRedirectFilter, cdot11SecAuxSsidAuthMacAlternate=cdot11SecAuxSsidAuthMacAlternate, cdot11SecAuthManagement=cdot11SecAuthManagement, cdot11MbssidMacAddrSupported=cdot11MbssidMacAddrSupported, cdot11SecAuxSsidProxyMobileIp=cdot11SecAuxSsidProxyMobileIp, cdot11SecAuxSsidBroadcast=cdot11SecAuxSsidBroadcast, cdot11SecSsidBackupVlanManagementGroup=cdot11SecSsidBackupVlanManagementGroup, cdot11SecAuxSsidMaxStations=cdot11SecAuxSsidMaxStations, ciscoDot11SsidSecMIBCompliances=ciscoDot11SsidSecMIBCompliances, ciscoDot11SsidSecMIBGroups=ciscoDot11SsidSecMIBGroups, cdot11MbssidIfBroadcast=cdot11MbssidIfBroadcast, cdot11MbssidIfMacAddress=cdot11MbssidIfMacAddress, cdot11SecSsidMaxBackupVlans=cdot11SecSsidMaxBackupVlans, cdot11SsidAuthenticationGroup=cdot11SsidAuthenticationGroup, cdot11MbssidInterfaceEntry=cdot11MbssidInterfaceEntry, cdot11SecSsidBackupVlanTable=cdot11SecSsidBackupVlanTable, CDot11SecAuthKeyMgmtType=CDot11SecAuthKeyMgmtType, cdot11SecAuxSsidAuthKeyMgmt=cdot11SecAuxSsidAuthKeyMgmt, ciscoDot11SsidSecMIBConformance=ciscoDot11SsidSecMIBConformance, cdot11SecAuxSsidWirelessNetId=cdot11SecAuxSsidWirelessNetId, cdot11ModuleAuthenticationGroup=cdot11ModuleAuthenticationGroup, cdot11SecVlanManagement=cdot11SecVlanManagement, cdot11SecSsidInformationElement=cdot11SecSsidInformationElement, cdot11SecAuxSsidRowStatus=cdot11SecAuxSsidRowStatus, cdot11SecAuxSsidAuthKeyMgmtOpt=cdot11SecAuxSsidAuthKeyMgmtOpt)
