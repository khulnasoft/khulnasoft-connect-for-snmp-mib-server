#
# PySNMP MIB module REDSTONE-RADIUS-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-RADIUS-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, ObjectIdentity, TimeTicks, Bits, Unsigned32, Counter32, Integer32, ModuleIdentity, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32", "Counter32", "Integer32", "ModuleIdentity", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Counter64")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
rsRadiusClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 19))
rsRadiusClientMIB.setRevisions(('1999-06-01 00:00',))
if mibBuilder.loadTexts: rsRadiusClientMIB.setLastUpdated('9906010000Z')
if mibBuilder.loadTexts: rsRadiusClientMIB.setOrganization('Redstone Communications Inc.')
rsRadiusClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1))
rsRadiusGeneralClient = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 1))
rsRadiusAuthClient = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2))
rsRadiusAcctClient = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3))
rsRadiusClientIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusClientIdentifier.setStatus('current')
rsRadiusClientAlgorithm = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("direct", 0), ("roundRobin", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsRadiusClientAlgorithm.setStatus('current')
rsRadiusAuthClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientInvalidServerAddresses.setStatus('current')
rsRadiusAuthClientServerTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2), )
if mibBuilder.loadTexts: rsRadiusAuthClientServerTable.setStatus('current')
rsRadiusAuthClientServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1), ).setIndexNames((0, "REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientServerAddress"))
if mibBuilder.loadTexts: rsRadiusAuthClientServerEntry.setStatus('current')
rsRadiusAuthClientServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: rsRadiusAuthClientServerAddress.setStatus('current')
rsRadiusAuthClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientServerPortNumber.setStatus('current')
rsRadiusAuthClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientRoundTripTime.setStatus('current')
rsRadiusAuthClientAccessRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientAccessRequests.setStatus('current')
rsRadiusAuthClientAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientAccessRetransmissions.setStatus('current')
rsRadiusAuthClientAccessAccepts = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientAccessAccepts.setStatus('current')
rsRadiusAuthClientAccessRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientAccessRejects.setStatus('current')
rsRadiusAuthClientAccessChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientAccessChallenges.setStatus('current')
rsRadiusAuthClientMalformedAccessResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientMalformedAccessResponses.setStatus('current')
rsRadiusAuthClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientBadAuthenticators.setStatus('current')
rsRadiusAuthClientPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientPendingRequests.setStatus('current')
rsRadiusAuthClientTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientTimeouts.setStatus('current')
rsRadiusAuthClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientUnknownTypes.setStatus('current')
rsRadiusAuthClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientPacketsDropped.setStatus('current')
rsRadiusAuthClientCfgServerTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3), )
if mibBuilder.loadTexts: rsRadiusAuthClientCfgServerTable.setStatus('current')
rsRadiusAuthClientCfgServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1), ).setIndexNames((0, "REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientServerAddress"))
if mibBuilder.loadTexts: rsRadiusAuthClientCfgServerEntry.setStatus('current')
rsRadiusAuthClientCfgServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: rsRadiusAuthClientCfgServerAddress.setStatus('current')
rsRadiusAuthClientCfgServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1812)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgServerPortNumber.setStatus('current')
rsRadiusAuthClientCfgKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgKey.setStatus('current')
rsRadiusAuthClientCfgTimeoutInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(3)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgTimeoutInterval.setStatus('current')
rsRadiusAuthClientCfgRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgRetries.setStatus('current')
rsRadiusAuthClientCfgMaxPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgMaxPendingRequests.setStatus('current')
rsRadiusAuthClientCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgRowStatus.setStatus('current')
rsRadiusAuthClientCfgPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgPrecedence.setStatus('current')
rsRadiusAuthClientCfgDeadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30)).clone(5)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAuthClientCfgDeadTime.setStatus('current')
rsRadiusAcctClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientInvalidServerAddresses.setStatus('current')
rsRadiusAcctClientServerTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2), )
if mibBuilder.loadTexts: rsRadiusAcctClientServerTable.setStatus('current')
rsRadiusAcctClientServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1), ).setIndexNames((0, "REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientServerAddress"))
if mibBuilder.loadTexts: rsRadiusAcctClientServerEntry.setStatus('current')
rsRadiusAcctClientServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: rsRadiusAcctClientServerAddress.setStatus('current')
rsRadiusAcctClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientServerPortNumber.setStatus('current')
rsRadiusAcctClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientRoundTripTime.setStatus('current')
rsRadiusAcctClientRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientRequests.setStatus('current')
rsRadiusAcctClientRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientRetransmissions.setStatus('current')
rsRadiusAcctClientResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientResponses.setStatus('current')
rsRadiusAcctClientMalformedResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientMalformedResponses.setStatus('current')
rsRadiusAcctClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientBadAuthenticators.setStatus('current')
rsRadiusAcctClientPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientPendingRequests.setStatus('current')
rsRadiusAcctClientTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientTimeouts.setStatus('current')
rsRadiusAcctClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientUnknownTypes.setStatus('current')
rsRadiusAcctClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientPacketsDropped.setStatus('current')
rsRadiusAcctClientCfgServerTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3), )
if mibBuilder.loadTexts: rsRadiusAcctClientCfgServerTable.setStatus('current')
rsRadiusAcctClientCfgServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1), ).setIndexNames((0, "REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientServerAddress"))
if mibBuilder.loadTexts: rsRadiusAcctClientCfgServerEntry.setStatus('current')
rsRadiusAcctClientCfgServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: rsRadiusAcctClientCfgServerAddress.setStatus('current')
rsRadiusAcctClientCfgServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1813)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgServerPortNumber.setStatus('current')
rsRadiusAcctClientCfgKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgKey.setStatus('current')
rsRadiusAcctClientCfgTimeoutInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(3)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgTimeoutInterval.setStatus('current')
rsRadiusAcctClientCfgRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgRetries.setStatus('current')
rsRadiusAcctClientCfgMaxPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgMaxPendingRequests.setStatus('current')
rsRadiusAcctClientCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgRowStatus.setStatus('current')
rsRadiusAcctClientCfgPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgPrecedence.setStatus('current')
rsRadiusAcctClientCfgDeadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30)).clone(5)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsRadiusAcctClientCfgDeadTime.setStatus('current')
rsRadiusClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2))
rsRadiusClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 1))
rsRadiusClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 2))
rsRadiusAuthClientCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 1, 1)).setObjects(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusGeneralClientGroup"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRadiusAuthClientCompliance = rsRadiusAuthClientCompliance.setStatus('current')
rsRadiusAcctClientCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 1, 2)).setObjects(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusGeneralClientGroup"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRadiusAcctClientCompliance = rsRadiusAcctClientCompliance.setStatus('current')
rsRadiusGeneralClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 2, 1)).setObjects(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusClientIdentifier"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusClientAlgorithm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRadiusGeneralClientGroup = rsRadiusGeneralClientGroup.setStatus('current')
rsRadiusAuthClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 2, 2)).setObjects(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientInvalidServerAddresses"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientServerPortNumber"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientRoundTripTime"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessRequests"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessRetransmissions"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessAccepts"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessRejects"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessChallenges"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientMalformedAccessResponses"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientBadAuthenticators"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientPendingRequests"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientTimeouts"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientUnknownTypes"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientPacketsDropped"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgServerPortNumber"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgKey"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgTimeoutInterval"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgRetries"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgMaxPendingRequests"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgRowStatus"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgPrecedence"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgDeadTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRadiusAuthClientGroup = rsRadiusAuthClientGroup.setStatus('current')
rsRadiusAcctClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 2, 3)).setObjects(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientInvalidServerAddresses"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientServerPortNumber"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientRoundTripTime"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientRequests"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientRetransmissions"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientResponses"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientMalformedResponses"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientBadAuthenticators"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientPendingRequests"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientTimeouts"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientUnknownTypes"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientPacketsDropped"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgServerPortNumber"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgKey"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgTimeoutInterval"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgRetries"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgMaxPendingRequests"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgRowStatus"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgPrecedence"), ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgDeadTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsRadiusAcctClientGroup = rsRadiusAcctClientGroup.setStatus('current')
mibBuilder.exportSymbols("REDSTONE-RADIUS-CLIENT-MIB", rsRadiusAcctClientCfgServerTable=rsRadiusAcctClientCfgServerTable, rsRadiusAcctClientCfgKey=rsRadiusAcctClientCfgKey, rsRadiusGeneralClientGroup=rsRadiusGeneralClientGroup, rsRadiusAcctClientServerTable=rsRadiusAcctClientServerTable, rsRadiusAuthClientCompliance=rsRadiusAuthClientCompliance, rsRadiusAcctClient=rsRadiusAcctClient, rsRadiusAcctClientServerPortNumber=rsRadiusAcctClientServerPortNumber, rsRadiusAuthClientRoundTripTime=rsRadiusAuthClientRoundTripTime, rsRadiusAcctClientCfgServerEntry=rsRadiusAcctClientCfgServerEntry, rsRadiusClientMIB=rsRadiusClientMIB, rsRadiusAuthClientCfgServerTable=rsRadiusAuthClientCfgServerTable, rsRadiusAcctClientCfgDeadTime=rsRadiusAcctClientCfgDeadTime, rsRadiusAuthClientAccessRetransmissions=rsRadiusAuthClientAccessRetransmissions, rsRadiusClientObjects=rsRadiusClientObjects, rsRadiusAcctClientRetransmissions=rsRadiusAcctClientRetransmissions, rsRadiusAcctClientRoundTripTime=rsRadiusAcctClientRoundTripTime, rsRadiusAuthClientAccessAccepts=rsRadiusAuthClientAccessAccepts, rsRadiusAuthClientTimeouts=rsRadiusAuthClientTimeouts, rsRadiusAcctClientServerEntry=rsRadiusAcctClientServerEntry, rsRadiusAcctClientResponses=rsRadiusAcctClientResponses, rsRadiusAcctClientCfgRowStatus=rsRadiusAcctClientCfgRowStatus, rsRadiusAuthClientBadAuthenticators=rsRadiusAuthClientBadAuthenticators, rsRadiusAuthClientCfgPrecedence=rsRadiusAuthClientCfgPrecedence, rsRadiusAuthClientPacketsDropped=rsRadiusAuthClientPacketsDropped, rsRadiusAcctClientBadAuthenticators=rsRadiusAcctClientBadAuthenticators, rsRadiusAcctClientTimeouts=rsRadiusAcctClientTimeouts, rsRadiusClientAlgorithm=rsRadiusClientAlgorithm, rsRadiusAuthClientServerPortNumber=rsRadiusAuthClientServerPortNumber, rsRadiusAuthClientCfgServerAddress=rsRadiusAuthClientCfgServerAddress, rsRadiusAcctClientGroup=rsRadiusAcctClientGroup, rsRadiusClientMIBGroups=rsRadiusClientMIBGroups, rsRadiusAuthClientCfgServerPortNumber=rsRadiusAuthClientCfgServerPortNumber, rsRadiusAuthClientCfgTimeoutInterval=rsRadiusAuthClientCfgTimeoutInterval, rsRadiusAuthClientServerAddress=rsRadiusAuthClientServerAddress, rsRadiusAcctClientPendingRequests=rsRadiusAcctClientPendingRequests, rsRadiusAuthClientInvalidServerAddresses=rsRadiusAuthClientInvalidServerAddresses, rsRadiusAcctClientCompliance=rsRadiusAcctClientCompliance, rsRadiusAcctClientCfgTimeoutInterval=rsRadiusAcctClientCfgTimeoutInterval, rsRadiusAcctClientInvalidServerAddresses=rsRadiusAcctClientInvalidServerAddresses, rsRadiusAcctClientUnknownTypes=rsRadiusAcctClientUnknownTypes, rsRadiusGeneralClient=rsRadiusGeneralClient, rsRadiusAcctClientCfgRetries=rsRadiusAcctClientCfgRetries, rsRadiusAuthClientMalformedAccessResponses=rsRadiusAuthClientMalformedAccessResponses, rsRadiusAuthClientGroup=rsRadiusAuthClientGroup, rsRadiusAcctClientCfgServerPortNumber=rsRadiusAcctClientCfgServerPortNumber, rsRadiusAuthClientCfgDeadTime=rsRadiusAuthClientCfgDeadTime, rsRadiusAcctClientCfgPrecedence=rsRadiusAcctClientCfgPrecedence, rsRadiusClientMIBConformance=rsRadiusClientMIBConformance, rsRadiusClientMIBCompliances=rsRadiusClientMIBCompliances, rsRadiusAuthClientCfgMaxPendingRequests=rsRadiusAuthClientCfgMaxPendingRequests, rsRadiusAuthClientAccessRejects=rsRadiusAuthClientAccessRejects, rsRadiusAuthClientUnknownTypes=rsRadiusAuthClientUnknownTypes, rsRadiusAuthClientCfgKey=rsRadiusAuthClientCfgKey, rsRadiusClientIdentifier=rsRadiusClientIdentifier, rsRadiusAuthClientPendingRequests=rsRadiusAuthClientPendingRequests, rsRadiusAuthClientCfgRetries=rsRadiusAuthClientCfgRetries, rsRadiusAcctClientMalformedResponses=rsRadiusAcctClientMalformedResponses, rsRadiusAuthClientServerTable=rsRadiusAuthClientServerTable, rsRadiusAuthClientServerEntry=rsRadiusAuthClientServerEntry, rsRadiusAcctClientRequests=rsRadiusAcctClientRequests, rsRadiusAcctClientPacketsDropped=rsRadiusAcctClientPacketsDropped, rsRadiusAuthClientCfgServerEntry=rsRadiusAuthClientCfgServerEntry, rsRadiusAuthClientAccessRequests=rsRadiusAuthClientAccessRequests, rsRadiusAuthClientAccessChallenges=rsRadiusAuthClientAccessChallenges, rsRadiusAcctClientCfgMaxPendingRequests=rsRadiusAcctClientCfgMaxPendingRequests, PYSNMP_MODULE_ID=rsRadiusClientMIB, rsRadiusAuthClientCfgRowStatus=rsRadiusAuthClientCfgRowStatus, rsRadiusAcctClientServerAddress=rsRadiusAcctClientServerAddress, rsRadiusAuthClient=rsRadiusAuthClient, rsRadiusAcctClientCfgServerAddress=rsRadiusAcctClientCfgServerAddress)
