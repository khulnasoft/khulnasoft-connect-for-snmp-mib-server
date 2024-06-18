#
# PySNMP MIB module SWCOMMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWCOMMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:05:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, NotificationType, IpAddress, iso, Bits, NotificationType, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, MibIdentifier, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "NotificationType", "IpAddress", "iso", "Bits", "NotificationType", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "MibIdentifier", "Unsigned32", "TimeTicks")
PhysAddress, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention", "MacAddress")
privateMgmt, = mibBuilder.importSymbols("SWPRIMGMT-MIB", "privateMgmt")
swComMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1))
if mibBuilder.loadTexts: swComMgmtMIB.setLastUpdated('0007150000Z')
if mibBuilder.loadTexts: swComMgmtMIB.setOrganization('enterprise, Inc.')
class ErrorReturnCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(201, 202, 203, 204, 205, 206, 207, 208, 209))
    namedValues = NamedValues(("cannotModifyMltMemberPort", 201), ("onlyOnePortInMlt", 202), ("moreThan4PortsInMlt", 203), ("mltWithDifferentVlan", 204), ("cannotModifyVlanPortWithMltMemberPort", 205), ("arpClassIdSpecified", 206), ("arpClassIdOnlyForIpSubnetVlan", 207), ("ipSubnetVlanArpClassIdCannotBeZero", 208), ("arpClassIdWithExistVid", 209))

agentConfigInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1))
agentBasicInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1))
agentRuntimeSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRuntimeSwVersion.setStatus('current')
agentPromFwVersion = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPromFwVersion.setStatus('current')
agentHwRevision = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentHwRevision.setStatus('current')
agentDeviceSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 42))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDeviceSerialNumber.setStatus('current')
agentMgmtProtocolCapability = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("snmp-ip", 2), ("snmp-ipx", 3), ("snmp-ip-ipx", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMgmtProtocolCapability.setStatus('current')
agentMibCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 7), )
if mibBuilder.loadTexts: agentMibCapabilityTable.setStatus('current')
agentMibCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 7, 1), ).setIndexNames((0, "SWCOMMGMT-MIB", "agentMibCapabilityIndex"))
if mibBuilder.loadTexts: agentMibCapabilityEntry.setStatus('current')
agentMibCapabilityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityIndex.setStatus('current')
agentMibCapabilityDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 7, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityDescr.setStatus('current')
agentMibCapabilityVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityVersion.setStatus('current')
agentMibCapabilityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("standard", 2), ("proprietary", 3), ("experiment", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentMibCapabilityType.setStatus('current')
agentStatusConsoleInUse = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("in-use", 2), ("not-in-use", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentStatusConsoleInUse.setStatus('current')
agentSerialPortDataBits = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSerialPortDataBits.setStatus('current')
agentSerialPortParityBits = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("none", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSerialPortParityBits.setStatus('current')
agentSerialPortStopBits = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSerialPortStopBits.setStatus('current')
agentPrimaryPowerState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("not-ready", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentPrimaryPowerState.setStatus('current')
agentRedundantPowerState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("not-ready", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRedundantPowerState.setStatus('current')
agentBasicConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2))
agentFirmwareFile = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentFirmwareFile.setStatus('current')
agentFirmwareSourceAddr = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentFirmwareSourceAddr.setStatus('current')
agentFirmwareUpdateCtrl = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("activate", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentFirmwareUpdateCtrl.setStatus('current')
agentFirmwareUpdateState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("other", 1), ("in-process", 2), ("invalid-file", 3), ("violation", 4), ("file-not-found", 5), ("disk-full", 6), ("complete", 7), ("time-out", 8), ("tftp-establish-fail", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentFirmwareUpdateState.setStatus('current')
agentSystemRestart = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("cold-start", 2), ("no-restart", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSystemRestart.setStatus('current')
agentRs232PortConfig = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("console", 2), ("out-of-band", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRs232PortConfig.setStatus('current')
agentBaudRateConfig = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("baudRate-2400", 2), ("baudRate-9600", 3), ("baudRate-19200", 4), ("baudRate-38400", 5), ("baudRate-57200", 6), ("baudRate-115200", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentBaudRateConfig.setStatus('current')
agentAutoLogoutConfig = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("never", 2), ("autoLogout-2mins", 3), ("autoLogout-5mins", 4), ("autoLogout-10mins", 5), ("autoLogout-15mins", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAutoLogoutConfig.setStatus('current')
agentTelnetState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentTelnetState.setStatus('current')
agentWebState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentWebState.setStatus('current')
agentFactoryReset = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("reset", 2), ("config", 3), ("system", 4), ("no-reset", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentFactoryReset.setStatus('current')
agentIpProtoConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3))
agentIpNumOfIf = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpNumOfIf.setStatus('current')
agentIpIfTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2), )
if mibBuilder.loadTexts: agentIpIfTable.setStatus('current')
agentIpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1), ).setIndexNames((0, "SWCOMMGMT-MIB", "agentIpIfIndex"))
if mibBuilder.loadTexts: agentIpIfEntry.setStatus('current')
agentIpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfIndex.setStatus('current')
agentIpIfAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfAddress.setStatus('current')
agentIpIfNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfNetMask.setStatus('current')
agentIpIfDefaultRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfDefaultRouter.setStatus('current')
agentIpIfMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1, 5), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfMacAddr.setStatus('current')
agentIpIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 6, 28))).clone(namedValues=NamedValues(("other", 1), ("ethernet-csmacd", 6), ("slip", 28)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpIfType.setStatus('current')
agentIpBootServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpBootServerAddr.setStatus('current')
agentIpGetIpFromBootpServer = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("manual", 2), ("frombootp", 3), ("fromdhcp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpGetIpFromBootpServer.setStatus('current')
agentIpSystemIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpSystemIpAddr.setStatus('current')
agentIpSystemSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpSystemSubnetMask.setStatus('current')
agentIpDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 3, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIpDefaultGateway.setStatus('current')
agentCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 4), )
if mibBuilder.loadTexts: agentCommunityTable.setStatus('current')
agentCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 4, 1), ).setIndexNames((0, "SWCOMMGMT-MIB", "agentCommunityString"))
if mibBuilder.loadTexts: agentCommunityEntry.setStatus('current')
agentCommunityString = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentCommunityString.setStatus('current')
agentCommunityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("read-only", 2), ("read-write", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentCommunityLevel.setStatus('current')
agentCommunitystate = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("valid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentCommunitystate.setStatus('current')
agentTrustHostTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 5), )
if mibBuilder.loadTexts: agentTrustHostTable.setStatus('current')
agentTrustHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 5, 1), ).setIndexNames((0, "SWCOMMGMT-MIB", "agentTrustHostId"))
if mibBuilder.loadTexts: agentTrustHostEntry.setStatus('current')
agentTrustHostId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentTrustHostId.setStatus('current')
agentTrustHostIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentTrustHostIPAddr.setStatus('current')
agentTrustHostState = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("valid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentTrustHostState.setStatus('current')
agentTrustHostIPMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 5, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentTrustHostIPMask.setStatus('current')
agentLogConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 6))
agentLogUploadLogFileName = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 6, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogUploadLogFileName.setStatus('current')
agentLogUploadLogSourceAddr = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 6, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogUploadLogSourceAddr.setStatus('current')
agentLogUploadLog = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("active", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogUploadLog.setStatus('current')
agentLogUploadLogState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("other", 1), ("in-process", 2), ("invalid-file", 3), ("violation", 4), ("file-not-found", 5), ("disk-full", 6), ("complete", 7), ("time-out", 8), ("tftp-establish-fail", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogUploadLogState.setStatus('current')
agentLogClearLog = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("active", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogClearLog.setStatus('current')
agentTblSize = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 7))
agentArpNumber = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 7, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentArpNumber.setStatus('current')
agentIpNumber = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 7, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIpNumber.setStatus('current')
agentStaticVlanNumber = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 7, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentStaticVlanNumber.setStatus('current')
agentRTC = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8))
agentRTCYear = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1980, 3999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRTCYear.setStatus('current')
agentRTCMonth = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRTCMonth.setStatus('current')
agentRTCDate = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRTCDate.setStatus('current')
agentRTCHour = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRTCHour.setStatus('current')
agentRTCMinute = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRTCMinute.setStatus('current')
agentRTCSecond = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRTCSecond.setStatus('current')
agentRTCWeekDay = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 8, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("date-Sunday", 1), ("date-Monday", 2), ("date-Tuesday", 3), ("date-Wednesday", 4), ("date-Thursday", 5), ("date-Friday", 6), ("date-Saturday", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRTCWeekDay.setStatus('current')
agentMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 9))
primaryPowerOn = NotificationType((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1) + (0,1))
primaryPowerOff = NotificationType((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1) + (0,2))
redundantPowerOn = NotificationType((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1) + (0,3))
redundantPowerOff = NotificationType((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1) + (0,4))
agentSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10))
agentSyslogState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSyslogState.setStatus('current')
agentSyslogMaxHostSupport = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSyslogMaxHostSupport.setStatus('current')
agentSyslogHostTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3), )
if mibBuilder.loadTexts: agentSyslogHostTable.setStatus('current')
agentSyslogHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1), ).setIndexNames((0, "SWCOMMGMT-MIB", "agentSyslogHostId"))
if mibBuilder.loadTexts: agentSyslogHostEntry.setStatus('current')
agentSyslogHostId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSyslogHostId.setStatus('current')
agentSyslogHostIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSyslogHostIp.setStatus('current')
agentSyslogHostSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1, 3), Bits().clone(namedValues=NamedValues(("informational", 0), ("warning", 1), ("error", 2), ("fatal", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSyslogHostSeverity.setStatus('current')
agentSyslogHostFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("local0", 1), ("local1", 2), ("local2", 3), ("local3", 4), ("local4", 5), ("local5", 6), ("local6", 7), ("local7", 8))).clone('local7')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSyslogHostFacility.setStatus('current')
agentSyslogHostUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(514, 530)).clone(514)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSyslogHostUDPPort.setStatus('current')
agentSyslogHostState = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("invalid", 4))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSyslogHostState.setStatus('current')
agentRemoteUserLogState = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1, 1, 1, 10, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRemoteUserLogState.setStatus('current')
mibBuilder.exportSymbols("SWCOMMGMT-MIB", agentStatusConsoleInUse=agentStatusConsoleInUse, agentRTCMonth=agentRTCMonth, agentRTCWeekDay=agentRTCWeekDay, agentCommunityString=agentCommunityString, agentBaudRateConfig=agentBaudRateConfig, agentRedundantPowerState=agentRedundantPowerState, agentIpIfEntry=agentIpIfEntry, agentSyslog=agentSyslog, agentFirmwareUpdateCtrl=agentFirmwareUpdateCtrl, agentRTCYear=agentRTCYear, agentRTCSecond=agentRTCSecond, agentSyslogHostSeverity=agentSyslogHostSeverity, agentMibCapabilityTable=agentMibCapabilityTable, agentStaticVlanNumber=agentStaticVlanNumber, agentCommunityLevel=agentCommunityLevel, agentSerialPortDataBits=agentSerialPortDataBits, agentLogUploadLogState=agentLogUploadLogState, PYSNMP_MODULE_ID=swComMgmtMIB, agentTelnetState=agentTelnetState, agentSyslogMaxHostSupport=agentSyslogMaxHostSupport, agentSyslogState=agentSyslogState, agentMibCapabilityVersion=agentMibCapabilityVersion, agentMibCapabilityType=agentMibCapabilityType, agentRs232PortConfig=agentRs232PortConfig, agentFactoryReset=agentFactoryReset, agentTrustHostEntry=agentTrustHostEntry, agentTrustHostIPAddr=agentTrustHostIPAddr, agentBasicConfig=agentBasicConfig, agentRTCMinute=agentRTCMinute, agentIpIfNetMask=agentIpIfNetMask, agentIpIfMacAddr=agentIpIfMacAddr, agentIpSystemSubnetMask=agentIpSystemSubnetMask, agentSyslogHostEntry=agentSyslogHostEntry, agentMibCapabilityIndex=agentMibCapabilityIndex, redundantPowerOff=redundantPowerOff, agentRemoteUserLogState=agentRemoteUserLogState, agentArpNumber=agentArpNumber, agentIpProtoConfig=agentIpProtoConfig, agentTrustHostTable=agentTrustHostTable, agentLogUploadLogSourceAddr=agentLogUploadLogSourceAddr, agentIpDefaultGateway=agentIpDefaultGateway, agentFirmwareUpdateState=agentFirmwareUpdateState, agentWebState=agentWebState, agentLogUploadLogFileName=agentLogUploadLogFileName, agentIpSystemIpAddr=agentIpSystemIpAddr, agentRTCDate=agentRTCDate, agentIpIfDefaultRouter=agentIpIfDefaultRouter, agentCommunityTable=agentCommunityTable, agentLogClearLog=agentLogClearLog, primaryPowerOn=primaryPowerOn, swComMgmtMIB=swComMgmtMIB, agentTblSize=agentTblSize, agentIpIfIndex=agentIpIfIndex, agentIpIfAddress=agentIpIfAddress, agentLogUploadLog=agentLogUploadLog, agentPromFwVersion=agentPromFwVersion, agentLogConfig=agentLogConfig, agentFirmwareFile=agentFirmwareFile, agentFirmwareSourceAddr=agentFirmwareSourceAddr, agentCommunitystate=agentCommunitystate, primaryPowerOff=primaryPowerOff, agentSerialPortParityBits=agentSerialPortParityBits, agentMIBTraps=agentMIBTraps, agentSyslogHostState=agentSyslogHostState, agentRuntimeSwVersion=agentRuntimeSwVersion, agentDeviceSerialNumber=agentDeviceSerialNumber, agentIpIfTable=agentIpIfTable, agentSyslogHostTable=agentSyslogHostTable, ErrorReturnCode=ErrorReturnCode, agentTrustHostState=agentTrustHostState, agentMibCapabilityEntry=agentMibCapabilityEntry, agentSyslogHostId=agentSyslogHostId, agentMgmtProtocolCapability=agentMgmtProtocolCapability, agentIpGetIpFromBootpServer=agentIpGetIpFromBootpServer, redundantPowerOn=redundantPowerOn, agentRTC=agentRTC, agentIpBootServerAddr=agentIpBootServerAddr, agentSyslogHostIp=agentSyslogHostIp, agentSerialPortStopBits=agentSerialPortStopBits, agentSystemRestart=agentSystemRestart, agentAutoLogoutConfig=agentAutoLogoutConfig, agentRTCHour=agentRTCHour, agentCommunityEntry=agentCommunityEntry, agentHwRevision=agentHwRevision, agentTrustHostIPMask=agentTrustHostIPMask, agentSyslogHostUDPPort=agentSyslogHostUDPPort, agentIpNumOfIf=agentIpNumOfIf, agentConfigInfo=agentConfigInfo, agentSyslogHostFacility=agentSyslogHostFacility, agentBasicInfo=agentBasicInfo, agentMibCapabilityDescr=agentMibCapabilityDescr, agentTrustHostId=agentTrustHostId, agentPrimaryPowerState=agentPrimaryPowerState, agentIpNumber=agentIpNumber, agentIpIfType=agentIpIfType)
